#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:09:22 2016

@author: Annie Tran
"""
import os
os.chdir('/Users/isarasuntichotinun/Desktop/ANNIE/CSC 591/Code/')
#get crime rate
from bs4 import BeautifulSoup as BS
import requests
from crimedata import crimeNum, crimerate
import pandas as pd
import numpy as np

#read in the data
data=pd.read_csv('/Users/isarasuntichotinun/Desktop/ANNIE/CSC 591/Data/structured_articles.csv')
del data['Unnamed: 0']

#find <meta property="og:description" content="12,253 (number) in 2013./>
#text = requests.get('https://knoema.com/atlas/Canada/topics/Crime-Statistics/Homicides/Homicides').text
#text=text.split(" ")

data['country']=data['country'].astype(str)

data[data['country']=='Iraqi Kurdistan']

#crime rates for the LA and Africa data
xl = pd.ExcelFile('/Users/isarasuntichotinun/Desktop/ANNIE/CSC 591/Data/Struct data LA new.xlsx')
xl.sheet_names
LAdata=xl.parse('useful data')

LAdata.rename(columns={'Target': 'target'}, inplace=True)

#LAdata = pd.read_csv('/Users/isarasuntichotinun/Desktop/ANNIE/CSC 591/Data/Struct data LA new.csv')

#
#If it starts out as a riot, mark it as a riot:
#LAdata['riot']=LAdata['etype'].map(lambda x: 0 if int(x) in {1, 2, 5, 6} else 1)
#
##if it escalates to a riot, mark it as a riot:
#for i in range(len(LAdata['riot'])):
#    if int(LAdata['escalation'].iloc[i]) in {3,4,7,8,9,10}:
#        LAdata.set_value(i,'riot',1)
        
#crimedict={}
uniquec=list(LAdata['country'].unique())

#replace space with dash so it can be put in a link
uniquec=map(lambda x: x.replace(' ','-'),uniquec)
LAdata['country']=map(lambda x: x.replace(' ','-'),LAdata['country'])




for i in range(len(uniquec)):
    country=uniquec[i]
    if country not in crimedict.keys():
        try:
            #All the liiiiinnnkkks to the crriimmes
            homcountlink = 'https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Homicides/Homicides'
            homratelink = 'https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Homicides/Homicide-rate'
            firecountlink = 'https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Homicide-by-Firearms/Number-of-homicides-by-firearm'
            fireratelink = 'https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Homicide-by-Firearms/Homicide-by-firearm-rate'
            motorcountlink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Burglary-Car-Theft-and-Housebreaking/Theft-Motor-Vehicle'
            motorratelink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Burglary-Car-Theft-and-Housebreaking/Theft-Motor-Vehicle-Rate'
            privatecountlink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Burglary-Car-Theft-and-Housebreaking/Theft-Private-Cars'
            privateratelink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Burglary-Car-Theft-and-Housebreaking/Theft-Private-Cars-Rate'
            burglarycountlink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Burglary-Car-Theft-and-Housebreaking/Burglary-count'
            burglaryratelink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Burglary-Car-Theft-and-Housebreaking/Burglary-rate'
            housecountlink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Burglary-Car-Theft-and-Housebreaking/Burglaryhousebreaking-count'
            houseratelink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Burglary-Car-Theft-and-Housebreaking/Burglaryhousebreaking-rate'
            assaultcountlink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Assaults-Kidnapping-Robbery-Sexual-Rape/Assault-count'
            assaultratelink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Assaults-Kidnapping-Robbery-Sexual-Rape/Assault-rate'
            kidnapcountlink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Assaults-Kidnapping-Robbery-Sexual-Rape/Kidnapping-count'
            kidnapratelink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Assaults-Kidnapping-Robbery-Sexual-Rape/Kidnapping-rate'
            rapecountlink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Assaults-Kidnapping-Robbery-Sexual-Rape/Rape-count'
            raperatelink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Assaults-Kidnapping-Robbery-Sexual-Rape/Rape-rate'
            robberycountlink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Assaults-Kidnapping-Robbery-Sexual-Rape/Robbery-count'
            robberyratelink='https://knoema.com/atlas/'+country+'/topics/Crime-Statistics/Assaults-Kidnapping-Robbery-Sexual-Rape/Robbery-rate'
        
            #get all the crime numbers and crime rates of a country
            homnum=crimeNum(homcountlink)
            homrate=crimerate(homratelink)
            firenum=crimeNum(firecountlink)
            firerate=crimerate(fireratelink)
            motornum=crimeNum(motorcountlink)
            motorrate=crimerate(motorratelink)
            privatenum=crimeNum(privatecountlink)
            privaterate=crimerate(privateratelink)
            burgnum=crimeNum(burglarycountlink)
            burgrate=crimerate(burglaryratelink)
            housenum=crimeNum(housecountlink)
            houserate=crimerate(houseratelink)
            assaultnum=crimeNum(assaultcountlink)
            assaultrate=crimerate(assaultratelink)
            kidnapnum=crimeNum(kidnapcountlink)
            kidnaprate=crimerate(kidnapratelink)
            rapenum=crimeNum(rapecountlink)
            raperate=crimerate(raperatelink)
            robberynum=crimeNum(robberycountlink)
            robberyrate=crimerate(robberyratelink)
                
                
            totalcrimes=homnum+firenum+motornum+privatenum+burgnum+housenum+assaultnum+kidnapnum+rapenum+robberynum
            
            #rate per 100,000 population
            expectedRate=(homnum/totalcrimes)*homrate+(firenum/totalcrimes)*firerate+(motornum/totalcrimes)*motorrate+ \
                          (privatenum/totalcrimes)*privaterate+(burgnum/totalcrimes)*burgrate+(housenum/totalcrimes)* \
                          houserate+(assaultnum/totalcrimes)*assaultrate+(kidnapnum/totalcrimes)*kidnaprate+(rapenum/totalcrimes)* \
                          raperate+(robberynum/totalcrimes)*robberyrate 
            
            
            crimedict[country]=expectedRate
        except:
            print i, country

crimedict['Scotland']=341.7285714
crimedict['New-Mexico']=597
crimedict["Cote-d'Ivoire"] = max(crimedict.values())

#locations the program couldn't find crime stats for
updatedlist=['England','Ireland','United Arab Emirates']
updatedlist=[]
for i in range(len(updatedlist)):
    if uniquec[i] not in crimedict.keys():
        updatedlist.append(uniquec[i])

#fill in the crime rate stats
for i in range(len(LAdata)):
    c = LAdata['country'][i]
    LAdata['crime rate'][i] = crimedict[c]
    

#group the target by numbers
     #target
    #1: Opposition supporters (Citizens)
    #2: Government
    #3: Police
    #4: Corporations
    #5: Religious Group
    #6: Fans
    #7: Military
    #8: Tourist

for i in range(len(LAdata)):
    if LAdata['Grouped Target'][i] in ['Citizens','citizens']:
        LAdata['Target'][i] = 1
    elif LAdata['Grouped Target'][i] == 'Government':
        LAdata['Target'][i] = 2
    elif LAdata['Grouped Target'][i] == 'Police':
        LAdata['Target'][i] = 3
    elif LAdata['Grouped Target'][i] == 'Corporations':
        LAdata['Target'][i] = 4
    elif LAdata['Grouped Target'][i] in ['Religious Group','Religious group']:
        LAdata['Target'][i]=5
    elif LAdata['Grouped Target'][i] == 'Fans':
        LAdata['Target'][i] = 6
    elif LAdata['Grouped Target'][i] == 'Military':
        LAdata['Target'][i] = 7
    elif LAdata['Grouped Target'][i] == 'Tourists':
        LAdata['Target'][i] = 8

LAdata = LAdata.drop('Grouped Target',1)

#LAdata.to_csv('cleanedLA.csv', sep=',', index_col = False)

#save as excel
writer = pd.ExcelWriter('cleanedLA.xlsx',engine='xlsxwriter')
LAdata.to_excel(writer,'Sheet1')
writer.save()

#save dictionary
np.save('crime_dictionary.npy',crimedict)

#to load dictionary
# Load
#read_dictionary = np.load('crime_dictionary.npy').item()

#or another way to save
f = open("crime_dictionary.txt","w")
f.write( str(crimedict) )
f.close()

