produkty = {"jajka":"szt",
            "ziemniaki":"kg",
            "mleko":"l",
            "pomidory":"szt"}

x = produkty.items()
lista = [i for (i,j) in x if j == "szt"]
print(lista)