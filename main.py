import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"


def main():
    countries_list = []
    currency_list = []
    code_list = []
    index_list = []

    print("Hello please choose selecct a country by number!")

    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    tbody = soup.find("tbody")
    trs = tbody.find_all("tr")

    for tr in trs:
        country = tr.find_all("td")[0].string
        currency = tr.find_all("td")[1].string
        code = tr.find_all("td")[2].string

        countries_list.append(country)
        currency_list.append(currency)
        code_list.append(code)

    for index, country in enumerate(countries_list):
        index_list.append(index)
        country_format = "#{0} {1}".format(index, country)
        print(country_format)

    ask(currency_list, code_list, index_list)


def ask(currency_list, code_list, index_list):
    try:
        value = int(input("#"))
        if value == index_list[value]:
            print(f"\nYou choose {currency_list[value]}\n\nCode is {code_list[value]}")
            ask_re = input("\ndo you want start over? y/n ")
            if ask_re == "y":
                main()
            elif ask_re == "n":
                print("ok bye")
            else:
                print("you must be wirte y/n ")
    except IndexError:
        print("Choose a number from list")
        ask(currency_list, code_list, index_list)
    except ValueError:
        print("That's wasn't a number")
        ask(currency_list, code_list, index_list)


main()