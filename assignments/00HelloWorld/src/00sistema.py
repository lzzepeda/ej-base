def main():
    #escribe tu código abajo de esta línea
   a=float(input("dame el valor de a"))
   b=float(input("dame el valor de b"))
   c=float(input("dame el valor de c"))
   d=float(input("dame el valor de d"))
   e=float(input("dame el valor de e"))
   f=float(input("dame el valor de f"))
   determinante= a*e-b*d
   if determinante == 0:
       print("el sistema no tiene solucion")
   else:
       x=(c*e-b*f)/determinante   
       y=(a*f-c*d)/determinante   
       print (x)
       print (y)

if __name__=='__main__':
    main()
