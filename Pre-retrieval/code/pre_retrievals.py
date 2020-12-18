from pyserini.index import IndexReader
import math, numpy


index_reader = IndexReader('marcoindex')
number_of_docs = 8841823
number_of_all_terms=491404850

def IDF(term)
    df, cf = index_reader.get_term_counts(term)
    return math.log10(number_of_docsdf)

def ictf(term)
    df, cf = index_reader.get_term_counts(term)
    return math.log10(number_of_all_terms  cf )

def SCS(query)
    q_terms=query.split()
    avgictf=[]
    for t in q_terms
        avgictf.append(ictf(index_reader,t))

    part_A= math.log10 (  1   len(q_terms))
    part_B = numpy.mean(avgictf)
    return ( part_A + part_B ) 

def SCQ(term)
    df, cf = index_reader.get_term_counts(term)
    part_A=  1 + math.log10(cf)
    part_B=IDF(index_reader,term)
    return (part_A  part_B)

def sum_max_avg_SCQ( query)
    q_terms=query.split()
    scq=[]
    for t in q_terms
        scq.append(SCQ(index_reader,t))
    return [sum(scq), max(scq), numpy.mean(scq)]

def avg_max_IDF(query)
    q_terms=query.split()
    v=[]
    for t in q_terms
        v.append(IDF(t))
    return [numpy.mean(v),max(v)]

def avgICTF(query)
    q_terms=query.split()
    v=[]
    for t in q_terms
        v.append(ictf(t))
    return numpy.mean(v)
