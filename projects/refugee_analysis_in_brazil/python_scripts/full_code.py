'''This is a python program to analyse and acquire the data on migration. It shall be used to write an academic paper. 
 
A) INSTRUCTIONS:
This first comment will adress the general instructions of this code and of the research. We will adress the functionalities of migration_scanner.py [COMMENTS] and describe the method of analisys [METHOD USED: QUANTITATIVE ANALISYS]
Here are some important links:
    - this repository:
    - Read.me: in the above repository
    - References, databases, articles, sources: in the read.me


B) COMMENTS
Every single operation will have its following hash (#) and identification number (1.1 , 2.3 , etc). You may search any specific part of this code using ctrl + f. the basic data structure of this file can be found in the READ.ME 


C) METHOD USED: QUANTITATIVE ANALISYS
 
We have now aquired the total number of refugees from Venezuela. The values do seem to increase from 2016 to 2017 and even more from 2017 to 2018-2019-2020. After 2020, the numbers are stable. In order to verify if this increase is justified from the new 2017 migration law and the Acolhida mission (2018 to 2021), 2 factors need to be demonstrated: 
A) a global increase in refugee numbers (application of the new law); 
B) The larger relative increase in venezuelan refugees compared to the global increase. 
 In short: Global_before/Global_After = global_increase_ratio                                                   !!! SHOWS THE EFFECTIVNESS OF THE 2017 LAW
VENEZUELA_before/Venezuela_after = venezuelan ratio
venezuelan ratio/global_increase_ratio = result                                                                            !!! if result == 1 or <1: 2018 policy is not effective

More on the read.me file'''



###################################### FIRST PART : INICIAL SETUP  ######################################


#1.1. import the pandas library
import pandas as pd
print('This is an open-source code used in the article XXXXXXX. To find more about it, visit READ.ME in the repository XXXXXXXX')
print('')

#1.2. Open the data on migration - 1994 to 2025 refugee request - on Brazil
open_data1 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_1994_2023.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
df1 = pd.DataFrame(open_data1)
print('DISPLAY OF THE FULL DATA FRAME')
print(df1)
print()

## 1.3. Visualize the Column Values
print()
print('columns: ')
print()
print()
print(df1.columns)
print()

####BASE COLUMNS####

    #1. 'PAIS_DE_NASCIMENTO' 
    #2. 'DATA_ENTRADA' 
    #3. 'DATA_REGISTRO' 
    #4. 'MUN_RESIDENCIA'
    #5. 'MUN_RECEBIMENTO' 
    #6. 'EST_CIV' 
    #7. 'UNIDADE_FEDERACAO_RECEBIMENTO'
    #8. "UNIDADE_FEDERACAO_RESIDENCIA' 
    #9. 'SEXO'
    #10. 'PAIS_DE_NACIONALIDADE'
    #11. 'ANONASCIMENTO'

## 1.4. Apply Filter: selecting only the necessary columns
df1_filter = df1.drop(['PAIS_DE_NASCIMENTO', 'EST_CIV', 'SEXO', 'MUN_RECEBIMENTO', 'ANONASCIMENTO'], axis=1)
print('Necessary columns filtered: ')
print()
print(df1_filter)
print()
print()

################################### SECOND PART : REFUGEE REQUESTS - GLOBAL  ###################################
print('Analysis: Global Refugee data')
print()

##3.1. Full Global DataFrame
global_data = df1_filter 
print('Global Dataframe - refugees from 1994 to 2023')
print(global_data)
print()
print('summary of Global Dataframe ')
print(global_data.describe())
print()

## 3.2. Filter - by date

print('global data frames by date: ')
print()

