#Using the basic tasks for urllib
import urllib.request

def main():
    url = "http://httpbin.org/xml"

    #Open the URL and retrieve some data
    result = urllib.request.urlopen(url)

    #Print result code for status
    print("Result code: {0}".format(result.status))

    #print the return data headers
    print("Data headers \n")
    print(result.getheaders())

    #print the return data itself
    print("Data \n")
    print(result.read().decode('utf-8'))

if __name__ == "__main__":
    main()