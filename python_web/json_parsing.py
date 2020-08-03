#Parse json objects to use it in python operations
import json

def main():
    jsonStr = '''{
            "sandwich" : "Jamon",
            "toasted" : true,
            "toppings" : [
                "Thousand Island Dressing",
                "Sauerkraut",
                "Pickels"
            ],
            "price" : 8.99
        }'''

    #parse the JSON data
    data = json.loads(jsonStr)
    #print information from the parsed dictionary/JSON
    print("Sandwich: " + data['sandwich'])
    if (data['toasted']):
        print("And it's toasted!")

    for i in data['toppings']:
        print("These are the toppings available: " + i)

if __name__ == "__main__":
    main()