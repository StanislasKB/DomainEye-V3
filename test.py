
import os 
import json
stream=os.popen("whois {}".format("google.com"))
temp_data_list=stream.readlines() 
data_list=temp_data_list[125:159]
data_list=data_list[1:]

data={}
for mot in data_list:
    tmp=mot.split(':')
    cle=tmp[0].replace(" ","_").lower()
    valeur=":".join(tmp[1:])
    data[cle]=valeur.replace('\n','')

print(data)
    
        
       
        
   
    
    
