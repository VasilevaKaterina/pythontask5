def transfer(n,sissch):
    s= " "
    num=n
    al="ABCDEF"
    while num>0:
        c=num % sissch
        if c<10:
                s = str(c) + s
        else: 
                s = al[c-10] + s
        num //= sissch
    return print ('вывод ', s)

def num():
    while True:
        system=int(input("введите целевую систему счисления(двоичная или восьмеричная): "))
        if system!=8 and system!=2:
            print("вы ввели некорректную систему счисления! повторите ввод!(двоичная или восьмеричная)")
        if system==2 or system==8:
            break
    return system

num_1=int(input("введите целое положительное число: "))
sys=num()
transfer(num_1,sys)
