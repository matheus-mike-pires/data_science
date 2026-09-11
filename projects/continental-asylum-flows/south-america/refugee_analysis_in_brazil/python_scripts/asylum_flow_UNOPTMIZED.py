import pandas as pd
#####


    
    


######################FILTER CLASS####################
nationality_chosen_in_filter = []

class Filter():
        
    def user_filter(filter, dataframes):
        if filter == '1':
            nationality_to_use = input('input a country name (country of nationality): ').upper()
            updated_dataframes = dataframes[dataframes['PAIS_DE_NACIONALIDADE'] == nationality_to_use]
            while len(updated_dataframes) == 0:
                print('this country has no avaible entries')
                nationality_to_use = input('input a country name (country of nationality): ').upper()
                updated_dataframes = dataframes[dataframes['PAIS_DE_NACIONALIDADE'] == nationality_to_use]
            print(f'displaying filters for {nationality_to_use}: ')
            print()
            nationality_chosen_in_filter.append(nationality_to_use)
            return updated_dataframes
            
        elif filter == '2':
            date_to_select = input('input a year of entry (from 1994 to 2026): ')
            updated_dataframes = dataframes[dataframes['DATA_ENTRADA'].str.endswith(date_to_select, na = False)]
            while len(updated_dataframes) == 0:
                print('this country has no avaible entries')
                date_to_select = input('input a year of entry (from 1994 to 2026): ')
                updated_dataframes = dataframes[dataframes['DATA_ENTRADA'].str.endswith(date_to_select, na = False)]
            print(f'displaying filters for the year of {date_to_select}: ')
            print()
            return updated_dataframes
            
        elif filter == '3':
            sex_to_select = input('Input 1 for male or 2 for famale: ')
            if sex_to_select == '1':
                updated_dataframes = dataframes[dataframes['SEXO'] == 'M' ]
                print('displaying filters for males: ')
                print()
                return updated_dataframes
            if sex_to_select == '2':
                updated_dataframes = dataframes[dataframes['SEXO'] == 'F']
                print('displaying filters for females: ')
                print()
                return updated_dataframes
            
            return updated_dataframes
        elif user_filter == '4':
            pass
        elif user_filter == '5':
            pass

###############################ANALYSIS########################################
def statistical_analysis(dataframe):
    print()
    global_dfs = dataframe
    print('This is a section reserved for analysis of migration policy in Brazil before the 2017, during its implementetion periods and after the process')
    print('You may filter the analysis by nationality and compare it to diffent time periods')
    print()
    print('general data: ')
    print(f'In the entire database, {len(global_dfs)} refuge requests were filtered')
    male_global = (len(global_dfs[global_dfs['SEXO'] == 'M']) / len(global_dfs)) * 100
    print(f'males represented a total of {round(male_global, 2)}% and females {round(100 - male_global, 2)}%')
    print()
    top_nationalities = global_dfs['PAIS_DE_NACIONALIDADE'].value_counts().head(3)
    top_nat_list = list(top_nationalities.items())
    print('Most frequent nationalities: ')
    for key, value in top_nat_list:
        print(f'{key}: {round((value/len(global_dfs)) * 100 , 2)}')
    
    print('Data by year groups: ')
    print()
    for_all_groups = Math_and_stats.general_math(global_dfs, global_dfs)
    print(f'between 1994 to 2016, {round((len(for_all_groups[0]) / len(global_dfs)) * 100 , 2)}% of the total requests were sent ')
    print(f'between 2017 to 2018, {round((len(for_all_groups[1]) / len(global_dfs)) * 100 , 2)}% of the total requests were sent ')
    print(f'between 2019 to 2026, {round((len(for_all_groups[2]) / len(global_dfs)) * 100 , 2)}% of the total requests were sent ')
    print()
    print()
    filtered_df = Filter.user_filter('1', dataframe) 
    print()
    print(filtered_df)
    print()
    print(f' Loading data of {nationality_chosen_in_filter[0]}. Averadges from 1994 to 2026')
    groups_made = Math_and_stats.general_math(dataframe, filtered_df)
    print()
    variables_made = Math_and_stats.variable_machine(groups_made)
    avg_results = Math_and_stats.calculate_avg(variables_made)
    print(f' - Between 1994 and 2016 (before legislation change), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[0]}% of the total refugees. ')
    print(f' - During legislation change (2017 - 2018), they represented {avg_results[1]}% of the total refugees.')
    print(f' - Between 2019 and 2026 (after legislation change), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[2]}% of the total refugees. ')
    print(f' - Considering 2017 to 2026 they represented {avg_results[3]}% of the total refugees.')
    print(f' - In the intire dataset (from 1994 to 2026), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[4]}% of the total refugees.')
    print()
    print()
    print('Do you wish to save the statistics presented?')
    wish_to_save = input('Press 1 to save, press 2 to proceed without saving: ')
    if wish_to_save == '1':
        name_of_file = input('input file name: ')
        with open(f'{name_of_file}.txt', 'w') as file:
            file.write(f'- Between 1994 and 2016 (before legislation change), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[0]}% of the total refugees. During legislation change (2017 - 2018), they represented {avg_results[1]}% of the total refugees. Between 2019 and 2026 (after legislation change), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[2]}% of the total refugees. Considering 2017 to 2026 they represented {avg_results[3]}% of the total refugees. In the intire dataset (from 1994 to 2026), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[4]}% of the total refugees. This data was obtained with the open source tool migration_flow.py, avaliable at the repository [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]. The raw data was obtained via CONAIRE (source [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]. Feel free to use it in your researches or work! If you need help, contact me [matheusolv.pires@gmail.com')
        print(f'Saved as {name_of_file}.txt')
        print()
        print(filtered_df)
        print()
        print()
        final_choice = input('Press 1 to save press any other key to return to menu: ')
        if final_choice == '1':
            save_csv(filtered_df)
            main(df1)
        else:
            main(df1)
    else:
        print()
        print(filtered_df)
        print()
        print()
        final_choice = input('Press 1 to save press any other key to return to menu: ')
        if final_choice == '1':
            save_csv(filtered_df)
            main(df1)
        else:
            main(df1)
            
    
    
    
    
    
    
