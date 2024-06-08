nome=input("digite seu nome:")
materia=input("digite a matéria que quer saber a nota:")
n1=int(input("digite sua nota:"))
n2=int(input("digite sua segunda nota:"))
minimo=int(6)
nota=(n1+n2)/ 2
if(nota >= minimo):
    print(nome +" "+"está aprovado em"+" " + materia)
else:
    print(nome +" "+"está reprovado em"+" "+ materia)