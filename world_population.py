import json
import pygal
from country_codes import get_country_code


# Заполняем список данными
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Построение словаря с данными численности населения
    cc_population = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            print(population)
            code = get_country_code(country_name)
            print(code)
            if code:
                cc_population[code] = population

for code, pop in enumerate(cc_population):
    print(code, pop)

wm = pygal.maps.world.World()
wm.title = 'World population in 2010, by Country'
wm.add('2010', cc_population)

wm.render_to_file('world_population.svg')
