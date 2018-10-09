#Preprocesamiento de RI_RIGC

#Parte de Carlos:
#2. Valor 1 punto. Pipeline de pre procesamiento: mostrar diagrama del pipeline para pre procesar el data set de frases para tenerlo listo para vectorizar
#3. Valor 1 punto. División de data set en training-validation y test: mostrar porcentaje de división de data set y y mostrar contenido de archivos con data set dividido
#4) Valor 1 punto. Data set preprocesado para vectorizar: mostrar contenido de archivos con distintas transformaciones de frases para vectorizar



#Eliminar PMID del inicio de las oraciones
cut -f3,4 sentences_RI_RIGC.txt
cut -f3,4 sentences_Other.txt

#Remover referencias a tablas, figuras, otros artículos, revistas, etc.
#script de python RefFilter.py. Se utilizó para limpiar ambos archivos


#Unir ambos archivos pre-procesados en un solo documento
cat RI_2.0.txt Other2.0.txt > RI_Other_Cat.txt

#Lematización y POS tag de RI_Other_Cat.txt
./corenlp.sh -annotators tokenize,ssplit,pos,lemma,ner,parse,depparse -outputFormat conll -file /home/mescobar/RI_Other_Cat.txt -outputDirectory /home/mescobar/RI_Other_Cat.conll


#Nos regresa el archivo RI_Other_Cat.conll, que tiene las columnas de lematización y POS tags
#Debemos parsear. Crear un archivo de las oraciones pero representadas como lemma y otro de las oraciones representadas como POs
#El archivo de POS mezclarlo con el archivo de letras o de palabras.
#Vectorizar esto pues ya es informativo. E.g. lemma lemma lemma pos pos pos 



#Para correr en paralelo la lematizacion y pos tagging porque era muy lento, Wong lo hizo para las primeras 25000
#lineas del archivo, yanis para las siguientes 25000 y para escobar las ultimas 26043. 
#Esto se hizo con head y tail.
#RI_Other_1W.txt, RI_Other_2Y.txt y RI_Other_3E.txt. Todos disponibles en /export/storage/users/mrivero/Bioinfo_DEWY/Bioinformatica/BioNLP/RI_O_conll

cat RI_Other_1W.txt.conll RI_Other-2.5Y.txt.conll RI_Other_3E.txt.conll > RI_Other_DEWY.conll



#Se unieorn los 3 archivos y nos quedamos con las columnas que consideramos informativas: lemma y POS
cut -f3,4 RI_Other_DEWY_1.0.conll > RI_O_lemma_POS.conll

#Representar cada oración como (lemma)(pos)(lemma)(pos)... Se considera que la oración termina con las etiquetas RI o OTHER (éstos no se incluyen en el archivo a vectorizar)
#se utilizó script de python "lemma_pos.py" disponible en  /export/storage/users/mrivero/Bioinfo_DEWY/Bioinformatica/BioNLP/RI_O_conll/LemmaPOS
#Se obtuvo entonces el documento con el nombre Lemma_POS_Line_E1.txt, frases transformadas a lemma y pos.
#Agregar etiquetas informativas (TF) cuando existiera uno en la frase. Se extrajeron los TF de http://regulondb.ccg.unam.mx/menu/download/datasets/files/network_tf_gene.txt
#y se buscaron en las frases transformadas. Para esto se utilizó el script de python TFtaggingLemmaPos.py


#Repetir lo mismo con otra combinación, como lemma 
#Obtener las columnas de lemma 
cut -f3 RI_Other_DEWY_1.0.conll > RI_O_Lemma.conll
#Representar cada oración de forma de Lemma. Se considera que la frase termina con las etiquetas RI o Other
#script de python LemmaLinen.py disponible en /export/storage/users/mrivero/Bioinfo_DEWY/Bioinformatica/BioNLP/RI_O_conll/Lemma
#Se obtuvo entonces el documento con el nombre Lemma_Line_E1.txt, las frases transformadas a forma de lemma.
#Agregar etiquetas informativas (TF) cuando existiera uno en la frase. Se extrajeron los TF de http://regulondb.ccg.unam.mx/menu/download/datasets/files/network_tf_gene.txt
#y se buscaron en las frases transformadas. Para esto se utilizó el script de python TFtagging.py y se obtuvo el documento LEmma_TF_E1.0.txt.


#Dividir los Datasets de Lemma_POS y de Lemma en training y test. Para esto se utilizó el script de python TrainingTestLemmaPOS.py y TrainingTestLemma.py respectivamente.
#Se utilizó 80% de los datos como training data y el 20% restante como test data para ambos casos.