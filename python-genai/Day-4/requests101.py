
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)  # Should print 200
print(response.json())  # Should print the JSON response from the API

print("*" * 20)  # Just a separator for better readability
print(response.headers)  # This will print the headers of the response
print(response.content)  # This will print the raw response body, which is in bytes

print("*" * 20)  # Another separator
#GET request with parameters:
params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
print(response.status_code)  # Should print 200
print(response.json())  # Should print the JSON response filtered by userId=1   

print("*" * 50)  # Another separator
#POST request:
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.status_code)  # Should print 201 (Created)
print(response.json())  # Should print the JSON response with the created post details  

print("*" * 50)  # Another separator

# POST with form data
form_data = {"username": "alice", "password": "secret"}
response = requests.post('https://httpbin.org/post', data=form_data)
print(response.status_code)  # Should print 200
print(response.json())  # Should print the JSON response showing the form data sent 
