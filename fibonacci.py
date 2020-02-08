def fibo(n):
	# Escriba aquí el código para calcular el n-esimo valor de la serie de fibonacci de forma no recursiva (use ciclos).
  if n == 0: return 0
  valor1 = 1
  valor2 = 1
  while n > 2:
      valor1, valor2 = valor2, valor1+valor2
      n -= 1
  return valor2

def fibo_rec(n):
	# Escriba aquí el código para calcular el n-esimo valor de la serie de fibonacci de forma recursiva (NO use ciclos).
  if n <= 1:
    return n  
  else:  
    return(fibo_rec(n-1) + fibo_rec(n-2))


print("Bienvenido a la calculadora de Fibonacci")

while True:
  print("Ingrese un valor mayor a cero.")
  numeroUsuario = int(input(""))
  if numeroUsuario >= 0:
    print("Respuesta no recursiva: %s " % fibo(numeroUsuario))
    print("Respuesta recursiva: %s" % fibo_rec(numeroUsuario))
  else:
    print("El numero ingresado no es mayor a cero")
