text = input('Digite uma frase: ').strip()

print(f'A letra "a" aparece {text.lower().count("a")} vezes na frase "{text.capitalize()}", e aparece a primeira vez na posição {text.lower().find("a")}.')
print(f'E aparece a última vez na posição {text.lower().rfind("a")}.')
