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
            ref_reads = 0
            a_reads = 0
            t_reads = 0
            g_reads = 0
            c_reads = 0

            for read_base in read_bases:
                if (read_base == '.' or read_base == ','):
                    ref_reads += 1
                elif (read_base == 'A' or read_base == 'a'):
                    a_reads += 1
                elif (read_base == 'T' or read_base == 't'):
                    t_reads += 1
                elif (read_base == 'G' or read_base == 'g'):
                    g_reads += 1
                elif (read_base == 'C' or read_base == 'c'):
                    c_reads += 1
                # If we see anthing other than these characters, raise exception
                else:
                    raise ValueError("Read bases are not in correct format")
                
            non_ref_reads = num_reads - ref_reads
                
            # Determine the maximum value and set the corresponding variables
            if a_reads >= t_reads and a_reads >= g_reads and a_reads >= c_reads:
                alt_reads = a_reads
                alternate_base = 'A'
            elif t_reads >= a_reads and t_reads >= g_reads and t_reads >= c_reads:
                alt_reads = t_reads
                alternate_base = 'T'
            elif g_reads >= a_reads and g_reads >= t_reads and g_reads >= c_reads:
                alt_reads = g_reads
                alternate_base = 'G'
            else:
                alt_reads = c_reads
                alternate_base = 'C'

            # If proportion of non-reference reads passes threshold, add position to list of variants
            if (non_ref_reads / num_reads) >= min_var_freq:
                print("found a variant!")
                variant = {
                    'CHROM': chromosome,
                    'POS': position,
                    'ID': '.',
                    'REF': reference_base,
                    'ALT': alternate_base, # need to update this logic because some positions can have multple alternate bases
                    'QUAL': '.',
                    'FILTER': '.', # need to update this change from PASS to whatever filter a position may have failed
                    'INFO': '.', # update this
                    'FORMAT': '.', # update this
                    'Sample': '.' # update this
                }
                variants.append(variant)
    return variants
                    
            

