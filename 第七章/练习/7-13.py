from random import randint, randrange

tmp = []
for i in range(0, randrange(1, 11)):
    tmp.append(randint(0, 9))
    A = set(tmp)

tmp = []
for j in range(0, randrange(1, 11)):
    tmp.append(randint(0, 9))
    B = set(tmp)

print(A)
print(B)
for m in range(0, 3):
    answer = input('Please input your answer of A&B:')
    answer = answer.replace(' ', '')
    a = set()
    for n in answer:
        a.add(int(n))
    if a == A&B:
        print('Well DOWN!')
        break
    else:
        print('Wrong anser!')
        if m == 2:
            print('The right answer is:')
            print(A&B)
        continue

# print(A|B)
# print(A&B)