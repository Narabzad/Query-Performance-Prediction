# Query-Performance-Prediction
State-of-the-art pre-retrieval and post-retrieval QPP methods on TREC datasets

You can find the implementation of pre-retrieval QPPs including avgIDf, maxIDF, SCS, avgICTF, avgSCQ, maxSCQ and sumSCQ. You need to set  the indexpath, number of documents in the collection and number of all terms in the collection in [pre-retrievals.py](https://github.com/Narabzad/Query-Performance-Prediction/blob/master/Pre-retrieval/code/pre_retrievals.py). 

You can find results of state-of-the-art query performance prediction methods in predicting Query-Likelihood (QL) retrieval model  on well-known TREC datasets such as Robust04, GOV2, ClueWeb09 and  ClueWeb12 and their associated topics.

Aggregating functions such as {avg,min,max,sum} has been utilized on query terms to calculate the QPP for the whole query.

Details of each of the methods can be found in the following references: 

- **Pre-retrieval methods :**
  - SCS : [Using Coherence-Based Measures to Predict Query Difficulty](https://link.springer.com/chapter/10.1007/978-3-540-78646-7_80)
  - SCQ : [Effective Pre-retrieval Query Performance Prediction Using Similarity and Variability Evidence](https://link.springer.com/chapter/10.1007/978-3-540-78646-7_80)
  - IDF : [Using Coherence-Based Measures to Predict Query Difficulty](https://link.springer.com/chapter/10.1007/978-3-540-78646-7_80)
  - PMI : [Predicting the effectiveness of queries and retrieval systems](https://dl.acm.org/doi/10.1145/1842890.1842906)
  - VAR : [Effective Pre-retrieval Query Performance Prediction Using Similarity and Variability Evidence](https://link.springer.com/chapter/10.1007/978-3-540-78646-7_80)

- **Post-retrieval methods :**
  - WIG : [Query performance prediction in web search environments](https://dl.acm.org/doi/10.1145/1277741.1277835)
  - Clarity : [Predicting query performance](https://dl.acm.org/doi/10.1145/564376.564429)
  - QF : [Query performance prediction in web search environments](https://dl.acm.org/doi/10.1145/1277741.1277835)
  - ISD : [Improved queryperformance prediction using standard deviation](https://dl.acm.org/doi/10.1145/2009916.2010063)
  - SD : [Standard Deviation as a Query Hardness Estimator](https://link.springer.com/chapter/10.1007/978-3-642-16321-0_21)
  - SMV : [Query Performance Prediction By Considering Score Magnitude and Variance Together](https://dl.acm.org/doi/abs/10.1145/2661829.2661906)
  - UEF : [Using statistical decision theory and relevance models for query-performance prediction](https://dl.acm.org/doi/10.1145/1835449.1835494)

Please do not hesitate to contact if you have any questions : narabzad@ryerson.ca
