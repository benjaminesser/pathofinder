# PathoFinder

PathoFinder is a Python-based tool designed to identify and classify pathogenic variants from genomic data. By integrating variant calling algorithms with specialized filters for high pathogenic potential, PathoFinder helps researchers and clinicians quickly determine the likelihood of variants being disease-causing.

## Features

- Variant calling from mpileup files.
- Integration with known databases for variant annotation.
- Scoring system to classify variants based on pathogenic potential.
- Command-line interface for easy integration into bioinformatics workflows.

## Installation

To install PathoFinder, you will need Python 3.6 or higher. You can install it directly from GitHub using the following commands:

```bash
git clone https://github.com/benjaminesser/PathoFinder.git
cd PathoFinder
pip install .
```
You will also need to instal vcfpy. You can install it directly using:

```
pip install vcfpy
```
## Usage

To use PathoFinder, you need to prepare your genomic data in the mpileup format. Once you have your data ready, you can run PathoFinder as follows:
```
pathofinder --input your_data.mpileup --output results.vcf
```
## Arguments
```
--input path to input mpileup file
--output path where output VCF file will be saved
```
## Contributing

Contributions to PathoFinder are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

PathoFinder is open source and avaible under the MIT License.

### Explanation
