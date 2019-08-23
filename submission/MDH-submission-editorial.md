# Submission/Editorial Process for MathDataHub (First Thoughts)

**Manifest**: This is a working document capturing the discussions at the
[Math Data Workshop](https://opendreamkit.org/2019/08/17/WorkshopOnDataInMathematics/).

**Author**: Michael Kohlhase, Computer Science,  FAU Erlangen Nürnberg, Germany

**Date**: August 2019. 

## 1. Background
The [MathDataHub System (MDH)](htp://mdhalpha.mathhub.info) collects Mathematical Data sets. The data sets are described formally via a

1. **schema theory** that describes the database schema and its relation to the mathematics,
2. a (flexible) **formalization of the mathematical background theory**, 
3. a set of **codecs** that mediate between the database level in 1. and the mathematical level in 2. programmatically.
4. a formalization of **dataset provenance**.
5. a **human-readable** (i.e. natural language; usually English) **document** that describes all of the above to the human readers. 

Given such a description, MDH generate a database extension and an importer from a JSON (or soon CSV) file that contains the dataset data in structured form. 

## 2. This document 
describes the process for dataset submission (technical) and the editorial process (mathematical) for MDH.

## 3. People involved and their Roles

There are six kinds of roles in MDH (there may be more, but these suffice for this document)

1. **Developers** who create and maintain the system code, data structure, and user interfaces. Currently Katja Bercic and Tom Wiesing.
2. **Knowledge Engineers** who create flexiformalizations and codecs. Currently, Dennis Müller, Florian Rabe, and Michael Kohlhase
3. **Dataset Authors** who create datasets, specify the mathematical objects involved, and
    provide provenance.
4. **Editors** who organize the mathematical evaluation of the data set and the technical
    creation of the formal submission. Currently, the Editors are
	[Katja Bercic](http://kwarc.info/people/kbercic/) and
	[Michael Kohlhase](http://kwarc.info/people/mkohlhase/). 
5. **Reviewers** who supply mathematical domain expertise and review
   submissions. Currently, these include
   [Gabriel Cunningham](http://www.gabrielcunningham.com) and
   [Jukka Kohohnen](http://math.aalto.fi/en/people/jukka.kohonen) 
6. **Readers** who use the MDH system to gain knowledge about the mathematical objects. 

The first four categories contribute to the submission and editorial processes. 

## 4. Dataset Preparation (Technical/Editorial)

Here are the steps of a MDH submission process; a new step is only started when the
previous one was successful.  

1. **Exposee**:  A potential dataset author *A* contacts an MDH editor *E*  with a
   human-oriented description *H*  of the proposed dataset submission *D*.
2. **Hosting Evaluation**:  *E* organizes a scientific evaluation of the novelty, interest, and plausibility of the
   data set, possibly involving reviewers as external domain experts in the process. Note that the goal
   of this evaluation is to decide on whether MDH wants to host the data set *D* and
   therefore will be quite quick and benevolent.
3. **Dataset Preparation**: *E* brings *A* into contact with some knowledge engineer *K*
who collaborates with *A* on the actual dataset submission. Together they 
   1. determine whether new codecs are necessary for *D*. If so, *K* prepares these using
   *A* as a domain expert.
   2. formalize the background theory in particular working out the mathematical type of
      the objects involved and defining the properties featured as columns in the
      dataset. 
   3. prepare a schema theory *S* for *D*, mostly by selecting codecs for the mathematical
      types from step 2. and then determining a subset of properties that form a key.
   4. bringing the dataset *D* into a form that is acceptable by the MDH importer
      generated from *S*.
   5. formalizing the dataset provenance for *D*

    All of these are iterated in a special a dedicated branch in a special MDH submission
	repository on http://gl.mathhub.info for safekeeping, reference, and accountability. 
4. **Dataset Evaluation**: The dataset *D* (or a subset, iff space matters) is uploaded to
   a public test server for MDH and the generated User Interface is evaluated by *E* and
   *A* together. This evaluation includes an integration test with existing datasets. Note
   that while the test server is public, any identifiers will be preliminary. 
   This evaluation process can result in an iteration over the dataset preparation step. In
   this step the human-oriented document *H* is also updated and prepared for publication
   on MDH.
5. **Dataset Deployment**: *D* and *H* are deployed on MDH and announced to the
   community. The raw submission *D/H/S*  is archived in a special repository on

## 5. (possibly) A Dataset Journal

Given the careful editorial process described above, we could extend MDH into an
**International Journal of Mathematical Data Sets** with little effort: just a on
[arXiv](http://arxiv.org), *A* could be given the choice to submit *H* to a specially
founded journal that would organize publication in  of *H* (and by reference *A* in the
archival literature) and thus generate academic reputation and recognition for *A* in
particular and the mathematical data set community in general.

The establishment of such a journal would be facilitated by MDH, but is a conceptually
separate process. 

   

<!--  LocalWords:  formalization Bercic flexiformalizations formalizing
 -->
