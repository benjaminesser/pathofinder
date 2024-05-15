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
    
    args = parser.parse_args()

    variants = call_variants(args.mpileup)

if __name__ == "__main__":
    main()
