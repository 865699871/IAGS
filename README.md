# IAGS: Inferring Ancestor Genome Structure under a wide range of evolutionary scenarios

The number of novel species with high quality genomes are rapidly accumulating, signaling the start of a golden age for the study of genome structure evolution. Here, we develop IAGS, a generalized novel computational framework to infer ancestral genome structure for a variety of evolutionary scenarios. IAGS provides four basic models to solve simple single-copy (GMP and GGHP) and complex multi-copy ancestor problems (Multi-copy GMP and GGHP) with blocks / endpoints matching optimization (BMO and EMO) strategies and their combinations to decode complex evolutionary history in a bottom-up manner.

## Dependencies
Python 3.6

Packages  | Version used in Research|
--------- | --------|
numpy  | 1.19.2 |
pandas  | 1.1.5 |
matplotlib  | 3.3.4 |

Gurobi solver 9.1.2 (https://www.gurobi.com/ ) with Academic License.  
conda install -c gurobi gurobi 
Development environment: Windows 10  
Development tool: Pycharm  

## Usage
Detailed instruction at docs UserGuide.pdf  
Example usages in scenarios  

## Introductions

### docs
User guide

### dataSturcture
Basic data structure for IAGS.

### inferringAncestorGenomeStructure
Containing the source code of four formulations, including GMP, GGHP, BMO and EMO.

### models
Containing the source code of four basic models for IAGS, including GMP, GGHP, Multi-copy GMP and Multi-copy GGHP.

### util
Including utils for downstream analysis.

### inputdata
Four real datasets used in our research, including block sequences for three Brassica, nine Yeast, five Gramineae and three Papaver species. The dataset source as following.

Species | URL | Block |
--------|-----|------|
Brassica rapa (field mustard) |	https://www.ncbi.nlm.nih.gov/assembly/GCF_000309985.2/	| https://www.nature.com/articles/s41477-020-0735-y#Sec19 |
Brassica nigra	| http://cruciferseq.ca 	|  https://www.nature.com/articles/s41477-020-0735-y#Sec19 |
Brassica oleracea (wild cabbage) |	https://www.ncbi.nlm.nih.gov/assembly/GCA_900416815.2	|  https://www.nature.com/articles/s41477-020-0735-y#Sec19 |
Eremothecium gossypii |	http://gryc.inra.fr/index.php?page=download |	Orthofinder and Drimm-Synteny |
Lachancea kluyveri	 | http://gryc.inra.fr/index.php?page=download	 |	Orthofinder and Drimm-Synteny |
Kluyveromyces lactis	| http://gryc.inra.fr/index.php?page=download	 |	Orthofinder and Drimm-Synteny |
Zygosaccharomyces rouxii	| http://gryc.inra.fr/index.php?page=download	 |	Orthofinder and Drimm-Synteny |
Lachancea thermotolerans	| http://gryc.inra.fr/index.php?page=download	 |	Orthofinder and Drimm-Synteny |
Lachancea waltii	| http://gryc.inra.fr/index.php?page=download	 |	Orthofinder and Drimm-Synteny |
Naumovozyma castellii	| http://gryc.inra.fr/index.php?page=download	 |	Orthofinder and Drimm-Synteny |
Kazachstania naganishii	| http://gryc.inra.fr/index.php?page=download	 |	Orthofinder and Drimm-Synteny |
Saccharomyces cerevisiae	| https://www.ncbi.nlm.nih.gov/assembly/GCF_000146045.2/	 |	Orthofinder and Drimm-Synteny |
Gordon, et al. pre-WGD Ancestor(Version 7 Aug2012)	| http://ygob.ucd.ie/	 |	Orthofinder and Drimm-Synteny |
Zea mays |	https://www.ncbi.nlm.nih.gov/assembly/GCF_902167145.1 |	Orthofinder and Drimm-Synteny |
Sorghum bicolor |	https://www.ncbi.nlm.nih.gov/assembly/GCF_000003195.3	  |	Orthofinder and Drimm-Synteny |
Oryza sativa	| https://www.ncbi.nlm.nih.gov/assembly/GCF_001433935.1/#/st	 |	Orthofinder and Drimm-Synteny |
Brachypodium distachyon	| https://www.ncbi.nlm.nih.gov/assembly/GCF_000005505.3	 |	Orthofinder and Drimm-Synteny |
Thinopyrum elongatum	| https://bigd.big.ac.cn/gwh/Assembly/965/show	 |	Orthofinder and Drimm-Synteny |
Papaver rhoeas |	https://xjtu-omics.github.io/Papaver-Genomics/ |	https://github.com/xjtu-omics/IAG/tree/master/inputFiles |
Papaver somniferum |		https://xjtu-omics.github.io/Papaver-Genomics/ |	https://github.com/xjtu-omics/IAG/tree/master/inputFiles |
Papaver setigerum		| 	https://xjtu-omics.github.io/Papaver-Genomics/ |	https://github.com/xjtu-omics/IAG/tree/master/inputFiles |

### scenarios
Pipline and example usages for four real datasets.


### simulations
Including Non-CRBs and CRBs simulations.
 

## Contact
If you have any questions, please feel free to contact: gaoxian15002970749@163.com, xfyang@xjtu.edu.cn, kaiye@xjtu.edu.cn






