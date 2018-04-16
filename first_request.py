import requests

url = "http://www.google.ca"
r = requests.get(url)

print(f"your request to {url} came back w/ status code {r.status_code}" )