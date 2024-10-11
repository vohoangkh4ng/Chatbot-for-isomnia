Environment International 155 (2021) 106703

## Insights into the roles of fungi and protist in the giant panda gut microbiome and antibiotic resistome

### A R T I C L E I N F O

**Keywords:**
Fungi
Protist
Antibiotic resistance genes
Network analysis
Multitrophic communities
Neutral model

The mammal gut is a rich reservoir of antibiotic resistance genes (ARGs), and the relationship between bacterial communities and ARGs has been widely studied. Despite ecological significance of microeukaryotes (fungi and protists), our understanding of their roles in the mammal gut microbiome and antibiotic resistome is still limited. Here, we used amplicon sequencing, metagenomic sequencing and high-throughput quantitative PCR to examine microbiomes and antibiotic resistomes of 41 giant panda fecal samples from individuals with different genders, ages, sampling sites and diet. Our results show that diverse protists inhabit in the giant panda gut ecosystem, dominated by consumers. Higher abundance of protistan consumers was detected in the elder compared to sub-adult and adult giant pandas. Diet is the main driving factor of variation in ARGs in the giant panda gut microbiome. Weighted correlation network analysis identified two key microbial modules from multitrophic communities, which all contributed to the variation in ARGs in the giant panda gut. Protists occupied an important position in the two modules which were dominated by fungal taxa. Deterministic processes made a more important contribution to microbial community assembly of the two modules than to bacterial, fungal and protistan communities. This study sheds new light on how key microbial modules contribute to the variation in ARGs, which is crucial in understanding dynamics of antibiotic resistome in the mammal gut, particularly endangered species.

## 1. Introduction

As one of the most iconic endangered species on Earth, the protection of giant panda (Ailuropoda melanoleuca) is of worldwide concern. It is well established that animal gut microbiome has an important influence on the physiology and health of the host, and gut microbial transplants hold promise for the treatment of specific diseases and maybe for the conservation of endangered animals in the future. Therefore, study of gut microbiome of giant panda might provide critical insights for their protection. To this point, most studies on the giant panda gut microbiome have focused on bacterial communities. For example, a recent study has showed that a large number of genes and species from bacteria changed with age in the giant panda gut. However, the importance of eukaryotes and viruses in the animal gut microbiome has only recently attracted attention. Although it has been realized that eukaryote and virus are important members of animal gut microbiome, composition D. Zhu et al. Environment International 155 (2021) 106703

and structure of eukaryotic microbiome and virome are poorly characterized in mammals, and especially for the giant panda.
Fungi and protists are important components of the eukaryota, and play key roles in animal gut ecosystems. Apart from direct impact on the host (e.g. fungal infection and parasites), fungi and protists may also regulate changes in other microbiota so as to affect host health through niche competition and predation. For example, Saccharomyces cerevisiae could reduce the incidence of colitis caused by adhesion of invasive Escherichia coli in the gut of mice, which may be due to competition between fungi and bacteria for ecological resources. Colonization of the protists Blastocystis and Entamoeba could cause variation in the gut microbiota in the human intestine. In addition, many gut protists are commonly colonized with some bacteria, which may also affect the host microbiome. A recent study has showed that bacterial diversity was positively correlated with eukaryotic diversity in the wild non-human primate gut. These studies have all indicated that there are complex interrelationships between fungi, protists and other microbiota in the animal gut, with consequence for the health of the host. However, our knowledge on the role of fungi and protists in the gut microbiome of giant pandas is very limited.
The emergence and dispersal of clinical antibiotic resistance have caused global concerns due to extensive and often unmonitored use of antibiotics in livestock farming and medicine. More specifically, the rapid emergence of resistant pathogens will affect our ability to treat infectious diseases, thus threatening human health worldwide. However, antibiotic resistance is also an ancient and prevalent feature of the environmental microbiome. Importantly, many studies have revealed that the mammal gut is a rich reservoir of antibiotic resistance genes (ARGs) which may be exchanged with pathogens via horizontal gene transfer. Several recent studies have shown that diverse ARGs existed in the gut of wild and captive giant pandas. However, factors driving the shifts in ARGs in the giant panda gut have not been well characterized. It has been suggested that fungi and protists may have a role in regulating ARGs in the environment. For example, Bahram et al. reported that the competition between fungi and bacteria made an important contribution to changes in the global soil antibiotic resistome. Protist predation on bacteria and fungi may also affect the environmental resistome. Fungi and protists are important parts of the giant panda gut microbiome, but it is not known if they affect the abundance and diversity of ARGs.
The gut ecosystem supports many micro-communities including bacteria, fungi and protists, and there are complex interactions between these taxa resulting in a number of multitrophic communities including consumers, prey, phototrophs and parasites. Ecological co-occurrence networks could provide critical information on the potential associations between taxa in these multitrophic communities. Although the relationship between these multitrophic communities and multifunctionality has been explored, very little is known about how these multitrophic communities affect the dynamics of ARGs.
Here, we analyzed the microbiome and antibiotic resistome of 41 individual giant panda fecal samples from two research facilities using 16S, ITS and 18S rRNA high-throughput sequencing, metagenomic sequencing and high-throughput quantitative PCR, respectively. The main objectives of our study were (1) to examine effects of gender, age, sampling site and diet on giant panda gut microbiome and antibiotic resistome, (2) to reveal variations in the composition and functional groups of protists along an age gradient, (3) to identify micro-food web modules significantly related to the abundance of ARGs and highlight the roles of fungi and protists in these modules using network analysis. Our results aim to shed new light on the role of micro-eukaryotes (fungi and protists) in the giant panda gut microbiome and antibiotic resistome, and contribute to the conservation of the giant panda.

