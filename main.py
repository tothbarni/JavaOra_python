import random

def dobas():
    return random.randint(2, 12)

def dobas_eredmenyek(max_csillag, szam):
    eredmenyek = [0] * 13
    
    for i in range(szam):
        dobott_ertek = dobas()
        eredmenyek[dobott_ertek] += 1
    
    max_elofordulas = max(eredmenyek)
    
    for ertek in range(2, 13):
        if eredmenyek[ertek] > 0:
            db = int(eredmenyek[ertek] / max_elofordulas * max_csillag)
            print(f"{ertek:2}   {'*' * db:{int(max_csillag)}}  ({eredmenyek[ertek]}db)")

dobas_eredmenyek(35, 50)