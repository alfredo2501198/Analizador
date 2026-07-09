import sys
import os
# Agregar la ryta del paquete
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))


from analyzer.text_analizer import (
    count_words,
    count_characters,
    count_sentences,
    longest_word
)

# 
def test_count_words():
    text = "Hola mundo"
    assert count_words(text) == 2

def test_count_characters():
    text = "Hola"
    assert count_characters(text)== 4

def test_count_sentences():
    text = "Hola mundo. Esto es una prueba"
    assert count_sentences(text) == 2


def test_longest_word():
    text = "Hola mundo de programación"
    assert longest_word(text) == "programación"

if __name__ == '__main__':
    print("ejecutando test ....")
    test_count_words()
    test_count_characters()
    test_count_sentences()
    test_longest_word()
    print("Todos los test se ejecutaron exitosamente")

# hasta aquí todo se ejecuta correctamente con algo como esto: ejecutando test .... Todos los test se ejecutaron exitosamente
# si alguna de las condiciones no se cumple se vera un error como este :
# assert count_characters(text)== 4  ^^^^^^^^^^^^^^^^^^^^^^^^^^ AssertionError
# nos pide que se cuenten 4 caracteres y solo hay 3 