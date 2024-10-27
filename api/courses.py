import requests

def get_cbr_rates():
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)

    from xml.etree import ElementTree as ET
    root = ET.fromstring(response.content)

    rates = {}

    for valute in root.findall('Valute'):
        char_code = valute.find('CharCode').text
        if char_code in ['USD', 'CNY']:
            value = valute.find('Value').text.replace(',', '.')
            rates[char_code] = float(value)

    return rates


if __name__ == "__main__":
    rates = get_cbr_rates()
    print("Курсы валют:")
    print(f"Доллар (USD): {round(rates['USD'], 2)} руб.")
    print(f"Китайский юань (CNY): {round(rates['CNY'])} руб.")