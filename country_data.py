

def asia():
    asian_countries = [
        "afghanistan", "armenia", "azerbaijan", "bahrain", "bangladesh", "bhutan",
        "brunei", "cambodia", "china", "cyprus", "georgia", "india", "indonesia",
        "iran", "iraq", "israel", "japan", "jordan", "kazakhstan", "kuwait",
        "kyrgyzstan", "laos", "lebanon", "malaysia", "maldives", "mongolia",
        "myanmar", "nepal", "north-korea", "oman", "pakistan", "palestine",
        "philippines", "qatar", "saudi-arabia", "singapore", "south-korea",
        "sri-lanka", "syria", "tajikistan", "thailand", "east-timor", "turkyie",
        "turkmenistan", "united-arab-emirates", "uzbekistan", "vietnam", "yemen"
    ]
    return asian_countries

def europe():
    european_countries = [
        "albania", "andorra", "austria", "belarus", "belgium",
        "bosnia-and-herzegovina", "bulgaria", "croatia", "czech-republic",
        "denmark", "estonia", "finland", "france", "germany", "greece",
        "hungary", "iceland", "ireland", "italy", "latvia", "liechtenstein",
        "lithuania", "luxembourg", "malta", "moldova", "monaco", "montenegro",
        "netherlands", "north-macedonia", "norway", "poland", "portugal",
        "romania", "san-marino", "serbia", "slovakia", "slovenia", "spain",
        "sweden", "switzerland", "ukraine", "united-kingdom", "vatican-city"
    ]
    return  european_countries


def africa():
    african_countries = [
        "algeria", "angola", "benin", "botswana", "burkina-faso", "burundi",
        "cape-verde", "cameroon", "central-african-republic", "chad", "comoros",
        "congo", "democratic-republic-of-the-congo", "djibouti", "egypt",
        "equatorial-guinea", "eritrea", "eswatini", "ethiopia", "gabon", "gambia",
        "ghana", "guinea", "guinea-bissau", "ivory-coast", "kenya", "lesotho",
        "liberia", "libya", "madagascar", "malawi", "mali", "mauritania",
        "mauritius", "morocco", "mozambique", "namibia", "niger", "nigeria",
        "rwanda", "sao-tome-and-principe", "senegal", "seychelles", "sierra-leone",
        "somalia", "south-africa", "south-sudan", "sudan", "tanzania", "togo",
        "tunisia", "uganda", "zambia", "zimbabwe"
    ]
    return african_countries


def oceania():
    oceania_countries = [
        "australia", "fiji", "kiribati", "marshall-islands", "micronesia",
        "nauru", "new-zealand", "palau", "papua-new-guinea", "samoa",
        "solomon-islands", "tonga", "tuvalu", "vanuatu"
    ]

    return oceania_countries


def north_america():
    north_american_countries = [
        "antigua-and-barbuda", "bahamas", "barbados", "belize", "canada",
        "costa-rica", "cuba", "dominica", "dominican-republic", "el-salvador",
        "grenada", "guatemala", "haiti", "honduras", "jamaica", "mexico",
        "nicaragua", "panama", "saint-kitts-and-nevis", "saint-lucia",
        "saint-vincent-and-the-grenadines", "trinidad-and-tobago", "united-states-of-america"
    ]
    return north_american_countries


def south_america():
    south_american_countries = [
        "argentina", "bolivia", "brazil", "chile", "colombia", "ecuador",
        "guyana", "paraguay", "peru", "suriname", "uruguay", "venezuela"
    ]
    return south_american_countries

def the_world():
    Asia = asia()
    Europe = europe()
    Africa = africa()
    Oceania = oceania()
    North_america = north_america()
    South_america = south_america()
    all_countries = Asia + Europe + Africa + Oceania + North_america + South_america 
    return all_countries
