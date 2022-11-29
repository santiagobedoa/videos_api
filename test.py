import requests

BASE = "http://127.0.0.1:5000/"

data = [
	{"likes": 10, "name": "Santi", "views": 100},
	{"likes": 18, "name": "How to make REST API", "views": 47},
	{"likes": 8902, "name": "Clickbait", "views": 14532}
]

for i in range(len(data)):
	response = requests.put(BASE + "video/" + str(i), data[i])
	print(response.json())

response = requests.patch(BASE + "video/1", {"likes": 20})

response = requests.get(BASE + "video/1")
print(response.json())