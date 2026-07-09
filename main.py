# se encarga de contener el objeto text

from analyzer.text_analizer import (
    count_words,
    count_sentences,
    count_characters,
    count_paragraphs,
    longest_word,
    longest_sentences,
    longest_paragraphs
)

text = """
        Hola mundo. Esta es un frase de prueba escrita directamente en el código de programacion.

        Esta es una prueba de nuestro analizador.        

        Podemos seguir agregando palabras para probar a nuestro analizador. """

print(f"Palabras: ", count_words(text))
print(f"Caracteres: ", count_characters(text))
print(f"Oraciones: ", count_sentences(text))
print(f"Palabra más larga: ", longest_word(text))
print(f"Parrafos: ", count_paragraphs(text))
print(f"Parrafo más largo: ", longest_paragraphs(text))
print(f"Oración más larga: ", longest_sentences(text))


# tiene algunos puntos a mejorar, ya que la palabra más larga cuenta los carácteres y es "programación."
# el punto esta sumando un caracter a la palabra por lo tanto se vuelve la más larga, lo cual puede generar errores.
# los testeo funcionan bien, tal cual lo generamos. 