## 2. Materials and methods

### 2.1. Samples collection

A total of 41 giant panda fecal samples were collected from the China Research Base of Giant Panda Breeding (Chenghua District, Chengdu) and the Conservation and Research Center for Giant Panda (Wolong) during January and March 2017. The fecal samples included samples from three infants, 15 sub-adults, 12 adults and 11 elders. Since infants may have inherited similar microbiomes/ARGs from their parents, we did not collected samples of their parents. Breast milk mixed with milk powder was provided to each infant giant panda. For sub-adult, adult and elders, bamboo was fed to giant pandas from Wolong, while the food of giant pandas from Chenghua was diverse and included steamed corn-bread, bamboo, apple and winter bamboo shoots. We collected fresh fecal samples after feeding periods, and returned them to the lab on dry ice. The fecal samples were collected in accordance with animal welfare requirements. Detailed information (including diet, gender, age, sampling site and health condition) relating to giant pandas is supplied in Supplementary Data 1.

### 2.2. DNA extraction, high-throughput sequencing and bioinformatics analysis

The UltraClean™ Fecal DNA Kit (MOBIO, USA) was used to extract DNA from 0.25 g homogenized fecal samples, following the instructions of the manufacturer. The isolated DNA was eluted into 100 μL EB buffer, and we used the Nanodrop ND-1000 spectrophotometer (Thermo Fisher, USA) to determine its quality and concentration. Three specific primer sets 515F/806R, gITS7/ITS4ngs and F1391/REukBr were selected to amplify the V4 region of the bacterial 16S rRNA gene, fungal ITS2 region and 18S V9 hypervariable region of eukaryotes, respectively. These primers were labeled with 8 base unique barcodes to distinguish the samples. Each extracted DNA sample was amplified in triplicate; the conditions and procedure of PCR amplification have been described previously. The Illumina Hiseq2500 platform was selected to sequence the PCR products in the Novogene Technology Co. Ltd., Tianjin, China.
The QIIME2 v2020.2 was selected to analyze obtained amplicon sequences following the online instructions. The DADA2 algorithm was used to determine amplicon sequence variants (ASVs) from the giant panda gut high-throughput sequencing data by denoising in the QIIME2 platform. The pre-trained Naive Bayes classifier was used to perform taxonomic assignments, and we selected Silva v138, UNITE v2020.2 and PR2 v4.12.0 reference databases to annotate the taxonomic information of bacterial, fungal and eukaryotic representative sequences via the sklearn python package, respectively. Before downstream analysis, some sequences (mitochondria, archaea, chloroplast and unassigned reads for 16S; fungi, metazoa, rhodophyta, streptophyta and ambiguous taxa for 18S) were removed as our study only focused on bacteria, fungi and protists, and we rarefied the obtained ASVs table to the same depth (bacteria: 35850, fungi: 11,937 and protist: 3660) according to the minimum number of sequences per sample. Fungal sequences of three samples were removed due to very low sequence number. The Shannon index and Weighted Unifrac and Bray Curtis distances of bacteria, fungi and protists were calculated in the QIIME2 platform. The functional groups of protists have been classified based on previous studies. 2.3. Antibiotic resistance genes (ARGs) detection

A total of 320 ARGs and 57 mobile genetic elements (MGEs) and one 16S rRNA gene were detected to investigate the composition and abundance of ARGs in the giant panda gut microbiome by using the SmartChip Real-time PCR system (Wafergen, USA). Information about primer sets targeting these genes is provided in Supplementary Data 2. The system and conditions of amplification were consistent with previous studies, and each sample was amplified in triplicate. A threshold cycle (CT) of 31 was used in our study as a detection limit. Only when three replicates were all amplified, did we think it had been detected. The calculation of relative abundance of ARGs followed the equation below.

```
Copy number of gene = 10((31 CT(measurement))/(10/3))
```

Relative abundance of antibiotic resistance gene = copy number of antibiotic resistance gene/copy number of 16S rRNA gene

3. Results

3.1. Composition, diversity and function of the giant panda gut microbiome

To further reveal the function and viral diversity of the giant panda gut microbiome, we selected six samples (sub-adult; Wolong) to perform metagenomic and virome analysis. The diet of the selected panda was mainly bamboo, which is close to the conditions in the wild. The procedure for metagenomic and virome analysis followed that used in previous studies. Briefly, for metagenomic data, clean data after quality control underwent de novo splicing by using MEGAHIT (K-mer: k-min 35, k-max 95 and k-step 20). Scaftigs with splicing length above 500 bp were screened for subsequent analysis. The predicted gene protein sequences were compared with KEGG and Cazyme databases to obtain functional annotation information. For virome analysis, the viral DNA was extracted from the samples and then the sequencing was performed. To obtain clean data, we used Soapnuke (v2.0.5) software to analyze the raw data (129.63G). After host removal, we identify viral sequences (74 641 815 reads) by blasting the NCBI NR and RefseqVirus databases (comparison similarity >= 80%, comparison length >= 500 bp, e <= 1e-5, defined as confirmed). Contigs comparison of viruses identified was performed to obtain the possible host information of phages by using the CRISPR Recognition Tool.

