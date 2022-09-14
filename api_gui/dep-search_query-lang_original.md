# Povpraševalni jezik

Na tej strani je podrobneje predstavljen formalizem, s pomočjo katerega iščemo po skladenjsko razčlenjenih korpusih na spletnem vmesniku [Drevesnik](https://orodja.cjvt.si/drevesnik/). Temelji na povpraševalnem jeziku, razvitem znotraj orodja [dep_search](http://bionlp-www.utu.fi/dep_search/), ki smo ga za potrebe iskanja po slovenskih korpusih prilagodili tako, da omogoča tudi iskanje po oblikoskladenjskih oznakah JOS (stolpec XPOS).

Možnosti iskanja so ponazorjene z nekaj izbranimi iskalnimi pogoji, na katere lahko tudi kliknemo in si ogledamo rezultate tovrstne poizvedbe v ročno označenem korpusu SSJ.

## Lastnosti pojavnice

### Iskanje po oblikah

Po besedni obliki pojavnice iščemo z vnosom poljubnega niza znakov. Primeri:

*   [hodim](https://orodja.cjvt.si/drevesnik/show/help-hodim/sl/0/10) poišče vse pojavnice z obliko _hodim_, zapisano s samimi malimi črkami
*   [Baron](https://orodja.cjvt.si/drevesnik/show/help-Baron/sl/0/10) poišče vse pojavnice z obliko _Baron_, zapisano z veliko začetnico

<!---
Izpuščeno, ker iskanje po atributih ali vrednostih tako ali tako ne dela, dela samo iskanje po polnem paru Atribut=Vrednost.

V malo verjetnem primeru, da je vneseno besedilo enake oblike kot ena izmed [oblikoslovnih oznak](https://universaldependencies.org/u/feat/index.html), orodje poišče pojavnice s to oznako. V tem primeru iskano besedno obliko zapišemo v narekovajih:

*   ["Gen"](http://bionlp-www.utu.fi/dep_search/?db=English&search=%22Person%22) poišče vse pojavnice z obliko _Gen_ in ne pojavnic z oznako _Gen_, ki označujejo pojavnice v rodilniku.
-->

Po osnovni obliki besede (lemi) iščemo s predpono `L=`:

*   [L=hoditi](https://orodja.cjvt.si/drevesnik/show/help-hoditi/sl/0/10) poišče vse pojavnice glagola _hoditi_

### Iskanje po oblikoslovnih lastnostih

*   ["Person"](http://bionlp-www.utu.fi/dep_search/?db=English&search=%22Person%22) searches for literal text _Person_ and not the tag _Person_

**Base form (lemma)** is given with the L= prefix.

*   [L=olla](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=L%3Dolla) searches for all forms of the Finnish verb _olla_

**POS and other morphological tags** can be specified by writing the tags as-is. If the tags are in form of Category=Tag, only tag part must be written. However, if multiple categories have the same tag value, the tag is mapped into the most frequent category. To seach other possible categories, also the category name must be specified.

*   [NOUN](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=NOUN) searches for all tokens with the POS tag _NOUN_
*   [Par](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=Par) searches for all tokens in partitive case (Note: _Par_ is interpreted to mean _Case=Par_)
*   [VerbForm=Inf](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=VerbForm%3DInf) searches for all infinitives
*   [Past](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=Past) searches for all past tense verbs (Note: _Past_ is interpreted to mean _Tense=Past_. Other possible category for _Past_ is _PartForm_, and to search for past participles _PartForm=Past_ must be typed.)

Also the whole categories can be searched. This is done by typing just the plain category name the same way than the tag values are used.

*   [PartForm](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=PartForm) searches for all participles: present (PartForm=Pres), past (PartForm=Past), agentive (PartForm=Agt) and negative (PartForm=Neg)

The full set of categories and tags used in any supported corpus can be found under the _Show types_ link on the main page (see e.g. [English](http://bionlp-www.utu.fi/dep_search/types/English) and [Czech](http://bionlp-www.utu.fi/dep_search/types/Czech)).  
  
It is also possible to combine all above token specification with AND (&) and OR (|) operators:

*   [walk&NOUN](http://bionlp-www.utu.fi/dep_search/?db=English&search=walk%26NOUN) searches for the word _walk_ when it is a noun, not verb
*   [NOUN&Plur&Par](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=NOUN%26Plur%26Par) searches for nouns in plural partitives
*   [L=tehdä&PartForm=Pres](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=L%3Dtehd%C3%A4%26PartForm%3DPres) searches for present participles of the verb _tehdä_
*   [L=kävellä|L=juosta](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=L%3Dk%C3%A4vell%C3%A4%7CL%3Djuosta) searches for all words with lemma _kävellä_ or _juosta_

Word forms, lemmas and tags can also be **negated** by typing the negation operator ! before the property.

*   [can&!AUX](http://bionlp-www.utu.fi/dep_search/?db=English&search=can%26%21AUX) searches for the word _can_ when it is not an auxiliary
*   [!Tra](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=%21Tra) searches for words which are not in translative case
*   [voi&!L=voida](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=voi%26%21L%3Dvoida) searches for the word _voi_ when the lemma is not _voida_

**Token can be left unspecified by typing an underscore character (\_).**

Dependency specification
------------------------

Dependencies are expressed using < and \> operators. These operators mimick "arrows" in the dependency graph.

*   token1 < token2 token1 is governed by token2
*   token1 > token2 token1 governs token2

The underscore character \_ stands for _any token_, that is, a token on which we place no particular restrictions. Here are simple examples of basic search expressions that restrict dependency structures:

*   [walk < \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=walk%20%3C%20_) searches for all cases of _walk_ which are governed by some word
*   [walk > \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=walk%20%3E%20_) searches for all cases of _walk_ which govern a word
*   [\_ < walk](http://bionlp-www.utu.fi/dep_search/?db=English&search=_%20%3C%20walk) searches for any token governed by _walk_

Note that the left-most token in the expression is always the target of the search and also identified in search results. While queries \_ <nsubj \_ and \_ >nsubj \_ match the excact same graphs, returned tokens differ.

The **dependency type** can be specified typing it right after the dependency operator: \_ <type \_ or \_ >type \_. The | character denotes a logical _or_, so any of the given dependency relations will match.

*   [\_ <cop \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=_%20%3Ccop%20_) searches for all copula verbs (are governed through a cop dependency)
*   [\_ >nsubj:cop \_](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=_%20%3Ensubj%3Acop%20_) searches for all words serving as a predicative in copula structures (govern a copula subject)
*   [\_ <nsubj|<nsubj:cop \_](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=_%20%3Cnsubj%7C%3Cnsubj%3Acop%20_) searches for all words serving as a subject - both standard and copula subject

You can specify a number of dependency restrictions at a time by chaining the operators:

*   [\_ >nsubj:cop \_ >cop \_](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=_%20%3Ensubj%3Acop%20_%20%3Ecop%20_) searches for words that govern both a copula subject and a copula verb
*   [\_ <nsubj:cop \_ >nmod \_](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=_%20%3Cnsubj%3Acop%20_%20%3Enmod%20_) searches for words that serve as a copula subject and at the same govern a nominal modifier
*   [\_ >nmod \_ >nmod \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=_%20%3Enmod%20_%20%3Enmod%20_) searches for words that govern two distinct nominal modifiers

Priority is marked using parentheses:

*   [\_ >nmod \_ >nmod \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=_%20%3Enmod%20_%20%3Enmod%20_) searches for words that govern two distinct nominal modifiers (two nommod dependencies in parallel)
*   [\_ >nmod (\_ >nmod \_)](http://bionlp-www.utu.fi/dep_search/?db=English&search=_%20%3Enmod%20%28_%20%3Enmod%20_%29) searches for words that govern a nominal modifier which, in turn governs another nominal modifier (chain of two nmod dependencies)
*   [NOUN >amod (\_ >amod|>acl \_)](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=NOUN%20%3Eamod%20%28_%20%3Eamod%7C%3Eacl%20_%29) searches for nouns that govern an adjectival modifier, where the adjectival modifier itself governs either another adjectival modifier or a participial modifier

**Negation** is marked using the negation operator !. Currently, you can negate the < and \> operators as well as dependency types as follows:

*   [\_ >nsubj:cop \_ !>cop \_](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=_%20%3Ensubj%3Acop%20_%20%21%3Ecop%20_) searches for all copula predicatives (governors of nsubj:cop dependents) that do not have a copula verb (do not govern a cop dependent)
*   [\_ <advcl \_ !>mark \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=_%20%3Cadvcl%20_%20%21%3Emark%20_) searches for heads of unmarked adverbial clauses (governed by advcl but not governing mark)
*   [\_ <nsubj \_ !(>amod|>acl) \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=_%20%3Cnsubj%20_%20%21%28%3Eamod%7C%3Eacl%29%20_) searches for subjects which do not govern adjectival or participial modifiers
*   [\_ <nsubj \_ >!amod \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=_%20%3Cnsubj%20_%20%3E%21amod%20_) searches for subjects which governs something but it cannot be an adjective (governed by nsubj and governs something which is not amod)

Note that in \_ !>amod \_ it is accepted that the token does not have any dependent, whereas in \_ >!amod \_ the token must have at least one dependent which is not _amod_.

**Direction** of the dependency relation can be specified using operators @R and @L, where the operator means that the right-most token of the expression must be at the right side or at the left side, respectively.

*   [VERB >nsubj@R \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=VERB%20%3Ensubj%40R%20_) searches for verbs which have _nsubj_ dependent to the right
*   [\_ >amod@L \_ >amod@R \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=_%20%3Eamod%40L%20_%20%3Eamod%40R%20_) searches for words that have two distinct adjectival modifiers (two _amod_ dependencies in parallel), one must be at the left side, the other at the right side
*   [\_ <case@R \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=_%20%3Ccase%40R%20_) searches for case markers where the governor token is at the right side, i.e. prepositions (as compared to postpositions)

Combining queries
-----------------

Several queries can be combined with the + operator. A query of the form query1 + query2 + query3 returns all trees which independently satisfy all three queries.

*   [(VERB >aux \_ >aux \_) + (\_ >conj (\_ >conj \_))](http://bionlp-www.utu.fi/dep_search/?db=English&search=%28VERB%20%3Eaux%20_%20%3Eaux%20_%29%20%2B%20%28_%20%3Econj%20%28_%20%3Econj%20_%29%29) searches for trees with a double auxiliary and a nested coordination

Universal quantifcation
-----------------------

An expression of the form [\_ -> NOUN](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=_%20-%3E%20NOUN) means "every token (\_) must be a NOUN" or in other words being a token implies being a NOUN. This is a form of universal quantification. Full tree specifications are allowed on both the left and the right side of the expression, so for example [NOUN -> NOUN <acl:relcl \_](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=NOUN%20-%3E%20NOUN%20%3Cacl%3Arelcl%20_) means "all nouns are governed by acl:relcl"

### Examples

Here we give some additional examples, all of which are "clickable" and search for the given expression in the currently released version of the general Finnish treebank.

*   [\_ <nmod \_ !>case \_](http://bionlp-www.utu.fi/dep_search/?db=English&search=_%20%3Cnmod%20_%20%21%3Ecase%20_) Nominal modifiers without case markers
*   [\_ >nsubj:cop \_ !>cop \_](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=_%20%3Ensubj%3Acop%20_%20%21%3Ecop%20_) Cases of dropped copula verb.
*   [ADJ&Tra <xcomp \_](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=ADJ%26Tra%20%3Cxcomp%20_) Adjective complemets in translative case
*   [VerbForm=Part <acl \_ >nsubj \_](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=VerbForm%3DPart%20%3Cacl%20_%20%3Ensubj%20_) Participial modifiers with a subject
