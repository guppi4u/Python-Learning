import http.client
import json

conn = http.client.HTTPSConnection("api.github.com")

# Add proper headers - GitHub requires this!
headers = {
    "User-Agent": "MyPythonApp/1.0"  # GitHub requires this header
}

conn.request("GET", "/users/octocat", headers=headers)
response = conn.getresponse()
data = response.read().decode()

print("Response status:", response.status)

user_data = json.loads(data) 
print("\nUser Data:")
print(user_data)
# printing user data json as pretty format
print("\nPretty User Data:")
print(json.dumps(user_data, indent=4))
conn.close()
