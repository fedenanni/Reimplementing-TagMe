# Reimplementing-TagMe
A few scripts for using the Entity Linker [TagMe](http://pages.di.unipi.it/ferragina/cikm2010.pdf), starting from a Wikipedia Dump. This work is inspired by the paper "On the Reproducibility of the TAGME Entity Linking System" [[paper](http://hasibi.com/files/ecir2016-tagme.pdf), [code](https://github.com/hasibi/TAGME-Reproducibility)].

## Starting Point

Download a Wikipedia dump from [here](https://dumps.wikimedia.org/enwiki/) and process it with the [WikiExtractor](http://medialab.di.unipi.it/wiki/Wikipedia_Extractor) with the following command:

```
python python WikiExtractor.py -l -s -o output/ [here put the path to the Wikipedia Dump .xml.bz2]
```
Note that the flag -s will keep the sections and the flag -l the links.

Having the Wiki dump processed by the WikiExtractor in the output/ folder, the first step is to collect a set of all entity-mentions in Wikipedia, so that you can later collect their appearance as ngrams. You do this by using the **1-CollectAllMentions.ipynb** that will produce a all_mentions.pickle file. 


