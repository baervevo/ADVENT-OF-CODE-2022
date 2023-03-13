with open('day_20.txt', 'r') as f:
    encrypted = [int(x.rstrip()) * 811589153 for x in f.readlines()]

indexes = [i for i in range(len(encrypted))]

for x in range(10):
    for i, value in enumerate(encrypted):
        new_index = (indexes.index(i) + value) % (len(indexes) - 1)
        indexes.remove(i)
        indexes.insert(new_index , i)
    
decrypted = [encrypted[i] for i in indexes]
zero_index = decrypted.index(0)

a = decrypted[((1000+zero_index) % len(encrypted))]
b = decrypted[((2000+zero_index) % len(encrypted))]
c = decrypted[((3000+zero_index) % len(encrypted))]

print(sum((a,b,c)))