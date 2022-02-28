import requests
import datetime
import json

# TODO: Send to SQL Server, Back-fill History, Automate
# temp_unix = 1634184000000
# temp comment

yesterday = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(
    days=1)

# timestamp is returned as decimal, multiply by 1000 to get milliseconds
yesterday_unix = int(yesterday.timestamp()) * 1000


def get_spotify_data(unix=yesterday_unix, limit=50):
    access_token = "BQBzxCQSIbVATXtPDUEExYwF1vfR7muQxAHiEWyvB8NKrKOzWPKiKrWYDp2TepZLrQGzYKe73N2Oh0h5MjvlnOvRBOU-uoGtwLXPdtAvS4GU8pXaqq1NwkG5kKZMkYdRqdYrejOy58UCny5IKhxo4WF6f6-YK_z3RVGPHTo7"

    headers = {"Authorization": f"Bearer {access_token}",
               "Content-Type": "application/json",
               "Accept": "application/json"}

    api_url = f"https://api.spotify.com/v1/me/player/recently-played?after={unix}&limit={limit}"

    api_get = requests.get(url=api_url, headers=headers)

    api_output = api_get.json()

    with open("spotify_api_output2.json", "w") as output_file:
        json.dump(api_output, output_file)


get_spotify_data(unix=1643691600000)
