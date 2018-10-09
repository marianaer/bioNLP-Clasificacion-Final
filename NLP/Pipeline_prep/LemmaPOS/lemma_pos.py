
# coding: utf-8

# In[7]:

#Representa las oraciones en función de sus valores de lematización y POS tagging.
lista=[]
bandera=0
salida=open('/home/mescobar/Escritorio/Lemma_POS_Line_E1.0.txt','w')
with open('/home/mescobar/Escritorio/RI_O_lemma_POS.conll', 'r') as archivo:
    for line in archivo:           #Recorre el archivo
        line=line.split()	#Splitea la línea
        if not(line==[]):     	#Si la línea no está vacía
            if(line[0]=='.'):   #ENtonces entra, si en la primera y la siguiente columna (lemma) hay
                if(line[1]=='.'): #un punto, la bandera es cierta.
                    bandera=1
            if(line[0]=='ri'): #si en la columna de lemma encuentra "ri"  (regulatory interaction)
                linea=str(lista)+'\n'  #salta la línea, elimina elementos que dificultan el parseo 
                linea=linea.replace(",","") #y escribe como una sola línea (oración).
                linea=linea.replace("[","")
                linea=linea.replace("]","")
                linea=linea.replace("\'","")
                salida.write(linea)
                lista=[]
            if(line[0]=='other'):   #Hace lo mismo para cuando encuentra other, pero la bandera de que 
                if bandera:  #hay un punto antes debe ser cierta para poder distinguir de la palabra 
                    linea=str(lista)+'\n'#other del final de linea de las que están en el texto.
                    linea=linea.replace(",","")
                    linea=linea.replace("[","")
                    linea=linea.replace("]","")
                    linea=linea.replace("\'","")
                    salida.write(linea)
                    lista=[]
                    bandera=0
            if(line[0]=='OTHER'):
                if bandera:
                    linea=str(lista)+'\n'
                    linea=linea.replace(",","")
                    linea=linea.replace("[","")
                    linea=linea.replace("]","")
                    linea=linea.replace("\'","")
                    salida.write(linea)
                    lista=[]
                    bandera=0
            if not(line[0]=='ri' or line[0]=='other' or line[0]=='OTHER'):
                lista.append(line[0]) #Si no encuentra algo que le indique que terminó la línea
                lista.append(line[1])  #Sigue escribiendo las columnas como oración.
salida.close()

