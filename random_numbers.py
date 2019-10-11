import time

def calculate_values():
    # parametros
    g = int(input('g: ')) # recebendo g
    c = int(input('c: ')) # recebendo c
    s_0 = [1] # valor inicial
    p = 100   # mod 2^m  

    while True:
        last_value = s_0[-1] # valor anterior calculado
        actual_value = (last_value * g + c) % p # calculando novo valor
        s_0.append(actual_value) # adicionando o valor calculado a lista

        # esquema para verificar se esta repetindo 
        values = s_0[:len(s_0)-2]   
        if actual_value in values:
            index = values.index(actual_value)
            if values[index-1] == last_value:
                s_0.pop()
                s_0.pop()
                break

    print(s_0)
    print(f'Foram gerados: {len(s_0)} elementos diferentes')


if __name__ == "__main__":
    calculate_values()
