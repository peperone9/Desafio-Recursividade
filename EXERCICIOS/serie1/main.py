
def main():
    print(serie(100))

def serie(n):
    if n >= 1:
        seq = serie(n - 1) + n
        return seq
    else:
        return n

if __name__ == "__main__":
    main()