##############################CLASS MATH##################################
class Math_and_stats():
    
    fix_the_code = open_data1 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/complete_until_2026_6.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
    
    def general_math(global_dataframe, filtered_dataframe):
    
        g_years = {
        year: global_dataframe[global_dataframe['DATA_ENTRADA'].str.endswith(str(year), na=False)]
        for year in range(1994, 2027)}
        
        filtered_years = {
        year: filtered_dataframe[filtered_dataframe['DATA_ENTRADA'].str.endswith(str(year), na=False)]
        for year in range(1994, 2027)}

    
        group1global = pd.concat([g_years[year] for year in range(1994, 2017)])
        group2global = pd.concat([g_years[year] for year in range(2017, 2019)])
        group3global = pd.concat([g_years[year] for year in range(2019, 2027)])
        
        group1filtered = pd.concat([filtered_years[year] for year in range(1994, 2017)])
        group2filtered = pd.concat([filtered_years[year] for year in range(2017, 2019)])
        group3filtered = pd.concat([filtered_years[year] for year in range(2019, 2027)])
        
        fix_it = len(filtered_dataframe['PAIS_DE_NACIONALIDADE'])
            
        return [group1global, group2global, group3global, group1filtered, group2filtered, group3filtered, fix_it]
        
    def variable_machine(all_groups):
    
        global_pre_law_entrance = len(all_groups[0])/23
        global_critical_years = (len(all_groups[1]))/2 
        global_aftermath = (len(all_groups[2]))/8 
        avg_of_last_y = (len(all_groups[1]) + len(all_groups[2])) / 10 
        absolute_global = (len(Math_and_stats.fix_the_code)) / 33
            
        filtered_pre_law_entrance = len(all_groups[3])/23
        filtered_critical_years = len(all_groups[4])/2 
        filtered_aftermath = len(all_groups[5])/8 
        avg_of_filtered_last_y = (len(all_groups[4]) + len(all_groups[5])) / 10 
        absolute_filter = all_groups[6] / 33
        
        return [global_pre_law_entrance, global_critical_years, global_aftermath, avg_of_last_y, filtered_pre_law_entrance, filtered_critical_years, filtered_aftermath, avg_of_filtered_last_y, absolute_filter, absolute_global]
        
    def calculate_avg(variable_list):
        filter_pre_law = round((variable_list[4]/variable_list[0]) * 100 , 2)
        filter_in_law = round((variable_list[5]/variable_list[1]) * 100 , 2)
        filter_after_law = round((variable_list[6]/variable_list[2]) * 100, 2)
        filter_in_and_after_law = round((variable_list[7]/variable_list[3]) * 100 , 2)
        filter_total = round((variable_list[8]/variable_list[9]) *100, 2)
        return [filter_pre_law, filter_in_law, filter_after_law, filter_in_and_after_law, filter_total]
        
       
        
        
    
        
            


###############################DISPLAY DATAFRAMES#################################

def display_any_dataframe(dataframes):
    print()
    print(dataframes)
    print()
    print()
    print('This is the currenct version of the DataFrame')
    print()
    print('1. Display full dataframe (not recommended)')
    print('2. Save it as CSV')
    print('3. Return')
    print()
    choice = input('Select an option: ')
    if choice == '1':
        print(dataframes.to_string())
        print()
        print('2. Save it as CSV')
        print('3. Return')    
        choice = print()
        choice = input('Select an option: ')
        if choice == '3':
            main(df1)
        if choice == '2':
            save_csv(dataframes)
    if choice == '2':
        save_csv(dataframes)
    if choice == '3':
        main(df1)

###################################SAVE CSV########################################
def save_csv(dataframes):
    name_of_file = input('Write the file name: ')
    dataframes.to_csv(f'{name_of_file}.csv', index=False)
    print()
    print('DataFrame has been saved!')
    print()
    main(df1)



