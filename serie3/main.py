num: int 

def main():
    global num 
    num = int(input("numero: "))
    print(serie3(num))

def serie3(n: int) -> float:
    serie = 0
    if n > 1:
       seq = 1/n + 1/serie3(n - 1)
       return seq  
    else:
       return n

if __name__ == "__main__":
    main()
