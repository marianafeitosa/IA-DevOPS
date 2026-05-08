# Lista de estudantes com notas
estudantes = [
    {"aluno": "Ana", "nota": 10},
    {"aluno": "Carlos", "nota": 6},
    {"aluno": "Marina", "nota": 9},
    {"aluno": "João", "nota": 4},
    {"aluno": "Fernanda", "nota": 10},
    {"aluno": "Pedro", "nota": 7},
    {"aluno": "Lucas", "nota": 5},
    {"aluno": "Julia", "nota": 8},
    {"aluno": "Rafaela", "nota": 3},
    {"aluno": "Bruno", "nota": 10},
]

# Parâmetro para separar os grupos
nota_corte = 7

grupo_aprovados = []
grupo_reprovados = []

# Separação dos grupos
for estudante in estudantes:
    if estudante["nota"] >= nota_corte:
        grupo_aprovados.append(estudante)
    else:
        grupo_reprovados.append(estudante)

# Exibir aprovados
print("=== Grupo Aprovados ===")
for aluno in grupo_aprovados:
    print(f'Aluno: {aluno["aluno"]} | Nota: {aluno["nota"]}')

# Exibir reprovados
print("\n=== Grupo Reprovados ===")
for aluno in grupo_reprovados:
    print(f'Aluno: {aluno["aluno"]} | Nota: {aluno["nota"]}')