#automiticly converts the list of toki pona words into lowercase and ordered by the lenght of the word

text = """ 
A
AKESI
ALA
ALASA
ALE
ANPA
ANTE
ANU
AWEN
E
EN
ESUN
IJO
IKE
ILO
INSA
JAKI
JAN
JELO
JO
KALA
KALAMA
KAMA
KASI
KEN
KEPEKEN
KILI
KIWEN
KO
KON
KULE
KULUPU
KUTE
LA
LAPE
LASO
LAWA
LEN
LETE
LI
LILI
LINJA
LIPU
LOJE
LON
LUKA
LUKIN
LUPA
MA
MAMA
MANI
MELI
MI
MIJE
MOKU
MOLI
MONSI
MU
MUN
MUSI
MUTE
NANPA
NASA
NASIN
NENA
NI
NIMI
NOKA
O
OLIN
ONA
OPEN
PAKALA
PALI
PALISA
PAN
PANA
PI
PILIN
PIMEJA
PINI
PIPI
POKA
POKI
PONA
PU
SAMA
SELI
SELO
SEME
SEWI
SIJELO
SIKE
SIN
SINA
SINPIN
SITELEN
SONA
SOWELI
SULI
SUNO
SUPA
SUWI
TAN
TASO
TAWA
TELO
TENPO
TOKI
TOMO
TU
UNPA
UTA
UTALA
WALO
WAN
WASO
WAWA
WEKA
WILE
NAMAKO
KIN
OKO
KIPISI
LEKO
MONSUTA
TONSI
JASIMA
KIJETESANTAKALU
SOKO
MESO
EPIKU
KOKOSILA
LANPAN
N
MISIKEKE
KU
"""
def sort(arr):
   
    # Sorting using sorted function
    # providing key as len
    r = (sorted(arr, key=len))
    return r
    
 

text = text.lower()
text = text.split()
text = sort(text)
text = text[::-1]
open("list","w").write(str(text))