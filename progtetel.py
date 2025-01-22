import random

def lista():
    lista = []
    for _ in range(10):
        szam = random.randint(5,15)
        lista.append(szam)
    return lista

lista = lista()
print(f"Lista: {lista}")

def osszegzes(lista):
    osszeg = 0
    for num in lista:
        osszeg = osszeg + num
    return osszeg

print(f"\nÖsszeg: {osszegzes(lista)}")

def megszamlalas(lista):
    db = 0
    for szam in lista:
        if szam > 10:
            db = db + 1
    return db

print(f"10-nél nagyobbak: {megszamlalas(lista)}")

def max(lista):
    m = 0
    for i in range(1, len(lista)):
        if (lista[m] < lista[i]):
            m = i
    return m

print(f"A legnagyobb elem indexe: {max(lista)}")

def min(lista):
    m = 0
    for i in range(1, len(lista)):
        if (lista[m] > lista[i]):
            m = i
    return m

print(f"A legkisebb elem indexe: {min(lista)}")

def eldontes(lista):
    i = 0
    n = len(lista)
    while (i < n) and not(lista[i] == 13):
        i += 1
    return i < n

print(f"Van e 13: {eldontes(lista)}")

def eldontes2(lista):
    i = 0
    n = len(lista)
    while (i < n) and (lista[i] > 10):
        i += 1
    return i >= n

print(f"Mind 13 e: {eldontes2(lista)}")

def lin_keres(lista):
    i = 0
    n = len(lista)
    while (i < n) and not(lista[i] == 15):
        i += 1
    if (i < n):
        return i+1
    else:
        return -1
   
print(f"Van e benne 15: {lin_keres(lista)}.helyen")