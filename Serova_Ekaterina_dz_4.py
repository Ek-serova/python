

#задание 2
import requests

def currency_rates(name_valut):
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    valutes = response.json()['Valute']
    valutes_enter = valutes[name_valut]
    course = valutes_enter ['Value']
    return (course)

print(currency_rates('USD'))

#задание 4

import until_module

until_module.currency_rates







