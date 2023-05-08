from django.shortcuts import render
from django.http import HttpResponse
import os 
import json
from DomainEyeApp.models import History

def home_view(request):
    return  render(request, 'home_view.html')

    
def data_view(request):
    lien=''
    historique=History()
    
    if request.method=='POST':
        stream=os.popen("whois {}".format(lien))
        temp_data_list=stream.readlines() 
        data_list=temp_data_list[125:159]
        data_list=data_list[1:]

        data={}
        for mot in data_list:
            tmp=mot.split(':')
            cle=tmp[0].replace(" ","_").lower()
            valeur=":".join(tmp[1:])
            data[cle]=valeur.replace('\n','')   
                
        #historique=History.objects.create(domain=lien)
        
    elif request.GET.get('search_history'):
        lien=str(request.GET.get('search_history'))
        stream=os.popen("whois {}".format(lien))
        temp_data_list=stream.readlines() 
        data_list=temp_data_list[125:159]
        del(data_list[0])

        data={}
        for mot in data_list:
            tmp=mot.split(':')
            cle=tmp[0].replace(" ","_").lower()
            valeur=":".join(tmp[1:])
            data[cle]=valeur.replace('\n','')   
    
        
       
        
   
      
    
    
    return render(request, 'data_view.html',data)
    
    
def history_view(request):
    historique=History.objects.all()
    return render(request,'history_view.html',{'history':historique})