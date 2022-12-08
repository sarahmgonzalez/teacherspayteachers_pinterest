from bs4 import BeautifulSoup
import json
import requests

# Set the URL of the teacherspayteachers.com page to scrape
url = "https://www.teacherspayteachers.com/Product/Lesson-Title-123456"

# Make a GET request to the URL and parse the HTML response using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract the title, image, and description of the lesson
title = soup.find("h1", class_="product-title").text
image_url = soup.find("img", class_="product-image").get("src")
description = soup.find("div", class_="product-description").text

# Generate the Pinterest post using the extracted information
pinterest_post = f"""
    <p>Check out this lesson on teacherspayteachers.com:</p>
    <h1>{title}</h1>
    <img src="{image_url}" alt="{title}" />
    <p>{description}</p>
    <p>Find more great lessons at teacherspayteachers.com!</p>
"""

# Set the access token and board ID for your Pinterest account
access_token = "YOUR_ACCESS_TOKEN"
board_id = "YOUR_BOARD_ID"

# Set the URL and headers for the Pinterest API request
api_url = f"https://api.pinterest.com/v1/pins/?access_token={access_token}&board={board_id}&note={title}&link={url}&image_url={image_url}"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Make a POST request to the Pinterest API to create the new pin
response = requests.post(api_url, headers=headers)

# Print the response from the Pinterest API
print(response.json())