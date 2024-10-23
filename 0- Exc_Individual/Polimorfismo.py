def fazer_animais_falarem(animais):
    for animal in animais:
        print(animal.fazer_som())

# Testando a função
animais = [Cachorro(), Gato()]
fazer_animais_falarem(animais)
