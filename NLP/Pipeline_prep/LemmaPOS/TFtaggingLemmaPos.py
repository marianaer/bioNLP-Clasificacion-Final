
# coding: utf-8

# In[1]:


diccionario={}#Declarando diccionario 
salida=open('/home/mescobar/Escritorio/Lemma_Pos_Line_TF_E1.0.txt','w')#Output
with open('/home/mescobar/Escritorio/EcoliTF.txt','r') as archivo:#Abriendo archivo
    for line in archivo:#Iterando en cada linea 
        line=line.split()#Spliteando 
        diccionario[line[0]]=[]#Llenando las llaves del diccionario con TF
with open('/home/mescobar/Escritorio/Lemma_POS_Line_E1.0.txt','r') as archivo:#Abriendo archivo
    for line in archivo:#Iterando en cada linea 
        line=line.split()#Spliteando 
        for i in diccionario.keys():#Iterando en cada TF del diccionario 
            if(i in line):#Si el TF esta en la linea
                if(line[len(line)-1]=='TF'):#Pero ya habiamos encontrado otro TF
                    continue#continua
                else:#Si es el primer TF encontrado
                    line.append('TF')#Agregamos TF a la linea
        linea=str(line)+'\n'#La lista se convierte en una linea con salto de linea 
        linea=linea.replace(",","")#Reemplazando caracteres que afecten un parseo a futuro 
        linea=linea.replace("[","")
        linea=linea.replace("]","")
        linea=linea.replace("\'","")
        salida.write(linea)#Escribiendo la linea ya limpia en el output 
salida.close()#Cerrando output

