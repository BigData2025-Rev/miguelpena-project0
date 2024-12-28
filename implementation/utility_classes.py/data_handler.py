import pandas as pd
from interface.data_interface import IData

class DataHandler(IData):
    def __init__(self, filename: str, data: pd.DataFrame):
        self.data = data
        self.filename = filename

    def update_data(self, data: pd.DataFrame):
        self.data = data
    
    def save(self):
        self.data.to_json(self.filename, orient='split', compression='infer')
    
    def load(self) -> pd.DataFrame:
        self.data = pd.read_json(self.filename, orient='split', compression='infer')
        return self.data
    
    def get_data(self) -> pd.DataFrame:
        return self.data