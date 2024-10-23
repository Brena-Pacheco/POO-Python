class Autor:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def mostrar_livros(self):
        return [livro.titulo for livro in self.__livros]

    @property
    def nome(self):
        return self.__nome

    @property
    def livros(self):
        return self.__livros


class Livro:
    def __init__(self, titulo, autor, codigo):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = codigo
        self.__disponivel = True
        self.__autor.adicionar_livro(self)  # Adiciona o livro ao autor

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        self.__disponivel = True

    @property
    def titulo(self):
        return self.__titulo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def disponivel(self):
        return self.__disponivel


class Biblioteca:
    total_livros = 0

    def __init__(self, nome):
        self.nome = nome
        self.__livros = []
        self.__emprestimos = {}

    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        Biblioteca.total_livros += 1

    def registrar_emprestimo(self, codigo_livro, cliente):
        for livro in self.__livros:
            if livro.codigo == codigo_livro and livro.disponivel:
                livro.emprestar()
                self.__emprestimos[codigo_livro] = cliente
                return True
        return False

    def registrar_devolucao(self, codigo_livro):
        if codigo_livro in self.__emprestimos:
            for livro in self.__livros:
                if livro.codigo == codigo_livro:
                    livro.devolver()
                    del self.__emprestimos[codigo_livro]
                    return True
        return False

    def mostrar_livros_disponiveis(self):
        return [livro.titulo for livro in self.__livros if livro.disponivel]

    @classmethod
    def mostrar_total_livros(cls):
        print(f'Total de livros na biblioteca: {cls.total_livros}')
