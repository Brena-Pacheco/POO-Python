# Criando autores
autor1 = Autor("J.K. Rowling")
autor2 = Autor("George R.R. Martin")

# Criando livros
livro1 = Livro("Harry Potter e a Pedra Filosofal", autor1, "001")
livro2 = Livro("Harry Potter e a Câmara Secreta", autor1, "002")
livro3 = Livro("A Guerra dos Tronos", autor2, "003")

# Criando biblioteca
biblioteca = Biblioteca("Biblioteca Municipal")

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Mostrando livros disponíveis
print("Livros disponíveis:", biblioteca.mostrar_livros_disponiveis())

# Registrando um empréstimo
if biblioteca.registrar_emprestimo("001", "João da Silva"):
    print("Empréstimo registrado com sucesso.")
else:
    print("Erro ao registrar o empréstimo.")

# Mostrando livros disponíveis após o empréstimo
print("Livros disponíveis após o empréstimo:", biblioteca.mostrar_livros_disponiveis())

# Registrando uma devolução
biblioteca.registrar_devolucao("001")

# Mostrando total de livros na biblioteca
Biblioteca.mostrar_total_livros()
