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

    @staticmethod
    def _file(self):
        csv_file_path = '/'.join(self.file_path, self.file_name)
        _csv_df = pd.read_csv(csv_file_path).drop('Open',axis=1)
        chart_data = _csv_df.to_dict(orient='records')
        chart_data = json.dumps(chart_data, indent=2)
        data = {'chart_data': chart_data}
        return data 
