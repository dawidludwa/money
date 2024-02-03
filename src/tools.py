def clean_data(df):
    # Drop columns: 'Unnamed: 20', 'Waluta' and 10 other columns
    df = df.drop(
        columns=[
            "Unnamed: 20",
            "Waluta",
            "Kwota blokady/zwolnienie blokady",
            "Waluta.1",
            "Kwota płatności w walucie",
            "Waluta.2",
            "Unnamed: 14",
            "Unnamed: 15",
            "Unnamed: 16",
            "Unnamed: 17",
            "Unnamed: 18",
            "Unnamed: 19",
        ]
    )
    # Drop column: 'Nazwa banku'
    df = df.drop(columns=["Nazwa banku"])
    # Drop column: 'Data księgowania'
    df = df.drop(columns=["Data księgowania"])
    # Drop rows with missing data in column: 'Kwota transakcji (waluta rachunku)'
    df = df.dropna(subset=["Kwota transakcji (waluta rachunku)"])
    # Change column type to datetime64[ns] for column: 'Data transakcji'
    df = df.astype({"Data transakcji": "datetime64[ns]"})
    # Drop column: 'Szczegóły'
    df = df.drop(columns=["Szczegóły"])
    # Change column type to float16 for column: 'Kwota transakcji (waluta rachunku)'
    df = df.astype({"Kwota transakcji (waluta rachunku)": "float"})
    # Rename column 'Kwota transakcji (waluta rachunku)' to 'amount'
    df = df.rename(columns={"Kwota transakcji (waluta rachunku)": "amount"})
    # Rename column 'Nr transakcji' to 'transaction_no'
    df = df.rename(columns={"Nr transakcji": "transaction_no"})
    # Rename column 'Nr rachunku' to 'account_number'
    df = df.rename(columns={"Nr rachunku": "account_number"})
    # Rename column 'Tytuł' to 'title'
    df = df.rename(columns={"Tytuł": "title"})
    # Rename column 'Dane kontrahenta' to 'details'
    df = df.rename(columns={"Dane kontrahenta": "details"})
    # Rename column 'Data transakcji' to 'date'
    df = df.rename(columns={"Data transakcji": "date"})
    # Rename column 'account_number' to 'account'
    df = df.rename(columns={"account_number": "account"})
    # Rename column 'transaction_no' to 'transaction'
    df = df.rename(columns={"transaction_no": "transaction"})
    # Replace all instances of "'" with "" in column: 'account'
    df["account"] = df["account"].str.replace("'", "", case=False, regex=False)
    # Replace all instances of "'" with "" in column: 'transaction'
    df["transaction"] = df["transaction"].str.replace("'", "", case=False, regex=False)
    # Remove leading and trailing whitespace in column: 'account'
    df["account"] = df["account"].str.strip()
    # Convert text to lowercase in column: 'title'
    df["title"] = df["title"].str.lower()
    # Remove leading and trailing whitespace in column: 'title'
    df["title"] = df["title"].str.strip()
    # Convert text to lowercase in column: 'details'
    df["details"] = df["details"].str.lower()
    # Remove leading and trailing whitespace in column: 'details'
    df["details"] = df["details"].str.strip()
    return df


