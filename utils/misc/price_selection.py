from utils.misc.data_for_calculate import dishes_appliances_materials_list, household_goods_list, shoes_clothes_list, \
    toys_list

type_cargo_dict = {
    "dishes_appliances_materials": dishes_appliances_materials_list,
    "household_goods": household_goods_list,
    "shoes_clothes": shoes_clothes_list,
    "toys": toys_list
}


def price_selection(brutto_weight, volume, type_of_transportation):
    for type_cargo, cargo_list in type_cargo_dict.items():
        if type_of_transportation == type_cargo:
            for i_tuple in cargo_list:
                if float(i_tuple[0]) < brutto_weight / volume <= float(i_tuple[1]):
                    return i_tuple[2]