Higher bacterial diversity (Shannon) was observed in the giant panda gut from the Wolong site in comparison to the Chenghua site (P < 0.05); however, fungal and protistan diversities did not produce significant difference between different sites (P > 0.05). Results of principal coordinates analysis (PCoA) illustrate that the giant panda gut fungal communities are clustered according to sampling site. PERMANOVA further revealed that sampling site and age all have significant influences on giant panda gut microbiomes including the relative contributions of bacteria, fungi and protists (P < 0.05; Table 1). Fourteen percent of the variation in fungi could be explained by sampling site, higher than the 10% for bacteria and 7% for protists. Gender and diet did not cause significant effects on giant panda gut protist communities (P > 0.05).

The neutral model could predict the distribution of most of the microbial ASVs (85.7–88%) in the giant panda gut. For bacteria and fungi, the number of ASVs falling above the neutral model prediction was double the number falling below; however, similar proportions (5.8–6.2%) were below and above the neutral model prediction for the protists. A higher R2 was observed in the bacteria (0.675) and protist (0.69) communities compared to fungi (0.45). The co-occurrence network revealed that fungi dominate interactions in the giant panda gut microbiome (fungi-fungi: 37.7%, fungi-bacteria: 40%, fungi-protist: 4.7%). Metabolism (10.7%) was the most Fig. 1.  Community structure of giant panda gut bacteria, fungi and protist is revealed by principal coordinates analysis (PCoA) based on the weighted unifrac and bray curtis distances, respectively. The variation explained by the PCoA axes is listed in parentheses.

Table 1
Comparison of giant panda gut microbial structure and ARG profiles using PERMANOVA (Adonis test).

| Category | Bacteria | | | Fungi | | | Protist | | | ARGs | |
|----------|----------|-----|-----|-------|-----|-----|--------|-----|-----|-----|-----|
|          | P        | R2  |     | P     | R2  |     | P      | R2  |     | P   | R2  |
| Gender   | 0.587    | 0.03|     | 0.067 | 0.05|     | 0.565  | 0.02|     | 0.036| 0.09|
| Age      | < 0.001  | 0.18|     | 0.003 | 0.12|     | 0.015  | 0.19|     | < 0.001| 0.27|
| Site     | < 0.001  | 0.10|     | < 0.001| 0.14|     | 0.023  | 0.07|     | < 0.001| 0.26|
| Diet     | < 0.001  | 0.27|     | < 0.001| 0.25|     | 0.173  | 0.15|     | < 0.001| 0.34|

Within Below Above the giant panda gut (Figure S9).

3.2.   Roles of protists in the giant panda gut microbiome
The co-occurrence network analysis identified three protist genera (Chrysophyceae_X, Cercomonas and Paratetramitus) involved in a large number of interactions with fungi and bacteria in the giant panda gut (Figure S7). The composition and abundance of dominant protist taxa were not significantly different across giant panda age classes (P > 0.05; Figure S10). For functional groups of protists, consumers (93.3%) were dominant, and a higher abundance of consumers was found in the older compared to sub-adult and adult groups (P < 0.05; Figure S11). Co-occurrence networks for different ages revealed that the network complexity (here defined by average changes in network properties, focusing particularly on edge, modularity and average degree) in the adult group (edge: 497, modularity: 2.645 and average degree: 5.316) is higher than sub-adult and elder groups (Fig. 3 and Table S1). The most negative edges (41.2%) were also observed in the network for the adult group (Table S1). The co-occurrence network further showed complex correlations between protist and other microbiome members, such as for the adult (protist-bacteria: 22 edges and protist-fungi: 37 edges), sub-adult (protist-bacteria: 23 edges and protist-fungi: 24 edges) and elder groups (protist-bacteria: 35 edges and protist-fungi: 8 edges). The abundant KEGG system (Figure S8a), and Glycoside Hydrolases (0.5%) and Glycosyl Transferases (0.3%) were two dominant enzymes in the giant panda gut microbiome (Figure S8b). Viral metagenomics analysis showed viruses involved in many functions (e.g. developmental stage) in D. Zhu et al.
Environment International 155 (2021) 106703

### Network co-occurrence analysis of giant panda gut microbiome

| Bacteria | Fungi | Protist |
|----------|-------|---------|
|          |       | Sub-adult |
|          |       | Adult |
|          |       | Elder |

Only R > 0.7 or < 0.7 and P < 0.01 of correlations were included. The size of the node is proportional to the number of connections (degree).

### Potential host

| Protist | Positive | Negative |
|---------|----------|----------|
|         |          | Cercomonas |
|         |          | Hypotrichia |
|         |          | Apatococcus |

Potential hosts of viruses were predicted by using viral metagenomics analysis, and three protist genera (Hypotrichia, Cercomonas and Apatococcus) presented complex correlations with these potential hosts of viruses in the co-occurrence network. The abundance of Amoebozoa had a significant negative correlation with multiple microbial function based on KEGG and CAZy annotations in the giant panda gut (P < 0.05; Table S2).

### Composition and abundance of ARGs in the giant panda gut microbiome

