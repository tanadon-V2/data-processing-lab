
import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

def filter_items(condition, dict_list):
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    values = [item[aggregation_key] for item in dict_list]
    return aggregation_function(values)

print("The average temperature of all the cities:")
avg = aggregate("temperature", lambda temps: sum(float(t) for t in temps) / len(temps), cities)
print(avg)
print()

print("all cities in Germany")
germany = filter_items(lambda c: c["country"].startswith("Germany"), cities)
for g in germany:
    print(g)
print()

print("all cities in Spain with a temperature above 12°C")
spain = filter_items(lambda c: c["country"].startswith("Spain") and float(c["temperature"]) > 12,cities)
for s in spain:
    print(s)
print()

print("Count the number of unique countries")
unique_countries = aggregate("country", lambda countries: len(set(countries)), cities)
print("unique countries", unique_countries)
print()

print("the average temperature for all the cities in Germany")
avg = aggregate("temperature", lambda temps: sum(float(t) for t in temps) / len(temps), germany)
print("average temperature", avg)
print()

print("the max temperature for all the cities in Italy")
italy = filter_items(lambda c: c["country"].startswith("Italy"),cities)
max_italy = aggregate("temperature", lambda temps: max(float(t) for t in temps), italy)
print(max_italy)
print()
