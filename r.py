 #黨名不能取做module同名

import random
r = random.randint(1,10)
while True:
    num = input('請猜數字')
    num = int(num)
    if num == r:
        print('恭喜你猜對了')
        break
    elif num > r :
        print('比答案大')
    elif num < r :
        print('比答案小')
    