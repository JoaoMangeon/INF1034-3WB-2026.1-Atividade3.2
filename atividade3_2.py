from turtle import *
from time import sleep

t = Turtle()
t.speed(200)

def desenha_retangulo(x, y, larg , alt, color):
    t.pu()
    t.goto(x,y)
    t.pd()

    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
       t.fd(larg)
       t.rt(90)
       t.fd(alt)
       t.rt(90)
    t.end_fill()

def desenha_circulo(x ,y , tamanho, color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(tamanho)
    t.end_fill()

def desenha_triangulo(x ,y , color ):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.goto(-50, 0)
    t.goto(-150, 100)
    t.goto(-150, -100)



def desenha_bandeira_franca():
    desenha_retangulo(-200, 200, 100, 200, '#012153')
    desenha_retangulo(-100, 200, 100, 200, 'white')
    desenha_retangulo(0, 200, 100, 200, '#D00921')

desenha_bandeira_franca()
sleep(3)
t.clear()

def desenha_bandeira_ucrania():
    desenha_retangulo(-200, 125, 400, 125, '#0157B7')
    desenha_retangulo(-200, 0, 400, 125, '#FFD701')

desenha_bandeira_ucrania()
sleep(3)
t.clear()

def desenha_bandeira_polonia():
    desenha_retangulo(-200, 125, 400, 125, 'white')
    desenha_retangulo(-200, 0, 400, 125, '#DD0C39')

desenha_bandeira_polonia()
sleep(3)
t.clear()

def desenha_bandeira_italia():
    desenha_retangulo(-200, 200, 100, 200, '#009246')
    desenha_retangulo(-100, 200, 100, 200, 'white')
    desenha_retangulo(0, 200, 100, 200, '#CE2B37')

desenha_bandeira_italia()
sleep(3)
t.clear()

def desenha_bandeira_russia():
    desenha_retangulo(-200, 125, 400, 100, 'white')
    desenha_retangulo(-200, 25, 400, 100, '#0039A6')
    desenha_retangulo(-200, -75, 400, 100, '#D52B1E')

desenha_bandeira_russia()
sleep(3)
t.clear()

def desenha_bandeira_holanda():
    desenha_retangulo(-200, 125, 400, 100, '#A91B27')
    desenha_retangulo(-200, 25, 400, 100, '#F7F7F7')
    desenha_retangulo(-200, -75, 400, 100, '#204487')

desenha_bandeira_holanda()
sleep(3)
t.clear()

def desenha_bandeira_colombia():
    desenha_retangulo(-200, 125, 400, 150, '#FEDB0D')
    desenha_retangulo(-200, -25, 400, 75, '#023893')
    desenha_retangulo(-200, -100, 400, 75, '#CD1128')

desenha_bandeira_colombia()
sleep(3)
t.clear()

def desenha_bandeira_gabao():
    desenha_retangulo(-200, 125, 400, 100, '#019E60')
    desenha_retangulo(-200, 25, 400, 100, '#FCD116')
    desenha_retangulo(-200, -75, 400, 100, '#3A76C4')

desenha_bandeira_gabao()
sleep(3)
t.clear()

def desenha_bandeira_irlanda():
    desenha_retangulo(-200, 200, 100, 200, '#179B62')
    desenha_retangulo(-100, 200, 100, 200, 'white')
    desenha_retangulo(0, 200, 100, 200, '#FF883D')

desenha_bandeira_irlanda()
sleep(3)
t.clear()

def desenha_bandeira_nigeria():
    desenha_retangulo(-200, 200, 100, 200, '#008751')
    desenha_retangulo(-100, 200, 100, 200, 'white')
    desenha_retangulo(0, 200, 100, 200, '#008751')

desenha_bandeira_nigeria()
sleep(3)
t.clear()

def desenha_bandeira_niger():
    desenha_retangulo(-200, 125, 400, 100, '#E05206')
    desenha_retangulo(-200, 25, 400, 100, 'white')
    desenha_retangulo(-200, -75, 400, 100, '#0EB02C')
    desenha_circulo(0, -50, 30,'#E05206')

desenha_bandeira_niger()
sleep(3)
t.clear()

def desenha_bandeira_costarica():
    desenha_retangulo(-200, 125, 400, 42, '#001489')
    desenha_retangulo(-200, 83, 400, 42,'white')
    desenha_retangulo(-200, 41, 400, 84, '#DA291C')
    desenha_retangulo(-200, -43, 400, 42, 'white')
    desenha_retangulo(-200, -85, 400, 42, '#001489')

desenha_bandeira_costarica()
sleep(3)
t.clear()

def desenha_bandeira_botswana():
    desenha_retangulo(-200, 125, 400, 95, '#6EA9D2')
    desenha_retangulo(-200, 30, 400, 10,'white')
    desenha_retangulo(-200, 20, 400, 42, 'black')
    desenha_retangulo(-200, -22, 400, 10, 'white')
    desenha_retangulo(-200, -32, 400, 95, '#6EA9D2')

desenha_bandeira_botswana()
sleep(3)
t.clear()

def desenha_bandeira_azerbaijao():
    desenha_retangulo(-200, 125, 400, 100, '#00B5E2')
    desenha_retangulo(-200, 25, 400, 100, '#EF3340')
    desenha_retangulo(-200, -75, 400, 100, '#509E30')

desenha_bandeira_azerbaijao()
sleep(3)
t.clear()

def desenha_bandeira_bahamas():
    desenha_retangulo(-200, 125, 400, 100, '#00788C')
    desenha_retangulo(-200, 25, 400, 100, '#FFC828')
    desenha_retangulo(-200, -75, 400, 100, '#00788C')

desenha_bandeira_bahamas()
sleep(3)
t.clear()






mainloop()

    