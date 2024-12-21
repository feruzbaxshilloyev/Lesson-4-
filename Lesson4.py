"""
def masala14(k):
    a, b = True, 1
    n, m = [], []
    while a:
        c = int(input(f"{b}-sonni kiriting: "))
        if c != 0:
            n.append(c)
            b += 1
        else:
            a = False

    for i in n:
        if i < k:
            m.append(i)
    return m
print(masala14(6))


def masala15(k):
    a, b = True, 1
    n, m = [], []
    while a:
        c = int(input(f"{b}-sonni kiriting: "))
        if c != 0:
            n.append(c)
            b += 1
        else:
            a = False

    for i in n:
        if i > k:
            return i
    return 0

print(masala15(4))



def masala16(k):
    a, b = True, 1
    n, m = [], []
    while a:
        c = int(input(f"{b}-sonni kiriting: "))
        if c != 0:
            n.append(c)
            b += 1
        else:
            a = False

    for i in n[::-1]:
        if i > k:
            return i
    return 0

print(masala16(4))



def masala17(B):
    a, b = True, 1
    n, m = [], []
    while a:
        c = int(input(f"{b}-sonni kiriting: "))
        if c != 0:
            n.append(c)
            b += 1
        else:
            a = False
    n.append(B)
    return n

print(masala17(18))


def masala18():
    a, b = True, 1
    n, m = [], []
    while a:
        c = int(input(f"{b}-sonni kiriting: "))
        if c != 0:
            n.append(c)
            b += 1
        else:
            a = False
    n.sort()
    for i in n:
        if i not in m:
            m.append(i)
    return m

print(masala18())
"""

def masala19():
    a, b = True, 1
    n, m = [], []
    while a:
        c = int(input(f"{b}-sonni kiriting: "))
        if c != 0:
            n.append(c)
            b += 1
        else:
            a = False

    for i in range(1, len(n)-1):
        if n[i] < n[i - 1]:
            m.append(n[i])
    return f"chap qo'shnisidan kichiklar {m} ularning soni {len(m)} ta"

print(masala19())
"""
import uuid

class Royxat:
    def __init__(self):
        self.ovqatlar = []

    def add_ovqat(self, ovqat, narxi):
        self.ovqatlar.append({ovqat: narxi})
        return f"'{ovqat}' menyuga qo'shildi, narxi: {narxi}"

    def menu_korsatish(self):
        print("Bizda mavjud ovqatlar: ")
        for i in self.ovqatlar:
            for ovqat, narx in i.items():
                print(f"{ovqat}: {narx} so'm)


class Buyurtma:
    def __init__(self):
        self.buyurtma_id = str(uuid.uuid4())[:6]
        self.tanlangan_ovqatlar = []
        self.total_price = 0

    def add_ovqat(self, ovqat):
        self.tanlangan_ovqatlar.append(ovqat)
        return f"'{ovqat}' buyurtmaga qo'shildi."

    def buyurtmani_korsatish(self):
        print(f"Buyurtma raqami: {self.buyurtma_id}")
        print("Tanlangan ovqatlar:")
        print(", ".join(self.tanlangan_ovqatlar))

class Mijoz:
    def __init__(self, ism, raqam):
        self.ism = ism
        self.raqam = raqam

    def __str__(self):
        return f"Mijoz: {self.ism}, Telefon: {self.raqam}"

class Yetkazuvchi:
    def __init__(self, ism, mashina_raqami):
        self.ism = ism
        self.mashina_raqami = mashina_raqami

    def __str__(self):
        return f"Yetkazib beruvchi: {self.ism}, Mashina raqami: {self.mashina_raqami}"

menu = Royxat()
buyurtma = Buyurtma()
mijoz = Mijoz('Feruz', '+998912345678')
yetkazuvchi = Yetkazuvchi('Shoxrux', '80|A 000 AA')

print(menu.add_ovqat("Shashlik", 15000))
print(menu.add_ovqat("Lag'mon", 18000))
print(menu.add_ovqat("Osh", 12000))
menu.menu_korsatish()

print(buyurtma.add_ovqat("Shashlik"))
print(buyurtma.add_ovqat("Lag'mon"))
buyurtma.buyurtmani_korsatish()

print(buyurtma.add_ovqat('Osh'))
buyurtma.buyurtmani_korsatish()
"""