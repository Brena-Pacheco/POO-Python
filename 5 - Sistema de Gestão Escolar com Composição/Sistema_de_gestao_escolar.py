# Classe Aluno
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def mostrar_info(self):
        print(f"Aluno: {self.nome}, Matrícula: {self.matricula}")

# Classe Curso
class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def mostrar_alunos(self):
        print(f"Alunos matriculados no curso {self.nome}:")
        for aluno in self.alunos:
            aluno.mostrar_info()

# Classe Escola
class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        print(f"Cursos na escola {self.nome}:")
        for curso in self.cursos:
            curso.mostrar_alunos()

# Testando o sistema escolar
aluno1 = Aluno("Alice", "001")
aluno2 = Aluno("Bob", "002")

curso1 = Curso("Matemática", "MAT101")
curso1.adicionar_aluno(aluno1)
curso1.adicionar_aluno(aluno2)

escola = Escola("Escola Exemplo")
escola.adicionar_curso(curso1)
escola.mostrar_cursos()
