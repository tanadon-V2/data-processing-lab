import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

print("all cities in Germany")
germany = []
germany = list(filter(lambda c: c["country"].startswith("Germany"), cities))
for g in germany:
    print(g)
print()

'''
Your code here

'''

# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C")
temp12 = []
spain = []
temp12 = list(filter(lambda c: float(c["temperature"]) > 12, cities))
spain = list(filter(lambda c: c["country"].startswith("Spain"), temp12))
for s in spain:
    print(s)
print()

'''
Your code here

'''

# Count the number of unique countries
print("Count the number of unique countries")
unique1 = []
unique2 = []
for city in cities:
    unique1.append(str(city['country']))
for u in unique1:
    if u not in unique2:
        unique2.append(u)
print("unique contries", len(unique2))
print()
'''
Your code here

'''

# Print the average temperature for all the cities in Germany
print("the average temperature for all the cities in Germany")
germany = []
germany = list(filter(lambda c: c["country"].startswith("Germany"), cities))
temp1 = 0
for g in germany:
    temp1 += float(g['temperature'])
print("average temperature", temp1/len(germany))
print()

'''
Your code here

'''

# Print the max temperature for all the cities in Italy
print("the max temperature for all the cities in Italy")
italy = []
temp3 = []
italy = list(filter(lambda c: c["country"].startswith("Italy"), cities))
for i in italy:
    temp3.append(float(i['temperature']))
print(max(temp3))
print()
'''
Your code here

'''
