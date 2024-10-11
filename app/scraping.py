import requests

def get_random_fact():
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    return response.json()  # Supondo que a API retorna JSON
