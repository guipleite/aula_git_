def ler_numeros(n):
	lista = []
	for i in range(n):
		x = int(input("Digite um número aqui: "))
		lista.append(x)
	return lista
	
if __name__ == "__main__":
	print(ler_numeros(10))