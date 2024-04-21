def ordenar_por_tamanho(strings):
    return sorted(strings, key=lambda x: (len(x), strings.index(x)))

def main():
    N = int(input())  
    for _ in range(N):
        conjunto_strings = input().split()  
        conjunto_ordenado = ordenar_por_tamanho(conjunto_strings)  
        print(*conjunto_ordenado) 

if __name__ == "__main__":
    main()
