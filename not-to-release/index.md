---
layout: base
title:  'Faroese UD'
udver: '2'
---

# UD for Faroese <span class="flagspan"><img class="flag" src="../../flags/svg/FO.svg" /></span>

## Tokenization and Word Segmentation

*

---
**Instruction**: Describe the general rules for delimiting words (for example, based on whitespace and punctuation) and exceptions to these rules. Specify whether words with spaces and/or multiword tokens occur. Include links to further language-specific documentation if available.

---

## Morphology

The PoS-tags follow the universal tag set and do not add any language-specific PoS-tags. The language specific features were converted automatically to the UD scheme from the original corpus tags.

### Tags

* Faroese uses all 17 universal tags.
* The only word tagged with [PART]() is the infinitive marker *at*.
* Auxiliaries ([AUX]()) are all verbal in Icelandic and can be grouped into four types:
  * The copula *vera* (be).
  * The auxiliary *hava* (have), selects the supine form of the main verb to form perfect tenses.
  <!-- * The passive auxiliary verða (become), geta (can), fá (can) which combines with the past participle of the main verb to form passives. -->
  <!-- * Modal and aspectual verbs that combine with the bare infinitive of the main verb, such as mega (may), vilja (want), munu (will) and skulu (shall). -->
* The tag [DET]() is used for articles and pronominal words used with a determiner function, including possessives. The tag [PRON]() is reserved for pronouns occurring as the head of a noun phrase.
<!-- * Participles (both present and past) are tagged with [ADJ](). -->
* Foreign proper names are tagged [PROPN]().


### Features

* Nouns have inherent gender (masc, fem or neutral), inflect for number (singular or plural), case (nominative, accusative, dative or genitive) and can take indefinite or definite article.
* Verbs can be used in the passive and the active voice. Finite forms in indicative or subjunctive mood in addition inflect for Tense (present or past), person (1, 2 or 3) and number (singular or plural). The imperative mood inflects for number (singular or plural). There are three types of nonfinite forms: infinitives, participles (present and past), and supine (used to form perfect tenses together with the auxiliary have). The past participle additionally inflects for gender (masc, fem or neutral), number (singular or plural) and case (nom or acc).

---
**Instruction**: Describe inherent and inflectional features for major word classes (at least NOUN and VERB). Describe other noteworthy features. Include links to language-specific feature definitions if any.

---

## Syntax

*

---
**Instruction**: Give criteria for identifying core arguments (subjects and objects), and describe the range of copula constructions in nonverbal clauses. List all subtype relations used. Include links to language-specific relations definitions if any.

---

## Treebanks

There are [N](../treebanks/LCODE-comparison.html) LANGUAGE UD treebanks:

  * [LANGUAGE-A](../treebanks/LCODE_a/index.html)
  * [LANGUAGE-B](../treebanks/LCODE_b/index.html)

---
**Instruction**: Treebank-specific pages are generated automatically from the README file in the treebank repository and
from the data in the latest release. Link to the respective `*-index.html` page in the `treebanks` folder, using the language code
and the treebank code in the file name.

---
