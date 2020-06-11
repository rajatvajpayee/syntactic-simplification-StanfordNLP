# Text Simplification


## Overview
It is a rule based approach for sentence simplification, implemented from the paper “A NovelSystem for Generating Simple Sentences from Complex and Compound Sentences”.

This method used Stanford Parser and Stanford CoreNLPto simplify sentences. Parser provides the dependency parsing and Coreference Resolution system of CoreNLP helps to solve coreference problem.

According to the Stanford Typed Dependency Manual, a simple sentence will have only one ‘nsubj’ or ‘nsubjpaas’

## Algorithm
```
> Break text into group of sentences { S1, S2, ………….. Si }
> For each sentence in { S1,……………… Si }
>> Create Basic and Collapsed SD of Si using Stanford Parser.
>> Generate Modified SD (MSD) of Si by taking subject clauses, ‘nsubj’ or ‘nsubjpass’ from Collapsed SD and other linked parts from Basic SD.
>> Remove dependencies, marked as ‘acl’, ‘appos’, ‘advcl’, ‘cc’, ‘ccomp’, ‘conj’, ‘dep’, ‘mark’, ‘parataxis’ and ‘ref’.
>> Identify subject clause ‘nsubj’ or ‘nsubjpass’.
>> Traverse all the parts that have links to each subject clause (‘nsubj’ or ‘nsubjpass’) and find the linked words.
>> Rearrange the words found in Step 5 to generate the complete simple sentences.
```

For example :
SachinTendulkar, who is a MP of Indian Parliament, played cricket’.

Following are the basic and modified dependencies obtained from the stanford parser-

Basic Stanford Dependencies | Modified Stanford Dependencies
----------------------------|------------------------------
compound(Tendulkar-2, Sachin-1)|nsubj(MP-7, Tendulkar-2)
nsubj(played-12, Tendulkar-2)|nsubj(played-12, Tendulkar-2)
nsubj(MP-7, who-4)|compound(Tendulkar-2, Sachin-1)
cop(MP-7, is-5)|cop(MP-7, is-5)
det(MP-7, a-6)|det(MP-7, a-6)
acl:relcl(Tendulkar-2, MP-7)|case(Parliament-10, of-8)
case(Parliament-10, of-8)|compound(Parliament-10, Indian-9)
compound(Parliament-10, Indian-9)|nmod(MP-7, Parliament-10)
nmod(MP-7, Parliament-10)|root(ROOT-0, played-12)
root(ROOT-0, played-12)|dobj(played-12, cricket-13)
dobj(played-12, cricket-13)|


Obtained Modified Stanford Dependencies are arranged according to the number linked with it.
Here in the current example, we obtained two ‘nsubj’
1. nsubj(MP-7, Tendulkar-2)
2. nsubj(played-12, Tendulkar-2)

Now for each ``nsubj`` we arrange the rest dependencies in order -
1. Sachin{1} Tendulkar{2} is{5} a{6} MP{7} of{8} Indian{9} Parliament{10}
2. Sachin{1} Tendulkar{2} played{12} cricket{13}

## Disadvantage
It highly rule based methods and it can produce false results even with a small error. Below are the outputs from the algorithm

**Original Sentence :**
Do not drive forward if obstacles are closer than 5m

**Result:**
['Obstacles are closer 5m ahead','Do not drive forward']

But, if there is a grammatical error in the sentence.

**Original Sentence :**
Do not drive forward if obstacles closer than 5m

**Result:**
['Do not drive forward']

Here, it is clearly visible that a grammatical mistake of ‘are’ has changed the whole meaning of the sentence.


## Usage

1. Download Stanford-nlp-core
> wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip

2. Unzip this core file 
> unzip stanford-corenlp-full-2018-10-05.zip

3. Install requirements 
> pip install -r requirements.txt

4. Run 
> python main.py



