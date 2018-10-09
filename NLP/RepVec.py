  GNU nano 2.0.9                                          Fichero: extraccion-caracteristicas-vectorizacion.py                                                                                  Modificado
# -*- encoding: utf-8 -*-

import os
from time import time
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

__author__ = 'CMendezC'

# Goal: Feature extraction, vectorizer and TF-IDF

# Parameters:
# 1) --inputPath Path to read input files.
# 2) --outputPath Path to save output files.
# 3) --vectorizer Vectorizer: b=binary, f=frequency, t=tf-idf.
# 4) --feature Extracted feature from documents: word, lemma, pos, ner

# Ouput:
# 1) Report with dictionary, vectors, cosine similarity matrix.

# Execution:
# python extraccion-caracteristicas-vectorizacion.py
# --inputPath /home/compu2/bionlp/lcg-bioinfoI-bionlp/representaciones-vectoriales/data-set-three-sentences
# --outputPath /home/compu2/bionlp/lcg-bioinfoI-bionlp/representaciones-vectoriales/reports-three-sentences
# --vectorizer b
# --feature word

# source activate python3
# python extraccion-caracteristicas-vectorizacion.py --inputPath /home/compu2/bionlp/lcg-bioinfoI-bionlp/representaciones-vectoriales/data-set-three-sentences --outputPath /home/compu2/bionlp/lcg-bioinfo$

###########################################################
#                       MAIN PROGRAM                      #
###########################################################

if __name__ == "__main__":
    # Parameter definition
    parser = argparse.ArgumentParser(description='Feature extraction and vectorizer.')
    parser.add_argument("--inputPath", dest="inputPath", required=True,
                      help="Path to read input files", metavar="PATH")
    parser.add_argument("--outputPath", dest="outputPath", required=True,
                          help="Path to place output files", metavar="PATH")
    parser.add_argument("--vectorizer", dest="vectorizer", required=True,
                      help="Vectorizer: b=binary, f=frequency, t=tf-idf", metavar="CHAR",
                      choices=('b', 'f', 't'), default='b')
    parser.add_argument("--feature", dest="feature", required=True,
                      help="Feature: word, lemma, pos, ner", metavar="TEXT",
                      choices=('word', 'lemma', 'pos', 'ner'), default='word')

 args = parser.parse_args()

    # Printing parameter values
    print('-------------------------------- PARAMETERS --------------------------------')
    print("Path to read input files: " + str(args.inputPath))
    print("Path to place output files: " + str(args.outputPath))
    print("Vectorizer: " + str(args.vectorizer))
    print("Feature: " + str(args.feature))

    # Start time
    t0 = time()

    print("Reading documents...")
    documents = []
    # Read documents from input path
    for path, dirs, files in os.walk(args.inputPath):
        for file in files:
            if file.endswith(args.feature):
                with open(os.path.join(args.inputPath, file), mode="r", encoding="utf-8") as iFile:
                    print("...{}".format(file))
                    # Add file to document list
                    documents.append(iFile.read())
    print("  Documents: {}".format(len(documents)))

    # Create vectorizer	  Crea 3 tipos de vectorizadores
    print('  Vectorizer: {}'.format(args.vectorizer))
    if args.vectorizer == "b":
        # Binary vectorizer  vectorizaor binario
        vectorizer = CountVectorizer(ngram_range=(1, 1), binary=True)
    elif args.vectorizer == "f":
        # Frequency vectorizer de frecuencias
        vectorizer = CountVectorizer(ngram_range=(1, 1))
    else:
	# Binary vectorizer
        vectorizer = TfidfVectorizer(ngram_range=(1, 1))

    matrix = csr_matrix(vectorizer.fit_transform(documents), dtype='double') #crea matriz sparse reserva espacio para aquellas posiciones donde	sí hay un valor	(no 0)
    print('   matrix.shape: ', matrix.shape)  #imprime shape de la matriz para que nos de sus dimensiones

    similarityMatrix = cosine_similarity(matrix)   #la pasamos a un constructor que calcula la similitud coseno y nos da una nueva matriz
    print("   Cosine similarity matrix shape: {}".format(similarityMatrix.shape))


    #crea
    with open(os.path.join(args.outputPath, "report-vectorizer.{}.{}.txt".format(args.feature, args.vectorizer)), encoding="utf-8", mode="w") as oFile:
        oFile.write("Vectorizer: {}\n".format(args.vectorizer))
        oFile.write(str(vectorizer.get_feature_names()))
        oFile.write("\n")
        oFile.write(str(matrix.toarray()))
        oFile.write("\n")
        oFile.write(str(similarityMatrix))

    print("Feature extraction and vectorizer in: %fs" % (time() - t0))
