from data_handling import FileHandling
import pandas as pd

class DataProcessing(object):
    def __init__(self, df, file_name):
        self.df = df
        self.file_name = file_name

    def change_data(self, x):
        if x == "male":
            return 1
        else:
            return 0

    def processing_dataset(self):
        df = self.df.copy()
        titanic_dataset = df[["Pclass", "Sex", "Age", "SibSp", "Fare", "Survived"]]

        # Format the string column & Fare to rounded by 2 decimals
        titanic_dataset["Sex"] = titanic_dataset["Sex"].apply(self.change_data)
        titanic_dataset["Fare"] = titanic_dataset["Fare"].apply(lambda x: "%.2f" % x)

        # Get the median age
        median_age = titanic_dataset["Age"].median()

        # Fill the missing age values with the median age
        titanic_dataset.loc[((titanic_dataset["Age"].isna()) | (titanic_dataset["Age"] == 0)), "Age"] = median_age
        
        # Change the datatype of Age and Fare
        titanic_dataset["Age"] = titanic_dataset["Age"].astype(int)
        titanic_dataset["Fare"] = titanic_dataset["Fare"].astype(float)

        return titanic_dataset

    def write_processed_data(self, df):
        processed_file_name = "./data/processed_" + self.file_name
        file_handler = FileHandling(file_name=processed_file_name)
        file_handler.write_data(df=df)

    def read_processed_data(self):
        processed_file_name = "./data/processed_" + self.file_name
        file_handler = FileHandling(file_name=processed_file_name)
        df = file_handler.read_data()

        return df
    
    def process_and_write_data(self):
        df = self.processing_dataset()
        self.write_processed_data(df=df)
