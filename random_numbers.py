# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Biomedical Engineering Post-Graduation Program
# Faculty of Electrical Engineering
# Virtual and Augmented Reality Group
# ------------------------------------------------------------------------------
# Author: Paulo Camargos Silva
# Contact: paulocamargoss@outlook.com
# ------------------------------------------------------------------------------
# Description: Congruential linear generator script.
# ------------------------------------------------------------------------------
# Usage: 
# Inside a python console, import the module and run the calculate_values method
#  Ex.:
#   >>> import random_numbers
#   >>> random_numbers.calculate_values()
#   g: 65   # type the g value
#   c: 23   # type the c value
#   [1, 88, 43, 18, 93, 68]
# ------------------------------------------------------------------------------

import time

def calculate_values():
    # parametros
    g = int(input('g: '))   # recebendo g
    c = int(input('c: '))   # recebendo c
    s_0 = [1]               # valor inicial
    p = 100                 # mod 2^m  

    while True:
        # valor anterior calculado
        last_value = s_0[-1]                    
        # calculando novo valor
        actual_value = (last_value * g + c) % p 
        # adicionando o valor calculado a lista
        s_0.append(actual_value)                
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
