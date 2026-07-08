# se encarga de contener el objeto text

from analyzer.text_analizer import (
    count_words,
    count_sentences,
    count_characters,
    longest_word
)

text = "Hola mundo, esta es un frase de prueba escrita directamente en el código de programacion"

print(f"Palabras: ", count_words(text))
print(f"Caracteres: ", count_characters(text))
print(f"Oraciones: ", count_sentences(text))
print(f"Palabra más larga: ", longest_word(text))

