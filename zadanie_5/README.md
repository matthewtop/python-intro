# Raport dotyczący bibliotek python - whois oraz requests

Wybór padł na biblioteki związane z dziedziną cyberbezpieczeństwa, mianowicie `whois` oraz `requests`.

## Instalacja oraz wykorzystanie kodu 
Poniższe instrukcje dotyczą przykładowego repozytorium, które zawiera przykładowe skrypty wykorzystujące obie biblioteki.

Sklonuj repozytorium i przejdź do folderu
```bash
git clone https://github.com/matthewtop/python-intro.git
cd python-intro/zadanie_5
```

Utwórz wirtualne środowisko venv i je aktywuj
```bash
python -m venv venv
source venv/bin/activate
```

Zainstaluj potrzebne zależności
```bash
pip install -r requirements.txt
```

Następnie przejdź do folderu examples i uruchom wybrany kod, np:
```bash
cd examples
python3 whois_example.py
```

## whois
### Linki
- [Dokumentacja](https://pypi.org/project/python-whois/)  
- [Repozytorium GitHub](https://github.com/joepie91/python-whois)

### Przeznaczenie i główne funkcje
Biblioteka `whois` służy do pobierania informacji WHOIS o domenach internetowych. Umożliwia łatwe zapytania o dane rejestracyjne domen, takie jak przykładowo:
- nazwa domeny,
- data utworzenia,
- serwery DNS,
- rejestrator domeny,
- kraj rejestracji

### Kluczowe zalety
- **Prosta i intuicyjna obsługa** – szybkie wykonywanie zapytań WHOIS bez konieczności pracy z surowym protokołem.
- **Wygodne API** – dane zwracane są w postaci obiektów z łatwym dostępem do atrybutów.
- **Umożliwia integrację z różnymi projektami** – przydatna w aplikacjach związanych z zarządzaniem domenami, bezpieczeństwem i analizą danych.

### Ograniczenia
- **Nie zawsze kompletne i ujednolicone dane** – ze względu na różne standardy WHOIS u różnych rejestratorów.
- **Brak oficjalnego wsparcia i możliwe problemy z kompatybilnością**
- **Zależność od dostępności serwerów WHOIS** – czasem mogą wystąpić opóźnienia lub ograniczenia w zapytaniach.
- **Możliwe problemy z działaniem na bardzo starych wersjach Pythona** (zalecane wersje 3.x).

## requests
### Linki
- [Dokumentacja](https://requests.readthedocs.io/en/latest/)
- [Repozytorium](https://github.com/psf/requests)

### Przeznaczenie i główne funkcje
`requests` to popularna biblioteka do wykonywania zapytań HTTP w Pythonie. Umożliwia łatwe wysyłanie żądań GET, POST, PUT, DELETE i innych, obsługę nagłówków, ciasteczek, sesji, uwierzytelniania i więcej.

### Kluczowe zalety
- **Bardzo prosta i czytelna składnia** – szybkie i wygodne wykonywanie zapytań HTTP.
- **Bogate możliwości konfiguracyjne** – wsparcie dla sesji, timeoutów, przekierowań, autoryzacji i wielu innych.
- **Bardzo duża i aktywna społeczność** – biblioteka jest dobrze utrzymywana i szeroko stosowana.
- **Kompatybilność z Python 2.7 i 3.x** – działa na większości wersji Pythona.

### Ograniczenia
- **Brak wbudowanego wsparcia dla asynchroniczności** – do asynchronicznych zapytań potrzebne są dodatkowe biblioteki (np. httpx, aiohttp).
- **Wydajność** – dla bardzo dużej liczby zapytań może być mniej wydajna.
