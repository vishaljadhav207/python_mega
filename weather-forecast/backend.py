import requests

url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)

# If the request was successful
if response.status_code == 200:
    todos = response.json()  # Convert the response to JSON
    for todo in todos:
        print(todo['title'])  # Print only the title of each todo
else:
    print("Failed to fetch data:", response.status_code)
