import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod
import datetime
import json
import pandas as pd


class Funcionario(ABC):
    def __init__(self, nome, matricula, numero_de_projetos):
        self.nome = nome
        self.matricula = matricula
        self.numero_de_projetos = numero_de_projetos
    
    @abstractmethod
    def calcular_salario(self):
        pass
    
    def calcular_pd(self):
        if self.numero_de_projetos > 0:
            return self.numero_de_projetos * 1000
        return 0

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        if nome.strip() == "":
            raise ValueError("Nome inválido")
        self._nome = nome
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula):
        if matricula is None:
            raise ValueError("Matrícula inválida")
        self._matricula = matricula
    
    @property
    def numero_de_projetos(self):
        return self._numero_de_projetos
    
    @numero_de_projetos.setter
    def numero_de_projetos(self, numero_de_projetos):
        if numero_de_projetos < 0:
            raise ValueError("Número de projetos não pode ser negativo")
        self._numero_de_projetos = numero_de_projetos
    
    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Número de projetos: {self.numero_de_projetos}"


class FuncionarioComissario(Funcionario):
    def __init__(self, nome, matricula, numero_de_projetos, salario_base, comissao, total_vendas):
        super().__init__(nome, matricula, numero_de_projetos)
        self.salario_base = salario_base
        self.comissao = comissao
        self.total_vendas = total_vendas

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        if salario_base <= 0:
            raise ValueError("Salário base deve ser maior que zero")
        self._salario_base = salario_base
    
    def calcular_salario(self):
        if self.total_vendas <= 0 or self.comissao <= 0:
            raise ValueError("Total de vendas e comissão precisam ser maiores que zero")
        salario = self.salario_base + (self.comissao * self.total_vendas)
        salario += self.calcular_pd()
        return salario
    
    def __str__(self):
        return super().__str__() + f", Salário Base: {self.salario_base}, Comissão: {self.comissao}, Total de Vendas: {self.total_vendas}"


