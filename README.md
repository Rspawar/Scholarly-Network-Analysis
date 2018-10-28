# Scholarly Network Analysis on Codd's World (The Database Community Publication Graph)
# Synopsis
Scholarly Network Analysis (SNA) is the study of a scientific research networks aiming to discover meaningful insights helpful to the research community to make data-driven research decisions. Analyzing these networks has become increasingly challenging due to the amount of scientific research being added daily, in addition to information being collected from more online sources (e.g. academic social platforms), making the network larger and more complex. Our work aims to present an early study on a specific network: the database community publication graph,  Codd's World. We specifically analyze the topics of the published papers, the relevance of authors and papers, and how this relates to raw publication counts. This work mainly demonstrates how Topic Modeling can be a useful entry point for SNA.
# Motivation
This analytical study is inspired by Prof. Dr. Erhard Rahm and Prof. Dr. Andreas Thor work on Citation analysis of database publications [1] and Prof. Dr. Erhard Rahm and David Aumüller work on Affiliation analysis of database publications [2].
# Overview of the Input Datasets
 
# Installation and Run
This Python 3.0 framework can be used for Topic Modeling and Visualization. The framework utilizes the Python library TOM (TOpic Modeling) [3] for topic extraction using Non-negative Matrix Factorization (NMF). The optimal number of topics can be set based on the output Greene metric plot for stablity analysis given the input dataset. The default is set to 10 based on the Input Dataset .csv (see output\greene.png).<br />
1) Install Python library TOM (TOpic Modeling)
2) Place the input dataset inside the folder TopicModeling next to file smallTestDataset.csv <br />
3) Type the name of the input dataset inside the file named CvsFileName.txt <br />
4) Run the program through command prompt opened in the same directory of script file <br />
```
   python TopicsNum.py
```
# Output
1) GlobalTopics.csv: File containing the extracted topics for all the years <br />
2) years: Folder containing yearly files with the topics appearing in that particular year <br />
3) years/final.csv: Detailed file generated after aggregating all the yearly files (This file is important for visualizing Topic Evolution over the years) <br />
4) output: Folder containing output visualizations Eg. Word Distribution in a Topic <br />
5) output/greene.png: Greene metric plot based on the input dataset and helpful to estimate the optimal number of topics <br />
6) output/topicevolution.png: Bubble chart for visualizing Topic Evolution over the years
# Scientific Publication Paper
The overview of the complete SNA carried out depicting the discovered insights on the formulated Research Questions can be found at [4].
# Contributors
Rutuja Shivraj Pawar, Sepideh Sadat Sobhgol
# License
This project is licensed under the terms of the MIT license.
# References
[1] Rahm, E., Thor, A.: Citation analysis of database publications. ACM Sigmod Record 34(4), 48{53 (2005)

[2] Aumüller, D., Rahm, E.: Affiliation analysis of database publications. ACM SIGMOD Record 40(1), 26{31 (2011)

[3] Guille, A., Soriano-Morales, E.P.: Tom: A library for topic modeling and browsing. In: EGC. pp. 451{456 (2016)

[4]

