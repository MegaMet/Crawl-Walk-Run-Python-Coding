#Creating a travel log

country = input("Please add a country name: ")
visits  = int(input("How many times have you visited: "))
list_of_cities = input("What cities have you visited there (separated with a ','): ").split(",")
print(list_of_cities)
cities = eval(str(list_of_cities))

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, visits, list_of_cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = list_of_cities

    travel_log.append(new_country)

add_new_country(country, visits, cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times\n"
      f"My favorite city was {travel_log[2]['cities'][0]}.")