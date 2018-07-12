""" 5.1 COMPUTING THE PARITY OF A WORD """


from collections import Counter


word = list(map(int,input().split(' ')))
count = 0
for i in word:
    if i is 1:
        count += 1
    else:
        pass
if count % 2 != 0:
    print('parity is 1')
else:
    print('parity is even')

""" using Collections counter """
