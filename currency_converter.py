import requests
import json


def convert_selected(amount, local, output_currencies):
    raw_rates = get_conversion_rates(local)
    adjusted_rate = dict()
    for currency in raw_rates:
        if currency in output_currencies:
            adjusted_rate[currency] = amount*raw_rates[currency]
    return adjusted_rate



def convert_all(amount, rate):
    raw_rates = get_conversion_rates(rate)
    adjusted_rate = dict()
    for currency in raw_rates:
        adjusted_rate[currency] = amount*raw_rates[currency]
    return adjusted_rate


def get_conversion_rates(local):
    pfile = open("private.txt", 'r')
    api_key = pfile.read().strip()
    response = requests.get("https://v6.exchangerate-api.com/v6/" + api_key + "/latest/" + local)
    if response.status_code == 200:
        content = response.content.decode("utf-8")
        json_content = json.loads(content)
        rates_dict = dict()
        # rates_dict['GBP'] = 1.3
        for key, value in json_content["conversion_rates"].items():
            rates_dict[key] = value

        return rates_dict

    else:
        print("Couldn't access change rates " + response.status_code)
        return None
