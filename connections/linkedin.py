import os
from dotenv import load_dotenv
import requests
from datetime import datetime

# Load environment variables
load_dotenv(dotenv_path="/Users/aryamanchanana/Desktop/repost/.env ")
access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
# Set the headers for authentication
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

def user_info(headers):
    '''
    Get user information from LinkedIn
    '''
    response = requests.get('https://api.linkedin.com/v2/me', headers=headers)
    user_info = response.json()
    return user_info

# Get user ID to make a UGC post
user_info_data = user_info(headers)
# print(user_info_data)
# urn = user_info_data['id']  # Use the correct field name ('id') for the user's urn

# UGC will replace shares over time.
api_url = 'https://api.linkedin.com/v2/ugcPosts'
author = f'urn:li:person:Hos7PlFDPO'


def post(message):
    print("-- Creating Post --")

    # Get the link and message from the user
    link = 'https://developer.linkedin.com/'
    today = datetime.now().strftime("%Y-%m-%d")
    post_data = {
        "author": author,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": message
                },
                "shareMediaCategory": "ARTICLE",
                "media": [
                    {
                        "status": "READY",
                        "description": {
                            "text": message
                        },
                        "originalUrl": link,
                        # You can optionally include a title
                        "title": {
                            "text": f"Daily Tech Insights - {today}"
                        }
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

# Send the post request to LinkedIn API

    r = requests.post(api_url, headers=headers, json=post_data)
    
    if r.status_code in [200, 201]:
        print("Post successful!")
    else:
        print(f"Failed to post. Status Code: {r.status_code}")
    
    # Print the response body to inspect further details
    print("Response JSON:", r.json())
