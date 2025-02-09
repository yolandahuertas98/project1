import pandas as pd
import openpyxl as oxl
import os
import time
import datetime

def extract_service():
    folder_path = 'C:/Users/Yolanda/Project1/data/raw'
    dataframes = pd.DataFrame()

    for filename in os.listdir(folder_path):
        file_id = filename[0:9]

        if filename.endswith('.csv'):
            df = pd.read_csv(os.path.join(folder_path, filename))
        elif filename.endswith('.xlsx'):
            df = pd.read_excel(os.path.join(folder_path, filename))
        
        order_id = int(time.time()*1000)
        df["ORDER_ID"] = order_id

        today = datetime.date.today()
        df["FECHA"] = today

        df['CLIENTE'] = file_id
        dataframes = pd.concat([dataframes, df], ignore_index=True)

    return dataframes
