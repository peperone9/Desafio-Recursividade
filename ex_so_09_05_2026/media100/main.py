import os

maior = -1
menor = -1
num: int 

arquivo: str 
diretorio: str 

def gravar():
    global arquivo 
    global diretorio
    arquivo = "ex38.txt"
    diretorio = "/tmp/exercicios/" 
    caminho = diretorio + arquivo 

    if(not(os.path.exists(diretorio) and os.path.isfile(arquivo))):
        os.makedirs(diretorio, exist_ok=True)
    



def maior_valor(n):
    global maior
    if(maior == -1):
        maior = n
    elif(n > maior):
        maior = n
    return maior

def menor_valor(n):
    global menor
    if(menor == -1):
        menor = n
    elif(n < menor):
        menor = n

def main():
    global num
    i = 0
    while(i < 5):
        num = int(input("numero: "))
        maior_valor(num)
        menor_valor(num)
        i += 1
    print(maior)
    print(menor)

if __name__ == "__main__":
    main()