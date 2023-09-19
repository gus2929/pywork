import getchar # getchar.py에 있는 class Getchar를 가져온거임

kb = getchar.Getchar()  # import getchar로 써주면 -> getchar.Getchar()로 써줘야 한다
key = ''  # 변수 만듦
    
while key!='Q':
    
    key = kb.getch()
    if key != '':
        print(key)
    else:
        pass
        
