# Codd’s World: Topics and their Evolution in the Database Community Publication Graph
# Synopsis
Scholarly Network Analysis (SNA) is the study of a scientific research networks aiming to discover meaningful insights helpful to the research community to make data-driven research decisions. Analyzing these networks has become increasingly challenging due to the amount of scientific research being added daily, in addition to information being collected from more online sources (e.g. academic social platforms), making the network larger and more complex. Our work aims to present an early study on a specific network: the database community publication graph,  Codd's World. We specifically analyze the topics of the published papers, the relevance of authors and papers, and how this relates to raw publication counts. This work mainly demonstrates how Topic Modeling can be a useful entry point for SNA.
# Motivation
This analytical study is inspired by Prof. Dr. Erhard Rahm and Prof. Dr. Andreas Thor work on Citation analysis of database publications [1] and Prof. Dr. Erhard Rahm and David Aumüller work on Affiliation analysis of database publications [2].
# Overview of the Input Datasets
The bibliographic database for computer sciences DBLP [3] was identified as the main source of information. To narrow down information in DBLP specific to the database community, the node of the foundational paper of Edgar Codd on relational databases [4] was identified. Further, the papers with transitive reference relationships to the main paper node were considered (i.e., papers that cite transitively the work of Codd). This led to the formation of the database community citation network graph (Codd's World). Based on this, further sub-graphs were constructed to form the database scholarly network. The resulting heterogeneous network consisted of four nodes, namely, (a) authors, (b) papers, (c) venues and (d) journals. The five types of relationships in the network consisted of authorship, collaboration, belonging to venue, belonging to journal and citation. Taken together, these nodes and relationships formed the database scholarly network, which was then further used for the SNA.<br />
The input datasets used can be found at [5]. 
# Installation and Run
This Python 3.0 framework can be used for Topic Modeling and Visualization. The framework utilizes the Python library TOM (TOpic Modeling) [6] for topic extraction using Non-negative Matrix Factorization (NMF). The default number of topics is set to 30 based on the Input Dataset used.<br />
1) Install Python library TOM (TOpic Modeling)
2) Type the name of the input dataset inside the file named CvsFileName.txt <br />
4) Run the program through command prompt <br />
```
   python TopicsNum.py
```
# Output
1) GlobalTopicsWithName.csv: File containing the extracted topics for all the years and meaningful names can be given to the topics manually <br />
2) TopicIDPaperID: File containing PaperID assigned to TopicID
3) years: Folder containing yearly files with the topics appearing in that particular year <br />
4) output: Folder containing output visualizations Eg. Word Distribution in a Topic <br />
5) topicevolution.png: Bubble chart for visualizing Topic Evolution over the years
# Detailed Technical Analysis Report
The detailed technical analysis report depicting the complete output and results can be found at [7].
# Contributors
Rutuja Shivraj Pawar, Sepideh Sadat Sobhgol
# License
This project is licensed under the terms of the MIT license.
# References
[1] Rahm, E., Thor, A.: Citation analysis of database publications. ACM Sigmod Record 34(4), 48{53 (2005)

[2] Aumüller, D., Rahm, E.: Affiliation analysis of database publications. ACM SIGMOD Record 40(1), 26{31 (2011)

[3] Ley, M.: The dblp computer science bibliography: Evolution, research issues, perspectives. In: International symposium on string processing and information retrieval. pp. 1{10. Springer (2002)

[4] Codd, E.F.: A relational model of data for large shared data banks. Communications of the ACM 13(6), 377{387 (1970)

[5] ftp://itidbftppublic:dbse0Run41rP@ftpiti.cs.uni-magdeburg.de/upload/protolabs/datasets/as-is/codds-world/2019-02

[6] Guille, A., Soriano-Morales, E.P.: Tom: A library for topic modeling and browsing. In: EGC. pp. 451{456 (2016)

[7] https://github.com/Rspawar/Scholarly-Network-Analysis/blob/master/Technical_Analysis_Report.pdf
