#Using request library to get and post
import requests

def main():
    #Using requets to issue a standard HTTP GET request
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    #printResults(result)

    #Send some parameters to the URL via a GET request, NO need encoding
    url = "http://httpbin.org/post"
    dataValues = {
        "key1" : "value1",
        "key2" : "value2"
    }
    result = requests.post(url, data=dataValues)
    #printResults(result)

    #Pass a custom header to the server
    url = "http://httpbin.org/get"
    headersValues = {
        "User-Agent" : "diego carrillo /1.0.0",
    }
    result = requests.get(url, headers=headersValues)
    printResults(result)




def printResults(restData):
    print("Result code: {0}".format(restData.status_code))
    print("\n")

    print("Headers: ---------------------")
    print(restData.headers)
    print("\n")

    print("Returned Data: ----------------------")
    print(restData.text)


if __name__ == "__main__":
    main()