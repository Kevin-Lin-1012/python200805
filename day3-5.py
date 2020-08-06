dic={}
print('歡迎進入系統')
while True:
    print('1.建立詞彙')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗學習成果')
    print('6.離開') 
    
    sel=int(input('輸入選項'))
    if sel==6:
        break
    elif sel<1 or sel>6:
        print('輸入錯誤')
    
    if sel==1:
        while True:
            a=input('輸入新單字\(按0可離開)')
            if a=='0':
                break
            b=input('輸入其中文')
            dic[a]=b
            print()
    elif sel==2:
        print(dic)
        print()
    elif sel==3:
        while True:
            c=input('輸入欲查之英文單字\(按0可跳出)')
            if c=='0':
                break
            if c in dic:
                print(dic[c])
            else:
                print('無此單字')
                print()
    elif sel==4:
        while True:
            d=input('輸入欲查之中文單字\(按0可離開)')
            for k,v in dic.items():
                if v==d:
                    print(k)
                    print()
    
                
        
      
    
    
