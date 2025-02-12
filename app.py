from ProductionCode.datasource import DataSource

#A simple file to just demonstrate the DataSource functionality
test = DataSource()
test.connect()
print(test.getRiskValuesbyCounty("TORNADO, HURRICANE, EARTHQUAKE", "Rice", "MN")) 
print(test.getCountyRow("Los Angeles", "CA")) 