#2013
print('g2013')
print()
g2013 = global_data[global_data['DATA_ENTRADA'].str.endswith('2013', na = False)]
print(g2013)
print()
#2014
print('g2014')
print()
g2014 = global_data[global_data['DATA_ENTRADA'].str.endswith('2014', na = False)]
print(g2014)
print()
#2015
print('g2015')
print()
g2015 = global_data[global_data['DATA_ENTRADA'].str.endswith('2015', na = False)]
print(g2015)
print()
#2016
print('g2016')
print()
g2016 = global_data[global_data['DATA_ENTRADA'].str.endswith('2016', na = False)]
print(g2016)
print()
#2017
print('g2017')
print()
g2017 = global_data[global_data['DATA_ENTRADA'].str.endswith('2017', na = False)]
print(g2017)
print()
#2018
print('g2018')
print()
g2018 = global_data[global_data['DATA_ENTRADA'].str.endswith('2018', na = False)]
print(g2018)
print()
#2019
print('g2019')
print()
g2019 = global_data[global_data['DATA_ENTRADA'].str.endswith('2019', na = False)]
print(g2019)
print()
#2020
print('g2020')
print()
g2020 = global_data[global_data['DATA_ENTRADA'].str.endswith('2020', na = False)]
print(g2020)
print()
#2021
print('g2021')
print()
g2021 = global_data[global_data['DATA_ENTRADA'].str.endswith('2021', na = False)]
print(g2021)
print()
#2022
print('g2022')
print()
g2022 = global_data[global_data['DATA_ENTRADA'].str.endswith('2022', na = False)]
print(g2022)
print()
#2023
print('g2023')
print()
g2023 = global_data[global_data['DATA_ENTRADA'].str.endswith('2023', na = False)]
print(g2023)
print()

## 3.3. Summary of Global DataFrames by date

#2013
print()
print('2013')
print()
print(g2013.describe())
print()
#2014
print()
print('2014')
print()
print(g2014.describe())
print()
#2015
print()
print('2015')
print()
print(g2015.describe())
print()
#2016
print()
print('2016')
print()
print(g2016.describe())
print()
#2017
print()
print('2017')
print()
print(g2017.describe())
print()
#2018
print()
print('2018')
print()
print(g2018.describe())
print()
#2019
print()
print('2019')
print()
print(g2019.describe())
print()
#2020
print()
print('2020')
print()
print(g2020.describe())
print()
#2021
print()
print('2021')
print()
print(g2021.describe())
print()
#2022
print()
print('2022')
print()
print(g2022.describe())
print()
#2023
print()
print('2023')
print()
print(g2023.describe())
print()

################################### THIRD PART : REFUGEE REQUESTS - VENEZUELA ###################################

print('Analisys: Refugee requests from Venezuela')
print()
print()

## 3.1. Apply Filter: only migrants from Venezuela
df_only_venez = df1_filter[df1_filter['PAIS_DE_NACIONALIDADE'] == 'VENEZUELA']
print('Venezuela DataFrame: Only refugees from Venezuela - from 1994 to 2023: ')
print()
print(df_only_venez)
print()
print()
print('Summary of Venezuela DataFrame:')
print()
print(df_only_venez.describe())
print()
print()

## 3.2. Filter - by date

print('Venezuela DataFrame by date: ')
print()
print()

#2013

print('v2013')
print()
v2013 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2013', na = False)]
print(v2013)
print()

#2014
print('v2014')
print()
v2014 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2014', na = False)]
print(v2014)
print()

#2015
print('v2015')
print()
v2015 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2015', na = False)]
print(v2015)
print()

#2016
print('v2016')
print()
v2016 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2016', na = False)]
print(v2016)
print()

#2017
print('v2017')
print()
v2017 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2017', na = False)]
print(v2017)
print()

#2018
print('v2018')
print()
v2018 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2018', na = False)]
print(v2018)
print()

#2019
print('v2019')
print()
v2019 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2019', na = False)]
print(v2019)
print()

#2020
print('v2020')
print()
v2020 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2020', na = False)]
print(v2020)
print()

#2021
print('v2021')
print()
v2021 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2021', na = False)]
print(v2021)
print()

#2022
print('v2022')
print()
v2022 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2022', na = False)]
print(v2022)
print()

