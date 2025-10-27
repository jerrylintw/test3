a,b= map(int,input().split())
key="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
word=""
if a==0 or b==0:
    print("0")
elif b < 2 or b > 36:
        print("Error") 
else:
     while a>0:
        rem=a%b
        word=key[rem]+word
        #key[rem]+word是把余数对应的字符加到word的前面
        a=a//b
        #a=a//b是更新a的值
print(word)
    
    

        
    
