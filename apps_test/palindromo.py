def reverse(text): 
    al_reves = ""
    for char in text:
        al_reves = char + al_reves
    return al_reves.upper()

def palindromo(texto):
    texto_sin_espacio = texto.replace(" ", "")
    texto_in_reverse = reverse(texto_sin_espacio)
    print(texto_in_reverse) 
    
palindromo("Amo la Paloma") 