import requests
from bs4 import BeautifulSoup
import schedule
import time
import json
import os
from datetime import datetime, timedelta

# Function to parse relative time strings into datetime objects
def parse_relative_time(time_str):
    current_time = datetime.now()
    if 'hour' in time_str:
        hours_ago = int(time_str.split()[0])
        return current_time - timedelta(hours=hours_ago)
    elif 'minute' in time_str:
        minutes_ago = int(time_str.split()[0])
        return current_time - timedelta(minutes=minutes_ago)
    elif 'day' in time_str:
        days_ago = int(time_str.split()[0])
        return current_time - timedelta(days=days_ago)
    # Add more cases as needed
    else:
        return current_time

# Function to scrape tech news
def scrape_tech_news():
    url = 'https://www.techcrunch.com'  # Replace with the actual tech news website
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    data_file = 'tech_news.json'
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example for extracting news titles and links
        articles = soup.find_all('div', class_='wp-block-tc23-post-picker')  # Modify based on website's structure
        news_list = []
        for article in articles:
            title_tag = article.find('h2')
            if title_tag:
                title = title_tag.text
                link = title_tag.find('a')['href']
                time_tag = article.find("div", class_='wp-block-tc23-post-time-ago')
                if time_tag:
                    time_str = time_tag.text.strip()
                    time_posted = parse_relative_time(time_str)
                    
                    news_item = {
                        'title': title,
                        'link': link,
                        'timeposted': time_posted.strftime('%Y-%m-%d %H:%M:%S')
                    }
                    news_list.append(news_item)

        # Only keep articles within the last 5 hours
        five_hours_ago = datetime.now() - timedelta(hours=5)
        news_list = [article for article in news_list if datetime.strptime(article['timeposted'], '%Y-%m-%d %H:%M:%S') > five_hours_ago]

        # Save the data to JSON file, replacing the old data
        with open(data_file, 'w') as file:
            json.dump(news_list, file, indent=4)

        print(f'Scraped {len(news_list)} articles and saved to {data_file}.')

    except requests.exceptions.RequestException as e:
        print(f'Error fetching the webpage: {e}')

# Schedule the scraping function to run every 5 hours
schedule.every(5).hours.do(scrape_tech_news)

# Initial run
scrape_tech_news()

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
