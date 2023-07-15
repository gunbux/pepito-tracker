import requests
from bs4 import BeautifulSoup

# Get the user's profile page
url = "https://twitter.com/{}/".format(handle)
response = requests.get(url)

# Parse the HTML of the page
soup = BeautifulSoup(response.content, "html.parser")

# Get the user's name, screen name, and number of followers
name = soup.find("span", class_="full-name").text
screen_name = soup.find("span", class_="screen-name").text
followers_count = soup.find("span", class_="followers").text

# Print the user's information
print(name, screen_name, followers_count)
