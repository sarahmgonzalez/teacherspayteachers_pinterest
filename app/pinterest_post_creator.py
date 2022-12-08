from bs4 import BeautifulSoup
import json
import requests

# Set the URL of the teacherspayteachers.com page to scrape
url = "https://www.teacherspayteachers.com/Product/Climate-Bundle-8826961"

# Make a GET request to the URL and parse the HTML response using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract the title, image, description, and standards of the lesson
title = soup.find("h1", class_="Text-module__root--3lnrt Text-module__headingLG--1mgj4 Text-module__colorExtraDark--qj5nL Text-module__noMarginBottom--1myL8 ProductPageSummary__header").text
print("title: ", title)

image_url = soup.find("img", class_="ProductPreviewSlider__slideImg").get("src")

description = soup.find("div", class_="ProductDescriptionLayout ProductDescriptionLayout--fromNewEditor").text

pinterest_post = f"""
    <p>Check out this lesson on teacherspayteachers.com:</p>
    <h1>{title}</h1>
    <img src="{image_url}" alt="{title}" />
    <p>{description}</p>
    <p>Find more great lessons at teacherspayteachers.com/Store/Vincent-Simonetti!</p>
"""


# standards = soup.find_all("div", class="ProductDescStandardsStackedSection__section", id="standards")
# standards_list = [s.text for s in standards]

# Generate the Pinterest post using the extracted information
# pinterest_post = f"""
#     <p>Check out this lesson on teacherspayteachers.com:</p>
#     <h1>{title}</h1>
#     <img src="{image_url}" alt="{title}" />
#     <p>{description}</p>
#     <p>Standards:</p>
#     <ul>
#         {''.join([f'<li>{s}</li>' for s in standards_list])}
#     </ul>
#     <p>Find more great lessons at teacherspayteachers.com/Store/Vincent-Simonetti!</p>
# """

print(pinterest_post)

# # Set the access token and board ID for your Pinterest account
# access_token = "YOUR_ACCESS_TOKEN"
# board_id = "YOUR_BOARD_ID"

# # Set the URL and headers for the Pinterest API request
# api_url = f"https://api.pinterest.com/v1/pins/?access_token={access_token}&board={board_id}&note={title}&link={url}&image_url={image_url}"
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded"
# }

# # Make a POST request to the Pinterest API to create the new pin
# response = requests.post(api_url, headers=headers)

# # Print the response from the Pinterest API
# print(response.json())