A total of 128 ARGs and 35 MGEs were detected in all giant panda samples. The relative abundances of ARGs in giant panda samples ranged from 0.036 to 0.467, and the number of ARGs detected was between 18 and 54. The detected ARGs were divided into 12 types based on resistance class of antibiotic, and multiple drug resistance (MDR) was the dominant type of ARGs in the giant panda gut, comprising 81.4% and 46.8% of the ARGs relative abundance and number, respectively. The highest relative abundance (0.43) and number (47) of ARGs were observed in the infant giant panda microbiome compared to the other ages classes (P < 0.05). The relative abundance and number of ARGs in the giant panda microbiome from Chenghua were significantly higher than those from Wolong, by 84.9% and 48.2%, respectively (P < 0.05). The PCoA revealed that the majority of samples were separated by sampling site along the PCo1 axis, which explained 44.2% of the variation, and numerous samples were clustered according to age class. The PERMANOVA further showed that diet, gender, age and site all significantly affected the composition of ARGs in the giant panda gut.

| Age | Sub-adult | Adult | Elder |
|-----|-----------|-------|-------|
|     |           |       |       |

| Sampling site | Wolong | Chenghua |
|---------------|--------|----------|

### Relative abundance and number of ARGs in each giant panda sample

| Age | Sub-adult | Adult | Elder |
|-----|-----------|-------|-------|

