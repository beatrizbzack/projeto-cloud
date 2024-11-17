import requests as req

# Teste de Login
resp2 = req.post(
    'http://acaec9c5d2e0b4120a9cff376509986a-1261828741.us-east-2.elb.amazonaws.com/login',
    json={
        "email": "humbas",
        "password": "humbas"
    }
)
print(resp2.status_code)
token = resp2.json().get('jwt')
print(token)

if token:  # Verifica se o token foi recebido com sucesso
    resp = req.get(
        'http://acaec9c5d2e0b4120a9cff376509986a-1261828741.us-east-2.elb.amazonaws.com/consultar',
        headers={
            'Authorization': f'Bearer {token}'  
        }
    )
    print(resp.status_code)
    print(resp.json())  # Exibe a resposta da API
else:
    print("Token não recebido.")
