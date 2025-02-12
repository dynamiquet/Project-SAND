from ProductionCode.datasource import DataSource

#A simple file to just demonstrate the DataSource functionality
test = DataSource()
test.connect()
test.getRiskValuesbyCounty("TORNADO", "Rice", "MN")
test.test("Rice", "MN")