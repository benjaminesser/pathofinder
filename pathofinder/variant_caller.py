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

    fields = line.strip().split()
    chromosome = fields[0]
    position = fields[1]
    reference_base = fields[2]
    num_reads = int(fields[3])
    read_bases = fields[4]
    base_qualities = fields[5]
    
    return chromosome, position, reference_base, num_reads, read_bases, base_qualities


def call_variants(mpileup_file, min_var_freq):

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
            base_counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
            ref_reads = 0
            
            # Set base counts based on read_bases
            for read_base in read_bases:
                normalized_base = read_base.upper()
                if normalized_base in base_counts:
                    base_counts[normalized_base] += 1
                elif read_base == '.' or read_base == ',':
                    ref_reads += 1

            non_ref_reads = num_reads - ref_reads

            # Determine alternate base with highest count
            alt_base = max(base_counts, key=base_counts.get)
            alt_base_count = base_counts[alt_base]

            # If proportion of non-reference reads is greater than threshold, add position to variants
            if (non_ref_reads / num_reads) >= min_var_freq:
                variant = {
                    'CHROM': chromosome,
                    'POS': position,
                    'ID': '.',
                    'REF': reference_base,
                    'ALT': alt_base,
                    'QUAL': '.',
                    'FILTER': '.',
                    'INFO': '.',
                    'FORMAT': '.',
                    'SAMPLE': ',' 
                }

                variants.append(variant)

    return variants