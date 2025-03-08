#3.3 Korzystanie z dokumentacji języka Python
#Wybrane funkcje wbudowane:
    # 1. abs(x) - zwraca wartość bezwzględną liczby x -> https://docs.python.org/3/library/functions.html#abs
    # 2. type(x) - zwraca typ zmiennej x -> https://docs.python.org/3/library/functions.html#type
    # 3. round(x,2) - zwraca zaokrągloną wartość liczby x - w tym przypadku liczba zostanie zaokrąglona do 2 miejsc po przecinku -> https://docs.python.org/3/library/functions.html#round
#Wybrane moduły z biblioteki standardowej:
    # 1. os - moduł zapewniający interakcję z systemem operacyjnym, takie jak np. uruchamianie procesów czy zarządzanie plikami -> https://docs.python.org/3/library/os.html#module-os
    # 2. math - moduł zawierający funkcje matematyczne, takie jak np. inf, exp, log, sin, sqrt -> https://docs.python.org/3/library/math.html#module-math
    # 3. random - moduł zawierający funkcje generujące liczby losowe -> https://docs.python.org/3/library/random.html#module-random
#Wybrane wyjątki:
    # 1. ZeroDivisionError - wyjątek zgłaszany przy próbie dzielenia przez zero -> https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
    # 2. SyntaxError - wyjątek zgłaszany przy błędzie składniowym -> https://docs.python.org/3/library/exceptions.html#SyntaxError
    # 3. ImportError - wyjątek zgłaszany przy błędzie importowania modułu, np. gdy takowy nie istnieje -> https://docs.python.org/3/library/exceptions.html#ImportError
 

import math
import os

#funkcje wbudowane
list1 = [11, 22, 33, 44, 55] 
list2 = [15, 28, 21, 60, 9]
listZip = list(zip(list1, list2)) #połączenie dwóch list w jedną listę używając funkcji zip -> https://docs.python.org/3/library/functions.html#zip
print("Połączona lista: ", listZip)

#moduł biblioteki standardowej os
nazwaSystemu = os.name #zwraca nazwę systemu operacyjnego, 'posix' dla Linux/macOS, 'nt' dla Windows -> https://docs.python.org/3/library/os.html#os.name 
print("Twoja nazwa systemu to " + nazwaSystemu)

#prezentacja obsługi wyjątku ImportError
try: #-> https://docs.python.org/3/reference/compound_stmts.html#try
    import modulWSBktoryNieIstnieje
except ImportError as e: #-> https://docs.python.org/3/library/exceptions.html#ImportError
    print("Moduł o nazwie nie istnieje")