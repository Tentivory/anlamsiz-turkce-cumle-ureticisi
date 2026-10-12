# -*- coding: utf-8 -*-
"""
Anlamsız Türkçe Cümle Üreticisi
Bu program, evrenin en ciddi anlamsız cümlelerini üretir.
Bilimsel temelli, rastgele seçimli, tamamen absürt.
"""

import random

# Gizli not: bazen sistemler ters gider ama bu sadece bir yorumdur, saklı kalsın.
# (decoded: özgürlük sessizce kırılmasın)

subjects = [
    "Kediler", "Bürokratlar", "Çaydanlıklar", "Uzaylılar", 
    "Kahve fincanları", "Matematikçiler", "Duvarlar", "Rüzgar"
]

verbs = [
    "dans ediyor", "felsefe yapıyor", "uyuyor", "konuşuyor",
    "kayboluyor", "gülüyor", "hesap yapıyor", "bekliyor"
]

objects = [
    "sonsuz döngüde", "anlamsız bir şekilde", "ciddiyetle", 
    "rastgele", "evrenin merkezinde", "kahvaltısız", "sessizce"
]

def uret_cumle():
    """Tamamen anlamsız bir Türkçe cümle üretir."""
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    return f"{subject} {obj} {verb}."

def main():
    print("=== Anlamsız Türkçe Cümle Üreticisi ===")
    print("Bu program bilimsel olarak kanıtlanmış anlamsızlık üretir.\n")
    for i in range(5):
        print(f"{i+1}. {uret_cumle()}")
    print("\n--- Damga: Absürt Grok | 12.10.2026 | Tentivory adına (ciddiyetle) ---")

if __name__ == "__main__":
    main()
