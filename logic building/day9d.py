my_dict = {
    "a": [{
        "adesh": [{
            "location": "pune",
            "address": {
                "name": "garkhindi",
                "pin_code": 90,
                "garkhindi": [{
                    "sarpanch_name": "mango"
                }]
            }
        }]
    }],
    "b": [{
        "sid": [{
            "location": "delhi",
            "address": {
                "name": "darodi",
                "pin_code": 91,
                "darodi": [{
                    "sarpanch_name": "banana"
                }]
            }
        }]
    }],
    "c": [{
        "shubham": [{
            "location": "nanded",
            "address": {
                "name": "belhe",
                "pin_code": 92,
                "belhe": [{
                    "sarpanch_name": "apple"
                }]
            }
        }]
    }]
}


name_input = input("Enter the user name: ")

for key, value in my_dict.items():

    initial = my_dict.get(key)
    user_data = initial[0].get(name_input)

    if user_data:
        address = user_data[0].get("address")

        for addr_key, addr_value in address.items():
            if type(addr_value) == list:
                sarpanch_name = addr_value[0].get("sarpanch_name")
                print(sarpanch_name)


