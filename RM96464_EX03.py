alunos = 49
notas_numero_impar= 0
notas_numero_par=0
for nota_impar in range(1,alunos + 2, 2):
    print("digitando a nota dos alunos impares")
    nota_aluno_impar=float(input("por favor insira a nota do aluno: {}".format(nota_impar)))
    notas_numero_impar = notas_numero_impar + nota_aluno_impar


media_impar = notas_numero_impar / 25
print("a media dos alunos impares foi  {}".format(media_impar))

for nota_par in range(2,alunos + 2, 2):
    print("digitando a nota dos alunos pares")
    nota_aluno_par=float(input("por favor insira a nota do aluno: {}".format(nota_par)))
    notas_numero_par = notas_numero_par + nota_aluno_par

media_par = notas_numero_par / 25
print("a media dos alunos pares foi {}".format(media_par))
