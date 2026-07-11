# Day 2: Moneycontrol Business News Scraper (RSS Data Ingestion)

import urllib.request
import xml.etree.ElementTree as ET

def fetch_moneycontrol_headlines(limit=5):
    # Moneycontrol's public RSS feed for Top Business News
    url = 'https://www.moneycontrol.com/rss/business.xml'
    
    try:
        print("Fetching live data from Moneycontrol...\n")
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
        
        root = ET.fromstring(xml_data)
        print(f"--- Top {limit} Business Headlines ---")
        
        count = 0
        for item in root.findall('.//item'):
            if count >= limit:
                break
                
            title = item.find('title').text
            pub_date = item.find('pubDate').text
            
            print(f"{count + 1}. {title}")
            print(f"   Published: {pub_date}\n")
            count += 1
            
    except Exception as e:
        print(f"Failed to fetch data. Error: {e}")

if __name__ == "__main__":
    fetch_moneycontrol_headlines(limit=5)
