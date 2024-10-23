class Animal:
    def fazer_som(self):
        raise NotImplementedError("Este método deve ser implementado por subclasses.")

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Testando as classes
cachorro = Cachorro()
gato = Gato()
print(cachorro.fazer_som())
print(gato.fazer_som())
