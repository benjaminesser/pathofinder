#!/usr/bin/env python3

"""
Command-line script to perform variant calling of pileup files

Similar to VarScan pileup2snp
"""

import argparse
from variant_caller import call_variants

def main():
    parser = argparse.ArgumentParser(
        prog="pathofinder",
        description="Command-line script to perform variant calling of mpileup files"
    )

    # Input
    parser.add_argument("mpileup", help="mpileup file", type=str)

    # Output
    parser.add_argument("-o", "--out", help="Write output to file. " \
                        "Default: stdout", metavar="FILE", type=str, required=False)

    # Optional arguments
    parser.add_argument("--min_var_freq", help="minimum proportion of non-reference bases at a position required to call it a variant", type=float, required=False, default=0.2)
    
    args = parser.parse_args()

    variants = call_variants(args.mpileup, args.min_var_freq)
    
    for variant in variants:
        print(variant)

if __name__ == "__main__":
    main()
