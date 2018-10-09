
# coding: utf-8

# In[35]:

#Código que filtra las referencias encontradas en archivos.
#Sustituye paréntesis con números por nada,lo cual en la mayoría de los casos son referencias.
import re 
salida=open('/home/mescobar/Escritorio/Tercer_Semestre/Bioinfo/senOth/Other_2.0.txt','w')
with open ('/home/mescobar/Escritorio/Tercer_Semestre/Bioinfo/senOth/Other_0.5.txt','r') as archivo:
    for line in archivo:
        line=re.sub(r"\(.*\d+.+?\)", "", line)
        line=re.sub(r"et al", "", line, flags=re.IGNORECASE)
        line=re.sub(r"molecular microbiology", "", line, flags=re.IGNORECASE)

        salida.write(line)
salida.close()

