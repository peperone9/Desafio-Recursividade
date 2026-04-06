
n: int

def main():
    global n
    n = int(input("Fatorial: "))
    print(recfat(n))


def recfat(n):

    if(n > 1):
        fat = recfat(n - 1) * n 
        return fat
    else:
        return n
    
if __name__ == "__main__":
    main()