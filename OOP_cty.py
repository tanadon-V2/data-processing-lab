
import csv, os

class DataLoader:
    def __init__(self, base_path=None):
        if base_path is None:
            self.base_path = os.path.realpath(
                os.path.join(os.getcwd(), os.path.dirname(__file__))
            )
        else:
            self.base_path = os.path.realpath(base_path)

    def load_csv(self, filename):
        cities = []
        with open(os.path.join(self.base_path, filename)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                cities.append(dict(r))
        return cities


class Table:
    def __init__(self, name, data):
        self.name = name
        self.table = data

    def filter(self, condition):
        filtered = [item for item in self.table if condition(item)]
        return Table(self.name, filtered)

    def aggregate(self, aggregation_function, aggregation_key):
        values = [
            item[aggregation_key]
            for item in self.table
        ]

        if aggregation_key == "temperature":
            values = [float(v) for v in values]
        return aggregation_function(values)

    
loader = DataLoader()
cities = loader.load_csv("Cities.csv")
my_table1 = Table("cities", cities)

print("The average temperature of all the cities:")
avg = my_table1.aggregate(lambda temps: sum(temps) / len(temps),"temperature")
print(avg)
print()

print("all cities in Germany")
germany = my_table1.filter(lambda c: c["country"].startswith("Germany"))

for g in germany.table:
    print(g)
print()
print("all cities in Spain with a temperature above 12°C")
spain = my_table1.filter(lambda c: c["country"].startswith("Spain") and float(c["temperature"]) > 12,)
for s in spain.table:
    print(s)
print()

print("Count the number of unique countries")
unique_countries = my_table1.aggregate(lambda countries: len(set(countries)), "country")
print("unique countries", unique_countries)
print()

print("the average temperature for all the cities in Germany")
avg = germany.aggregate(lambda temps: sum(temps) / len(temps), "temperature")
print("average temperature", avg)
print()

print("the max temperature for all the cities in Italy")
italy = my_table1.filter(lambda c: c["country"].startswith("Italy"))
max_italy = italy.aggregate(max,"temperature")
print(max_italy)
print()
