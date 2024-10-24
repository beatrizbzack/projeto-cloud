import requests as req

token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2aXZpIiwiZXhwIjoxNzI5NzkxMTE5fQ.e01arOtPmkbhTuR39kynPC4qxANvHE0HssMRFJJy6_k'

resp = req.get(
    'http://localhost:8000/consultar',
    headers={
        'accept': 'application/json',
        'Authorization':  f'Bearer {token}'  
    }
)
print(resp.status_code, resp.text)