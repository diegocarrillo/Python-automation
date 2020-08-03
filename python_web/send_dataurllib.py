#Send data to web server using urllib

import urllib.request
import urllib.parse

def main():
    url = "http://httpbin.org/get"

    #Create data to pass to the GET request
    args = {
        "name": "Diego Carrillo",
        "is_author": True
    }

    #Data needs to be url-encoded before passing as arguments
    data = urllib.parse.urlencode(args)

    #Issue the request with the data params as part of the URL
    #result = urllib.request.urlopen(url + "?" + data)

    #Issue the request with a data parameter to use POST
    url = "http://httpbin.org/post"
    data_encoded = data.encode()
    result = urllib.request.urlopen(url, data=data_encoded)

    print("Result code {0}".format(result.status))
    print("Returned Data: -----------------------")
    print(result.read().decode('utf-8'))

if __name__ == "__main__":
    main()