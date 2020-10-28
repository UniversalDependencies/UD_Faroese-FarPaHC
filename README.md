# Summary

UD_Icelandic-FarPaHC is a conversion of the [Faroese Parsed Historical Corpus (FarPaHC)](https://github.com/einarfs/farpahc) to the Universal Dependencies scheme.

The conversion was done using [UDConverter](https://github.com/thorunna/UDConverter).

# Introduction

The Faroese Parsed Historical Corpus (FarPaHC) is a 53,000 word corpus which includes three texts from the 19th and 20th centuries. These texts were originally manually parsed according to the Penn Parsed Corpora of Historical English (PPCHE) annotation scheme. Two of these parsed texts where then automatically converted to the Universal Dependencies scheme to create UD_Faroese-FarPaHC.

## Contents

### Files

UD_Faroese-FarPaHC consists of two Faroese texts:

- `NTACTS` -  Acts of the Apostles. Edition: 1937.

      Author:      Jákup Dahl
      Birthdate:   1878, died 1944 on his birthday, 5 June
      TextId:      ntacts
      Textname:    Ápostlasögan (Acts of the Apostles)[Originally published in Varðin 8, 1928, 
                   as Ápostlasögan og hini almennu brævini (Acts of the Apostles and the Letters)]
      Edition:     "1937. Nýggja Testamenti. [The New Testament]
                   Givið út hevur Det danske Bibelselskab. [Published by the Danish Bible Society]
                   P. Haase og söns boghandel, Keypmannahavn. [Copenhagen]"
      Text online: http://old.bibelselskabet.dk/farbib/web/bibelen.htm
      Translation: From Greek
      Date:        1928
      Text genre:  Bible translation
      Wordcount:   17758 
      Sample:      Sample is from Acts 1:1-17:34, pp. 251-295

- `NTJOHN` - Gospel of St. John. Edition: 1937.

	  Author:       Jákup Dahl
	  Birthdate:    1878, died 1944 on his birthday, 5 June
	  TextId:       ntjohn
	  Textname:     Evangeliið eftir Jóhannes, (Gospel of St. John) [Originally published in Varðin 16, 1936.]
	  Edition:      "1937. Nýggja Testamenti. [The New Testament] 
	                Givið út hevur Det danske Bibelselskab. [Published by the Danish Bible Society] 
	                P. Haase og söns boghandel, Keypmannahavn. [Copenhagen]"
	  Text online:  http://old.bibelselskabet.dk/farbib/web/bibelen.htm
	  Translation:  From Greek
	  Date:         1936
	  Text genre:   Bible translation
	  Wordcount:    23873
	  Sample:       Exhaustive sample of John, pp. 196-250
    
### Sentences

Each sentence ID in UD_Faroese-FarPaHC  carries the following information:

Example ID: `1928.NTACTS.REL-BIB,1.1`

- Publication year of the text (`1928`)
- Name of the text (`NTACTS`)
- Text genre (`REL-BIB`)
- Index within text (`1`)
- Index within file (`1`)

As all the texts in the corpus are excerpts from the Bible, the only text genre present in the sentence IDs is `REL-BIB`, i.e., _religious text, biblical_.

### Additional notes: Morphological Features

The UD morphological features in the corpus were converted from the FarPaHC PoS tags, which do not encode all possible grammatical categories for the language as described by the [UD language documentation for Faroese](https://universaldependencies.org/is/index.html). The features that do appear in UD_Faroese-FarPaHC are shown below, organised by grammatical category.

- Nouns: `Case`, `Definite`, `Number`
- Verbs: `Tense`, `Mood`, `Verbform`, `Case`
- Pronouns: `Case`, `Gender`, `Number`
- Numerals: `Case`
- Adjectives: `Case`, `Degree`
- Adverbs: `Case`, `Degree`, (`Definite`, `Number`)
- Determiners: `Case`
- Other: `Foreign`

## Data split

**TRAIN:**
- `1936.NTJOHN.REL-BIB`

**DEV:**
- First 300 sentences from `1928.NTACTS.REL-BIB`

**TEST:**
- Last 300 sentences from `1928.NTACTS.REL-BIB`

# Acknowledgments

This project is funded by The Icelandic Student Innovation Fund, grant no. 206457-0091.

## References

* (citation)


# Changelog

* 2020-11-15 v2.7
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.7
License: CC BY-SA 4.0
Includes text: yes
Genre: fiction bible nonfiction
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: converted from manual
Relations: converted from manual
Contributors: Arnardóttir, Þórunn; Hafsteinsson, Hinrik; Sigurðsson, Einar Freyr; Ingason, Anton Karl; Rögnvaldsson, Eiríkur; Wallenberg, Joel
Contributing: elsewhere
Contact: thar@hi.is, hinrik.hafst@gmail.com, einar.freyr.sigurdsson@arnastofnun.is
===============================================================================
</pre>
