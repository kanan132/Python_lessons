#pip install bs4
import requests
from bs4 import BeautifulSoup
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning # verify=False, ssl

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




save_path = './'
completeName = os.path.join(save_path, "ss.txt")
file1 = open(completeName, "w")
ww = 0
while ww <= 12500:
    r = requests.get("https://www.railwagonlocation.com/ru/gng-2007-codes.php?start=" + str(ww), verify=False) # verify=False, ssl
    rr = r.content
    soup = BeautifulSoup(rr, 'html.parser') 
    rows = soup.find("tbody")
    for i in range(500):

        try:
            rows = rows.find_next("tr").find_next("td")
            rows2 = rows.text.strip() + "\t" + rows.find_next("td").text.strip()
            file1.write(rows2 + "\n")
        except:
            break
    ww += 500

file1.close()
