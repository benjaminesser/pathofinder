# Benchmark snpfinder vs VarScan mpileup2snp

I used the `NA12878_child.mpileup` file from lab 1 to benchmark both variant callers. This file was derived from running `samtools mpileup` on `NA12878_child.sorted.bam` against `hg19.fa` on chromosome 6 from position 128405804-128605805.

## VarScan mpileup2snp

I used the command `java -jar VarScan.jar mpileup2snp ../example_files/NA12878_child.mpileup --min-var-frequency 0.2 --min-freq-for-hom 0.8 --min-coverage 10 --min-avg-qual 0 --strand-filter 0 --output-vcf 1 --variants 1 > varscan_child.vcf` to run VarScan mpileup2snp. I chose these arguments to mimic the default functionality of `snpfinder`. 

By putting `time` before this command, we get the following output:
```
java -jar VarScan.jar mpileup2snp ../example_files/NA12878_child.mpileup  0.2  23.95s user 0.89s system 130% cpu 19.073 total
```
Adding up the user and system time to get the actual CPU time across all CPUs, this command takes 24.84s.

## snpfinder

I used the command `snpfinder ../example_files/NA12878_child.mpileup -o snpfinder_child.vcf` to run snpfinder.

By putting `time` before this command, we get the following output:
```
snpfinder ../example_files/NA12878_child.mpileup -o snpfinder_child.vcf  1.25s user 0.02s system 68% cpu 1.859 total
```
Adding up the user and system time to get the actual CPU time across all CPUs, this command takes 1.27s.

## Results

On this dataset, `snpfinder` takes only 1.27s, while `mpileup2snp` take 24.84s. That's almost 20x faster!

Unfortunately this isn't due to our genius implementation. Rather, `mpileup2snp` is doing a lot more than `snpfinder`. There many `mpileup2snp` arguments that we left out of `snpfinder`. The VCF file created by `mpileup2snp` is a lot more sophisicated, with significantly more information in the INFO, FORMAT, and SAMPLE columns (including p-values). Instead, `snpfinder` is a lightweight variant caller, focusing mostly on just finding the positions of SNPs.

## Scaling

I took 100 lines of the `NA12878_child.mpileup` and duplicated them to create different sized mpileup files to run both variant callers on.

[graph](scaling.png)

I believe both run in linear time, just with different slopes.

## Memory

Reminder to look at memory usage.