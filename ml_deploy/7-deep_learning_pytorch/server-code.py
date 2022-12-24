from flask import Flask, request
import pickle
import torch
import torch.nn as nn
from torch.nn import functional as F
import numpy as np

local_scaler = pickle.load(open('sc.pickle','rb'))

# Pytorch - Neural network
# Fix the neural network parameters
input_size=2
output_size=2
hidden_size=10

# Neural network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.fc2 = torch.nn.Linear(hidden_size, hidden_size)
        self.fc3 = torch.nn.Linear(hidden_size, output_size)


    def forward(self, X):
        X = torch.relu((self.fc1(X)))
        X = torch.relu((self.fc2(X)))
        X = self.fc3(X)

        return F.log_softmax(X,dim=1)

model = Net()

app = Flask(__name__)

@app.route('/model',methods=['POST'])
def hello_world():
    request_data = request.get_json(force=True)
    age = request_data['age']
    salary = request_data['salary']
    model.load_state_dict(torch.load('customer_buy_state_dict'))
    proc_data = model(torch.from_numpy(local_scaler.transform(np.array([[age, salary]]))).float())
    _, predicted_output = torch.max(proc_data.data,-1)

    return "The prediction is {}".format(predicted_output)

if __name__ == "__main__":
    app.run(port=8005, debug=True)

