ll = [x for x in open('input25.txt').read().strip().split('\n')]
cardPublicKey = int(ll[0])
doorPublicKey = int(ll[1])
subjectNumber = 7
cardSecret=0
doorSecret=0

value = 1
while value != cardPublicKey:
    value *= subjectNumber
    value = value%20201227
    cardSecret+=1

value = 1
while value != doorPublicKey:
    value *= subjectNumber
    value = value%20201227
    doorSecret+=1

value = 1
for i in range(cardSecret):
    value *= doorPublicKey
    value = value % 20201227

print(value)
