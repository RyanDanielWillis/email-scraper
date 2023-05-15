from autoscraper import AutoScraper
import csv
import requests
import bs4
import time



url1 = 'https://expoplaza-tuttofood.fieramilano.it/en/exhibitors/alfa-ath-d-koukoutaris-sa'

wanted_list = ['info@alfapastry.com']

scraper = AutoScraper()
result = scraper.build(url1, wanted_list)
print(result)

result2 = scraper.get_result_similar('https://expoplaza-tuttofood.fieramilano.it/en/exhibitors/a-pizza')

print(result2)

result_list = [result, result2]

#start parsing all vendor links on main page
URLS = []
URL = 'https://expoplaza-tuttofood.fieramilano.it/en/exhibitors'

# Fetch all the HTML source from the url
response = requests.get(URL)
time.sleep(5)


# Parse HTML and extract links
soup = bs4.BeautifulSoup(response.text, 'html.parser')
links = soup.find_all("a")

# save dirty url list
for link in links:
    URLS.append(link.get('href'))

# clean URLs
clean_urls = []
for x in URLS:
    if "/en/exhibitors/" in str(x):
        clean_urls.append('https://expoplaza-tuttofood.fieramilano.it/en/exhibitors' + str(x))
    else:
        continue

rows = []
#scrape emails from clean url list
for i in clean_urls:
    z = 0
    rows.append(scraper.get_result_similar(clean_urls[z]))
    z += 1
    time.sleep(4)


# field names 
fields = ['Address', 'City', 'Country', 'Website', 'Stand', 'Phone', 'Email'] 
  
with open('email_scrape.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(rows)
