Z = ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
texts = []
for X in range(8):
    temporary = []
    for i in range(8):
        for j in range(16):
            st = 'ff'*X + Z[i]+Z[j] + 'ff'*(8-1-X)
            temporary.append(st)
    texts.append(temporary)

file = open('plaintexts.txt','w')
for i in texts:
    st = ' '.join(i) + '\n'
    file.write(st)
file.close()