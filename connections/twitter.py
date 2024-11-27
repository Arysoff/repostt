
import os
from dotenv import load_dotenv
import requests
from requests_oauthlib import OAuth1

# Load environment variables
load_dotenv(dotenv_path="/Users/aryamanchanana/Desktop/repost/.env ")

# Access keys from .env
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
bearer_access_token = os.getenv("TWITTER_BEARER_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# #print("apikey",api_key)
# BASE_URL = "https://api.twitter.com/2/tweets"

# # Post a tweet using HTTP requests
# def post_tweet(content):
#     # Prepare headers with authentication
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json",
#     }

#     # Payload for the tweet
#     payload = {
#         "text": content
#     }

#     try:
#         # Send POST request to Twitter API
#         response = requests.post(BASE_URL, headers=headers, json=payload)

#         # Check if the request was successful
#         if response.status_code == 201:
#             print("Tweet posted successfully!")
#             tweet_id = response.json().get("data", {}).get("id")
#             print(f"Tweet URL: https://twitter.com/user/status/{tweet_id}")
#         else:
#             print(f"Error: {response.status_code} - {response.json()}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# if __name__ == "__main__":
#     tweet_content = input("Enter the content of your tweet: ")
#     post_tweet(tweet_content)
auth = OAuth1(api_key, api_secret, access_token, access_secret)

# Twitter API v2 endpoint for posting tweets
url = "https://api.twitter.com/2/tweets"

# Function to post a tweet
def post_tweet(content):
    # The correct parameter is 'text' not 'status'
    data = {
        "text": content  # Content of the tweet
    }

    try:
        # Send the POST request to the Twitter API
        response = requests.post(url, auth=auth, json=data)

        # Check if the request was successful
        if response.status_code == 201:
            print("Tweet posted successfully!")
            tweet_id = response.json().get("data", {}).get("id")
            print(f"Tweet URL: https://twitter.com/user/status/{tweet_id}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    tweet_content = input("Enter the content of your tweet: ")
    post_tweet(tweet_content)