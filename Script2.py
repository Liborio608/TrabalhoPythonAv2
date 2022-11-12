A = "A.M."
P = "P.M."
n = 1
def conversao ( h, m ):
    if 0 <= h <= 12 and 0 <= m < 60:
        return f" {h} : {m}  {A} "
    elif 12 < h < 24 and 0 <= m < 60:
        return f" { h - 12 } : {m}  {P} "
def saida ( h, m ):
    if h > 23 or h < 0:
        print( "Hora Digitada Invalida, Digite Novamente!" )
    elif m > 59 or m < 0:
        print( "Hora Digitada Invalida, Digite Novamente!" )
    else:
        print( f" {conversao(h, m)} " )
while n != 0:
    h = int ( input( "Digite As Horas Em AM: " ))
    if h < 0:
        break
    m = int ( input( "Digite Os Minutos Em AM: " ))
    saida ( h, m )