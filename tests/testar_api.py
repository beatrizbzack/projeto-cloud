import requests as req

# Teste de Login
resp2 = req.post(
    'http://localhost:8000/login',
    json={
        "email": "lalaa1",
        "password": "123"
    }
)
print(resp2.status_code)
token = resp2.json().get('jwt')
print(token)

if token:  # Verifica se o token foi recebido com sucesso
    resp = req.get(
        'http://localhost:8000/consultar',
        headers={
            'Authorization': f'Bearer {token}'  
        }
    )
    print(resp.status_code)
    print(resp.json())  # Exibe a resposta da API
else:
    print("Token não recebido.")
