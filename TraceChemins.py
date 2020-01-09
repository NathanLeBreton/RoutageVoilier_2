# IMPORTS
import sys
import time
import os

from bokeh.models import ColumnDataSource

def MeilleurChemin(arrayLat,arrayLong,arrayDist,arrayTime,arrayStress,arrayTimeGlobale,arrayStressGlobale):
    tailleList = 0         
    with open("noisy_iso.dat", "r") as ins:
        for line in ins:
            cdc = line
            maListe = cdc.split(" ")
            tailleList = tailleList+1
            #on lit seulement les lignes qui contiennent des données
            if maListe[0] == '\n':
                break
            elif maListe[0] != '##':
                for j in range(len(maListe)):
                    #print("value : " + maListe[j])
                    maListe[j] = float(maListe[j]) 
                arrayLat.append(maListe[8])
                arrayLong.append(maListe[9])
                arrayDist.append(maListe[5])
                arrayTime.append(maListe[7])         
      
    with open("noisy_isofront.dat", "r") as ins:
        for line in ins:
            cdc = line
            maListe = cdc.split(" ")       
            for i in range(len(maListe)):
                try:
                    maListe[i] = float(maListe[i])
                except: 
                    pass
            for i in range (1,tailleList-2):
                arrayStress.append(maListe[1])          
      
    
   
    #le meilleur chemin :
    with open("noisy_isofront.dat", "r") as ins:
        for line in ins:
            cdc = line
            maListe = cdc.split(" ")       
            for i in range(len(maListe)):
                try:
                    maListe[i] = float(maListe[i]) 
                except : 
                    pass
                
    for i in range(len(arrayLat)):
        arrayTimeGlobale.append(maListe[0])
        arrayStressGlobale.append(maListe[1]) 
        
def AutresChemins(tabChemin):
    #autres chemins 
    tabStress = []
    tabTime = []
    with open("noisy_front.dat", "r") as ins:
        num = 1
        for line in ins:
            cdc = line
            maListe = cdc.split(" ")
            for j in range(len(maListe)):
                try:
                    maListe[j] = float(maListe[j])
                except:
                    pass
                tabTime.append(maListe[0])
                tabStress.append(maListe[1])
    
    
    val = 0
    with open("noisy_ps.dat", "r") as ins:
        arrayDist = []
        arrayTime = []
        arrayLat = []
        arrayLong = []
        arrayStress = []
        arrayTimeGlobal = []
        
        
        #Je reset toutes les sources pour effacer les anciens chemins 
        for i in range(len(tabChemin)):           
            tabChemin[i].data = dict(x=arrayLong, y=arrayLat, dist=arrayDist,time=arrayTime,
                                     x2=[], y2=[]) 
        
        for line in ins:
            cdc = line
            maListe = cdc.split(" ")
            #if maListe est vide : ligne blanche
            if maListe[0] == '\n':
                #si array deja vide on fait rien
                #sinon on affiche la ligne et on reset les 2 array
                if len(arrayLat)!=0 and len(arrayLong)!=0 :                        

                    
                    for i in range(len(arrayLat)):                    
                        arrayStress.append(tabStress[val])
                        arrayTimeGlobal.append(tabTime[val])
                        
                   
                    val = val+1  
                           
                    s = ColumnDataSource(data=dict(x=arrayLong, y=arrayLat, dist=arrayDist,
                                               time=arrayTime, stress=arrayStress,
                                               x2=arrayTimeGlobal, y2=arrayStress))  
                    
                    tabChemin.append(s)
                          
                    arrayDist = []
                    arrayTime = []
                    arrayLat = []
                    arrayLong = []
                    arrayStress = []  
                    
                    arrayStressGlobal = []
                    arrayTimeGlobal = []
                    
            #on lit seulement les lignes qui contiennent des données
            if maListe[0] != '##' and maListe[0] != '\n':          
                for j in range(len(maListe)):
                    maListe[j] = float(maListe[j]) 
                #on extrait les x et y 
                arrayLat.append(maListe[8])
                arrayLong.append(maListe[9])
                arrayDist.append(maListe[5])
                arrayTime.append(maListe[7])
                
        
                
