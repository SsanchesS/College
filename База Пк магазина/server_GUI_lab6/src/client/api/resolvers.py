import requests

def check_login(username: str, password: str):
    data = f'{{ "username": "{username}", "password": "{password}" }}'
    r = requests.post('http://127.0.0.1:8000/login/log', data=data)
    answer = r.json()
    print(answer)
    code = answer["code"]
    message = answer["message"]
    if code != 200:
        print(f"Server error:{message}")
        return None
    else:
        return answer["id"][0]