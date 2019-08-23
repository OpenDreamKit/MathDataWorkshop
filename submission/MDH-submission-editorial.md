# Submission/Editorial Process for MathDataHub (First Thoughts)

This is a working document capturing the discussions at the [Math Data Workshop](https://opendreamkit.org/2019/08/17/WorkshopOnDataInMathematics/). 

## Background
The [MathDataHub System (MDH)](htp://mdhalpha.mathhub.info) collects Mathematical Data sets. The data sets are described formally via a

1.  schema theory, that describes the database schema and its relation to the mathematics
2. a (flexible) formalization of the mathematical background theory, and a 
3. set of codecs that mediate between the database level in 1. and the mathematical level in 2. programmatically.
4. a formalization of dataset provenance.
5. a human-readable (i.e. natural language; usually English) document that describes all of the above to the human readers. 

Given such a description, MDH generate a database extension and an importer from a JSON (or soon CSV) file that contains the dataset data in structured form. 

## This document 
describes the process for dataset submission (technical) and the editorial process (mathematical) for MDH.

## People involved and their Roles

There are five kinds of roles in MDH (there may be more, but these suffice for this document)

1. **Developers** who create and maintain the system code, data structure, and user interfaces. Currently Katja Bercic and Tom Wiesing.
2. **Knowledge Engineers** who create flexiformalizations and codecs. Currently, Dennis Müller, Florian Rabe, and Michael Kohlhase
3. **Dataset Authors** who create datasets, specify the mathematical objects involved, and provide provenance.
4. **Editors** who organize the mathematical evaluation of the data set and the technical creation of the formal submission. 
5. **Readers** who use the MDH system to gain knowledge about the mathematical objects. 

The first four categories contribute to the submission and editorial processes. 

## Dataset Preparation (Technical)

A potential 

<!--  LocalWords:  formalization Bercic flexiformalizations
 -->
