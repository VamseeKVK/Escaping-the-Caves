import numpy as np
from pyfinite import ffield
import galois

F = ffield.FField(7, gen=0x83, useLUT=-1)


def rum(idk, banunu):

    if banunu == 0:
        return 1

    elif banunu == 1:
        return idk

    elif banunu % 2 == 0:
        bhai = rum(idk, banunu // 2)
        return F.Multiply(bhai, bhai)

    else:
        bhai = rum(idk, banunu // 2)
        return F.Multiply(F.Multiply(bhai, bhai), idk)


def kya(lmt, khtm):
    uttar = [0] * 8
    for i in range(8):
        temp = []
        gun = [F.Multiply(lmt[i][j], khtm[i]) for j in range(8)]
        for k in range(8):
            temp.append(np.bitwise_xor(uttar[k], gun[k]))
        uttar = temp
    return uttar


# In[2]:


def hojayega(cipher):
    sedha = ""
    for i in range(0, len(cipher), 2):
        sedha += chr(16 * (ord(cipher[i:i + 2][0]) - ord('f')) + ord(cipher[i:i + 2][1]) - ord('f'))
    return sedha


# In[3]:


vandei = [[] for i in range(8)]
ivande = [[[] for i in range(8)] for j in range(8)]
input_file = open('plaintexts.txt', 'r')
output_file = open('ciphertexts.txt', 'r')
input = (input_file.readlines()[0]).strip().split(' ')
output = output_file.readlines()

isi = []
for khtm in input:
    isi.append(hojayega(khtm)[0])
# print(isi)
# print(len(output))

osi = []
for i in range(len(output)):
    x = []
    for khtm in output[i].strip().split(' '):
        x.append(hojayega(khtm)[i])
    osi.append(x)

vande = [[] for _ in range(8)]
mat = [[[] for _ in range(8)] for _ in range(8)]
for k in range(8):
    for i in range(1, 127):
        for j in range(1, 128):
            flag = True
            for m in range(128):
                if ord(osi[k][m]) != rum(F.Multiply(rum(F.Multiply(rum(ord(isi[m]), i), j), i), j), i):
                    flag = False
                    break
            if flag:
                vande[k].append(i)
                mat[k][k].append(j)

print("Possible diagonal values: \n")
print(mat)
print("\n\nPossible rumts: \n")
print(vande)


osi = []
for i in range(len(output) - 1):
    x = []
    for khtm in output[i].strip().split(' '):
        x.append(hojayega(khtm)[i + 1])
    osi.append(x)

for ind in range(7):
    for i in range(1, 128):
        for p1, e1 in zip(vande[ind + 1], mat[ind + 1][ind + 1]):
            for p2, e2 in zip(vande[ind], mat[ind][ind]):
                flag = True
                for k in range(128):
                    x1 = F.Multiply(rum(F.Multiply(rum(ord(isi[k]), p2), e2), p2), i)
                    x2 = F.Multiply(rum(F.Multiply(rum(ord(isi[k]), p2), i), p1), e1)
                    c1 = np.bitwise_xor(x1, x2)
                    if (ord(osi[ind][k]) != rum(c1, p1)):
                        flag = False
                        break
                if flag:
                    vande[ind + 1] = [p1]
                    mat[ind + 1][ind + 1] = [e1]
                    vande[ind] = [p2]
                    mat[ind][ind] = [e2]
                    mat[ind][ind + 1] = [i]
print('\n\n===========================\n\n')
print("Linear Transformation Matrix A values: \n")
print(mat)
print("\n\nrumt Vector E values : \n")
print(vande)



# In[4]:


def kyaa(khtm, lin_mat, exp_vec):
    khtm = [ord(m) for m in khtm]
    thmt = [rum(khtm[i], exp_vec[i]) for i in range(8)]
    thmt = kya(lin_mat, thmt)
    thmt = [rum(thmt[i], exp_vec[i]) for i in range(8)]
    thmt = kya(lin_mat, thmt)
    thmt = [rum(thmt[i], exp_vec[i]) for i in range(8)]
    return thmt



input_file = open('plaintexts.txt', 'r')
output_file = open('ciphertexts.txt', 'r')
input = input_file.readlines()
output = output_file.readlines()

isi = []
for i in range(len(input)):
    x = []
    for khtm in input[i].strip().split(' '):
        x.append(hojayega(khtm))
    isi.append(x)

osi = []
for i in range(len(output)):
    x = []
    for khtm in output[i].strip().split(' '):
        x.append(hojayega(khtm))
    osi.append(x)

for indexex in range(0, 6):
    bacha = indexex + 2

    episode = [e[0] for e in vande]
    onclasttime = np.zeros((8, 8), dtype=int)

    for i in range(8):
        for j in range(8):
            if len(mat[i][j]) != 0:
                onclasttime[i][j] = mat[i][j][0]
            else:
                onclasttime[i][j] = 0

    for index in range(8):
        if index > (7 - bacha):
            continue

        for i in range(1, 128):
            onclasttime[index][index + bacha] = i
            flag = True
            for bus, outs in zip(isi[index], osi[index]):
                x1 = kyaa(bus, onclasttime, episode)[index + bacha]
                x2 = outs[index + bacha]
                if x1 != ord(x2):
                    flag = False
                    break
            if flag:
                mat[index][index + bacha] = [i]

A = np.zeros((8, 8), dtype=int)

for i in range(0, 8):
    for j in range(0, 8):
        if len(mat[j][i]) != 0:
            A[i][j] = mat[j][i][0]

E = episode

print('\n\nLinear Transformation Matrix:\n', A)
print('\n\n')
print('rumt Vector:\n', E)


# In[5]:


tuhai = np.zeros((128, 128), dtype=int)

for idk in range(0, 128):
    temp = 1
    for banunu in range(1, 127):
        thmtult = F.Multiply(temp, idk)
        tuhai[banunu][thmtult] = idk
        temp = thmtult

GF = galois.GF(2 ** 7)
A = GF(A)
hua = np.linalg.inv(A)


# In[6]:


psda = "lhisiniokohpkrmsiifqgfglhrikgqfq"  # Encrypted password
GF = galois.GF(2 ** 7)


def losteyes(bsss, E):
    return [tuhai[E[i]][bsss[i]] for i in range(8)]


def hehe(bsss, A):
    bsss = GF(bsss)
    A = GF(A)
    return np.matmul(A, bsss)


dp = ""
for i in range(0, 2):
    chachu = psda[16 * i:16 * (i + 1)]
    cb = []
    for j in range(0, 15, 2):
        cb += [(ord(chachu[j]) - ord('f')) * 16 + (ord(chachu[j + 1]) - ord('f'))]
    kyaa = losteyes(hehe(losteyes(hehe(losteyes(cb, E), hua), E), hua), E)
    for ch in kyaa:
        dp += chr(ch)

print("\n\npassword is", dp)