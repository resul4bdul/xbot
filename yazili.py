import json
import random
from difflib import get_close_matches as yaxin_cavab_tap

ad = input("Söhbətdə istifadə etmək istəyiniz adı daxil edin: ")

def json_yüklə():
    try:
        with open('db.json', 'r', encoding='utf-8') as fayl:
            return json.load(fayl).get("verilənlər", {})
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def json_yaz(verilənlər):
    with open('db.json', 'w', encoding='utf-8') as fayl:
        json.dump({"verilənlər": verilənlər}, fayl, indent=2, ensure_ascii=False)

def uyğun_cavab_tap(sual, suallar):
    uyğunlar = yaxin_cavab_tap(sual, suallar, n=1, cutoff=0.6)
    return uyğunlar[0] if uyğunlar else None

def cavab_tap(sual, database):
    yakın_sual = uyğun_cavab_tap(sual, database.keys())
    if yakın_sual:
        return random.choice(database[yakın_sual])
    else:
        return "XBot: Bu sualın cavabını bilmirəm. Mənə öyrədə bilərsiniz?"

def x_bot():
    database = json_yüklə()

    while True:
        sual = input(f'{ad}: ')
        if sual == 'çıx':
            break
        
        veriləcək_cavab = cavab_tap(sual, database)
        print("X-Bot:", veriləcək_cavab)

        if veriləcək_cavab.startswith("XBot: Bu sualın cavabını bilmirəm. Mənə öyrədə bilərsiniz?"):
            cavab_say = input("Öyrətmək istəmirsinizsə 'keç' yazın, öyrətmək üçün isə neçə dənə cavab əlavə edəcəyinizi rəqəmlə yazın: ")
            if cavab_say  != 'keç':
                cavab_say  = int(cavab_say)
                if cavab_say  > 0:
                    yeni_cavablar = []
                    for _ in range(cavab_say):
                        yeni_cavab = input("Yeni cavabı yazın: ")
                        yeni_cavablar.append(yeni_cavab)
                    if sual not in database:
                        database[sual] = []
                    database[sual].extend(yeni_cavablar)
                    json_yaz(database)
                    print("X-Bot: Təşəkkür edirəm, yeni bir şey öyrəndim.")

if __name__ == '__main__':
    x_bot()

