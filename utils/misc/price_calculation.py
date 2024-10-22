from utils.misc.data_for_calculate import insurance_tax_list


def price_calculation(brutto_weight: float, cargo_price: float, unlicensed_tax: bool, city: str, invoice_price: float):
    if cargo_price < 200:
        if unlicensed_tax:
            if city == "Moscow":
                cargo_price += 0.5
            elif city == "Almaty":
                cargo_price -= 0.2
            price = cargo_price * brutto_weight
            for i_tuple in insurance_tax_list:
                if i_tuple[0] < invoice_price / brutto_weight <= i_tuple[1]:
                    price += price * i_tuple[2]
        else:
            price = cargo_price * brutto_weight
            for i_tuple in insurance_tax_list:
                if i_tuple[0] < invoice_price / brutto_weight <= i_tuple[1]:
                    price += price * i_tuple[2]
    else:
        cargo_price_mod = cargo_price / brutto_weight
        if unlicensed_tax:
            if city == "Moscow":
                cargo_price_mod += 0.5
            elif city == "Almaty":
                cargo_price_mod -= 0.2
            price = cargo_price_mod * brutto_weight
            for i_tuple in insurance_tax_list:
                if i_tuple[0] < invoice_price / brutto_weight <= i_tuple[1]:
                    price += price * i_tuple[2]
        else:
            price = cargo_price_mod * brutto_weight
            for i_tuple in insurance_tax_list:
                if i_tuple[0] < invoice_price / brutto_weight <= i_tuple[1]:
                    price += price * i_tuple[2]
    return price