########################################
def display_options1():
    print()
    print('By applying the filters, you may choose one of the options to search specific info')
    print('the avaible filters: ')
    print()
    print('1. Filter by nationality') #filter == '1':
    print('2. Filter by entry date') #filter == '2'
    print('3. Filter by sex') #filter == '3'
    print('4. Apply multiple filters')
    print('5. Return')
    print()
    
def display_options2():
    print('2. Filter by entry date') #filter == '2'
    print('3. Filter by sex') #filter == '3'
    
def display_after():
    print()
    print('1. Visualize the full DataFrame')
    print('2. Download the current dataframe as a CSV file')
    print('3. Return to main menu')


#####################FILTER UI###############
def filters_to_data(df1):
    display_options1()
    choice1 = input('choose an option: ')
    #Starting with nationality
    if choice1 == '1':
        update_df_entry = Filter.user_filter(choice1, df1) 
        print()
        print(update_df_entry)
        display_after()
        print()
        nationality_chosen_in_filter.clear()
        select_opt = input('Select an option: ')
        if select_opt == '1':
            display_any_dataframe(update_df_entry)
        elif select_opt == '2':
            save_csv(update_df_entry)
        if select_opt == '3':
            main(df1)
        
     #Starting with Date 
    if choice1 == '2':
        update_df_entry = Filter.user_filter(choice1, df1) 
        print()
        print(update_df_entry)
        display_after()
        select_opt = input('Select an option: ')
        if select_opt == '1':
            display_any_dataframe(update_df_entry)
        elif select_opt == '2':
            save_csv(update_df_entry)
        if select_opt == '3':
            main(df1)
      #Starting with Sex
    if choice1 == '3':
        update_df_entry = Filter.user_filter(choice1, df1) 
        print()
        print(update_df_entry)
        print()
        display_after()
        select_opt = input('Select an option: ')
        if select_opt == '1':
            display_any_dataframe(update_df_entry)
        elif select_opt == '2':
            save_csv(update_df_entry)
        if select_opt == '3':
            main(df1)
        #multiple
    if choice1 == '4':
        print('filter: by nationality')
        choice1 = print()
        choice1 = input('Press 1 to appy it, press any other key to skip: ')
        if choice1 == '1':
            df1 = Filter.user_filter(choice1, df1) 
            print(df1)
            print()
            print()
        print('filter: by date')
        choice1 = print()
        choice1 = input('Press 2 to appy it, press any other key to skip: ')
        if choice1 == '2':
            df1 = Filter.user_filter(choice1, df1) 
            print(df1)
            print()
            print()
        print('filter: by sex')
        choice1 = print()
        choice1 = input('Press 3 to appy it, press any other key to skip: ')
        if choice1 == '3':
            df1 = Filter.user_filter(choice1, df1) 
            print(df1)
            print()
            print()
        display_after()
        select_opt = input('Select an option: ')
        if select_opt == '1':
            display_any_dataframe(df1)
        elif select_opt == '2':
            save_csv(df1)
        if select_opt == '3':
            main(df1)


###########MAIN###########

def main(df1):
    print()
    valid_options = ['1', '2', '3', '4', '5', '6']
    print('1. Verify the full database of refuge requests')
    print('2. Filter the database')
    print('3. Verify the statistcs')
    print('4. Request contact')
    print('5. How to use')
    print('6. Exit')
    print()
    choice = input('select an option: ')
    while choice not in valid_options:
        choice = input('please, select a valid option: ')
    if choice == '1':
        df1 = update_data
        df1 = df1.drop(['PAIS_DE_NASCIMENTO', 'EST_CIV', 'MUN_RECEBIMENTO'], axis=1)
        display_any_dataframe(df1)
    if choice == '2':
        filters_to_data(df1)
    if choice == '3':
        statistical_analysis(df1)
    if choice == '4':
        print()
        print('if you need help or have any suggestions, feel free to contact me:')
        print('matheusolv.pires@gmail.com')
        print()
        main(df1)
    if choice == '5':
        print('Acess the following repository: XXXXXXXXXXXXXXXXXX')
        print('click on the README.md file')
        print('Follow the instructions displayed')
        print()
        print()
        main(df1)
    if choice == '6':
        print()
        print('Thank you for using this program')
        
##########################################INSERTING######################################
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
df1 = update_data
df1 = df1.drop(['PAIS_DE_NASCIMENTO', 'EST_CIV', 'MUN_RECEBIMENTO'], axis=1)
df1['DATA_ENTRADA'] = df1['DATA_ENTRADA'].fillna('')
df1['DATA_ENTRADA'] = df1['DATA_ENTRADA'].astype(str).str.strip()
###########################################################################################
print('***********************')
print('This is a python program made to explore the data on refugees  in Brasil')
print('The analisys mainly relies on the python library Pandas and on the statistical analysis of the data gathered. ')
print('for more information, acess the repository: ')
print('!!! Follow the instructions on READ.ME to download the necessary files and properly run this program !!!')
print('***********************')
print()
print()
if __name__ == '__main__':
    main(df1)