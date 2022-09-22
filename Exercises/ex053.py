phrase = input('Digite uma frase: ').strip()

adj_phrase = phrase.replace(' ', '').upper()

newphrase = ''

for letter in range(len(adj_phrase) - 1, -1, -1):
    newphrase += adj_phrase[letter]

if adj_phrase == newphrase:
    print(f'A frase "{phrase.upper()}" é palíndromo!')
else:
    print(f'A frase "{phrase.upper()}" NÃO é palíndromo!')
