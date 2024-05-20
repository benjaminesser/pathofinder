def build_vcf(variants, output_file):
    """
    Builds a VCF file from a list of variants.

    Parameters:
    - variants: List of dictionaries, each representing a variant. Each dictionary should have the following keys:
        - 'CHROM': Chromosome
        - 'POS': Position
        - 'ID': Identifier
        - 'REF': Reference base
        - 'ALT': Alternate base
        - 'QUAL': Quality score
        - 'FILTER': Filter status
        - 'INFO': Additional information
        - 'FORMAT': Format of the genotype data
        - 'SAMPLE': List of sample data corresponding to the FORMAT

    - output_file: Path to the output VCF file.
    """
    # VCF header lines
    vcf_header = [
        "##fileformat=VCFv4.1",
        "##source=PathoFinder",
        '##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">',
        '##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">',
        "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSAMPLE"
    ]

    # Write the header and variants to the VCF file
    with open(output_file, 'w') as vcf_file:
        # Write the header lines
        for line in vcf_header:
            vcf_file.write(line + '\n')
        
        # Write each variant
        for variant in variants:
            
            # Create the variant line
            variant_line = (
                f"{variant['CHROM']}\t"
                f"{variant['POS']}\t"
                f"{variant['ID']}\t"
                f"{variant['REF']}\t"
                f"{variant['ALT']}\t"
                f"{variant['QUAL']}\t"
                f"{variant['FILTER']}\t"
                f"{variant['INFO']}\t"
                f"{variant['FORMAT']}\t"
                f"{variant['SAMPLE']}"
            )
            
            # Write the variant line
            vcf_file.write(variant_line + '\n')

    