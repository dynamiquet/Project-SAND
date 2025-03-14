from ProductionCode.datasource import DataSource

#A simple file to just demonstrate the DataSource functionality
test = DataSource()
test.connect()
print(test.get_risk_values_by_county("TORNADO, HURRICANE, EARTHQUAKE", "Rice", "MN")) 
print(test.get_county_row("Los Angeles", "CA")) 
