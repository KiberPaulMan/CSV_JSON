import json
import pygal
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
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
            code = get_country_code(country_name)
            if code:
                cc_population[code] = population

# Групировка стран по 3-м уровням населения
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
# сс_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    if pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
