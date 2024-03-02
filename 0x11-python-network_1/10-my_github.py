import requests

username = "mahmoudnabil133"
url = f"https://api.github.com/users/{username}"
response = requests.get(url)

if response.status_code == 200:
    user_data = response.json()
    user_id = user_data["id"]
    print("Your GitHub user ID is:", user_id)
else:
    print("Failed to fetch user data:", response.status_code)
