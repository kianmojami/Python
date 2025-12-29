#Hands-on 16
#Kian Mojami

import json
from urllib.request import urlopen

def main():
    with urlopen("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json") as response:
             source = response.read()
    data = json.loads(source)
    print(data)
    country = data["usd"]
    print(country)
            
    with urlopen("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.min.json") as response2:
             countrysource = response2.read()
    data2 = json.loads(countrysource)
    print(data2)

    convert = True
    while convert:
        destination = input("Enter a country currency to convert to: ")
        if destination in country:
            amount = float(input("Enter an amount to convert: $"))
            total = amount * float(country[destination])
            destinationCountry = data2[destination]
            print(f"A ${amount} US dollars is worth ${total} in {destinationCountry}")
            another = input("Another? Yes or No: ").capitalize()
            while another not in ("Yes", "No"):
                print("Invalid Input")
                another = input("Another? Yes or No: ").capitalize()
            if another == "No":
                convert = False
        else:
            print("Country code not found")

main()