class FuncionarioHoralista(Funcionario):
    def __init__(self, nome, matricula, numero_de_projetos, valor_por_hora, horas_por_dia):
        super().__init__(nome, matricula, numero_de_projetos)
        self.valor_por_hora = valor_por_hora
        self.horas_por_dia = horas_por_dia

    @property
    def valor_por_hora(self):
        return self._valor_por_hora

    @valor_por_hora.setter
    def valor_por_hora(self, valor_por_hora):
        if valor_por_hora <= 0:
            raise ValueError("Valor por hora deve ser maior que zero")
        self._valor_por_hora = valor_por_hora

    @property
    def horas_por_dia(self):
        return self._horas_por_dia

    @horas_por_dia.setter
    def horas_por_dia(self, horas_por_dia):
        if horas_por_dia <= 0:
            raise ValueError("Horas por dia deve ser maior que zero")
        self._horas_por_dia = horas_por_dia

    def simular_pagamento_mensal(self, ano, mes):
        dias_no_mes = (datetime.date(ano, mes % 12 + 1, 1) - datetime.timedelta(days=1)).day
        total_horas_trabalhadas = self.horas_por_dia * dias_no_mes
        salario_total = self.valor_por_hora * total_horas_trabalhadas
        return salario_total
    
    def calcular_salario(self):
        salario = self.simular_pagamento_mensal(2024, 10)
        salario += self.calcular_pd()
        return salario
    
    def __str__(self):
        return super().__str__() + f", Valor Por Hora: {self.valor_por_hora}, Horas Por Dia: {self.horas_por_dia}"


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, matricula, numero_de_projetos, salario_base):
        super().__init__(nome, matricula, numero_de_projetos)
        self.salario_base = salario_base

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        if salario_base <= 0:
            raise ValueError("Salário base deve ser maior que zero")
        self._salario_base = salario_base
    
    def calcular_salario(self):
        salario = self.salario_base
        salario += self.calcular_pd()
        return salario
    
    def __str__(self):
        return super().__str__() + f", Salário Base: {self.salario_base}"


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Funcionários")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f5")

        self.nome_var = tk.StringVar()
        self.matricula_var = tk.StringVar()
        self.num_proj_var = tk.StringVar()
        self.salario_var = tk.StringVar()
        self.comissao_var = tk.StringVar()
        self.total_vendas_var = tk.StringVar()
        self.valor_hora_var = tk.StringVar()
        self.horas_dia_var = tk.StringVar()
        self.tipo_funcionario_var = tk.StringVar(value="Mensalista")

        self.funcionarios = []

        # Criar o layout
        self.create_widgets()

    def create_widgets(self):
        # Título
        title = tk.Label(self.root, text="Cadastro de Funcionários", font=("Helvetica", 16, "bold"), bg="#f5f5f5")
        title.pack(pady=10)

        # Seção Dados Pessoais
        dados_pessoais_frame = ttk.LabelFrame(self.root, text="Dados Pessoais", padding=10)
        dados_pessoais_frame.pack(pady=10, padx=20, fill=tk.X)

        self.nome_entry = self.create_label_entry(dados_pessoais_frame, "Nome", self.nome_var, 0, 0)
        self.matricula_entry = self.create_label_entry(dados_pessoais_frame, "Matrícula", self.matricula_var, 1, 0)
        self.num_proj_entry = self.create_label_entry(dados_pessoais_frame, "Número de Projetos", self.num_proj_var, 2, 0)

        # Tipo de Funcionário
        tipo_frame = ttk.Frame(dados_pessoais_frame)
        tipo_frame.grid(row=3, column=0, columnspan=2, pady=5)

        tipo_label = tk.Label(tipo_frame, text="Tipo de Funcionário:")
        tipo_label.pack(side=tk.LEFT)

        tipo_combobox = ttk.Combobox(tipo_frame, textvariable=self.tipo_funcionario_var, 
                                      values=["Mensalista", "Comissário", "Horalista"], state="readonly")
        tipo_combobox.pack(side=tk.LEFT)
        tipo_combobox.bind("<<ComboboxSelected>>", self.on_tipo_funcionario_change)

        # Seção Salário
        salario_frame = ttk.LabelFrame(self.root, text="Salário", padding=10)
        salario_frame.pack(pady=10, padx=20, fill=tk.X)

        self.salario_entry = self.create_label_entry(salario_frame, "Salário Base", self.salario_var, 0, 0)
        self.comissao_entry = self.create_label_entry(salario_frame, "Comissão", self.comissao_var, 1, 0)
        self.total_vendas_entry = self.create_label_entry(salario_frame, "Total de Vendas", self.total_vendas_var, 2, 0)
        self.valor_hora_entry = self.create_label_entry(salario_frame, "Valor por Hora", self.valor_hora_var, 3, 0)
        self.horas_dia_entry = self.create_label_entry(salario_frame, "Horas por Dia", self.horas_dia_var, 4, 0)

        # Botões
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        cadastrar_button = ttk.Button(button_frame, text="Cadastrar Funcionário", command=self.cadastrar_funcionario)
        cadastrar_button.pack(side=tk.LEFT, padx=5)

        processar_button = ttk.Button(button_frame, text="Processar Pagamentos", command=self.processar_pagamentos)
        processar_button.pack(side=tk.LEFT, padx=5)

    def create_label_entry(self, parent, label_text, variable, row, column):
        label = tk.Label(parent, text=label_text)
        label.grid(row=row, column=column, padx=5, pady=5)
        entry = tk.Entry(parent, textvariable=variable)
        entry.grid(row=row, column=column + 1, padx=5, pady=5)
        return entry

    def on_tipo_funcionario_change(self, event):
        tipo = self.tipo_funcionario_var.get()
        self.salario_entry.configure(state='normal' if tipo == "Mensalista" else 'disabled')
        self.comissao_entry.configure(state='normal' if tipo == "Comissário" else 'disabled')
        self.total_vendas_entry.configure(state='normal' if tipo == "Comissário" else 'disabled')
        self.valor_hora_entry.configure(state='normal' if tipo == "Horalista" else 'disabled')
        self.horas_dia_entry.configure(state='normal' if tipo == "Horalista" else 'disabled')

    def cadastrar_funcionario(self):
        nome = self.nome_var.get()
        matricula = self.matricula_var.get()
        numero_de_projetos = int(self.num_proj_var.get())
        salario_base = float(self.salario_var.get()) if self.salario_var.get() else 0
        comissao = float(self.comissao_var.get()) if self.comissao_var.get() else 0
        total_vendas = float(self.total_vendas_var.get()) if self.total_vendas_var.get() else 0
        valor_hora = float(self.valor_hora_var.get()) if self.valor_hora_var.get() else 0
        horas_dia = float(self.horas_dia_var.get()) if self.horas_dia_var.get() else 0
        
        try:
            if self.tipo_funcionario_var.get() == "Mensalista":
                funcionario = FuncionarioMensalista(nome, matricula, numero_de_projetos, salario_base)
            elif self.tipo_funcionario_var.get() == "Comissário":
                funcionario = FuncionarioComissario(nome, matricula, numero_de_projetos, salario_base, comissao, total_vendas)
            elif self.tipo_funcionario_var.get() == "Horalista":
                funcionario = FuncionarioHoralista(nome, matricula, numero_de_projetos, valor_hora, horas_dia)
            else:
                raise ValueError("Tipo de funcionário inválido")
                
            self.funcionarios.append(funcionario)
            messagebox.showinfo("Sucesso", f"Funcionário {nome} cadastrado com sucesso!")
            self.limpar_campos()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
    def limpar_campos(self):
        self.nome_var.set("")
        self.matricula_var.set("")
        self.num_proj_var.set("")
        self.salario_var.set("")
        self.comissao_var.set("")
        self.total_vendas_var.set("")
        self.valor_hora_var.set("")
        self.horas_dia_var.set("")
        self.tipo_funcionario_var.set("Mensalista")
        self.on_tipo_funcionario_change(None)  # Atualiza o estado dos campos

    def processar_pagamentos(self):
        if not self.funcionarios:
            messagebox.showwarning("Atenção", "Nenhum funcionário cadastrado!")
            return
        
        resultados = []
        for funcionario in self.funcionarios:
            try:
                salario = funcionario.calcular_salario()
                resultados.append(f"{funcionario.nome}: Salário a receber: R$ {salario:.2f}")
            except ValueError as e:
                resultados.append(f"{funcionario.nome}: Erro ao calcular salário - {str(e)}")

        resultado_str = "\n".join(resultados)
        messagebox.showinfo("Resultados dos Pagamentos", resultado_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

