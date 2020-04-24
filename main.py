from student import student


def crea_estudiantes(count_estudiantes):
	print ("metodo vacio")

def ordena_edades(list_students):
	print ("metodo vacio")

def separa_generos(list_students):
	print ("metodo vacio")

def main():
	options = 1
	list_stud = []

	while options != "0":
		options = input("menu opciones 1. crea estudiantes - 2.ordena edades - 3.separa generos - 0. salir: ")

		if options == "1":
			print("crea estudiantes")

		if options == "2":
			print("ordena edades")

		if options == "3":
			print("separa generos")

if __name__ == "__main__":
	main()
