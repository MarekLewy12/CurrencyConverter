import requests

print("Please input currency acronyms, i.e 'USD'")
print("Currency to convert never changes - to change please run the program again")
print("To quit, simply press 'enter'\n")

owned_currency = (input("Currency to convert: ")).lower()
if not owned_currency:
    exit()

cache = {}

while True:

    url = f'http://www.floatrates.com/daily/{owned_currency}.json'

    r = requests.get(url).json()

    if owned_currency != 'usd' and owned_currency != 'eur':
        usd = (r['usd']['rate'])
        eur = (r['eur']['rate'])
        temp_cache = {'usd': usd, 'eur': eur}
        cache.update(temp_cache)
    if owned_currency == 'usd':
        eur = (r['eur']['rate'])
        cache.update({'eur': eur})
    if owned_currency == 'eur':
        usd = (r['usd']['rate'])
        cache.update({'usd': usd})

    currency_to_exchange_for = (input("Currency to exchange to: ")).lower()
    if not currency_to_exchange_for:
        break

    owned_money = float(input("How much money to convert?: "))

    if currency_to_exchange_for in cache.keys():
        exchange_result = round(owned_money * cache[f'{currency_to_exchange_for}'], 2)
        print(f"You received {exchange_result} {currency_to_exchange_for.upper()}.")
        continue

    else:
        needed_currency = r[f'{currency_to_exchange_for}']['rate']  # Needs to be cached
        exchange_result = round(owned_money * needed_currency, 2)
        print(f"You received {exchange_result} {currency_to_exchange_for.upper()}.")
        cache[f'{currency_to_exchange_for}'] = needed_currency
        continue

