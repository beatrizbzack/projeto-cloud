import requests as req
import json

# Teste de Login
resp2 = req.post(
    'http://localhost:8000/login',
    json={
        "email": "teste2",
        "password": "123"
    }
)
print(resp2.status_code)
token=resp2.json()['jwt'] 

resp = req.get(
    'http://localhost:8000/consultar',
    headers={
        'accept': 'application/json',
        'Authorization':  f'Bearer {token}'  
    }
)
print(resp.status_code, f'SEU FUN FACT ALEATÓRIO: {json.loads(resp.text).get("text")}')