#2023
print('v2023')
print()
v2023 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2023', na = False)]
print(v2023)
print()

## 3.3. Short Form: description of the main elemets in the DataFrames
print()
print('Summary of Venezuela DataFrame by date')
print('')
print('v2013')
print(v2013.describe())
print()
print('v2014')
print(v2014.describe())
print()
print('v2015')
print(v2015.describe())
print()
print('v2016')
print(v2016.describe())
print()
print('v2017')
print(v2017.describe())
print()
print('v2018')
print(v2018.describe())
print()
print('v2019')
print(v2019.describe())
print()
print('v2020')
print(v2020.describe())
print()
print('v2021')
print(v2021.describe())
print()
print('v2022')
print(v2022.describe())
print()
print('v2023')
print(v2023.describe())
print()


print()
print()


################################### FOUTH PART :  GROUP DATA  ###################################

## 4.1. Definig the Groups [TO UNDERSTAND THE METHODS, PROCEED TO THE READ ME FILE IN THE REPOSITORY

print()
print('defining the time period')
print()
print('group 1: before the law  -  2013 to 2017')
print()
print('group 2: implementation of the law and start of missao acolhida - 2017 to 2018')
print()
print('group 3: five years of the new migration and of missao acolhida 2019 to 2023 ')
print()
print()

## 4.2 Creating the Data Frames by group (Global and Venezuela)

        #Global : group 1 (g2013,g2014,g2015,g2016); group 2 (g2017, g2018); group 3 (g2019,g2020,g2021,g2022,g2023)
        
group1global = pd.concat([g2013,g2014,g2015,g2016])
group2global = pd.concat([g2017, g2018])
group3global = pd.concat([g2019,g2020,g2021,g2022,g2023])
print()
print('GROUP 1 GLOBAL : Global Refugee Values from 2013 to 2016')
print()
print()
print(group1global)
print()
print()        
print('GROUP 2 GLOBAL : Global Refugee Values from 2017 to 2018')
print()
print()
print(group2global)
print()
print()
print('GROUP 3 GLOBAL : Global Refugee Values from 2019 to 2023')
print()
print()
print(group3global)
print()
print()
 
 #Venezuela : group 1 (v2013,v2014,v2015,v2016); group 2 (v2017, v2018); group 3 (v2019,v2020,v2021,v2022,v2023)
 
group1venez = pd.concat([v2013,v2014,v2015,v2016])
group2venez = pd.concat([v2017, v2018])
group3venez = pd.concat([v2019,v2020,v2021,v2022,v2023])

print()
print('GROUP 1 VENEZ : Venezuela Refugee Values from 2013 to 2016')
print()
print()
print(group1venez)
print()
print()        
print('GROUP 2 VENEZ : Venezuela Refugee Values from 2017 to 2018')
print()
print()
print(group2venez)
print()
print()
print('GROUP 3 VENEZ : Venezuela Refugee Values from 2019 to 2023')
print()
print()
print(group3venez)
print()
print()

## 4.3. Definig the Variables

print()
print()
print('definig the variables for global refugees: ')
print()
print()
print('global_pre_law_entrance = averadge of group1global')
global_pre_law_entrance = len(group1global)/4
print('global_critical_years = averadge of group2global')
global_critical_years = len(group2global)/2
print('global_aftermath = averadge of group3global')
global_aftermath = len(group3global)/5
print()
print()
print('definig the variables for Venezuela refugees: ')
print()
print()
print('venez_pre_law_entrance = averadge of group1venez')
venez_pre_law_entrance = len(group1venez)/4
print('venez_critical_years = averadge of group2venez')
venez_critical_years = len(group2venez)/2
print('venez_aftermath = averadge of group3venez')
venez_aftermath = len(group3venez)/5
print()
print()
print('questions to awnser: ')
print('efficency of the law: are refugees entering in Brazil more frequently after the law than before the law?')
print('Venezuelan refugees: how prevalent were they before the law?')
print('efficiency of missao acolhida: are Venezuelan refugees more or less prevalent in relative terms?')
print()
print()
print(f'testing global_pre_law_entrance : value = {global_pre_law_entrance} refugees')
print(f'testing global_critical_years : value = {global_critical_years} refugees')
print(f'testing  global_aftermath: value = {global_aftermath} refugees')
print(f'testing venez_pre_law_entrance : value = {venez_pre_law_entrance} refugees')
print(f'testing  venez_critical_years: value = {venez_critical_years} refugees')
print(f'testing  venez_aftermath: value = {venez_aftermath} refugees')
print('')
print('sucess')

