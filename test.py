import requests

url = "http://localhost:5000/api/chat"  # Flask server URL
data = {"message": "Hey Peter, tell me a joke!"}

response = requests.post(url, json=data)  # Send the POST request with JSON data
print(response.json())  # Print the response from the server