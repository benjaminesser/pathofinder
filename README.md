# PathoFinder

PathoFinder is a Python-based tool designed to identify and classify pathogenic variants from genomic data. By integrating variant calling algorithms with specialized filters for high pathogenic potential, PathoFinder helps researchers and clinicians quickly determine the likelihood of variants being disease-causing.

# Features

- Variant calling from mpileup files.
- Integration with known databases for variant annotation.
- Scoring system to classify variants based on pathogenic potential.
- Command-line interface for easy integration into bioinformatics workflows.

# Installation

To install PathoFinder, you will need Python 3.6 or higher. You can install it directly from GitHub using the following commands:

```bash
git clone https://github.com/benjaminesser/PathoFinder.git
cd PathoFinder
python3 setup.py install
```
# Usage

To use PathoFinder, you need to prepare your genomic data in the mpileup format. Once you have your data ready, you can run PathoFinder as follows:
```
pathofinder your_data.mpileup -o output.vcf
```
## Arguments
```
mpileup path to input mpileup file
-o, --out path where output VCF file will be saved
--min_var_freq to specify minimum proportion of non-reference bases at a position required to call it a variant (default is 0.2)
--min_hom_freq to specify minimum proportion of non-reference bases at a position required to call a variant homozygous (default is 0.8)
```
