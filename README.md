# Reimplementing-TagMe
A few scripts for using the Entity Linker [TagMe](http://pages.di.unipi.it/ferragina/cikm2010.pdf), starting from a Wikipedia Dump. This work is inspired by the paper "On the Reproducibility of the TAGME Entity Linking System" [[paper](http://hasibi.com/files/ecir2016-tagme.pdf), [code](https://github.com/hasibi/TAGME-Reproducibility)].

## Starting Point

Download a Wikipedia dump from [here](https://dumps.wikimedia.org/enwiki/) and process it with the [WikiExtractor](http://medialab.di.unipi.it/wiki/Wikipedia_Extractor) with the following command:

```
python python WikiExtractor.py -s -o output/ -l enwiki-20190401-pages-articles-multistream.xml.bz2
```

