""" 
* converter for spss and excel file 
* dependencies 
* pyreadstat (spss file)
* openpyxl (excel)
"""
import json 
import pandas as pd
import pyreadstat
from openpyxl import load_workbook


class Read_CSV:
    def __init__(self, file_name="data.csv", file_path="app/data"):
        self.file_name = file_name
        self.file_path = file_path 

    @classmethod
    def _file(cls, file_name, file_path):
        path = '/'
        _file_path = path.join([file_path, file_name])
        _csv_df = pd.read_csv(file_path).drop('Open',axis=1)
        chart_data = _csv_df.to_dict(orient='records')
        chart_data = json.dumps(chart_data, indent=2)
        data = {'chart_data': chart_data}
        return cls(data)  
