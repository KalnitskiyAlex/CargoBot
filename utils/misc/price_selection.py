from utils.misc.data_for_calculate import dishes_appliances_materials_list, household_goods_list, shoes_clothes_list, \
    toys_list

type_cargo_dict = {
    "dishes": dishes_appliances_materials_list,
    "appliances": dishes_appliances_materials_list,
    "materials": dishes_appliances_materials_list,
    "household": household_goods_list,
    "clothes": shoes_clothes_list,
    "toys": toys_list
}


def price_selection(brutto_weight: float, volume: float, type: str):
    for type_cargo, cargo_list in type_cargo_dict.items():
        if type == type_cargo:
            for i_tuple in cargo_list:
                if float(i_tuple[0]) < float(brutto_weight) / float(volume) <= float(i_tuple[1]):
                    return i_tuple[2]

