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
im = Image.open('gen.png')
im.save('gen_copy.png')
im.close()
im = Image.open('gen_copy.png')

rm.seed(72)
for i in range(0, n):
    cele = [[rm.randint(0, szer_mapy), rm.randint(0, wys_mapy)] for j in range(0, dl_genu)]
    pop += [cele]
for i in range(0, n):
    print(pop[i])

# i = 0
# obr = ImageDraw.Draw(im)
# for j in range(0, dl_genu):
#     obr.ellipse([pop[i][j][0] - 10, pop[i][j][1] - 10, pop[i][j][0] + 10, pop[i][j][1] + 10], fill='red', outline='red')
# im.load()
# im.show()

def zliczanie_czarnych(popul, l_os):
    eval_l = []
    for i in range(0, l_os):
        img = Image.open('gen_copy.png')
        img_d = ImageDraw.Draw(img)
        for j in range(0, dl_genu):
            img_d.ellipse([popul[i][j][0] - 10, popul[i][j][1] - 10, popul[i][j][0] + 10, popul[i][j][1] + 10],
                          fill='red', outline='red')
        img.load()
        z = int(img.getcolors()[-1][0])
        img.close()
        eval_l += [z]
    return eval_l


czarne = zliczanie_czarnych(pop, n)
print("Zliczone czarne: \n", czarne)

r1 = rm.randint(0, n - 1)
r2 = rm.randint(0, n - 1)

os1 = pop[r1] if czarne[r1] <= czarne[r2] else pop[r2]
print("Os1: ", os1)

r1 = rm.randint(0, n - 1)
r2 = rm.randint(0, n - 1)

os2 = pop[r1] if czarne[r1] <= czarne[r2] else pop[r2]
print("Os2: ", os2)

s = [rm.randint(0, szer_mapy), rm.randint(0, wys_mapy)]
print("Srodek: ", s)

r = rm.randint(0, wys_mapy)
print("Promien: ", r)

wew_os1 = [x for x in os1 if abs(x[0] - s[0]) + abs(x[1] - s[1]) <= r]
zew_os1 = [x for x in os1 if abs(x[0] - s[0]) + abs(x[1] - s[1]) >= r]
print('wew_os2', wew_os1, 'zew_os2', zew_os1)

wew_os2 = [x for x in os2 if abs(x[0] - s[0]) + abs(x[1] - s[1]) <= r]
zew_os2 = [x for x in os2 if abs(x[0] - s[0]) + abs(x[1] - s[1]) >= r]
print('wew_os2', wew_os2, 'zew_os2', zew_os2)

nowy1 = wew_os1 + zew_os2
nowy2 = wew_os2 + zew_os1

print("Nowy1: ", nowy1)
print("Nowy2: ", nowy2)

while len(nowy1) > dl_genu:
    del nowy1[rm.randint(0, dl_genu - 1)]

while len(nowy2) < dl_genu:
    i = rm.randint(0, len(wew_os1) - 1)
    if not wew_os1[i] in nowy2:
        nowy2 += [wew_os1[i]]

print("Nowy1: ", nowy1)
print("Nowy2: ", nowy2)

def mut(gen, dl):
    gen[rm.randint(0, dl - 1)] = [rm.randint(0, 128), rm.randint(0, 128)]
    return gen


def step(gen, dl):
    i, j = rm.randint(0, dl - 1), rm.randint(0, dl - 1)

    gen[i][0] += int((rm.random() - 0.5) * 0.25 * 5)
    gen[j][0] += int((rm.random() - 0.5) * 0.25 * 5)

    if gen[i][0] < 0:
        gen[i][0] = 0
    elif gen[i][0] > 128:
        gen[i][0] = 128
    if gen[j][0] < 0:
        gen[j][0] = 0
    elif gen[j][0] < 128:
        gen[j][0] = 128
    return gen


if rm.random() < p_mute1: nowy1 = mut(nowy1, dl_genu)
if rm.random() < p_mute2: nowy1 = step(nowy1, dl_genu)
if rm.random() < p_mute1: nowy2 = mut(nowy2, dl_genu)
if rm.random() < p_mute2: nowy2 = step(nowy2, dl_genu)
potomek = []
potomek += [nowy1, nowy2]

print("Potomkowie: \n")
for i in range(len(potomek)):
    print(potomek[i])

