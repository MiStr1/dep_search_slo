# Povpraševalni jezik

Na tej strani je podrobneje predstavljen formalizem, s pomočjo katerega iščemo po skladenjsko razčlenjenih korpusih na spletnem vmesniku [Drevesnik](https://orodja.cjvt.si/drevesnik/). Temelji na povpraševalnem jeziku, razvitem znotraj orodja [dep_search](http://bionlp-www.utu.fi/dep_search/), ki smo ga za potrebe iskanja po slovenskih korpusih prilagodili tako, da omogoča tudi iskanje po oblikoskladenjskih oznakah JOS (stolpec XPOS). Možnosti iskanja so v nadaljevanju ponazorjene z nekaj izbranimi iskalnimi pogoji, na katere lahko tudi kliknemo in si ogledamo rezultate tovrstne poizvedbe v ročno označenem korpusu SSJ.

## Lastnosti pojavnice

### Iskanje po oblikah

Po besedni obliki pojavnice iščemo z vnosom poljubnega niza znakov. Primeri:

*   [hodim](https://orodja.cjvt.si/drevesnik/show/demo-hodim/sl/0/10) poišče vse pojavnice z obliko _hodim_, zapisano s samimi malimi črkami
*   [Delo](https://orodja.cjvt.si/drevesnik/show/demo-Delo/sl/0/10) poišče vse pojavnice z obliko _Delo_, zapisano z veliko začetnico

<!---
Izpuščeno, ker iskanje po atributih ali vrednostih tako ali tako ne dela, dela samo iskanje po polnem paru Atribut=Vrednost.

V malo verjetnem primeru, da je vneseno besedilo enake oblike kot ena izmed [oblikoslovnih oznak](https://universaldependencies.org/u/feat/index.html), orodje poišče pojavnice s to oznako. V tem primeru iskano besedno obliko zapišemo v narekovajih:

*   ["Gen"](http://bionlp-www.utu.fi/dep_search/?db=English&search=%22Person%22) poišče vse pojavnice z obliko _Gen_ in ne pojavnic z oznako _Gen_, ki označujejo pojavnice v rodilniku.
-->

Po osnovni obliki besede (lemi) iščemo s predpono **L=**:

*   [L=hoditi](https://orodja.cjvt.si/drevesnik/show/demo-hoditi/sl/0/10) poišče vse pojavitve pojavnic z lemo _hoditi_

### Iskanje po oblikoslovnih lastnostih

Besedno vrsto in druge oblikoslovne lastnosti pojavnice lahko opredelimo na dva načina, saj so vsi korpusi označeni tako z označevalno shemo <a href="https://nl.ijs.si/jos/" target="_blank">JOS</a> kot <a href="https://universaldependencies.org/" target="_blank">Universal Dependencies</a> (UD). Oba sistema sta dobro dokumentirana in primerljiva z vidika ustreznosti naslavljanja specifik slovenščine, zato je izbira enega ali drugega odvisna predvsem od uporabnikovih preferenc.

#### Oblikoslovne lastnosti po shemi JOS

Po oblikoskladenjskih oznakah JOS iščemo s predpopono `X=`, pri čemer je pri teh oznakah podprta tudi uporaba posebnih operatorjev `.` (ki nadomešča poljuben znak) in `*` (ki nadomešča poljubno število pojavitev znaka na levi). Glede na specifike naloženih korpusov je trenutno možno zgolj iskanje po angleški različici oznak. Primeri:

*   [X=Ncfsl](https://orodja.cjvt.si/drevesnik/show/demo-Ncfsl/sl/0/10) poišče vse pojavnice z oznako za občne samostalnike ženskega spola v mestniku ednine
*   [X=Ncf.l](https://orodja.cjvt.si/drevesnik/show/demo-Ncf_l/sl/0/10) poišče vse pojavnice z oznako za občne samostalnike ženskega spola v mestniku poljubnega števila
*   [X=Ncf.\*](https://orodja.cjvt.si/drevesnik/show/demo-Ncf_/sl/0/10) poišče vse pojavnice z oznako za občne samostalnike ženskega spola poljubnega sklona in števila

#### Oblikoslovne lastnosti po shemi UD

Po besedni vrsti UD iščemo z vpisom iskane besedne vrste, po drugih oblikoslovnih lastnostih pa z opisom iskane oznake v obliki para atributa in njegove vrednosti, npr. `Kategorija=Oznaka`. 

*   [NOUN](https://orodja.cjvt.si/drevesnik/show/demo-NOUN/sl/0/10) poišče vse pojavnice z besedno vrsto _NOUN_ (občni samostalniki).
*   [VerbForm=Inf](https://orodja.cjvt.si/drevesnik/show/demo-Inf/sl/0/10) poišče vse pojavnice z oznako za nedoločnike. 

<!---
Izpuščeno, ker iskanje po atributih ali vrednostih tako ali tako ne dela, dela samo iskanje po polnem paru Atribut=Vrednost.

Iščemo lahko tudi zgolj po oznakah, a orodje v primeru več različnikih kategorij s to oznako kot rezultat vrne samo zadetke znotraj najpogostejše kategorije. V teh primerih je zato priporočljivo iskanje z eksplicitno izpisano kombinacijo kategorije in oznake.
...
*   [Par](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=Par) searches for all tokens in partitive case (Note: _Par_ is interpreted to mean _Case=Par_)
...
*   [Past](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=Past) searches for all past tense verbs (Note: _Past_ is interpreted to mean _Tense=Past_. Other possible category for _Past_ is _PartForm_, and to search for past participles _PartForm=Past_ must be typed.)
...
Možno je tudi iskanje po kategorijah brez opredelitve oznak:

*   [PartForm](http://bionlp-www.utu.fi/dep_search/?db=Finnish&search=PartForm) poišče deležnike v vseh oblikah: sedanjiku (PartForm=Pres), pretekliku (PartForm=Past) ...
--->

### Posebni operatorji
  
Vse zgoraj navedene lastnosti pojavnice lahko med seboj tudi kombiniramo s posebnima operatorjema **&** (in) oz. **|** (ali):

*   [lepo&X=R.\*](https://orodja.cjvt.si/drevesnik/show/demo-lepo_R/sl/0/10) poišče vse pojavnice z obliko _lepo_, ki so po shemi JOS označene kot prislov (in ne npr. pridevnik)
*   [L=delati|L=narediti](https://orodja.cjvt.si/drevesnik/show/demo-op_delati-narediti/sl/0/10) poišče vse pojavnice z lemo _delati_ ali _narediti_
*   [NOUN&Number=Plur](https://orodja.cjvt.si/drevesnik/show/demo-op_NOUN-Plur/sl/0/10) poišče vse samostalnike v množini
*   [L=prst&Gender=Masc](https://orodja.cjvt.si/drevesnik/show/demo-op_prst-Masc/sl/0/10) poišče vse pojavnice z lemo _prst_ moškega spola

Pri iskanju po besednih oblikah, lemah in oznakah lahko uporabimo tudi **negacijo** z vpisom operatorja **!** pred lastnostjo, po kateri ne želimo iskati. Primeri:

*   [L=biti&!AUX](https://orodja.cjvt.si/drevesnik/show/demo-neg_biti-AUX/sl/0/10) poišče vse pojavnice z lemo _biti_, ki niso označene kot pomožni glagol
*   [ADJ&!X=A.\*](https://orodja.cjvt.si/drevesnik/show/demo-neg_ADJ-A/sl/0/10) poišče vse pojavnice, ki so po shemi UD označene kot pridevnik, po shemi JOS pa ne

Za iskanje po pojavnicah brez opredeljenih lastnosti uporabimo podčrtaj (\_).

## Skladenjske relacije

Skladenjske relacije zapisujemo z operatorjema `<` in `>`, ki posnemata puščice, s kakršnimi so običajno ponazorjena skladenjska razmerja med besedami v odvisnostno razčlenjenih povedih (odvisnostnih drevesih).

*   `A < B` pomeni, da je pojavnica A podrejena pojavnici B, npr. _deževno_ < _jutro_
*   `A > B` pomeni, da je pojavnica A nadrejena pojavnici B, npr. _berem_ > _časopis_

Podčrtaj \_ predstavlja _katerokoli pojavnico_, torej pojavnico, ki ji ne želimo opredeliti dodatnih lastnosti. Spodaj navajamo nekaj preprostih primerov iskanj po odvisnostnih skladenjskih strukturah:

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
