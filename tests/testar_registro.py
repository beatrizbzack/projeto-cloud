import requests as req


# Teste de Regristro
resp1 = req.post(
    'http://localhost:8000/registrar', 
    json={
        "name": "lalaa",
        "email": "lalaa",
        "password": "123"
    }
)
print(resp1.status_code, resp1.text)