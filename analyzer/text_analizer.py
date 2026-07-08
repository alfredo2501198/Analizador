# cuenta cuantas palabras.
def count_words (text):
    return len(text.split())

# Cuenta cuantos caractéres
def count_characters (text):
    return len(text)

# Cuenta oraciones, definiendo si existe un punto entre las palabras.
def count_sentences(text):
    sentences = text.split(".")
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

#
def longest_word (text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)