def set_new_names(df):
    shops = {
        "Lidl": "lidl",
        "jarosław bugaj": "ps",
        "Allegro": "allegro",
        "Apteka": "pharmacy",
        "Biedronka": "biedronka",
        "PayPal": "paypal",
        "Google": "google",
        "Castorama": "castorama",
        "piekarnia oracz": "oracz",
        "ING Bank": "ing",
        "Zabka": "zabka",
        "Poczta Polska": "polish post",
        "paypro s.a.": "paypro",
        "myjnia 24h": "myjnia",
        "Orlen": "orlen",
        "zus centrum": "zus",
        "centrum": "delkatesy",
        "sądeckie wodociągi": "wodociągi",
        "Vinted": "vinted",
        "McDonalds": "mcdonalds",
        "Orange": "orange",
        "market obi": "obi",
        "pgnig obrót detaliczny": "pgnig",
        "payu": "payu",
        "Netflix": "netflix",
        "galeria usmiechu": "galeria usmiechu",
        "chatgpt subscription": "chatgpt",
        "pepco": "pepco",
        "rossmann": "rossmann",
        "auchan": "auchan",
        "bnp paribas": "bnp paribas",
        "ul.nawojowska": "ul.nawojowska",
        "disney": "disney",
        "rtv euro agd": "rtv euro agd",
        "github": "github",
        "pyszne.pl": "pyszne.pl",
        "p.h. aika": "aika",
        "CashBill": "cashbill",
        "centrum urody": "beauty center",
        "al capone": "al capone",
        "al. capone": "al capone",
        "ul. grodzka": "ul. grodzka",
        "Empik": "empik",
        "blue media": "blue media",
        "H&M": "h&m",
        "alfa sp. jawna": "alfa",
        "Jysk": "jysk",
        "aldi sp. z o.o.": "aldi",
        "Media Markt": "media markt",
        "mediaexpert": "mediaexpert",
        "bluemedia": "bluemedia",
        "piekarnia-ciastka": "piekarnia-ciastka",
        "wizz air": "wizz air",
        "wojas s.a.": "wojas",
        "centrum tranow tarnow pol": "centrum",
        "diagmed": "diagmed",
        "kaufland": "kaufland",
        "lejawa": "lejawa",
        "mobilevikings": "mobile vikings",
        "mobileviking": "mobile vikings",
        "lewiatan": "lewiatan",
        "player.pl": "player.pl",
        "medicine": "medicine",
        "barska clinic": "barska clinic",
        "mhr nowy sącz": "Małopolska Hodowla Roślin",
        "mhr nowy sacz sklep": "Małopolska Hodowla Roślin",
        "reserved": "reserved",
        "deichmann": "deichmann",
        "bolt": "bolt",
        "leroy merlin": "leroy merlin",
        "stacja paliw": "stacja paliw",
        "lpp sinsay": "sinsay",
        "ryanair": "ryanair",
        "inpost": "inpost",
        "browar personallo": "browar personall",
        "browar personall": "browar personall",
        "bp-": "bp",
        "myjnia": "myjnia",
        "yak z nepalu": "yak z nepalu",
        "ludwa dawid jan, i ludwa anna, edmunda ciećkiewicza 11, 33-300 nowy sącz": "konto",
        "ludwa dawid, i ludwa anna, babiego lata 9, 33-100 tarnów": "konto",
        "ludwa dawid jan, edmunda ciećkiewicza 11, 33-300 nowy sącz": "konto",
        "ludwa dawid, i ludwa anna, edmunda ciećkiewicza 11, 33-300 nowy sącz": "konto",
        "ludwa dawid, babiego lata 9, 33-100 tarnów": "konto",
        "rtveuroagd": "rtveuroagd",
        "jolanta wojciechowska": "jolanta wojciechowska",
        "decathlon": "decathlon",
        "ryanair": "ryanair",
        "jysk": "jysk",
        "revolut": "revolut",
        "empik": "empik",
    }

    for key, value in shops.items():
        df.loc[df["details"].str.contains(key, case=False), "details_2"] = value
    return df


def set_category(df):
    categories = {
        "grocery store": [
            "Lidl",
            "Biedronka",
            "Zabka",
            "Auchan",
            "oracz",
            "Aldi",
            "Centrum",
            "Lewiatan",
            "Kaufland",
            "aika",
        ],
        "Financial Services": [
            "PayPal",
            "ING Bank",
            "paypro",
            "PayU",
            "BNP Paribas",
            "CashBill",
            "Blue Media",
        ],
        "Healthcare": [
            "Apteka",
            "Pharmacy",
            "Diagmed",
            "Barska Clinic",
            "spec. praktyka lek",
        ],
        "Retail": [
            "Pepco",
            "Rossmann",
            "H&M",
            "Jysk",
            "Media Markt",
            "rtveuroagd",
            "Empik",
        ],
        "Food Service": [
            "McDonalds",
            "pyszne.pl",
            "Al Capone",
            "Yak from Nepal",
            "Grodzka St. Address",
            "Pyszne.pl",
            "Bakery & Cookies 39819",
        ],
        "Alcosol": ["Al Capone"],
        "Utility": ["Orange", "PGNiG Retail", "Sądeckie Waterworks"],
        "Transport": ["Wizz Air", "Bolt"],
        "Transport vacation": ["Wizz Air", "Ryanair"],
        "Ps": ["ps"],
        "Personal": ["Individual", "Beauty Center", "konto", "jolanta wojciechowska"],
        "Lejawa": ["lejawa"],
        "Clothes": [
            "H&M",
            "Wojas SA",
            "medicine",
            "Reserved",
            "Vinted",
            "Deichmann",
            "Sinsay",
        ],
        "Home Improvement": [
            "Castorama",
            "Obi Market",
            "Małopolska Hodowla Roślin",
            "Leroy Merlin",
            "alfa",
        ],
        "Entertainment": ["Netflix", "Disney", "player.pl"],
        "Technology": ["Google", "GitHub", "Mobile Vikings", "chatgpt"],
        "Postal Services": ["Polish Post", "InPost"],
        "Bills": ["ZUS", "wodociągi"],
        "Net": ["Allegro"],
        "dentist": ["galeria usmiechu"],
        "car": ["myjnia", "bp", "orlen", "Fuel Station", "24h Car Wash"],
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            df.loc[df["details"].str.contains(keyword, case=False), "category"] = (
                category
            )

    return df
