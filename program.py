wiek = input("Podaj wiek uzytkownika: ")
# Sprawdzamy czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi by podany jako liczba")
wiek = int(wiek)
if wiek >= 18 and wiek <=50:
    print("Witaj w naszym sklepie z alkoholem")
elif wiek > 50:
    print("Witaj w naszym sklepie z alkoholem")
    print("W twoim wieku alkohol jest już szkodliwy")
else:
    exit("Jestes za młody na alkohol!")
