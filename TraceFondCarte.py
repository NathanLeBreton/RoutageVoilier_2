# IMPORTS
import sys
import time
import os

from bokeh.models import ColumnDataSource

def Carto(source, arrayGlobalX,arrayGlobalY):
    os.chdir(source+"Projet/")
    with open("background2.dat", "r") as ins:
        arrayX = []
        arrayY = []
       
        numCarte = 0
        for line in ins:
            cdc = line
            TabValeur = line.split(" ")
            if TabValeur[0] == '\n': 
                #si array deja vide on fait rien
                #sinon on affiche la ligne et on reset les 2 array
                if len(arrayX)!=0 and len(arrayY)!=0 :                               
                   
                    arrayGlobalX.append(arrayX)
                    arrayGlobalY.append(arrayY)
                    
                    arrayX = []
                    arrayY = []
            else:
                for j in range(len(TabValeur)):
                    TabValeur[j] = float(TabValeur[j]) 
                arrayX.append(TabValeur[0])
                arrayY.append(TabValeur[1])