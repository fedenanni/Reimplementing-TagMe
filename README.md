# Reimplementing-TagMe
How to re-build the Entity Linker [TagMe](http://pages.di.unipi.it/ferragina/cikm2010.pdf) in a few scripts, starting from a Wikipedia Dump. This work is inspired by the paper "On the Reproducibility of the TAGME Entity Linking System" [[paper](http://hasibi.com/files/ecir2016-tagme.pdf), [code](https://github.com/hasibi/TAGME-Reproducibility)].

## Step-By-Step Procedure

### Process a Wikipedia Dump

Download a Wikipedia dump from [here](https://dumps.wikimedia.org/enwiki/) and process it with the [WikiExtractor](http://medialab.di.unipi.it/wiki/Wikipedia_Extractor) with the following command:

```
python python WikiExtractor.py -l -s -o output/ [here put the path to the Wikipedia Dump .xml.bz2]
```
Note that the flag -s will keep the sections and the flag -l the links.

### Extract entity, mention and ngram frequencies + entity aspects

Having the Wiki dump processed by the WikiExtractor in the "output/" folder, the first step is to collect a set of all entity-mentions in Wikipedia, so that you can later collect their frequency as ngrams. You can do this by using 
```
1-CollectAllMentions.ipynb 
```
that will produce a all_mentions.pickle file.

The second step will extract mention, ngrams and entity counts as well as mention_to_entities statistics (e.g., how many times the mention "Obama" is pointing to "Barack_Obama" and how many times to "Michele_Obama"). Statistics are still divided in the n-folders consituting the output of the WikiExtractor and will be saved in the "Store-Counts/" folder as json files. The script will also store a .json file for each entity, with all its aspects (see [here](https://madoc.bib.uni-mannheim.de/49596/1/EAL.pdf) to know more about Entity-Aspect Linking). 
```
2-ExtractingFreqAndAspects.ipynb
```

The final pre-processing script will aggregate all counts needed for using TagMe in single .pickle files and save them in the "Resources/" folder. You can do this by running:
```
3-AggregateCounts.ipynb
```
Note that after having processed each json from "Store-Counts/", the script will save an intermediate count in "Resources/". This way you could start already using TagMe, with partial statistics.

### Download resources

To use directly my reimplementation of TagMe withouth processing a Wikipedia dump you can download all resources needed from [here]().
