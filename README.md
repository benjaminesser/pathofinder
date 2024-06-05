# snpfinder

snpfinder is a Python-based tool designed to identify single nucleotide polymorphisms (SNPs) from mpileup files. By integrating variant calling algorithms, snpfinder helps researchers quickly and efficiently pinpoint SNPs form genomic data.

# Features

- Variant calling from mpileup files.
- Output into VCF file format.
- Command-line interface for easy integration into bioinformatics workflows.

# Installation

To install snpfinder, you will need Python 3.6 or higher. You can install it directly from GitHub using the following commands:

```bash
git clone https://github.com/benjaminesser/snpfinder.git
cd snpfinder
python3 setup.py install
```
# Usage

To use snpfinder, you need to prepare your genomic data in the mpileup format. Once you have your data ready, you can run snpfinder as follows:
```
snpfinder [your_data.mpileup] -o [output.vcf]
```

Here is an example command that uses a test file from this repo:
```
snpfinder example_files/test.mpileup -o test.vcf --min_var_freq 0.3 --min_hom_freq 0.75 --min_coverage 15
```

This should create a file `test.vcf` with the following contents:
```
##fileformat=VCFv4.2
##source=snpfinderv1.0
##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
##FILTER=<ID=LowDepth,Descri