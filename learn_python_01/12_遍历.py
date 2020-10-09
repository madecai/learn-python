print('==============================遍历列表1')
tars = ['div', 'br', 'span', 'h1']
i = 0
while i < len(tars) :
    print(tars[i], end='、')
    i += 1
print('==============================遍历列表2')
for tar in tars :
    print(tar, end='、')

print('==============================遍历str')
for item in 'abcde' :
    print(item, end='、')

print('==============================遍历range')   
for item in range(5) :
    print(item, end='、')
print()

print('==============================遍历字典，见10_字典.py')