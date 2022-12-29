from data_processing import DataProcessing
from data_prediction import DataPredict


file_name = "./data/titanic.csv"
dp = DataProcessing(file_name=file_name)
dp.process_and_write_data()
predict_obj = DataPredict(file_name=file_name)