import os
import pandas as pd
from auxiliars import*
from settings import*
from fuel import Fuel
from datetime import datetime
from fuels import Fuels


def process_data():

    list_files = ['fuel_price.csv', 'ele-fuel.csv']
    list_files = get_file_list(pelp_input_dir)

    ofuels = Fuels()

    if('fuel_price.csv' in list_files):
        df = pd.read_csv(os.path.join(pelp_input_dir, 'fuel_price.csv'))
        df_melted = df.melt(id_vars=["time", "scenario"], var_name="fuel", value_name="price")
        if bWriteTempFiles:
            df_melted.to_csv(temp_out_dir+os.sep+'fuel_price_data.csv', index=False)
        data_fuel_price = df_melted.values


    if('ele-fuel.csv' in list_files):
        df = pd.read_csv(os.path.join(pelp_input_dir, 'ele-fuel.csv'))
        data = df.values
        for row in data:
            str_id = row[0]
            str_name = row[1]
            str_end_time = row[2]
            str_start_time = row[3]
            str_report = row[4]
            str_availability = row[5]
            str_consider_availability = row[6]
            str_fuel_price = row[7]
            str_fuel_type = row[8]
            fuel = Fuel(str_name, str_id, str_end_time, str_start_time, str_report, str_availability, str_consider_availability, str_fuel_price, str_fuel_type)
            
            for rdata in data_fuel_price:
                if(rdata[2] == str_name):
                    str_time = rdata[0]
                    str_scenario = rdata[1]
                    str_price = rdata[3]
                    dt_date = datetime.strptime(str_time, format_time)
                    nyear = dt_date.year
                    fuel.set_price_by_year_and_scenario(nyear, str_scenario, float(str_price))
            ofuels.add_fuel(fuel)
    return ofuels
 