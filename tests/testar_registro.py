import requests as req


# Teste de Regristro
resp1 = req.post(
    'http://localhost:8000/registrar', 
    json={
        "name": "humberto",
        "email": "humberto@mail.com",
        "password": "123"
    }
)
print(resp1.status_code, resp1.text)