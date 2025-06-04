import whois

def get_domain_info(name):
    """
    Pobiera informacje WHOIS dla podanej domeny i zwraca wybrane dane
    
    Args:
        name (str): Nazwa domeny do sprawdzenia

    Returns:
        dict: Słownik z informacjami o domenie (nazwa, data utworzenia, DNS, 
        rejestrator i kraj rejestracji)
    """

    domain = whois.whois(name)

    return{
        "Nazwa domeny": domain.domain_name,
        "Data utworzenia": domain.creation_date,
        "Serwery DNS": domain.name_servers,
        "Rejestrator": domain.registrar,
        "Kraj rejestracji": domain.country
    }

#przyklad uzycia
info = get_domain_info("portal.wsb.pl")

for key, value in info.items():
    print(f"{key}: {value}")

