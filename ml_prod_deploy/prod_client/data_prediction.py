from data_processing import DataProcessing
from data_handling import FileHandling
import requests
import pandas as pd
import json

class DataPredict(object):
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.url = "http://127.0.0.1:5000/model"

    def call_api(self, datum):
        response = requests.post(url=self.url, data=datum)
        pred_data = json.loads(response.text)
        datum["prediction"] = pred_data["prediction"]

        return datum
    
    def predict_data(self):
        dp = DataProcessing(file_name=self.file_name)
        df = dp.read_processed_data()
        data = []
        for datum in df.to_dict(orient='records'):
            dat = self.call_api(datum=datum)
            data.append(dat)

        return pd.DataFrame(data)

    def predict_and_write_data(self):
        predicted_data = self.predict_data()
        fh = FileHandling(file_name="./data/predicted_data.csv")
        fh.write_data(df=predicted_data)

