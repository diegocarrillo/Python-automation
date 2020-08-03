#Process JSON data returned from a server

#Use the JSON module
import json

def main():
    #define a python dictionary
    pythonData = {
        "sandwich": "Jamon",
        "toasted": True,
        "toppings": ["Thousand Island Dressing",
                    "Sauerkraut",
                    "Picles"],
        "price": 8.99
    }

    #Serialize to JSON using Dumps
    jsonStr = json.dumps(pythonData, indent=4)

    #Print the resulting JSon String
    print("JSON Data: ---------------------")
    print(jsonStr)

if __name__ == "__main__":
    main()