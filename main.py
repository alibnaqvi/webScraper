import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Set up the ChromeDriver service
service = Service(executable_path='/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)

# Open the YouTube video page
video_url = 'https://www.youtube.com/watch?v=IDHere'
driver.get(video_url)

# Scroll to load comments
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(20)  # Wait for comments to load
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find comment elements
comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

# Open a CSV file to write comments
with open('youtube_comments.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write each comment to the CSV file
    for comment in comments:
        writer.writerow([comment.text])

driver.quit()
