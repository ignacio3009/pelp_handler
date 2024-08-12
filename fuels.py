from fuel import Fuel
from scenario import Scenario

class Fuels:
    
    def __init__(self):
        self.fuels = {}
        self.scenarios = {}

    def add_fuel(self, fuel):
        self.fuels[fuel.name] = fuel
    def add_scenario(self, scenario):
        self.scenarios[scenario.name] = scenario
    def get_fuel(self, name):
        return self.fuels[name]
    def get_scenario(self, name):
        return self.scenarios[name]
    
    def get_fuel_price(self, fuel_name, year):
        fuel = self.get_fuel(fuel_name)
        return fuel.get_price(year)

    def get_fuel_price_by_scenario(self, fuel_name, scenario_name, year):
        fuel = self.get_fuel(fuel_name)
        scenario = self.get_scenario(scenario_name)
        return fuel.get_price(year) * scenario.get_price(year)

    def get_fuel_price_by_scenario_and_fuel(self, fuel_name, scenario_name, year):
        fuel = self.get_fuel(fuel_name)
        scenario = self.get_scenario(scenario_name)
        return fuel.get_price(year) * scenario.get_price(year)

    def add_fuel(self, fuel, scenario):
        self.fuels[fuel.name][scenario] = fuel

    def get_fuel(self, fuel_name, scenario):
        return self.fuels[fuel_name][scenario]

    def add_scenario(self, str_scenario):
       if not str_scenario in self.scenarios:
           self.scenarios[str_scenario] = Scenario(str_scenario)

    def get_scenarios(self):
        return [i for i in self.scenarios]
    

    