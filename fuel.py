class Fuel:

    def __init__(self, name,id=None, end_time=None, start_time=None, report=None, availability=None, consider_availability=None, fuel_price=None, fuel_type=None):
        self.name = name
        self.id = id
        self.end_time = end_time
        self.start_time = start_time
        self.report = report
        self.availability = availability
        self.consider_availability = consider_availability
        self.fuel_price = fuel_price
        self.fuel_type = fuel_type
        self.data = {}

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_end_time(self):
        return self.end_time

    def get_start_time(self):
        return self.start_time

    def get_report(self):
        return self.report

    def get_availability(self):
        return self.availability

    def get_consider_availability(self):
        return self.consider_availability

    def get_fuel_price(self):
        return self.fuel_price

    def get_fuel_type(self):
        return self.fuel_type

    def set_id(self, id):
        self.id = id

    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_start_time(self, start_time):
        self.start_time = start_time
    def set_report(self, report):
        self.report = report
    def set_availability(self, availability):
        self.availability = availability
    def set_consider_availability(self, consider_availability):
        self.consider_availability = consider_availability
    def set_fuel_price(self, fuel_price):
        self.fuel_price = fuel_price
    def set_fuel_type(self, fuel_type):
        self.fuel_type = fuel_type

    def set_price_by_year(self, price, year):
        self.data[year] = price

    def get_price_by_year(self, year):
        return self.data[year]
    
    def set_price_by_year_and_scenario(self, year, scenario, price):
        #add scenario to list of scenarios
        if scenario not in self.data:
            self.data[scenario] = {}
        self.data[scenario][year] = price

        if 'scenario' not in self.data:
            self.data['scenario'] = []
        if scenario not in self.data['scenario']:
            self.data['scenario'].append(scenario)


    def get_price_by_year_and_scenario(self, year, scenario):
        return self.data[scenario][year]
    
    def get_scenarios(self):
        return self.data['scenarios']
