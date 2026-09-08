#this version is very straightfoward and shall run without any delays.for a detailed explanation of the project, check READ.md
#for a detailed explanation of the code, check full_code_explanation.py. for the final version, check main.py

import pandas as pd

open_data1 = pd.read_csv(!!!ENTER_YOUR_FILE_PATH!!!, on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
df1 = pd.DataFrame(open_data1)
df1_filter = df1.drop(['PAIS_DE_NASCIMENTO', 'EST_CIV', 'SEXO', 'MUN_RECEBIMENTO', 'ANONASCIMENTO'], axis=1)

global_data = df1_filter 
g2013 = global_data[global_data['DATA_ENTRADA'].str.endswith('2013', na = False)]
g2014 = global_data[global_data['DATA_ENTRADA'].str.endswith('2014', na = False)]
g2015 = global_data[global_data['DATA_ENTRADA'].str.endswith('2015', na = False)]
g2016 = global_data[global_data['DATA_ENTRADA'].str.endswith('2016', na = False)]
g2017 = global_data[global_data['DATA_ENTRADA'].str.endswith('2017', na = False)]
g2018 = global_data[global_data['DATA_ENTRADA'].str.endswith('2018', na = False)]
g2019 = global_data[global_data['DATA_ENTRADA'].str.endswith('2019', na = False)]
g2020 = global_data[global_data['DATA_ENTRADA'].str.endswith('2020', na = False)]
g2021 = global_data[global_data['DATA_ENTRADA'].str.endswith('2021', na = False)]
g2022 = global_data[global_data['DATA_ENTRADA'].str.endswith('2022', na = False)]
g2023 = global_data[global_data['DATA_ENTRADA'].str.endswith('2023', na = False)]

  
df_only_venez = df1_filter[df1_filter['PAIS_DE_NACIONALIDADE'] == 'VENEZUELA']
v2013 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2013', na = False)]
v2014 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2014', na = False)]
v2015 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2015', na = False)]
v2016 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2016', na = False)]
v2017 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2017', na = False)]
v2018 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2018', na = False)]
v2019 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2019', na = False)]
v2020 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2020', na = False)]
v2021 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2021', na = False)]
v2022 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2022', na = False)]
v2023 = df_only_venez[df_only_venez['DATA_ENTRADA'].str.endswith('2023', na = False)]

        
group1global = pd.concat([g2013,g2014,g2015,g2016])
group2global = pd.concat([g2017, g2018])
group3global = pd.concat([g2019,g2020,g2021,g2022,g2023])

group1venez = pd.concat([v2013,v2014,v2015,v2016])
group2venez = pd.concat([v2017, v2018])
group3venez = pd.concat([v2019,v2020,v2021,v2022,v2023])


global_pre_law_entrance = len(group1global)/4
global_critical_years = len(group2global)/2
global_aftermath = len(group3global)/5
avg_of_last_y = (len(group2global) + len(group3global)) / 7

venez_pre_law_entrance = len(group1venez)/4
venez_critical_years = len(group2venez)/2
venez_aftermath = len(group3venez)/5
avg_of_venez_last_y = (len(group2venez) + len(group3venez)) / 7


print('efficency of the law: are refugees entering in Brazil more frequently after the law than before the law?')

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
total_global_refugee_entrance_rate = round(avg_of_last_y / global_pre_law_entrance, 2)
print(f'rate of entrance was of {total_global_refugee_entrance_rate}')
if total_global_refugee_entrance_rate > 1:
    print(f'it represents an increase of about {total_global_refugee_entrance_rate} times in comparison to the previus value')
else:
    print(f'it represents an decrease of about {total_global_refugee_entrance_rate} times in comparison to the previus value')
print()
print()



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
relative_number_of_venez_in_total = round((avg_of_venez_last_y/avg_of_last_y) * 100, 2)
print(f'From 2017 to 2023, Venezuelans represented, on avg, {relative_number_of_venez_in_total}% of the total refugees')
