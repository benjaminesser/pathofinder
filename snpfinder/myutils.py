import os

def parse_mpileup_line(line):

    """
    Parse a single line from an mpileup file.

    Parameters
    ----------
    line : str
        A line from an mpileup file.

    Returns
    -------
    tuple
        A tuple containing the chromosome, position, reference base,
        number of reads, read bases, and base qualities.
    """

    # set each column of mpileup to corresponding variable
    fields = line.strip().split()
    chromosome = fields[0]
    position = fields[1]
    reference_base = fields[2]
    num_reads = int(fields[3])
    read_bases = fields[4]
    base_qualities = fields[5]
    
    return chromosome, position, reference_base, num_reads, read_bases, base_qualities

def call_variants(mpileup_file, min_var_freq, min_hom_freq, min_coverage):

    """
    Perform variant calling on an mpileup file.

    Parameters
    ----------
    mpileup_file : str
        Path to the mpileup file.

    Returns
    -------
    list of tuple
        A list of variants. Each variant is represented as a tuple
        containing the chromosome, position, reference base, variant base, 
        and number of reads.
    """



    variants = []
    with open(mpileup_file, 'r') as f:
        for line in f:
            chromosome, position, reference_base, num_reads, read_bases, base_qualities = parse_mpileup_line(line)
            
            # if there are 0 reads for a given positon, move to the next position
            if num_reads == 0:
                continue

            base_counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
            ref_reads = 0
            
            # set base counts based on read_bases
            i = 0
            while i < len(read_bases):
                read_base = read_bases[i]
                # if read base is A,T,G,C increment base_counts
                if read_base.upper() in base_counts:
                    base_counts[read_base.upper()] += 1
                # if read base is . or , increment reference reads
                elif read_base in '.,':
                    ref_reads += 1
                # if read base is + or - skip the next few bases as they are part of the indel
                elif read_base in "+-":
                    if i + 1 < len(read_bases) and read_bases[i + 1].isdigit():
                        indel_len = int(read_bases[i + 1])
                        i += indel_len
                # if read base is $ or ^ or some other character, we simply skip it
                i += 1

            # determine alternate base with highest count
            alt_base = max(base_counts, key=base_counts.get)
            alt_base_count = base_counts[alt_base]

            # if proportion of non-reference reads is greater than threshold, add position to variants
            non_ref_reads = num_reads - ref_reads
            if (non_ref_reads / num_reads) >= min_var_freq:
                variant = {
                    'CHROM': chromosome,
                    'POS': position,
                    'ID': '.',
                    'REF': reference_base,
                    'ALT': alt_base,
                    'QUAL': '.',
                    'FILTER': '.',
                    'INFO': f'DP={num_reads}',
                    'FORMAT': 'GT',
                    'SAMPLE': '.' 
                }

                # If proportion of non-reference bases is greater than threshold to consider position homozygous, update genotype accordingly
                if (alt_base_count / num_reads) >= min_hom_freq:
                    variant['SAMPLE'] = '1/1'
                # If proportion of alternate bases is less than threshold, call genotype heterozygous
                else:
                    variant['SAMPLE'] = '0/1'

                # If read depth is less than min coverage, caught by filter
                if (num_reads < min_coverage):
                    variant['FILTER'] = 'LowDepth'
                # If read depth equal to or greater than min coverage, passes filter
                else:
                    variant['FILTER'] = 'PASS'

                variants.append(variant)

    return variants

def build_vcf(variants, output_path, min_coverage):

    """
    Create a VCF file from a list of variant dictionaries.
    
    Parameters:
    - variants: List of dictionaries, each representing a variant with keys
                'CHROM', 'POS', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', and 'FORMAT'.
    - output_path: Path to the output VCF file.
    """

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path) if os.path.dirname(output_path) else '.'
    os.makedirs(output_dir, exist_ok=True)

    # Open the output file
    output_file =  open(output_path, "w")

    # Create and write VCF header
    header = f"""##fileformat=VCFv4.2
##source=snpfinderv1.0
##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
##FILTER=<ID=LowDepth,Description="Depth of coverage below {min_coverage}">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##CHROM POS ID  REF ALT QUAL    FILTER  INFO    FORMAT  SAMPLE""" 
    output_file.write(header)

    # Writ