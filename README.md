# [Telefonszám ellenőrző](https://github.com/kovacs-balazs/gyvakk-telefonszam)

A szoftver a felhasználó által megadott telefonszámot ellenőrzi le a különböző szempontok alapján. Először az országazonosító előtagot veszi figyelembe először, ez alapján meghatározza, hogy a telefonszám pontosan melyik országhoz tartozik. Forrás hiányában a program nem tudja meghatározni a külföldi országok telefonszolgáltatóját. Másodszor magyar telefonszám esetén a telefonszám szolgáltatója meghatározásra, majd ez egy szótárba lementésre kerül. Amennyiben a telefonszám magyar, de a szolgáltatóját nem lehetett meghatározni, akkor a program 'Unknown' névvel fogja tovább kezelni a telefonszámot. A program bementként elfogad .txt kiterjesztésű fájlt, illetve felhasználó által beírt telefonszámot is. A bemenet megadása mind grafikus, mind konzolos módon támogatott. 

**Nemzetközi telefonszámok listája:**
https://gist.github.com/ally-commits/9073ff23fc7f96fab1290fdec22775bc

**Magyarországi szolgáltatok és azok előtagjainak táblázata:**
| Szolgáltató | Előtag |
| :---: | :---: |
| [Yettel](https://www.yettel.hu/) | 20 |
| [Telekom](https://www.telekom.hu/) | 30 |
| [Digi](https://digi.hu/) | 50 |
| [Vodafone](https://www.vodafone.hu/) | 70 |

## Használat

### Grafikus Felhasználói Felület
#### Indítóparancs:
```
python main.py
```
</br>
A szoftver elindítása után a megnyíló grafikus felületben két féle módon lehet megadni a bemeneti telefonszámot/telefonszámokat. A 'Kiválasztás' gombra kattintva a megnyíló ablakban lehet kiválasztani az ellenőrizendő .txt fájlt, vagy fájlokat. A másik lehetőség, hogy a 'Telefonszám' nevű szövegmezőbe írt telefonszámot az 'Ellenőrzés' gombra kattintva leellenőrizhető, illetve mentésre kerül. A 'Listázás' gombbal kilistázásra kerülnek a szolgáltatók és előfordulásaik.

### Konzol
#### Indítóparancs:
```
python main.py --nogui
```
</br>
A szoftver elindítása után először meg kell adni az ellenőrizni kívánt telefonszámot. A program a telefonszám információit a konzolba kiírja, majd érvényes telefonszám esetén a szótárba felvenni. Továbbiakban a bemenetekhez olyan parancsokat írhatóak, amelyek a megadott eseménysort fogják végrehajtani.

**Bemenetekhez írható parancsok:**

| Parancs | Esemény |
| :-------: | :-------: |
| `exit` | Program megállítása |
| `list` | Szolgáltatók kilistázása |

## Beállítások

  Az indítóparancs utáni argumentumok segítségével egyszerűen konfigurálhatóak a szoftver beállításai. Több argumentum is megadható egyszerre az indítóparancsban. Az argumentumok sorrendje felcserélhető. A kerekítés kikapcsolása felülírja a kerekítési értéket, így nem ajánlott egyszerre mindkét argumentum használata.

| Argumentum | Beállítás | Példa |
| :---: | :---: | :---: |
| `--nogui` | Konzol használata | `python main.py --nogui` |
| `--autogenerate` | Telefonszámok generálása | `python main.py --autogenerate` |
| `--file <file név>` | Fájl kiválasztása | `python main.py --file telefonszamok.txt` |

**További példák:**
```
python main.py --nogui --autogenerate --file telefonszamok.txt
python main.py --nogui --file telefonszamok.txt
python main.py --nogui --autogenerate
python main.py --file telefonszamok.txt
python main.py --autogenerate
```

