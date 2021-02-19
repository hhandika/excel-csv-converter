from glob import glob
from typing import List

import pandas as pd

def find_files(filepath: str) -> List[str]:
    return glob(filepath)      


def convert_excel_to_csv(filenames: List[str]):
    for excel in filenames:
        out_filenames = excel.replace('.xlsx','.csv')
        dataframe = pd.read_excel(excel, engine='openpyxl')
        dataframe.to_csv(out_filenames, index=False)