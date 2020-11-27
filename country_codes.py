from pygal_maps_world import i18n


def get_country_code(country_name):
    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
    return None
