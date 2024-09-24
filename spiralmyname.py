import turtle #pag75      # importa os graficos tartaruga
t = turtle.Pen()
turtle.bgcolor("black") 
colors =["red","yellow","blue","green"]

#Pede o nome do usuário usando a janela pop-up do turtle
your_name= turtle.textinput("entre com o seu nome","qual é o seu nome?")

#desenhe uma espiral na tela usando o nome,escrevendo-o 100 vezes
for x in range(100):
 t.pencolor(colors[x%4])   #circula pelas quatros cores
 t.penup() # não desenha as linhas normais
 t.forward(x*4)#apenas move a tartaruga pela tela
 t.write(your_name, font =("Arial",int((x+4)/4),"bold"))
 t.left(92)
         