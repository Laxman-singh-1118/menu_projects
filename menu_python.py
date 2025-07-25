import psutil
import time

def ram_monitor():
    try:
        while True:
            ram = psutil.virtual_memory()
            print(f"RAM Usage: {ram.percent}% | Available: {round(ram.available / 1e9, 2)} GB | Total: {round(ram.total / 1e9, 2)} GB")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitor stopped.")

ram_monitor()

from twilio.rest import Client

# Twilio account details
account_sid = input("your_account_sid")
auth_token = input("your_auth_token")
client = Client(account_sid, auth_token)

# Phone numbers
from_number = input("your_twilio_number")
to_number =input( "number_to_call")
# Make the call
call = client.calls.create(
    from_=from_number,
    to=to_number,
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)

import tweepy

# Replace with your actual credentials
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Post a tweet
tweet = "Hello, Twitter (X)! This is a tweet from Python. 🐍🚀"
api.update_status(tweet)

print("Tweet posted successfully!")

from twilio.rest import Client

# Credentials
account_sid = input("put ur sid of twilio")
auth_token = input('pls put ur token')# KEEP THIS SAFE!

client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body="Hello from Python using Twilio!",
    from_=input("Your Twilio phone number"),
    to=input('Destination phone number')
)

print("Message SID:", message.sid)


import tweepy

# Twitter API credentials
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate to Twitter
# Use OAuth1UserHandler for Tweepy v4+, else use OAuthHandler for older versions
try:
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
except AttributeError:
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Post a tweet
tweet = "Hello, world! This is a test tweet from Python."
try:
    api.update_status(tweet)
    print("Tweet posted successfully!")
except Exception as e:
    print(f"Error: {e}")

# Note: If you get a ModuleNotFoundError, install tweepy with: pip install tweepy


import requests
import json

# LinkedIn API credentials
client_id = ""
client_secret = ""
access_token= ""
person_id = ""

# Define the post data
def create_post_data(text):
    post_data = {
        "author": f"urn:li:person:{person_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.Post": {
                "shareMediaCategory": "ARTICLE",
                "text": {
                    "text":"this is a test post from the python script and its very tense and exciting to debug. Thank you."
                }
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    return post_data

# Post to LinkedIn
def post_to_linkedin(text):
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    post_data = create_post_data(text)
    try:
        response = requests.post(url, headers=headers, data=json.dumps(post_data))
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        if response.status_code == 201:
            print("Post created successfully!")
        else:
            print("Error occurred while posting to LinkedIn.")
    except Exception as e:
        print(f"Exception occurred: {e}")

# Example usage
text = "Hello, world! This is a test post."
post_to_linkedin(text)


from PIL import Image, ImageDraw, ImageFont

# Set image dimensions and background color
width, height = 400, 300
background_color = (30, 30, 30)  # dark gray

# Create a blank image
img = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(img)

# Draw a blue rectangle
draw.rectangle([(50, 50), (350, 120)], fill=(0, 102, 204))

# Draw a red circle
draw.ellipse([(150, 150), (250, 250)], fill=(255, 0, 0))

# Add text (optional font customization)
font = ImageFont.load_default()
draw.text((60, 60), "Hello, Digital World!", fill=(255, 255, 255), font=font)

# Save the image
img.save("my_digital_art.png")
print("✅ Image saved as 'my_digital_art.png'")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Step 1: Configure the browser
options = Options()
options.add_argument("--headless")  # Run in background
driver = webdriver.Chrome(options=options)

# Step 2: Open Google search
query = "India vs England score"
driver.get(f"https://www.google.com/search?q={query}")
time.sleep(2)  # Let the page load

# Step 3: Extract score result
try:
    score_box = driver.find_element(By.CLASS_NAME, "BNeawe")  # common result container
    print("🏏 Live Score:", score_box.text)
except Exception as e:
    print("❌ Could not find score:", e)

driver.quit()

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the website content
url = "https://www.google.com/search?q=india+vs+england"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Step 2: Find the score summary
score_summary = None
# Try to find the score summary in a span or div with relevant attributes
for tag in soup.find_all(["div", "span"]):
    if tag.text and ("India" in tag.text or "England" in tag.text) and ("-" in tag.text or ":" in tag.text):
        score_summary = tag.text.strip()
        break

# Step 3: Save the data to a CSV file
if score_summary:
    df = pd.DataFrame([[score_summary]], columns=["Score Summary"])
    df.to_csv("website_data.csv", index=False)
    print("✅ Data downloaded and saved as 'website_data.csv'")
else:
    print("❌ Could not find the score summary on the page.")


import sys
import time

# Create a sample tuple and list
my_tuple = (1, 2, 3, 4, 5)
my_list = [1, 2, 3, 4, 5]

# 1️⃣ Memory usage
print("🔍 Memory size (bytes):")
print(f"Tuple: {sys.getsizeof(my_tuple)}")
print(f"List : {sys.getsizeof(my_list)}")

# 2️⃣ Speed Test: Iterating multiple times
start_tuple = time.time()
for _ in range(1000000):
    for item in my_tuple:
        pass
end_tuple = time.time()

start_list = time.time()
for _ in range(1000000):
    for item in my_list:
        pass
end_list = time.time()

print("\n⚡ Speed test (1M iterations):")
print(f"Tuple: {end_tuple - start_tuple:.5f} seconds")
print(f"List : {end_list - start_list:.5f} seconds")

# 3️⃣ Mutability check
print("\n🔧 Mutability:")
try:
    my_tuple[0] = 100
except TypeError:
    print("Tuple: ❌ Cannot modify – it’s immutable")

my_list[0] = 100
print("List : ✅ Can modify – it’s mutable")

# 4️⃣ Hashability test
print("\n🔐 Hashability:")
try:
    hash(my_tuple)
    print("Tuple: ✅ Hashable – usable as dictionary key")
except TypeError:
    print("Tuple: ❌ Not hashable")

try:
    hash(my_list)
    print("List : ✅ Hashable")
except TypeError:
    print("List : ❌ Not hashable – cannot be a dictionary key")
