# Summary

UD_Icelandic-FarPaHC is a conversion of the [Faroese Parsed Historical Corpus (FarPaHC)](https://github.com/einarfs/farpahc) to the Universal Dependencies scheme
<!-- 1-2 sentences (see [release checklist](http://universaldependencies.org/release_checklist.html#the-readme-file) for README guidelines) ... -->

The conversion was done using [UDConverter](https://github.com/thorunna/UDConverter).

# Introduction

The Faroese Parsed Historical Corpus (FarPaHC) is a 53,000 word corpus which includes three texts from the 19th and 20th centuries. These texts were originally manually parsed according to the Penn Parsed Corpora of Historical English (PPCHE) annotation scheme. Two of these parsed texts where then automatically converted to the Universal Dependencies scheme to create UD_Faroese-FarPaHC.

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
Contributors: Sigurðsson, Einar Freyr
Contributing: elsewhere
Contact: einar.freyr.sigurdsson@arnastofnun.is
===============================================================================
</pre>
