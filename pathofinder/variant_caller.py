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


def call_variants(mpileup_file):

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

            if():  # if we decide that this position is a variant, add it to variants list

            else:
                continue
