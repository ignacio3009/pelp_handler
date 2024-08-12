import os
import pandas
from auxiliars import*
from settings import*

pelp_input_dir = r'C:\Users\ignac\OneDrive\2024.tnep\02.data\PELP\Base de Datos PELP 2023-2027 Informe Preliminar_v2\Acelerando la Transición Energética\Input'
pelp_output_dir = r'C:\Users\ignac\OneDrive\2024.tnep\02.data\PELP\Base de Datos PELP 2023-2027 Informe Preliminar_v2\Acelerando la Transición Energética\Output'
temp_out_dir = r'./temp'

list_files = get_file_list(pelp_input_dir)
if('fuel_price.csv' in list_files):
    df = pandas.read_csv(os.path.join(pelp_input_dir, 'fuel_price.csv'))
    df_melted = df.melt(id_vars=["time", "scenario"], var_name="fuel", value_name="price")
    if bWriteTempFiles:
        df_melted.to_csv(temp_out_dir+os.sep+'fuel_price_data.csv', index=False)
    data = df_melted.values
    for row in data:
        print(row)
        break





