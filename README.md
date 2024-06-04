# snpfinder

snpfinder is a Python-based tool designed to identify single nucleotide polymorphisms from mpileup files. By integrating variant calling algorithms and specialized filters, snpfinder helps researchers quickly and efficiently pinpoint SNPs form genomic data.

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
snpfinder your_data.mpileup -o output.vcf
```
## Arguments
```
mpileup path to input mpileup file
-o, --out path where output VCF file will be saved
--min_var_freq to specify minimum proportion of non-reference bases at a position required to call it a variant (default is 0.2)
--min_hom_freq to specify minimum proportion of non-reference bases at a position required to call a variant homozygous (default is 0.8)
```
