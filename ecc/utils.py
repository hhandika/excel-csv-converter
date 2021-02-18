from glob import glob

import pandas as pd

def find_files(filepath: str):
    return glob(filepath)      


def convert_excel_to_csv(filenames):
    """Batch converting excel files to csv.

    Args:
        filepath (string): Use wildcard to match filenames.
    """
    for excel in filenames:
        out_filenames = excel.replace('.xlsx','.csv')
        dataframe = pd.read_excel(excel, engine='openpyxl')
        dataframe.to_csv(out_filenames, index=False)