| Sampling site | Wolong | Chenghua |
|---------------|--------|----------| the giant panda microbiome, and diet (34%) explained the most varia-                      0.0024; Figure S14b), and the relationship between diversity of bacteria
tion in ARGs (P < 0.05; Table 1). Similar to the ARGs, the microbiome of                  and fungi and abundance of ARGs was not significant (P                    >  0.05;
infant   giant   pandas    had   the   highest   abundance      (0.24)   of  MGEs         Figure S14c and S14d). Giant panda gut microbiomes including bacteria,
compared to the other age classes, and the relative abundance of MGEs                     fungi and protists were divided into 39 microbial modules (commonly
in the giant panda microbiome from Chenghua was higher than that                          including    multitrophic    communities)      in   the  Weighted      correlation
from Wolong, by 97.3% (P < 0.05; Figure S13).                                             network analysis, which revealed that Module#28 (R                 =  0.443, P   =
0.0054) and Module#30 (R          = 0.425, P     = 0.0077) have a significant
positive correlation with the abundance of ARGs (Figure S15a), and
3.4.  Relationship between microbiomes and ARGs in the giant panda gut                    significant correlations between microbial taxa in the two modules and
ARGs were also observed (P           <  0.001; Figure S15b and S15c). In-
The abundance of MGEs had a significant positive correlation with                     teractions between microbial taxa from Module#28 and Module#30
the abundance of ARGs in the giant panda microbiome (R = 0.75, P <                        were revealed in co-occurrence networks (Fig. 6). Ascomycota (fungi)
0.001; Figure S14a). A distinctly negative correlation was found be-                      dominated     the   two    co-occurrence      networks,    and    Alveolata    and
tween bacterial diversity and abundance of ARGs (R                 =   -0.48, P   =
Ascomycota
a                                                                                      Firmicutes
Unidentified
Actinobacteria
Basidiomycota
lortierellomycota
Proteobacteria
Bacteroidetes
Roze llomycota
Opisthokonta
Alveolata
Planctomycetes
Module#28
Average Degree: 28.592
Average Clustering Coefficient: 0.919
b                                                                                        Ascomycota
Unidentified
Basidiomycota
Firmicutes
Stramenopiles
lucoromycota
Alveolata
Opisthokonta
Actinobacteria
Proteobacteria
Rozellomycota
Archaeplastida
Module#30
Average Degree: 46.210
Average Clustering Coefficient: 0.951
Fig. 6. Network co-occurrence analysis of giant panda gut microbiome including bacteria, fungi and protist from the module which significantly correlated with
abundance of ARGs. Only R > 0.7 or <         0.7 and P < 0.01 of correlations were included in this network. The size of the node is proportional to the number of
connections (degree). Opisthokonta (protists) and Actinobacteria (bacteria) all had complex interactions with bacteria, fungi and protists in the two co-occurrence networks. A lower number of microbial ASVs in the two modules could be predicted by the neutral model compared to bacterial, fungal and protistan communities.

## Discussion

The present study is the first to systematically characterize the viral, bacterial, fungal and protistan composition of the giant panda gut by amplicon and metagenomic sequencing. In our study, giant panda gut microbial communities (bacteria, fungi and protist) are all sensitive to sampling site. This may be due to the fact that, apart from infant giant pandas, the diet of other giant panda age classes was different between sampling sites. It is well established that diet makes an important contribution to changes in animal gut microbiome. Our findings also demonstrate that diet could influence giant panda gut microbial communities. Certainly, other environmental factors (e.g. environmental microbiome, climate and precipitation) can also affect microbial communities in giant panda gut at different sites, but the effects of diet appear to be the main driving factor in our study.

Our results presented that diverse protists were found in the giant panda gut, and a majority of these protists were characterized as consumers. A recent study of the gut microbiome of non-human primates also indicated that protists commonly inhabit the non-human primate gut, with most of them being non-pathogenic. Protistan consumers can generally regulate bacterial and fungal communities through predation. Therefore, we thought that protists are important community members in the giant panda gut system as they are in non-human primates. Our network analysis further shows that several protistan taxa occupy key positions in the giant panda gut microbiome and are potential hosts for viruses, suggesting that if the loss of protists may affect the giant panda intestinal homeostasis by altering interactions between microorganisms. Recently a study also indicated that the presence of protistan Blastocystis could alter gut microbiome to promote faster recovery from induced colitis. Through metagenomic analysis, we determined that the protistan Amoebozoa had a significant effect on multiple microbial function in the gut, indicating that some protistan taxa have an important contribution to the giant panda growth by affecting gut microbial function. Although related studies are very limited in the mammal gut, previous studies showed that protists play an important role in the wood digestion in the termite gut. These suggest that protists could play an important role in the giant panda gut ecosystem, and they should be studied as important community members in the mammal gut.

Our study shows that age is one of the biggest influences on giant panda gut protist communities. This suggests that the role of protists in the giant panda gut microbiome may be distinct at different life stages of giant panda. This is further supported by our results showing that the abundance of protistan consumers was related to changes in age, and the highest relative abundance of protistan consumers was found in the elder compared to the sub-adult and adult giant pandas. Gut properties will change with increasing animal age, and our results indicate that age could significantly affect giant panda gut bacterial and fungal communities. Therefore, the age-dependent change of protistan consumer might be due to changes in gut properties and food resources (e.g. bacterial and fungal community increases). In the network analysis, the number of edges between protist and bacteria in the elder age class were also much more abundant than the sub-adult and adult age classes. These all indicate that the degree of protistan predation on bacteria may be the greatest in the gut of older giant pandas, which may influence gut homeostasis. The lowest network complexity was observed in the gut microbiome of the oldest giant panda group, which also partially confirms this point. Alterations in gut homeostasis may facilitate colonization of pathogens and affect nutrient absorption and subsequently influence the health of the host.

Consistent with several previous studies, our results also found diverse ARGs in the giant panda gut microbiome, which was dominated by multiple drug resistance (MDR). We showed that diet shaped the diversity and abundance of ARGs in the giant panda gut microbiome, and the relative abundance of ARGs in bamboo-fed giant pandas was the lowest compared to those fed on milk, apple and bamboo shoots. This indicates that we might be able to mitigate the abundance of ARGs in the giant panda gut microbiome by managing their diets. In addition, the unique diet of giant panda might be the main reason that the abundance of ARGs in the giant panda gut microbiome was generally lower than those in the human, swine and dairy cattle. Our findings further indicated that bacterial diversity had a significant negative correlation with the abundance of ARGs in the giant panda gut, which has also been demonstrated in other environments. In addition, we also revealed that MGEs were significantly positively correlated with the abundance of ARGs in the giant panda gut, suggesting that MGEs may contribute to increases in ARGs by horizontal gene transfer. This is supported some previous findings. Combined with the fact that the giant panda gut antibiotic resistome is dominated by MDR, there is a high risk that potential pathogens can acquire multidrug resistance genes in the giant panda gut by horizontal gene transfer.

We further identified two functional modules from multitrophic communities, which were significantly positively correlated with the abundance of ARGs in the giant panda gut microbiome. Previous studies mostly focused on the effects of bacteria or one type of microorganism on ARGs, however, microbial communities usually form complex network structures in the ecosystem to perform their ecological functions. Therefore, this finding expands our insight that key multitrophic communities might contribute to the change in ARGs in the giant panda gut ecosystem. Moreover, the two modules were dominated by fungal taxa, indicating that some fungal taxa have an important effect on the variations in ARGs in the giant panda gut microbiome. There are two reasons for this: the first is that some fungi can produce antibiotics, which may increase the selective pressure on bacteria; and the second is that fungi and bacteria compete for ecological niches, therefore might expand the bacterial antibiotic resistome. Recently, several studies have also highlighted the effects of fungi on ARGs in other environments (e.g. soils). Interestingly, protists occupied an important position in the two modules, indicating that they could also affect ARGs in the giant panda gut microbiome. The pressure from protistan predation on bacteria supports this result, especially given the majority of the protists in the two modules are consumers. In addition, we found that two bacterial taxa from the Actinobacteria were important components of the two modules. As we know, many Actinobacteria taxa are commonly associated with the production of antibiotics. Finally, our results reveal that the contribution of neutral processes to microbial communities in the two modules was lower than that in the bacterial, fungal and protistan communities, suggesting that a deterministic process makes a more important contribution to the assemblage of the two modules than to the bacterial, fungal and protistan communities. Consequently, future studies may need to pay more attention to the role of multitrophic communities in shaping ARGs.

## Conclusion

Taken together we show that diet is the main driving factor of changes in ARGs in the giant panda gut microbiome, and the two functional modules identified from multitrophic communities also contribute to the changes in ARGs. Our data further reveal that a deterministic process makes a more important contribution to microbial community assembly of the two modules than it does for the bacterial, fungal and protistan communities. This study highlights the roles of fungi and protists in shaping the microbiome and resistome in the giant panda gut, potentially guiding future efforts of giant panda conservation through improving microbial communities to mitigate antibiotic resistance of the gut ecosystem

## Data availability

We submitted the obtained raw sequencing data to the NCBI Sequence Read Archive under the accession number PRJNA397169. The authors declare that the other main data supporting the findings of this study are available within this Article and in the Supplementary Information files. Extra data supporting the findings of this study are available from the corresponding author upon reasonable request

## Code availability

Custom codes for all analyses are available from the corresponding authors upon request

## CRediT authorship contribution statement

Dong Zhu: Methodology, Software, Formal analysis, Investigation, Writing - original draft, Writing - review & editing, Visualization, Funding acquisition. Lu Lu: Methodology, Software, Formal analysis, Investigation, Writing - original draft, Writing - review & editing, Visualization, Funding acquisition. Zejun Zhang: Investigation, Data curation, Writing - review & editing. Dunwu Qi: Investigation, Data curation, Writing - review & editing. Mingchun Zhang: Investigation, Data curation, Writing - review & editing. Patrick O’Connor: Writing - review & editing. Fuwen Wei: Writing - review & editing. Yong-Guan Zhu: Conceptualization, Methodology, Investigation, Writing - original draft, Writing - review & editing, Supervision

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper

## Acknowledgments

This work was funded by the National Natural Science Foundation of China (42077216, 42090063 and 42071279) and the Innovative Team Foundation of China West Normal University (CXTD2020-2)

## Appendix A. Supplementary material

Supplementary data to this article can be found online at https://doi.org/10.1016/j.envint.2021.106703 D. Zhu et al.
Environment International 155 (2021) 106703

| Author(s) | Title | Journal | Volume | Page(s) |
|-----------|-------|---------|--------|---------|
| Geisen, S., Mitchell, E.A.D., Adl, S., Bonkowski, M., Dunthorn, M., Ekelund, F., Fernandez, L.D., Jousset, A., Krashevska, V., Singer, D., Spiegel, F.W., Walochnik, J., Lara, E. | Soil protists: a fertile frontier in soil biology research | FEMS Microbiol. Rev. | 42 | 293–323 |
| Guo, W., Mishra, S., Wang, C., Zhang, H., Ning, R., Kong, F., Zeng, B., Zhao, J., Li, Y. | Comparative study of gut microbiota in wild and captive giant pandas (Ailuropoda melanoleuca) | Genes | 10 | 827 |
| Guo, M., Liu, G., Chen, J., Ma, J., Lin, J., Fu, Y., Fan, G., Lee, S.M.-Y., Zhang, L. | Dynamics of bacteriophages in gut of giant pandas reveal a potential regulation of dietary intake on bacteriophage composition | Sci. Total Environ. | 734 | 139424 |
| Hicks, A.L., Lee, K.J., Couto-Rodriguez, M., Patel, J., Sinha, R., Guo, C., Olson, S.H., Seimon, A., Seimon, T.A., Ondzie, A.U., Karesh, W.B., Reed, P., Cameron, K.N., Lipkin, W.I., Williams, B.L. | Gut microbiomes of wild great apes fluctuate seasonally in response to diet | Nat. Commun. | 9 | 1786 |
| Hu, T., Dai, Q., Chen, H., Zhang, Z., Dai, Q., Gu, X., Yang, X., Yang, Z., Zhu, L. | Geographic pattern of antibiotic resistance genes in the metagenomes of the giant panda | Microb. Biotechnol. | 14 | 186–197 |
| Huang, G., Wang, X., Hu, Y., Wu, Q., Nie, Y., Dong, J., Ding, Y., Yan, L., Wei, F. | Diet drives convergent evolution of gut microbiomes in bamboo-eating species | Science China-Life Sciences | 64 | 88–95 |
| Johnke, J., Cohen, Y., de Leeuw, M., Kushmaro, A., Jurkevitch, E., Chatzinotas, A. | Multiple micro-predators controlling bacterial communities in the environment | Curr. Opin. Biotechnol. | 27 | 185–190 |
| Kang, D., Li, J. | Giant panda protection: challenges and hopes | Environ. Sci. Pollut. Res. | 26 | 18001–18002 |
| Koenig, L., Wentrup, C., Schulz, F., Wascher, F., Escola, S., Swanson, M.S., Buchrieser, C., Horn, M. | Symbiont-mediated defense against Legionella pneumophila in Amoebae | Mbio | 10 | e00333–e00419 |
| Laforest-Lapointe, I., Arrieta, M.-C. | Microbial eukaryotes: a missing link in gut microbiome studies | Msystems | 3 | e00201–e00217 |
| Laxminarayan, R., Duse, A., Wattal, C., Zaidi, A.K.M., Wertheim, H.F.L., Sumpradit, N., Vlieghe, E., Levy Hara, G., Gould, I.M., Goossens, H., Greko, C., So, A.D., Bigdeli, M., Tomson, G., Woodhouse, W., Ombaka, E., Peralta, A.Q., Qamar, F.N., Mir, F., Kariuki, S., Bhutta, Z.A., Coates, A., Bergstrom, R., Wright, G.D., Brown, E.D., Cars, O. | Antibiotic resistance-the need for global solutions | Lancet Infect. Dis. | 13 | 1057–1098 |
| Lee, W.-J., Hase, K. | Gut microbiota-generated metabolites in animal health and disease | Nat. Chem. Biol. | 10 | 416–424 |
| Li, S., Shi, S., Bu, L. | Rail network must protect giant pandas | Nature | 545 | 289 |
| Liu, J., Taft, D.H., Maldonado-Gomez, M.X., Johnson, D., Treiber, M.L., LemayQ, D.G., DePeters, E.J., Mills, D.A. | The fecal resistome of dairy cattle is associated with diet during nursing | Nat. Commun. | 10 | 4406 |
| Liu, P., Chen, W., Chen, J.-P. | Viral metagenomics revealed sendai virus and coronavirus infection of malayan pangolins (Manis javanica) | Viruses-Basel | 11 | 979 |
| Loucks, C.J., Lu, Z., Dinerstein, E., Wang, H., Olson, D.M., Zhu, C.Q., Wang, D.J. | Ecology - Giant pandas in a changing landscape | Science | 294 | 1465 |
| Mahnert, A., Moissl-Eichinger, C., Zojer, M., Bogumil, D., Mizrahi, I., Rattei, T., Luis Martinez, J., Berg, G. | Man-made microbial resistances in built environments | Nat. Commun. | 10 | 968 |
| Mann, A.E., Mazel, F., Lemay, M.A., Morien, E., Billy, V., Kowalewski, M., Di Fiore, A., Link, A., Goldberg, T.L., Tecot, S., Baden, A.L., Gomez, A., Sauther, M.L., Cuozzo, F. P., Rice, G.A.O., Dominy, N.J., Stumpf, R., Lewis, R.J., Swedell, L., Amato, K., Parfrey, L.W. | Biodiversity of protists and nematodes in the wild nonhuman primate gut | The ISME Journal | 14 | 609–622 |
| Morton, E.R., Lynch, J., Froment, A., Lafosse, S., Heyer, E., Przeworski, M., Blekhman, R., Segurel, L. | Variation in rural African gut microbiota is strongly correlated with colonization by entamoeba and subsistence | PLoS Genet. | 11 | e1005658 |
| Mustafa, G.R., Li, C., Zhao, S., Jin, L., He, X., Shabbir, M.Z., He, Y., Li, T., Deng, W., Xu, L., Xiong, Y., Zhang, G., Zhang, H., Huang, Y., Zou, L. | Metagenomic analysis revealed a wide distribution of antibiotic resistance genes and biosynthesis of antibiotics in the gut of giant pandas | BMC Microbiol. | 21 | 15 |
| Nazir, R., Shen, J.-P., Wang, J.-T., Hu, H.-W., He, J.-Z. | Fungal networks serve as novel ecological routes for enrichment and dissemination of antibiotic resistance genes as exhibited by microcosm experiments | Sci. Rep. | 7 | 15457 |
| Nieves-Ramirez, M.E., Partida-Rodriguez, O., Laforest-Lapointe, I., Reynolds, L.A., Brown, E.M., Valdez-Salazar, A., Moran-Silva, P., Rojas-Velazquez, L., Morien, E., Parfrey, L.W., Jin, M., Walter, J., Torres, J., Arrieta, M.C., Ximenez-Garcia, C., Finlay, B.B. | Asymptomatic intestinal colonization with protist blastocystis is strongly associated with distinct microbiome ecological patterns | Msystems | 3 | e00007–e00018 |
| Nishimura, Y., Otagiri, M., Yuki, M., Shimizu, M., Inoue, J., Moriya, S., Ohkuma, M. | Division of functional roles for termite gut protists revealed by single-cell transcriptomes | The ISME Journal | 14 | 2449–2460 |
| Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., Duchesnay, E. | Scikit-learn: Machine learning in python | J. Mach. Learn. Res. | 12 | 2825–2830 |
| Pernthaler, J. | Predation on prokaryotes in the water column and its ecological implications | Nat. Rev. Microbiol. | 3 | 537–546 |
| Ramirez, K.S., Leff, J.W., Barberan, A., Bates, S.T., Betley, J., Crowther, T.W., Kelly, E.F., Oldfield, E.E., Shaw, E.A., Steenbock, C., Bradford, M.A., Wall, D.H., Fierer, N. | Biogeographic patterns in below-ground diversity in New York City’s Central Park are similar to those observed globally | Proc. Roy. Soc. B-Biol. Sci. | 281 | 20141988 |
| Ross, B.D., Verster, A.J., Radey, M.C., Schmidtke, D.T., Pope, C.E., Hoffman, L.R., Hajjar, A.M., Peterson, S.B., Borenstein, E., Mougous, J.D. | Human gut bacteria contain acquired interbacterial defence systems | Nature | 575 | 224–228 |
| Seipke, R.F., Kaltenpoth, M., Hutchings, M.I. | Streptomyces as symbionts: an emerging and widespread theme? | FEMS Microbiol. Rev. | 36 | 862–876 |
| Shier, W.T. | On the origin of antibiotics and mycotoxins | Toxin Rev. | 30 | 6–30 |
| Sloan, W.T., Lunn, M., Woodcock, S., Head, I.M., Nee, S., Curtis, T.P. | Quantifying the roles of immigration and chance in shaping prokaryote community structure | Environ. Microbiol. | 8 | 732–740 |
| Sokol, H., Leducq, V., Aschard, H., Hang-Phuong, P., Jegou, S., Landman, C., Cohen, D., Liguori, G., Bourrier, A., Nion-Larmurier, I., Cosnes, J., Seksik, P., Langella, P., Skurnik, D., Richard, M.L., Beaugerie, L. | Fungal microbiota dysbiosis in IBD | Gut | 66 | 1039–1048 |
| Sullam, K.E., Rubin, B.E.R., Dalton, C.M., Kilham, S.S., Flecker, A.S., Russell, J.A. | Divergence across diet, time and populations rules out parallel evolution in the gut microbiomes of Trinidadian guppies | ISME J. | 9 | 1508–1522 |
| Sultan, I., Rahman, S., Jan, A.T., Siddiqui, M.T., Mondal, A.H., Haq, Q.M.R. | Antibiotics, resistome and resistance mechanisms: A bacterial perspective | Front. Microbiol. | 9 | 2066 |
| Sun, A., Jiao, X.-Y., Chen, Q., Trivedi, P., Li, Z., Li, F., Zheng, Y., Lin, Y., Hu, H.-W., He, J.-Z. | Fertilization alters protistan consumers and parasites in crop-associated microbiomes | Environ. Microbiol. |  |  |
| Thapa, A., Hu, Y., Wei, F. | The endangered red panda (Ailurus fulgens): Ecology and conservation approaches across the entire range | Biol. Conserv. | 220 | 112–121 |
| Tsukayama, P., Boolchandani, M., Patel, S., Pehrsson, E.C., Gibson, M.K., Chiou, K.L., Jolly, C.J., Rogers, J., Phillips-Conroy, J.E., Dantas, G. | Characterization of wild and captive baboon gut microbiota and their antibiotic resistomes | Msystems | 3 | e00016–e00018 |
| van Bergeijk, D.A., Terlouw, B.R., Medema, M.H., van Wezel, G.P. | Ecology and genomics of Actinobacteria: new concepts for natural product discovery | Nat. Rev. Microbiol. | 18 | 546–558 |
| Wallace, M.J., Fishbein, S.R.S., Dantas, G. | Antimicrobial resistance in enteric bacteria: current state and next-generation solutions | Gut Microbes | 12 | e1799654 |
| Wang, A.Y., Popov, J., Pai, N. | Fecal microbial transplant for the treatment of pediatric inflammatory bowel disease | World J. Gastroenterol. | 22 | 10304–10315 |
| Wei, F., Wang, X., Wu, Q. | The giant panda gut microbiome | Trends Microbiol. | 23 | 450–452 |
| Wheeler, Matthew L., Limon, Jose J., Bar, Agnieszka S., Leal, Christian A., Gargus, M., Tang, J., Brown, J., Funari, Vincent A., Wang, Hanlin L., Crother, Timothy R., Arditi, M., Underhill, David M., Iliev, Iliyan D. | Immunological consequences of intestinal fungal dysbiosis | Cell Host Microbe | 19 | 865–873 |
| Wu, Q., Wang, X., Ding, Y., Hu, Y., Nie, Y., Wei, W., Ma, S., Yan, L., Zhu, L., Wei, F. | Seasonal variation in nutrient utilization shapes gut microbiome structure and function in wild giant pandas | Proc. Roy. Soc. B-Biol. Sci. | 284 | 20170955 |
| Xiang, Q., Zhu, D., Chen, Q.-L., Delgado-Baquerizo, M., Su, J.-Q., Qiao, M., Yang, X.-R., Zhu, Y.-G. | Effects of diet on gut microbiota of soil collembolans | Sci. Total Environ. | 676 | 197–205 |
| Xiong, W., Jousset, A., Guo, S., Karlsson, I., Zhao, Q., Wu, H., Kowalchuk, G.A., Shen, Q., Li, R., Geisen, S. | Soil protist communities form a dynamic hub in the soil microbiome | ISME J. | 12 | 634–638 |
| Yang, S., Gao, X., Meng, J., Zhang, A., Zhou, Y., Long, M., Li, B., Deng, W., Jin, L., Zhao, S., Wu, D., He, Y., Li, C., Liu, S., Huang, Y., Zhang, H., Zou, L. | Metagenomic analysis of bacteria, fungi, bacteriophages, and helminths in the gut of giant pandas | Front. Microbiol. | 9 | 1717 |
| Young, V.B. | The intestinal microbiota in health and disease | Curr. Opin. Gastroenterol. | 28 | 63–69 |
| Youngblut, N.D., Reischer, G.H., Walters, W., Schuster, N., Walzer, C., Stalder, G., Ley, R. E., Farnleitner, A.H. | Host diet and evolutionary history explain different aspects of gut microbiome diversity among vertebrate clades | Nat. Commun. | 10 | 2200 |
| Zhang, W., Liu, W., Hou, R., Zhang, L., Schmitz-Esser, S., Sun, H., Xie, J., Zhang, Y., Wang, C., Li, L., Yue, B., Huang, H., Wang, H., Shen, F., Zhang, Z. | Age-associated microbiome shows the giant panda lives on hemicelluloses, not on cellulose | ISME J. | 12 | 1319–1328 |
| Zhao, Y., Su, J.-Q., An, X.-L., Huang, F.-Y., Rensing, C., Brandt, K.K., Zhu, Y.-G. | Feed additives shift gut microbiota and enrich antibiotic resistance in swine gut | Sci. Total Environ. | 621 | 1224–1232 |
| Zhu, D., Ding, J., Yin, Y., Ke, X., O’Connor, P., Zhu, Y.-G. | Effects of earthworms on the microbiomes and antibiotic resistomes of detritus fauna and phyllospheres | Environ. Sci. Technol. | 54 | 6000–6008 |
| Zhu, D., Xinag, Q., Yang, X.-R., Ke, X., O’Connor, P., Zhu, Y.-G. | Trophic transfer of antibiotic resistance genes in a soil detritus food chain | Environ. Sci. Technol. | 53 | 7770–7781 |
| Zhu, Y.-G., Penuelas, J. | Changes in the environmental microbiome in the Anthropocene | Glob. Change Biol. | 26 | 3175–3177 |
| Zhu, Y.-G., Zhao, Y., Li, B., Huang, C.-L., Zhang, S.-Y., Yu, S., Chen, Y.-S., Zhang, T., Gillings, M.R., Su, J.-Q. | Continental-scale pollution of estuaries with antibiotic resistance genes | Nat. Microbiol. | 2 | 16270 |
| Zhu, Y.-G., Zhao, Y., Zhu, D., Gillings, M., Penuelas, J., Ok, Y.S., Capon, A., Banwart, S. | Soil biota, antimicrobial resistance and planetary health | Environ. Int. | 131 | 105059 | 