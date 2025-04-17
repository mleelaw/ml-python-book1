ticker_symbols = {"GM": "General Motors", "CAT": "Catepillar", "EK": "Eastman Kodak"}

purchases = [
    ("GM", 100, "10-sep-2001", 48),
    ("CAT", 100, "1-apr-1999", 24),
    ("GM", 200, "1-jul-1998", 56),
    ("GM", 150, "15-may-2002", 32),
    ("EK", 200, "22-feb-2000", 62),
    ("CAT", 120, "30-nov-2001", 29),
    ("GM", 80, "5-mar-2003", 41),
    ("GM", 225, "12-aug-1999", 36),
    ("EK", 95, "7-oct-2002", 58),
    ("CAT", 180, "18-jun-2000", 26),
    ("GM", 110, "3-jan-2001", 30),
    ("GM", 250, "29-apr-2002", 44),
    ("EK", 140, "14-dec-1999", 64),
]


def purchase_list():
    print("Purchase List")
    print("-" * 25)
    for purchase in purchases:
        update_list = (purchase[1]) * (purchase[3])

        for ticker, name in ticker_symbols.items():
            if purchase[0] == ticker:
                print(f"{name} stock purchased for {update_list}")


def investment_by_ticker():

    new_dictionary = {}

    for ticker, name in ticker_symbols.items():
        new_ticker = ticker
        ticker_list = []

        for purchase in purchases:
            if purchase[0] == ticker:
                ticker_list.append(purchase)

        new_dictionary[new_ticker] = ticker_list

    total_total = []
    for company, totals in new_dictionary.items():

        holdings = []

        for total in totals:
            total_of_company = (total[1]) * (total[3])
            holdings.append(total_of_company)

        total_holdings_per_company = sum(holdings)
        total_total.append(total_holdings_per_company)

        print(f"*{company} Holdings: ${total_holdings_per_company}")
    print("Portfolio Total")
    print("-" * 25)
    final_total = sum(total_total)
    print(f"Total value of stock in portfolio ${final_total}")


investment_by_ticker()
purchase_list()
