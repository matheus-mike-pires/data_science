import pandas as pd


nationality_chosen_in_filter = []

class Filter():
        
    def nation(dataframes):
            nationality_to_use = input('input a country name (country of nationality): ').upper()
            updated_dataframes = dataframes[dataframes['PAIS_DE_NACIONALIDADE'] == nationality_to_use]
            while len(updated_dataframes) == 0:
                print('this country has no avaible entries')
                nationality_to_use = input('input a country name (country of nationality): ').upper()
                updated_dataframes = dataframes[dataframes['PAIS_DE_NACIONALIDADE'] == nationality_to_use]
            print(f'displaying filters for {nationality_to_use}: ')
            print()
            nationality_chosen_in_filter.clear()
            nationality_chosen_in_filter.append(nationality_to_use)
            
            return updated_dataframes
            
            
open_data1 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_1994_2023.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data2 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2024.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data3 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2025.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data4 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2026_01.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data5 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2026_02.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data6 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2026_03.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data7 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2026_04.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data8 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2026_05.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data9 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2026_06.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)

update_data = pd.concat([open_data1, open_data2, open_data3, open_data4, open_data5, open_data6, open_data7, open_data8, open_data9])
df1 = update_data.drop(['PAIS_DE_NASCIMENTO', 'EST_CIV', 'MUN_RECEBIMENTO'], axis=1)
dataframe = df1

class Math_and_stats:
    def __init__(self, global_dataframe):
        self.global_dataframe = global_dataframe
        self.global_years = {
            year: global_dataframe[global_dataframe['DATA_ENTRADA'].str.endswith(str(year), na=False)]
            for year in range(1994, 2027)
        }
        
    def filter_dataframe(self, filtered_dataframe):
        filtered_years = {
            year: filtered_dataframe[filtered_dataframe['DATA_ENTRADA'].str.endswith(str(year), na=False)]
            for year in range(1994, 2027)
        }
    
        group1global = pd.concat([self.global_years[year] for year in range(1994, 2017)])
        group2global = pd.concat([self.global_years[year] for year in range(2017, 2019)])
        group3global = pd.concat([self.global_years[year] for year in range(2019, 2027)])
        
        group1filtered = pd.concat([filtered_years[year] for year in range(1994, 2017)])
        group2filtered = pd.concat([filtered_years[year] for year in range(2017, 2019)])
        group3filtered = pd.concat([filtered_years[year] for year in range(2019, 2027)])
        
        full_filtered = len(filtered_dataframe['PAIS_DE_NACIONALIDADE'])
    
        return [group1global, group2global, group3global, group1filtered, group2filtered, group3filtered, full_filtered]
        
    def variable_machine(self, all_groups):
        global_pre_law_entrance = len(all_groups[0]) / 23
        global_critical_years = len(all_groups[1]) / 2 
        global_aftermath = len(all_groups[2]) / 8 
        avg_of_last_y = (len(all_groups[1]) + len(all_groups[2])) / 10 
        
        absolute_global = len(self.global_dataframe) / 33
            
        filtered_pre_law_entrance = len(all_groups[3]) / 23
        filtered_critical_years = len(all_groups[4]) / 2 
        filtered_aftermath = len(all_groups[5]) / 8 
        avg_of_filtered_last_y = (len(all_groups[4]) + len(all_groups[5])) / 10 
        absolute_filter = all_groups[6] / 33
        
        return [
            global_pre_law_entrance, global_critical_years, global_aftermath, 
            avg_of_last_y, filtered_pre_law_entrance, filtered_critical_years, 
            filtered_aftermath, avg_of_filtered_last_y, absolute_filter, absolute_global
        ]
    
    def calculating_it(self, variable_list):
        filter_pre_law = round((variable_list[4] / variable_list[0]) * 100, 2) if variable_list[0] > 0 else 0.0
        filter_in_law = round((variable_list[5] / variable_list[1]) * 100, 2) if variable_list[1] > 0 else 0.0
        filter_after_law = round((variable_list[6] / variable_list[2]) * 100, 2) if variable_list[2] > 0 else 0.0
        filter_in_and_after_law = round((variable_list[7] / variable_list[3]) * 100, 2) if variable_list[3] > 0 else 0.0
        filter_total = round((variable_list[8] / variable_list[9]) * 100, 2) if variable_list[9] > 0 else 0.0
        return [filter_pre_law, filter_in_law, filter_after_law, filter_in_and_after_law, filter_total]


def statistical_analysis(dataframe):
    print()
    global_dfs = dataframe
    
    print('This is a section reserved for analysis of migration policy in Brazil before 2017, during its implementation periods, and after the process.')
    print('You may filter the analysis by nationality and compare it to different time periods.')
    print('\nGeneral data: \n')
    print(f'In the entire database, {len(global_dfs)} refuge requests were filtered.')
    
    male_global = (len(global_dfs[global_dfs['SEXO'] == 'M']) / len(global_dfs)) * 100
    print(f'Males represented a total of {round(male_global, 2)}% and females {round(100 - male_global, 2)}%.')
    print()
    
    top_nationalities = global_dfs['PAIS_DE_NACIONALIDADE'].value_counts().head(3)
    top_nat_list = list(top_nationalities.items())
    print('Most frequent nationalities: ')
    for key, value in top_nat_list:
        print(f'{key}: {round((value / len(global_dfs)) * 100, 2)}')
    print('\nLoading data by year groups: \n')
    
    stats_instance = Math_and_stats(global_dfs)
    filtered_df = global_dfs.copy() 
    
    for_all_groups = stats_instance.filter_dataframe(filtered_df)
    print(f'Between 1994 to 2016, {round((len(for_all_groups[0]) / len(global_dfs)) * 100, 2)}% of the total requests were sent.')
    print(f'Between 2017 to 2018, {round((len(for_all_groups[1]) / len(global_dfs)) * 100, 2)}% of the total requests were sent.')
    print(f'Between 2019 to 2026, {round((len(for_all_groups[2]) / len(global_dfs)) * 100, 2)}% of the total requests were sent.\n')
    
    filtered_df = Filter.nation(dataframe)
    
    print(filtered_df)
    print(f'\nLoading data of {nationality_chosen_in_filter[0]}. Averages from 1994 to 2026:\n')
    
    groups_made = stats_instance.filter_dataframe(filtered_df)
    variables_made = stats_instance.variable_machine(groups_made)
    avg_results = stats_instance.calculating_it(variables_made)

    
    print(f' - Between 1994 and 2016 (before legislation change), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[0]}% of the total refugees.')
    print(f' - During legislation change (2017 - 2018), they represented {avg_results[1]}% of the total refugees.')
    print(f' - Between 2019 and 2026 (after legislation change), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[2]}% of the total refugees.')
    print(f' - Considering 2017 to 2026 they represented {avg_results[3]}% of the total refugees.')
    print(f' - In the entire dataset (from 1994 to 2026), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[4]}% of the total refugees.\n')
    
    wish_to_save = input('Do you wish to save the statistics presented? Press 1 to save, press 2 to proceed without saving: ')
    if wish_to_save == '1':
        name_of_file = input('Input file name: ')
        with open(f'{name_of_file}.txt', 'w') as file:
            file.write('OOOOOOOO')
        print(f'Saved as {name_of_file}.txt\n')

    final_choice = input('Press 1 to save CSV, press any other key to finish/return: ')
    if final_choice == '1':
        print("CSV saved successfully.")
        
    nationality_chosen_in_filter.clear()

statistical_analysis(dataframe)
