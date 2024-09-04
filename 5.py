def inverter_string(s):
    inverso = ""
    for char in s:
        inverso = char + inverso
    return inverso

def main():
    s = input("Informe a string: ")
    print("String invertida:", inverter_string(s))

if __name__ == "__main__":
    main()
