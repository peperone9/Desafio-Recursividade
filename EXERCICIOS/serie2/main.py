
limite: int = 0

def serie2(n: int) -> int:
    if(n >= 1):
        seq = n + serie2(n - 1)
        return seq
    else:
        return n

def main():
    global limite 
    limite = int(input("numero: "))
    print(serie2(limite))

if __name__ == "__main__":
    main()