print()
print("início")
i = 0
while(i<10):
    i += 1
    if(i%2==0):
        continue
    if(i>5):
        break
    print(i)
# Quando o break é executado automáticamente todo laço de repetição while é interrompido, juntamente o else também é interrompido
else:
    print("else")
print("fim")
print()