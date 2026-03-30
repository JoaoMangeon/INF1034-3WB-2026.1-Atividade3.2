from turtle import *
from time import sleep

t = Turtle()
t.speed(200)

def desenha_retangulo(x, y, larg, alt, color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color('black')
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
       t.fd(larg)
       t.rt(90)
       t.fd(alt)
       t.rt(90)
    t.end_fill()

def desenha_circulo(x, y, tamanho, color):
    t.pu()
    t.goto(x,y)
    t.pd()
    
    t.color(color)
    t.begin_fill()
    t.fillcolor(color)
    t.circle(tamanho)
    t.end_fill()

def desenha_triangulo(x, y, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()

    t.setheading(0) 
    t.lt(40)
    t.fd(200)
    t.lt(101)
    t.fd(200)
    t.seth(270)
    t.fd(252)
    t.end_fill()

def desenha_estrela_8_pontas(x, y, color):
    t.pu()
    t.goto(x, y)
    t.rt(22.5)
    t.fd(10)
    t.lt(180)
    t.pd()
    
    t.color('white')
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(8):
        t.fd(20)
        t.lt(135)
    t.end_fill()




def desenha_bandeira_franca():
    desenha_retangulo(-250, 125, 134, 252, '#012153')
    desenha_retangulo(-116, 125, 134, 252, 'white')
    desenha_retangulo(18, 125, 134, 252, '#D00921')

desenha_bandeira_franca()
sleep(3)
t.clear()

def desenha_bandeira_ucrania():
    desenha_retangulo(-250, 125, 402, 126, '#0157B7')
    desenha_retangulo(-250, -1, 402, 126, '#FFD701')

desenha_bandeira_ucrania()
sleep(3)
t.clear()

def desenha_bandeira_polonia():
    desenha_retangulo(-250, 125, 402, 126, 'white')
    desenha_retangulo(-250, -1, 402, 126, '#DD0C39')

desenha_bandeira_polonia()
sleep(3)
t.clear()

def desenha_bandeira_italia():
    desenha_retangulo(-250, 125, 134, 252, '#009246')
    desenha_retangulo(-116, 125, 134, 252, 'white')
    desenha_retangulo(18, 125, 134, 252, '#CE2B37')

desenha_bandeira_italia()
sleep(3)
t.clear()

def desenha_bandeira_russia():
    desenha_retangulo(-250, 125, 402, 84, 'white')
    desenha_retangulo(-250, 41, 402, 84, '#0039A6')
    desenha_retangulo(-250, -43, 402, 84, '#D52B1E')

desenha_bandeira_russia()
sleep(3)
t.clear()

def desenha_bandeira_holanda():
    desenha_retangulo(-250, 125, 402, 84, '#A91B27')
    desenha_retangulo(-250, 41, 402, 84, '#F7F7F7')
    desenha_retangulo(-250, -43, 402, 84, '#204487')

desenha_bandeira_holanda()
sleep(3)
t.clear()

def desenha_bandeira_colombia():
    desenha_retangulo(-250, 125, 402, 126, '#FEDB0D')
    desenha_retangulo(-250, -1, 402, 63, '#023893')
    desenha_retangulo(-250, -64, 402, 63, '#CD1128')

desenha_bandeira_colombia()
sleep(3)
t.clear()

def desenha_bandeira_gabao():
    desenha_retangulo(-250, 125, 402, 84, '#019E60')
    desenha_retangulo(-250, 41, 402, 84, '#FCD116')
    desenha_retangulo(-250, -43, 402, 84, '#3A76C4')

desenha_bandeira_gabao()
sleep(3)
t.clear()

def desenha_bandeira_irlanda():
    desenha_retangulo(-250, 125, 134, 252, '#179B62')
    desenha_retangulo(-116, 125, 134, 252, 'white')
    desenha_retangulo(18, 125, 134, 252, '#FF883D')

desenha_bandeira_irlanda()
sleep(3)
t.clear()

def desenha_bandeira_nigeria():
    desenha_retangulo(-250, 125, 134, 252, '#008751')
    desenha_retangulo(-116, 125, 134, 252, 'white')
    desenha_retangulo(18, 125, 134, 252, '#008751')

desenha_bandeira_nigeria()
sleep(3)
t.clear()

def desenha_bandeira_niger():
    desenha_retangulo(-250, 125, 402, 84, '#E05206')
    desenha_retangulo(-250, 41, 402, 84, 'white')
    desenha_retangulo(-250, -43, 402, 84, '#0EB02C')
    desenha_circulo(-50, -30, 30,'#E05206')

desenha_bandeira_niger()
sleep(3)
t.clear()

def desenha_bandeira_costarica():
    desenha_retangulo(-250, 125, 402, 42, '#001489')
    desenha_retangulo(-250, 83, 402, 42,'white')
    desenha_retangulo(-250, 41, 402, 84, '#DA291C')
    desenha_retangulo(-250, -43, 402, 42, 'white')
    desenha_retangulo(-250, -85, 402, 42, '#001489')

desenha_bandeira_costarica()
sleep(3)
t.clear()

def desenha_bandeira_botswana():
    desenha_retangulo(-250, 125, 402, 95, '#6EA9D2')
    desenha_retangulo(-250, 30, 402, 10,'white')
    desenha_retangulo(-250, 20, 402, 42, 'black')
    desenha_retangulo(-250, -22, 402, 10, 'white')
    desenha_retangulo(-250, -32, 402, 95, '#6EA9D2')

desenha_bandeira_botswana()
sleep(3)
t.clear()

def desenha_bandeira_azerbaijao():
    desenha_retangulo(-250, 125, 402, 84, '#00B5E2')
    desenha_retangulo(-250, 41, 402, 84, '#EF3340')
    desenha_retangulo(-250, -43, 402, 84, '#509E30')
    desenha_circulo(-49, -30, 30, 'white')
    desenha_circulo(-39, -24, 24, '#EF3340')
    desenha_estrela_8_pontas(-18, 4, 'white')

desenha_bandeira_azerbaijao()
sleep(3)
t.clear()
t.seth(0)

def desenha_bandeira_bahamas():
    desenha_retangulo(-250, 125, 402, 84, '#00788C')
    desenha_retangulo(-250, 41, 402, 84, '#FFC828')
    desenha_retangulo(-250, -43, 402, 84, '#00788C')
    desenha_triangulo(-250, -128, 'black')


desenha_bandeira_bahamas()
sleep(3)
t.clear()
t.seth(0)

escolha = textinput('Bandeiras', 'Digite a bandeira que você deseja:')

if escolha == 'França':
   desenha_bandeira_franca()

if escolha == 'Ucrânia':
   desenha_bandeira_ucrania()

if escolha == 'Polônia':
   desenha_bandeira_polonia()

if escolha == 'Itália':
   desenha_bandeira_italia()

if escolha == 'Rússia':
   desenha_bandeira_russia()

if escolha == 'Holanda':
   desenha_bandeira_holanda()

if escolha == 'Colômbia':
   desenha_bandeira_colombia()

if escolha == 'Gabão':
   desenha_bandeira_gabao()

if escolha == 'Irlanda':
   desenha_bandeira_irlanda()

if escolha == 'Nigéria':
   desenha_bandeira_nigeria()

if escolha == 'Niger':
   desenha_bandeira_niger()

if escolha == 'Costa Rica':
   desenha_bandeira_costarica()

if escolha == 'Botswana':
   desenha_bandeira_botswana()

if escolha == 'Azerbaijão':
   desenha_bandeira_azerbaijao()

if escolha == 'Bahamas':
   desenha_bandeira_bahamas()




mainloop()

    