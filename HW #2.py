# Irene Gerrish
# HW 2

!pip3 install BeautifulSoup
!pip3 install --upgrade pip

from bs4 import BeautifulSoup
import urllib.request
import csv

# Crawler detection
import random
import time

# Script will pause for a n seconds
time.sleep(random.uniform(1, 5))
print('Pause Ended')

# Open a webpage
web_address = 'https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks'
web_page = urllib.request.urlopen(web_address)
web_page # stored

# Combining tools using lecture notes
with open('biden_speech.csv', 'w') as f: # set up w/ writer
    w = csv.DictWriter(f, fieldnames = ("date", "title", "text", "citation")) # define column names
    w.writeheader() # write the header
    web_address = 'https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks'
    web_page = urllib.request.urlopen(web_address)
    soup = BeautifulSoup(web_page.read()) # soup the webpage
    all_speeches = soup.find_all('tr') # find list of speeches
    for i in range(1, 2):
        try:
            speech = {} # dictionary
            speech_i = all_speeches[i].find_all('td')
            speech["date"] = speech_i[0].text # speech date
            speech["title"] = speech_i[1].text # title
            inner_page_url = web_address + speech_i[0].a['href']
            inner_page = urllib.request.urlopen(inner_page_url) # open speech
            inner_soup = BeautifulSoup(inner_page.read()) # soup page
        except:
            speech['citation'] = "NA"
    w.writerow(speech) # write row for this speech
    time.sleep(random.uniform(1, 5)) # sleep

# last line, per assignment suggestions: time.sleep(random.uniform(1, 5)) # be polite, sleep!

# You have already installed the BeautifulSoup package, so no need to install it again
from bs4 import BeautifulSoup
import urllib.request
import csv
import random
import time

# Define a function to scrape and save speech data
def scrape_and_save_speech_data():
    # Open a webpage
    web_address = 'https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks'
    web_page = urllib.request.urlopen(web_address)

    # Create a CSV file for writing
    with open('biden_speech.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=("date", "title", "text", "citation"))
        w.writeheader()

        soup = BeautifulSoup(web_page, 'html.parser')  # Specify the parser
        all_speeches = soup.find_all('tr')  # Find all speech rows in the table

        for i in range(1, len(all_speeches)):  # Iterate through all speeches
            try:
                speech = {}  # Create a dictionary for each speech
                speech_i = all_speeches[i].find_all('td')

                # Extract data
                speech["date"] = speech_i[0].text.strip()
                speech["title"] = speech_i[1].text.strip()
                inner_page_url = 'https://www.presidency.ucsb.edu' + speech_i[0].find('a')['href']
                inner_page = urllib.request.urlopen(inner_page_url)
                inner_soup = BeautifulSoup(inner_page, 'html.parser')

                # Find and extract text from inner page
                text = inner_soup.find('div', class_='field-docs-content')
                if text:
                    speech["text"] = text.get_text().strip()
                else:
                    speech["text"] = "NA"

                w.writerow(speech)  # Write the speech data to the CSV file

            except Exception as e:
                print(f"An error occurred: {str(e)}")

            time.sleep(random.uniform(1, 5))  # Sleep for a random amount of time

# Call the function to scrape and save speech data
scrape_and_save_speech_data()




