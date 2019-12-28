import random as rm
from PIL import Image, ImageDraw

# ---------------------
n = 44
dl_genu = 15
szer_mapy = 128
wys_mapy = 128
populacja_poczatkowa = []
p_mute1 = 0.18
p_mute2 = 0.12
# ---------------------


# ---------------------
def licz_czarne(p, l_os):
    eval_l = []
    for k in range(0, l_os):
        img = Image.open('gen_copy.png')
        img_d = ImageDraw.Draw(img)
        for j in range(0, dl_genu):
            img_d.ellipse([p[k][j][0] - 10, p[k][j][1] - 10, p[k][j][0] + 10, p[k][j][1] + 10],
                          fill='red', outline='red')
        img.load()
        z = int(img.getcolors()[-1][0])
        img.close()
        eval_l += [z]
    return eval_l


def mut(gen, dl):
    gen[rm.randint(0, dl - 1)] = [rm.randint(0, 128), rm.randint(0, 128)]
    return gen


def step(gen, dl):
    t, j = rm.randint(0, dl - 1), rm.randint(0, dl - 1)
    gen[t][0] += int((rm.random() - 0.5) * 0.25 * 5)
    gen[j][0] += int((rm.random() - 0.5) * 0.25 * 5)

    if gen[t][0] < 0:
        gen[t][0] = 0
    elif gen[t][0] > 128:
        gen[t][0] = 128
    if gen[j][0] < 0:
        gen[j][0] = 0
    elif gen[j][0] < 128:
        gen[j][0] = 128
    return gen


# ------------------------
im = Image.open('gen.png')
im.save('gen_copy.png')
im.close()

rm.seed(72)
for i in range(0, n):
    cele = [[rm.randint(0, szer_mapy), rm.randint(0, wys_mapy)] for j in range(0, dl_genu)]
    populacja_poczatkowa += [cele]
for i in range(0, n):
    print(populacja_poczatkowa[i])

czarne = licz_czarne(populacja_poczatkowa, n)
populacja = populacja_poczatkowa

for pokolenie in range(0, 50):
    dzieci = []
    for i in range(0, 12):
        r1 = rm.randint(0, n - 1)
        r2 = rm.randint(0, n - 1)
        os1 = populacja[r1] if czarne[r1] <= czarne[r2] else populacja[r2]

        r3 = rm.randint(0, n - 1)
        r4 = rm.randint(0, n - 1)
        os2 = populacja[r3] if czarne[r3] <= czarne[r4] else populacja[r4]

        s = [rm.randint(0, szer_mapy), rm.randint(0, wys_mapy)]
        r = rm.randint(0, wys_mapy)

        wew_os1 = [x for x in os1 if abs(x[0] - s[0]) + abs(x[1] - s[1]) <= r]
        zew_os1 = [x for x in os1 if abs(x[0] - s[0]) + abs(x[1] - s[1]) >= r]

        wew_os2 = [x for x in os2 if abs(x[0] - s[0]) + abs(x[1] - s[1]) <= r]
        zew_os2 = [x for x in os2 if abs(x[0] - s[0]) + abs(x[1] - s[1]) >= r]

        nowy1 = wew_os1 + zew_os2
        nowy2 = wew_os2 + zew_os1

        while len(nowy1) > dl_genu:
            del nowy1[rm.randint(0, dl_genu - 1)]

        while len(nowy2) < dl_genu:
            i = rm.randint(0, len(wew_os1) - 1)
            if not wew_os1[i] in nowy2:
                nowy2 += [wew_os1[i]]

        while len(nowy2) > dl_genu:
            del nowy2[rm.randint(0, dl_genu - 1)]

        while len(nowy1) < dl_genu:
            i = rm.randint(0, len(wew_os2) - 1)
            if not wew_os2[i] in nowy1:
                nowy1 += [wew_os2[i]]

        if rm.random() < p_mute1: nowy1 = mut(nowy1, dl_genu)
        if rm.random() < p_mute2: nowy1 = step(nowy1, dl_genu)
        if rm.random() < p_mute1: nowy2 = mut(nowy2, dl_genu)
        if rm.random() < p_mute2: nowy2 = step(nowy2, dl_genu)

        dzieci += [nowy1, nowy2]

    nowa_populacja = populacja + dzieci

    najlepsi = []
    while len(najlepsi) < n:
        minimum = min(czarne)
        indeks = czarne.index(minimum)
        najlepsi.append(nowa_populacja[indeks])
        nowa_populacja.remove(nowa_populacja[indeks])
        czarne.remove(czarne[indeks])
    populacja = najlepsi
    czarne = licz_czarne(populacja, len(populacja))
    najmniej_czarnych = min(czarne)
    indeks = czarne.index(najmniej_czarnych)

    im = Image.open('gen_copy.png')
    obr = ImageDraw.Draw(im)
    for j in range(0, dl_genu):
        obr.ellipse([populacja[indeks][j][0] - 10, populacja[indeks][j][1] - 10, populacja[indeks][j][0]
                     + 10, populacja[indeks][j][1] + 10], fill='red', outline='red')
    im.save('gen%d.png' % pokolenie)
    im.close()
