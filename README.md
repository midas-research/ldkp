
# LDkp

LDkp is Long Documents Keyphrase dataset developed by

  

<br>

<p  align="center">

<img  src="https://github.com/midas-research/ldkp/blob/main/MIDAS-logo.jpg"  alt="MIDAS lab at IIIT-Delhi"  width="60%"/>

<br>

</p>

<br>

LDkp (Long Document keyphrase) dataset is the first benchmark corpus of 1.3M documents for identifying  keyphrases  from  long  documents. The LDkp dataset is released in two versions :

 - **LDkp3k**: consists of 0.1M keyphrase tagged long documents, is created using keyphrases from KP20k [(Meng et al., 2017)](https://aclanthology.org/P17-1054/) and their corresponding long document text from S2ORC [(Lo et al., 2020)](https://aclanthology.org/2020.acl-main.447/).
 - **LDkp10k**: The second dataset LDkp10k consisting of 1.3M long documents along with target keyphrases is created using keyphrases from
OAGKX [(Çano, 2019)](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3062) and their corresponding long document text from S2ORC [(Lo et al., 2020)](https://aclanthology.org/2020.acl-main.447/).

Since both datasets consist of a large number of examples, we present three versions of training split for both of the datasets with sizes, as shown below:

<br>

<p  align="center">

<img  src="https://github.com/midas-research/ldkp/blob/main/Dataset_distribution.png"  alt="Dataset Distribution"  width="60%"/>

<br>

</p>

<br>


## Dataset format
To be added
## Steps to download the dataset

 1. Clone the repository onto your system where you want to download the dataset.
 2. Run pip install -r requirements.txt
 3. Move the files helper.py, ldkp3k.py and ldkp10k.py to a place where you want to download the dataset.
 4. Using ldkp3k.py you can download the LDkp3k dataset either in base format or in CoNLL format
 5. Using the ldkp10k.py you can download the LDkp10k dataset either in base format or in CoNLL format.

## Terms of Use

1. This corpus can be used freely for research purposes.
2. The paper listed below provide details of the creation and use of the corpus. If you use the corpus, then please cite the     paper.
3. If interested in commercial use of the corpus, send email to midas@iiitd.ac.in.
4. If you use the corpus in a product or application, then please credit the authors and [Multimodal Digital Media Analysis Lab - Indraprastha Institute of Information Technology, New Delhi](http://midas.iiitd.edu.in) appropriately. Also, if you send us an email, we will be thrilled to know about how you have used the corpus.
5. Multimodal Digital Media Analysis Lab - Indraprastha Institute of Information Technology, New Delhi, India disclaims any responsibility for the use of the corpus and does not provide technical support. However, the contact listed above will be happy to respond to queries and clarifications.
6. Rather than redistributing the corpus, please direct interested parties to this [page](https://github.com/midas-research/ldkp)

Please feel free to send us an email:
- with feedback regarding the corpus.
- with information on how you have used the corpus.
- if interested in having us analyze your data for emotion, and other affectual information.
- if interested in a collaborative research project.

Copyright (C) 2019 Multimodal Digital Media Analysis Lab - Indraprastha Institute of Information Technology, New Delhi (MIDAS, IIIT-Delhi)

## References
 To be added
