def shop(Input):
    inv = [0,0]
    num = 30
    while Input != 'q':
        print("Welcome to the shop you have", num,"coins")
        Input = input("you can get a (p)otion for $5 or some (f)ood for $3 and to quit press q")
        if Input == 'p':
            if num >=5:
                inv[0] += 1
                num -= 5
                print(inv)
            else:
                print(inv)
                print("you dont have enough money")
        elif Input == 'f':
            if num >=3:
                inv[1] += 1
                num -= 3
                print(inv)
            else:
                print(inv)
                print("you dont have enough money")

            
shop('j')
