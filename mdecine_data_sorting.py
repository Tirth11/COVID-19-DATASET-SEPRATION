# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:26:55 2020

@author: Darshan Sapariya
"""


#%%Importing libraies and files
import numpy as np 
import pandas as pd
import pickle as pi
f=open("medicine.pickle","rb")
dicti=pi.load(f)
f.close()

data = pd.read_excel('FinalMRDS.xlsx')
covidMRNo = pd.read_excel('final.xlsx')

#%%Saperating Required columns

req_data = data[['MRNo', 'Gender', 'AgeYears', 'medicine', 'medicinequantity']]

#%% Filling Nans in MRNo, gender and age column

req_data['MRNo'].fillna(value = 0, inplace = True)
req_data['Gender'].fillna(value = 0, inplace = True)
req_data['AgeYears'].fillna(value = 0, inplace = True)

for a in range(0,len(req_data),1):
    if req_data['MRNo'][a]!=0:
        num=req_data['MRNo'][a]
    else :req_data['MRNo'][a]=num
    
for a in range(0,len(req_data),1):
    if req_data['Gender'][a]!=0:
        num=req_data['Gender'][a]
    else :req_data['Gender'][a]=num
    
for a in range(0,len(req_data),1):
    if req_data['AgeYears'][a]!=0:
        num=req_data['AgeYears'][a]
    else :req_data['AgeYears'][a]=num

#%%
req_data.dropna(inplace=True)

#%%creating list of unwanted things

garbagelist = '|'.join(['SYRINGE', 'GLOVES','BAG', 'NEEDLE', 'MASK', 'VEINFLON', 'THERMOMETER','PAINT','TRANSHALER', 'CANULA', 'Form','TAPE','TEGADERM','CERTOFIX','SHAMPOO','BLADE','BANDAGE','SAC','COTTON','KIT','TEST','VOLUVEN','TUBING','CERTOFIX','TRIO', 'CANNULA', 'INHALER','SPRAY','SUSPENSION','WATER','DROP', 'MERSILK','DS%', 'LINE','UROMETER','VANILLA','CATGUT','BLADE'])
#If more things has to be removed or want the removed things to be added
#Edit this list if and add or remove the keyword as per the need and run whole code again

for i in range(0,len(garbagelist),1):
    req_data['Notreq'] = 0

# for index, Notreq in req_data.iterrows():
#     for i in range(0,len(garbagelist),1):
#       req_data['Notreq'] + req_data['medicine'].str.find(garbagelist[i]) + 1

req_data['Notreq'] = req_data['medicine'].str.contains(garbagelist).astype(int)

#%%REMOVIG UNWANTED THINGS
index = req_data[req_data['Notreq']==1].index
req_data.drop(index,inplace=True)
#%%FINALIZING THE DATA
final_data = req_data[['MRNo', 'AgeYears', 'Gender', 'medicine','medicinequantity']]
#%%FEATURING THE FINAL DATA
final_data = final_data.set_index(['MRNo', 'Gender', 'AgeYears','medicine'])
# #%%
# new = final_data.groupby(['MRNo', 'Gender', 'AgeYears']).sum()
# #%%
# new.to_excel('medicines_of_Corona.xlsx', header=True)

#%%EXPORTING THE DATA
final_data.to_excel('Medicines_of_covid_patients.xlsx', header = True)