def is_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

def main():
    num = int(input("Informe um número: "))
    if is_fibonacci(num):
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
