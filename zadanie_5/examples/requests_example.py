import requests

def fetch_url_content(url):
    """
    Pobiera zawartość strony internetowej pod podanym adresem URL.
    
    Args:
        url (str): Adres URL strony do pobrania, np. "https://www.google.com".
        
    Returns:
        dict: Słownik z kodem statusu odpowiedzi i zawartością strony (tekst).
    """
    response = requests.get(url)  #zapytanie HTTP GET do podanego URL
    
    # sprawdzenie czy zapytanie się powiodło (status 200 oznacza OK)
    if response.status_code == 200:
        content = response.text  # Pobierz zawartość strony jako tekst
    else:
        content = None
    
    return {
        "status_code": response.status_code,
        "content": content
    }

# Przykład użycia
result = fetch_url_content("https://www.google.com")

print("Kod statusu:", result["status_code"])
print("Fragment zawartości strony:", result["content"][:200])  # Wyświetl pierwsze 200 znaków