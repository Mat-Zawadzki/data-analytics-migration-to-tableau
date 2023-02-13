#%%
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join



class cleanFiles():
    def __init__(self):
        self.list_of_files = []
        self.list_of_years = []
        self.list_of_dataframes = []
        self.how_many_rows_in_all_dataframes = 0
        self.combined_data_frame = pd.DataFrame()


    def get_list_of_files(self):
        self.list_of_files = [f for f in listdir('F://csvfiles')]
        for file_path in range(len(self.list_of_files)):
            self.list_of_files[file_path] = ("F://csvfiles//" + self.list_of_files[file_path])
        self.list_of_files.sort()
        #print(self.list_of_files)


    def get_list_of_years(self):
        self.get_list_of_files()
        for file_path in self.list_of_files:
            file_path = file_path[14:18]
            self.list_of_years.append(file_path)
        print(self.list_of_years)


    def get_names_for_dataframes(self):
        '''Appends the list_of_dataframes with names for them to be changed into dataframes  '''
        for file_path in range(len(self.list_of_files)):
            dataframe_name = "pd_read_" + self.list_of_years[file_path]
            self.list_of_dataframes.append(dataframe_name)


    def create_dataframes_for_files(self):
        self.get_names_for_dataframes()
        '''Changes the list_of_dataframes from names into dataframes'''
        for num in range(len(self.list_of_dataframes)):
            self.list_of_dataframes[num] = pd.read_csv(self.list_of_files[num])
            #print(self.list_of_dataframes)


    '''Kept this function for individual dataframe cleaning and testing'''

    '''def remove_null_columns(self):
        #removes null columns and replaces nan values with 0s

        for dataframe in self.list_of_dataframes:
            for col in dataframe.axes[1]:
                if dataframe[col].isnull().any() == True:
                    if dataframe[col].isnull().sum() == len(dataframe):
                        dataframe = dataframe.drop([col], axis = 1)
                    else:
                        dataframe[col] = dataframe[col].fillna(0)
            self.how_many_rows_in_all_dataframes = self.how_many_rows_in_all_dataframes + len(dataframe.axes[0])
            #print(dataframe.axes[1])
            #print(self.how_many_rows_in_all_dataframes)
            #print(len(dataframe.axes[1]))'''


    def set_indexes_for_dataframes(self):
        '''Sets an index column (Value) for the dataframes to be concated on'''
        for dataframe in self.list_of_dataframes:
            #print(len(dataframe.axes[0]))
            dataframe["Value"] = range(self.how_many_rows_in_all_dataframes+1, len(dataframe.axes[0])+self.how_many_rows_in_all_dataframes+1)
            self.how_many_rows_in_all_dataframes = self.how_many_rows_in_all_dataframes + len(dataframe.axes[0])
            dataframe.set_index("Value", inplace = True)


    def create_and_clean_combined_dataframe(self):
        '''Creates empty dataframe and concats with list of dataframes while cleaning (Found it easier and quicker than cleaning the dataframes individually)'''
        self.combined_data_frame = pd.concat([self.list_of_dataframes[0], self.list_of_dataframes[1], self.list_of_dataframes[2], self.list_of_dataframes[3], self.list_of_dataframes[4], self.list_of_dataframes[5], self.list_of_dataframes[6], self.list_of_dataframes[7], self.list_of_dataframes[8]], axis = 0)
        for col in self.combined_data_frame.axes[1]:
            if self.combined_data_frame[col].isnull().any() == True:
                if self.combined_data_frame[col].isnull().sum() == len(self.combined_data_frame):
                    self.combined_data_frame = self.combined_data_frame.drop([col], axis = 1)
                else:
                    self.combined_data_frame[col] = self.combined_data_frame[col].fillna(0)


    def combined_dataframe_to_csv(self):
        '''Exports into a .csv file'''
        self.combined_data_frame.to_csv("C://Work//combineddataframe//combineddataframe2.csv")



def main():
    cf = cleanFiles()
    cf.get_list_of_years()
    cf.create_dataframes_for_files()
    cf.set_indexes_for_dataframes()
    cf.create_and_clean_combined_dataframe()
    cf.combined_dataframe_to_csv()
    


if __name__ == "__main__":
    main()

#%%

