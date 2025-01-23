import pandas as pd
from services.extract import extract_service
from services.transform import normalize_material
from services.transform import clean_convert_thickness
from services.transform import clean_convert_units

extract_data_df = extract_service()
print(extract_data_df)

extract_data_df['MATERIAL'] = extract_data_df['MATERIAL'].apply(normalize_material)

extract_data_df['GROSOR'] = extract_data_df['GROSOR'].apply(clean_convert_thickness)

extract_data_df['CANTIDAD'] = extract_data_df['CANTIDAD'].apply(clean_convert_units)

extract_data_df['PLEGADO'] = extract_data_df['PLEGADO'].apply(lambda x: x.strip().lower() == 'si')
print(extract_data_df)

print('hola')

