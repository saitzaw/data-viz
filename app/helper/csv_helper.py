""" 
* openpyxl (excel)
"""
import json 
import pandas as pd
import pyreadstat
from openpyxl import load_workbook

"""
only for CSV file 
""" 
class Read:

    """ If the parameters are missing, use the default value """
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