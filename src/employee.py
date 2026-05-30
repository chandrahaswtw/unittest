import requests


def getEmployeeData(id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")
    if response.ok:
        return response.text
    else:
        return "Bad response"
