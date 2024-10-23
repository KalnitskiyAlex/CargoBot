from utils.misc.data_for_calculate import insurance_tax_list


def price_calculation(brutto_weight: float, base_price: float, unlicensed_tax: bool, city: str, invoice_price: float):
    if base_price < 200:
        if unlicensed_tax:
            if city == "Moscow":
                base_price += 0.5
            elif city == "Almaty":
                base_price -= 0.2

            price = float(base_price) * float(brutto_weight)
            for i_tuple in insurance_tax_list:
                if i_tuple[0] < float(invoice_price) / float(brutto_weight) <= i_tuple[1]:
                    price += price * i_tuple[2]
        else:
            price = float(base_price) * float(brutto_weight)
            for i_tuple in insurance_tax_list:
                if i_tuple[0] < float(invoice_price) / float(brutto_weight) <= i_tuple[1]:
                    price += price * i_tuple[2]
    else:
        cargo_price_mod = float(base_price) / float(brutto_weight)
        if unlicensed_tax:
            if city == "Moscow":
                cargo_price_mod += 0.5
            elif city == "Almaty":
                cargo_price_mod -= 0.2
            price = float(cargo_price_mod) * float(brutto_weight)
            for i_tuple in insurance_tax_list:
                if i_tuple[0] < float(invoice_price) / float(brutto_weight) <= i_tuple[1]:
                    price += price * i_tuple[2]
        else:
            price = float(cargo_price_mod) * float(brutto_weight)
            for i_tuple in insurance_tax_list:
                if i_tuple[0] < float(invoice_price) / float(brutto_weight) <= i_tuple[1]:
                    price += price * i_tuple[2]
    return price
