## Compare vcf output with vcf file from 1000 Genomes

I took .bam files of `HG00733` chromosome 20 from 1000Genomes. I derived the `mpileup` file using `samtools mpileup` agianst `hg38.fa`, on chromosome 20 from position 10,000,000 to 10,500,000, ran it through `snpfinder` to get `output.vcf`
Then I downloaded a portion containing chromosome 20 of the vcf file provided for HG00733 from 1000 Genomes, `1000.vcf`. This file is too large to include in this repo, to compare you need to download it yourself.

## Commands I used to create `mpileup` from `.bam`

To download specific genomic region from chromosome 20 `.bam ` file:
`samtools view -b "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/HG00733/exome_alignment/HG00733.chrom20.ILLUMINA.bwa.PUR.exome.20130422.bam" 20:10000000-10090000 > output.bam `

This provided me with filtered `output.bam` which I then used to convert to `output.mpileup`

To generate `mpileup` from `output.bam`:
`samtools mpileup -f ~/public/genomes/hg38.fa output.bam > output.mpileup`

To download specific genomic region from chromosome 20:
`tabix -h ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/20201028_3202_raw_GT_with_annot/20201028_CCDG_14151_B01_GRM_WGS_2020-08-05_chr20.recalibrated_variants.vcf.gz chr20:10018820-10026000 > updated_specific_region_chr20.vcf`

This provides me with the public dataset `.vcf ` file I want to use to compare my datasets.

## Comparing Chr20 on position 10018848 - Allele Matching:

`snpfinder` VCF output file provides reference allele is `T` and alternate allele is `A` where in the 1000Genomes provided VCF file, it shows that the reference allele is `TC` and atlernate allele is `T`

This indicates a mismatch in the reference and alternate alleles between the two files which may be caused by different representations of the same genomic variation.

## Genotype Check:

`snpfinder` VCF file reports a homozygous alternate genotype `(1/1)` for all its entries which means the individual is homozygous for the alternate allele at all positions listed.

However in the 1000Genomes provided VCF file, we see that at position '1001848', there is a report for homozygous reference genotype `(0/0)` which indicates no variation from the refernece genome at this position in the 1000 Genomes data.

## Comparing depth at position 10018848:

`snpfinder` VCF file reports a depth of `21` for position 10018848 with a genotype `1/1`
However, the 1000.vcf file provides a much higher depth, `DP=97500` which suggests extensive sampling.

## Comparing at position 10025334

Our output.vcf file reports reference allele of `G` and alternate allele of `A` which is the same as VCF file provided by 1000 Genomes which reports the same reference and alternate alleles. However there is a discrepency in depth coverage. In our VCF file we see a DP of `18` where as in the provided VCF file we see a DP OF `99200`.

A very high depth of coverage typically provides a strong confidence level in detection of the variant, however 18 may still be sufficicent for detecting homozygous variants. The massive difference in DP suggests that 1000 Genomes data might have been generated using high throughput sequencing that covers a larger number of reads.

## Comparing at position 10019063

In our VCF file, the position at chromosome 20, shows a `C>A` mutation, same as in the VCF file downloaded from 1000 genomes. However again we see that in our VCF file, the genotype shows homozygous alternate `(1/1)` where as in the other we see mixture of genotypes, with the majority being homozygous reference `(0/0)`. This discrepancy in genotype calls could be due to differences in variant calling parameters. The depth of coverage in our output.vcf file shows to be `217` while in the 1000.vcf the depth of coverage is much higher, at `94876`.

## Comparing at position 10018974

Both files show the same reference allele `C` however we have a discrepency when it comes to alternate alleles. In output.vcf we see `G` as the alternate allele compared to `T` in 1000.vcf. Our VCF reports `DP=133`, which is higher than some other positions we have looked at. 1000.vcf reports `DP=97976`, which is commonly high depth of coverage we have seen for this vcf file. The extensive data also includes various genotypes across multiple samples, suggesting wide variability. While we commonly see homozygous alternate `(1/1)` in output.vcf.

## Conclusion

The discrepnancy between the alleles likely indicates a difference in how variants are annotated or interperted between different analysis pipelines. 

It's important to note that we do not know the variant caller used to generate this VCF file on 1000 Genomes. It's quite likely that this file was generated using very different filtering mechanisms than `snpfinder`'s default parameters.
