import random

range(5) #從零開始。結為不包含
range(3)
#90%以上寫for i in  range用來產生的for loop是為了讓他的內容重複執行某個固定次數
for i in range(100):
    #print(i)
    r = random.randint(1,1000)
    print('這是第', i+1, '次產生隨機數: ', r)  #逗點後面就要空格表示比較好
    
range(8, 10) 
range(2, 20 ,3) #2是開始值，20是結尾值，3是step遞增值
range(10, 3, -2)
    
for i in range(100):
    print("hi") 
    