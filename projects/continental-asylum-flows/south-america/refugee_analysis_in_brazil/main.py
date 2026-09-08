import pandas as pd
#####
        
    


######################FILTER CLASS####################

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
def statistical_analysis():
    print()
    print('As presented in README.MD, this program was made as part of a study on the efficency of the new migration law in Brazil. ')
    print('To find extra details about the methods used in this process, verify the readme.md and the full_code_explanation.py')
    print('The statistical study measured the averadge numbers of refuge requests from venezuelan nationals and the overall request numbers before and after 2017.')
    print()
    print('1. NOT DONE, WAIT')
    




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
    valid_options = ['1', '2', '3', '4', '5']
    print('1. Verify the full database of refuge requests')
    print('2. Filter the database')
    print('3. Request contact')
    print('4. How to use')
    print('5. Exit')
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
        print()
        print('if you need help or have any suggestions, feel free to contact me:')
        print('matheusolv.pires@gmail.com')
        print()
        main(df1)
    if choice == '4':
        print('Acess the following repository: https://github.com/matheus-mike-pires/data_science/edit/main/projects/continental-asylum-flows/south-america/refugee_analysis_in_brazil/')
        print('click on the README.md file')
        print('Follow the instructions displayed')
        print()
        print()
        main(df1)
    if choice == '5':
        print()
        print('Thank you for using this program')
        
##########################################INSERTING######################################
open_data1 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_1994_2023.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data2 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2024.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data3 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2025.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data4 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2026_01.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
open_data5 = pd.read_csv('/storage/emulated/0/Download/SOLICITANTES_REFUGIO_DIV_1994_2023/SOLICITANTES_REFUGIO_DIV_2026_02.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
update_data = pd.concat([open_data1, open_data2, open_data3, open_data4, open_data5])
df1 = update_data
df1 = df1.drop(['PAIS_DE_NASCIMENTO', 'EST_CIV', 'MUN_RECEBIMENTO'], axis=1)
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
