import vcfpy
import os

def create_vcf_from_variants(variants, output_path):
    """
    Create a VCF file from a list of variant dictionaries.
    
    Parameters:
    - variants: List of dictionaries, each representing a variant with keys like
                'CHROM', 'POS', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', and 'FORMAT'.
    - output_path: Path to the output VCF file.
    """
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir) and output_dir != '':
        os.makedirs(output_dir)

    
    header = vcfpy.Header(
        lines=[
            vcfpy.HeaderLine(key="fileformat", value="VCFv4.2"),
            vcfpy.HeaderLine(key="source", value="PathoFinder"),
            
        ],
        samples=vcfpy.SamplesInfos(["Sample1"])  
    )

    header.add_line(vcfpy.FormatHeaderLine({"ID": "GT", "Number": "1", "Type": "String", "Description": "Genotype"}))


    gt_format_mapping = {
        "ID": "GT",
        "Number": "1",
        "Type": "String",
        "Description": "Genotype"
    }
    gt_format_line = vcfpy.FormatHeaderLine.from_mapping(gt_format_mapping)
    header.add_line(gt_format_line)


    writer = vcfpy.Writer.from_path(output_path, header)

    # Iterate over the variant dictionaries to create VCF records
    for variant in variants:
        variant_type = determine_variant_type(variant['REF'], variant['ALT'])
        record = vcfpy.Record(
            CHROM=variant['CHROM'],
            POS=int(variant['POS']),
            ID=variant.get('ID', '.'),
            REF=variant['REF'],
            ALT=[vcfpy.Substitution(variant_type, variant['ALT'])],
            QUAL=str(variant.get('QUAL', '.')),
            FILTER=variant.get('FILTER', []),
            INFO=variant.get('INFO', {}),
            FORMAT=["GT"],
            #calls=[vcfpy.Call(sample='Sample1', data=variant.get('SAMPLE', {'GT': '0/1'}))]
            #calls=[vcfpy.Call(sample='Sample1', data={"GT": variant.get('SAMPLE', {'GT': '0/1'})['GT']})]
            calls=[vcfpy.Call(sample='Sample1', data={"GT": variant['SAMPLE']['GT']})]
        )
        
        
        writer.write_record(record)

    
    writer.close()


def determine_variant_type(ref, alt):
    if len(ref) == 1 and len(alt) == 1:
        return "SNV"
    elif len(ref) > len(alt):
        return "DEL"
    elif len(ref) < len(alt):
        return "INS"
    else:
        return "MNV"  # Multinucleotide variant


test_variants = [
    {'CHROM': '1', 'POS': '123456', 'REF': 'G', 'ALT': 'A', 'QUAL': '60', 'FILTER': ['PASS'], 'INFO': {}, 'FORMAT': ['GT'], 'SAMPLE': {'GT': '0/1'}},
    {'CHROM': '1', 'POS': '123459', 'REF': 'T', 'ALT': 'C', 'QUAL': '50', 'FILTER': ['PASS'], 'INFO': {}, 'FORMAT': ['GT'], 'SAMPLE': {'GT': '1/1'}}
]

output_vcf_path = 'test_output.vcf'
create_vcf_from_variants(test_variants, output_vcf_path)

def print_vcf_contents(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())

print_vcf_contents(output_vcf_path)