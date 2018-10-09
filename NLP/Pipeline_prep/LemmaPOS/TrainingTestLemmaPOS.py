
# coding: utf-8

# In[57]:


import random
training_data=open('/home/mescobar/Escritorio/Lemma_Pos_Train.txt','w') #Crea archivos de train y test 
testing_data=open('/home/mescobar/Escritorio/Lemma_Pos_Test.txt','w')
with open("/home/mescobar/Escritorio/Lemma_POS_Line_TF_E1.0.txt","r") as file: #Abre archivo Preprocesado Lemma_POS
    data=list()#convierte el archivo a una lista
    for line in file:
        data.append(line.split('\n'))
random.shuffle(data)#"Shufflea" la lista aleatoriamente
train_data = data[:int((len(data)+1)*.80)] #80% de la long. de la lista es el set de entrenamiento
test_data = data[int(len(data)*.80+1):] #20% de la long de la lista es el set de evaluación

for i in train_data:
        linea=str(i)+'\n'#La lista se convierte en una linea con salto de linea 
        linea=linea.replace(",","")#Reemplazando caracteres que afecten un parseo a futuro 
        linea=linea.replace("[","")
        linea=linea.replace("]","")
        linea=linea.replace("\'","")
        training_data.write(linea)
training_data.close()

for j in test_data:
        linea=str(j)+'\n'#La lista se convierte en una linea con salto de linea 
        linea=linea.replace(",","")#Reemplazando caracteres que afecten un parseo a futuro 
        linea=linea.replace("[","")
        linea=linea.replace("]","")
        linea=linea.replace("\'","")
        testing_data.write(linea)
testing_data.close()

