def pig_latin_sentence(sentence):
    VOWELS = "aeiou"
    new_sentence = []
    for word in sentence.split():
        consonants = 0
        if word[0].lower() in VOWELS:
            new_sentence.append(word + 'yay')
            continue
        for letter in word.lower():
          if letter not in VOWELS:
                consonants += 1
                continue
          new_sentence.append(word[consonants:] + word[:consonants] + 'ay')
          break
    return " ".join(new_sentence)
if __name__ == '__main__':
    sentence = "smile floor happy egg"
    print(pig_latin_sentence(sentence))
