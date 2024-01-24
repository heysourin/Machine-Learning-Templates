#### READING CSV FILE FROM AN URL ####
import requests
from io import StringIO
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv" #REPLACE IT YOUR URL
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14;  rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests-get(url, headers=headers)
data = StringIO(req.text)
pd.read_csv (data)
