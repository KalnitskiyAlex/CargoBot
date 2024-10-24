from utils.misc.data_for_calculate import (dishes_appliances_materials_list, household_goods_list, shoes_clothes_list,
                                           toys_list)

type_cargo_dict = {
    "Посуда": dishes_appliances_materials_list,
    "Быт.техника": dishes_appliances_materials_list,
    "Стр.материалы": dishes_appliances_materials_list,
    "Хоз.товары": household_goods_list,
    "Обувь/Одежда": shoes_clothes_list,
    "Игрушки": toys_list
}


def price_selection(brutto_weight: float, volume: float, type: str):
    for type_cargo, cargo_list in type_cargo_dict.items():
        if type == type_cargo:
            for i_tuple in cargo_list:
                if float(i_tuple[0]) < float(brutto_weight) / float(volume) <= float(i_tuple[1]):
                    return i_tuple[2]
