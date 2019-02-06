states = {
    "CA": "California",
    "NJ": "New Jersey",
    "WI": "Wisconsin",
    "NY": "New York"
}

print(states["CA"])
print(states["WI"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000 # 39,500,000
    },
    "NJ": {
        "NAME": "New Jersey",
        "POPULATION": 9000000 #9,000,000
    },
    "WI": {
        "NAME": "Wisconsin",
        "POPULATION": 5800000 # 5,800,000
    },
    "NY": {
        "NAME": "New york",
        "POPULATION": 19500000 # 19,500,000
    }
}

print (nested_dictionary["CA"])
print(nested_dictionary["CA"]["POPULATION"])
print(nested_dictionary["NY"]["NAME"])
print(nested_dictionary["NY"]["POPULATION"])


complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000, # 39,500,000
        "CITIES":[
            "Fresno",
            "Los Banos",
            "Clovis"
        ]
    },
    "NJ": {
        "NAME": "New Jersey",
        "POPULATION": 9000000, #9,000,000
        "CITIES":[
            "newark",
            "trenton"
        ]
    },
    "WI": {
        "NAME": "Wisconsin",
        "POPULATION": 5800000, # 5,800,000
        "CITIES":[
            "Maddison",
            "Milwaukee",
            "Green bay"
        ]
    },
    "NY": {
        "NAME": "New york",
        "POPULATION": 19500000, # 19,500,000
        "CITIES":[
            "New york City",
            "Rockseter",
            "Buffalo"
        ]
    }
}