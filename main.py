import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"


def main():
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    tbody = soup.find("tbody")
    trs = tbody.find_all("tr")
    for tr in trs:
        country = tr.find_all("td")[0].string
        print(country)


main()