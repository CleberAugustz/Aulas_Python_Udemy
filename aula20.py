'''print('antes de entrar no laço')
for item in range(10):
    print(item)
    if(item==6):
        print('A condição estabelicida retornou true')
        break
print('Depois de ter entrado no laço')'''
print()
print('Inicio')
i = 0
while(i<10):
    i += 1
    if(i%2==0):
        continue
    if(i>5):
        break
    print(i)
else:
    print('else')
print('Fim')
print()