################################### FIFTH PART :  STATISTICAL ANALYSIS  ###################################

# First Question : efficency of the law

print('efficency of the law: are refugees entering in Brazil more frequently after the law than before the law?')
print('regarding the first years of implementation: ')
global_refugee_entrance_rate = round(global_critical_years/global_pre_law_entrance, 2)
print(f'rate of entrance was of {global_refugee_entrance_rate}')
if global_refugee_entrance_rate > 1:
    print(f'it represents an increase of about {global_refugee_entrance_rate} times in comparison to the previus value')
else:
    print(f'it represents an decrease of about {global_refugee_entrance_rate} times in comparison to the previus value')
print()


print('regarding the last years of implementation: ')
final_global_refugee_entrance_rate = round(global_aftermath/global_pre_law_entrance, 2)
print(f'rate of entrance was of {final_global_refugee_entrance_rate}')
if final_global_refugee_entrance_rate > 1:
    print(f'it represents an increase of about {final_global_refugee_entrance_rate} times in comparison to the previus value')
else:
    print(f'it represents an decrease of about {final_global_refugee_entrance_rate} times in comparison to the previus value')
print()


print('regarding both the last years of implementation and the first 2 years of implementation - 2017 to 2023: ')
avg_of_last_y = len(group2global) + len(group3global) / 7
total_global_refugee_entrance_rate = round(avg_of_last_y / global_pre_law_entrance, 2)
print(f'rate of entrance was of {total_global_refugee_entrance_rate}')
if total_global_refugee_entrance_rate > 1:
    print(f'it represents an increase of about {total_global_refugee_entrance_rate} times in comparison to the previus value')
else:
    print(f'it represents an decrease of about {total_global_refugee_entrance_rate} times in comparison to the previus value')
print()
print()


# Second Question : efficency of the Missao Acolhida

print('how prevalent were Venezuelans refugees before missao acolhida?')

relative_number_of_venez_pre_law = round((venez_pre_law_entrance/global_pre_law_entrance) * 100, 2)
print(f'From 2013 to 2016, Venezuelans represented, on avg, {relative_number_of_venez_pre_law}% of the total refugees')
print()
print('how prevalent were Venezuelans refugees during the start of missao acolhida and the implemention of the law?')
relative_number_of_venez_during_law = round((venez_critical_years/global_critical_years) * 100, 2)
print(f'From 2017 to 2018, Venezuelans represented, on avg, {relative_number_of_venez_during_law}% of the total refugees')
print()
print('how prevalent were Venezuelans refugees after the starting years of missao acolhida and the implemention of the law?')
relative_number_of_venez_in_aftermath = round((venez_aftermath/global_aftermath) * 100, 2)
print(f'From 2019 to 2023, Venezuelans represented, on avg, {relative_number_of_venez_in_aftermath}% of the total refugees')
print()
print('how prevalent were Venezuelans refugees between the starting years of missao acolhida and the implemention of the law and 2023?')
avg_of_last_y = len(group2global) + len(group3global) / 7
avg_of_venez_last_y = len(group2venez) + len(group3venez) / 7
relative_number_of_venez_in_total = round((avg_of_venez_last_y/avg_of_last_y) * 100, 2)
print(f'From 2017 to 2023, Venezuelans represented, on avg, {relative_number_of_venez_in_total}% of the total refugees')
print()
print()

