#Retrieve and parse jsons from http URL
import requests
import json

def main():
    url = "http://httpbin.org/json"
    result = requests.get(url)

    #Use the built-in JSON function to return parsed data
    dataobj = result.json()
    print(json.dumps(dataobj, indent=4))

    #Access data in the python object
    #print(list(dataobj.keys()))

    #print(dataobj['slideshow']['slides'][0]['title'])
    #print("There are {0} slides".format(len(dataobj['slideshow']['slides'])))
    for _ in dataobj['slideshow']['slides']:
        print(_['title'])



if __name__ == "__main__":
    main()