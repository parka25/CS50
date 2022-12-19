import requests
import sys
if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Missing Command-Line Arguement")
        sys.exit(1)
else:
    print("Missing Command-Line Arguement")
    sys.exit(1)
try:
    request = request.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = request.json()
    bitcoin = response["bpi"]["USD"]["rate_float"]
    total = bitcoin * value
    print(total)
except requests.RequestException:
    print("Request Exemption")
    sys.exit(1)
