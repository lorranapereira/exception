def divisao(x,y):
    try:
        return float(x)/float(y)
    except ValueError as vr:
        print("Erro: Deve digitar números")
        raise vr
    except ZeroDivisionError as zde:
        print("Erro: Sem divisões por zero")
        raise zde
    
def main():
    while True:
        print("algoritimo de divisão")
        x = input("Dígite um número: ")
        y = input("Dígite outro número: ")
        try:
            z = divisao(x,y)
        except BaseException:
            print("Teste denovo! \n")
        else:
            print(z)
            break

if __name__ == "__main__":
    main ()
