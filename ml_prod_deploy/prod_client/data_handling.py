import pandas as pd

class FileHandling(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        data = pd.read_csv(self.file_name)

        return data

    def write_data(self, df):
        df.to_excel(self.file_name)
