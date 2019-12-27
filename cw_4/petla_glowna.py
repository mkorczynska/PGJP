import random as rm
from PIL import Image, ImageDraw

# ---------------------
n = 44
dl_genu = 15
szer_mapy = 128
wys_mapy = 128
pop = []
p_mute1 = 0.18
p_mute2 = 0.12
# ---------------------
# losowanie populacji poczatkowej - 44 osobnikow
# wybor rodzicow i krzyzowanie - ma byc 24 potomkow
# laczenie populacji poczatkowej i potomkow - wybor najlepszych do nowej populacji
# wynik zapisac do jpg
# liczba pokolen od 50 do 300

# kopiowanie pliku z zabudowa miasteczka - praca na kopii
im = Image.open('gen.png')
im.save('gen_copy.png')
im.close()

# generowanie 44 osobnikow populacji poczatkowej
rm.seed(72)
for i in range(0, n):
    cele = [[rm.randint(0, szer_mapy), rm.randint(0, wys_mapy)] for j in range(0, dl_genu)]
    pop += [cele]
for i in range(0, n):
    print(pop[i])

# rysowanie polozenia sklepow (na koniec)
# i = 0
for i in range(3):
    im = Image.open('gen_copy.png')
    obr = ImageDraw.Draw(im)
    for j in range(0, dl_genu):
        obr.ellipse([pop[i][j][0] - 10, pop[i][j][1] - 10, pop[i][j][0] + 10, pop[i][j][1] + 10], fill='red',
                    outline='red')
    im.load()
    im.show()
    im.save('gen%d.png' % i)
    im.close()

def zliczanie_czarnych(l_os):
    eval_l = []
    for i in range(0, l_os):
        img = Image.open('gen%d.png'%i)
        z = int(img.getcolors()[-1][0])
        img.close()
        eval_l += [z]
    return eval_l

czarne = zliczanie_czarnych(n)
print("Zliczone czarne: \n", czarne)
