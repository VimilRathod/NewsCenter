from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import SettingsForm

# Getting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')
# finding all the h2 tags from the parsed webpage
toi_headings = toi_soup.find_all('h2')
# removing footers
toi_headings = toi_headings[0:-13]
toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



# Getting news from Hindustan times

ht_r = requests.get("https://www.hindustantimes.com/india-news/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
# finding all the divisions in the class headingfour from the parsed webpage
ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
# Fetching all the elements except for the first three
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)

# Getting news from CBC

cbc_r = requests.get("https://www.cbc.ca/news/")
cbc_soup = BeautifulSoup(cbc_r.content, 'html.parser')
# finding all the h3 tags from the parsed webpage
cbc_headings = cbc_soup.findAll("h3")
# Fetching out only the useful data
cbc_headings = cbc_headings[1:35]
cbc_news = []

for cth in cbc_headings:
    cbc_news.append(cth.text)

def index(request):
    # Making an instance of the SettingsForm class
    form = SettingsForm()
    
    if request.method == "POST":
        # Fetching the data obtained in the post method
        data = SettingsForm(request.POST)
        # Checking if the data is valid and meaningful
        if data.is_valid():
            # Fetching data from different form elements
            d1 = data.cleaned_data['TOI']
            d2 = data.cleaned_data['HT']
            d3 = data.cleaned_data['CBC']
            # Rendering data back to the HTML page
            return render(request, 'news/index.html', {'toi_news':toi_news, 'ht_news': ht_news, 'cbc_news': cbc_news, 'form': SettingsForm(), 'd1': d1, 'd2': d2, 'd3': d3})
    else:
        # Returning empty form back to the HTML page if there a get method
        return render(request,"index.html",{'form':form})