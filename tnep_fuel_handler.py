from process_fuel import process_data
import pandas as pd
from settings import*
import os

header = ['id', 'fuel_name', 'fuel_type', 'price',  'unit', 'mmbtu_per_unit', 'co2_emissions']
sub_header = ['integer', 'string', 'string', 'float', 'string', 'float', 'Kg/Mbtu']
ofuels = process_data()


def create_sheet_Fuel(oFuels):
    data = []
    data.append(header)
    data.append(sub_header)
    for fuel in oFuels.get_fuels().values():
        data.append([fuel.get_id(), fuel.get_name(), fuel.get_fuel_type(), fuel.get_fuel_price(), fuel.get_unit(), fuel.get_mmbtu_per_unit(), fuel.get_co2_emissions()])
    df = pd.DataFrame(data,index=None, columns=None)
    df.to_csv(os.path.join(temp_out_dir, 'Fuel.csv'), index=False, header=False)


create_sheet_Fuel(ofuels)


