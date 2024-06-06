## Compare vcf output with vcf file from 1000 Genomes

I took .bam files of `HG00733` chromosome 20 from 1000Genomes. I derived the `mpileup` file using `samtools mpileup` agianst `hg38.fa`, on chromosome 20 from position 10,000,000 to 10,500,000, ran it through snpfinder to get `output.vcf`
Then I downloaded a portion containing chromosome 20 of the vcf file provided for HG00733 from 1000 Genomes


## Comparing Chr20 on position 10018848 - Allele Matching:

SNPFinder VCF output file provides reference allele is `T` and alternate allele is `A` where in the 1000Genomes provided VCF file, it shows that the reference allele is `TC` and atlernate allele is `T`

This indicates a mismatch in the reference and alternate alleles between the two files which may be caused by different representations of the same genomic variation.

## Genotype Check:

SNPFinder VCF file reports a homozygous alternate genotype `(1/1)` for all its entries which means the individual is homozygous for the alternate allele at all positions listed.

However in the 1000Genomes provided VCF file, we see that at position '1001848', there is a report for homozygous reference genotype `(0/0)` which indicates no variation from the refernece genome at this position in the 1000 Genomes data.

## Comparing depth at position 10018848:

SNPFinder VCF file reports a depth of `21` for position 10018848 with a genotype `1/1`
However, the 1000Genomes VCF file provides a much higher depth, `DP=97500` which suggests extensive sampling.

## Comparing at position 10025334
Our VCF file reports reference allele of `G` and alternate allele of `A` which is the same as VCF file provided by 1000 Genomes which reports the same reference and alternate alleles. However there is a discrepency in depth coverage. In our VCF file we see a DP of `18` where as in the provided VCF file we see a DP OF `99200`.

A very high depth of coverage typically provides a strong confidence level in detection of the variant, however 18 may still be sufficicent for detecting homozygous variants. The massive difference in DP suggests that 1000 Genomes data might have been generated using high throughput sequencing that covers a larger number of reads.

## Conclusion
The discrepnancy between the alleles likely indicates a difference in how variants are annotated or interperted between different analysis pipelines.
In terms of genotype discrpency, the contrast could come from differences in sequence alignment algorthims or variant calling paramters.
In terms of depth differences, while there is high depth with 1000 Genomes, there is still moderate depth within SNPFinder VCF files, which is good for detection of homozygous variants but is less reliable for heterozygous variants.
