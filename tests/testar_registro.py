import requests as req


# Teste de Regristro
resp1 = req.post(
    'http://acaec9c5d2e0b4120a9cff376509986a-1261828741.us-east-2.elb.amazonaws.com/registrar', 
    json={
        "name": "humbas",
        "email": "humbas",
        "password": "humbas"
    }
)
print(resp1.status_code, resp1.text)