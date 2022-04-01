#to bedzie plik na ktorym bedziemy pracowali z repo

def hello(name):
	return "Hello" + str(name)


def dodaj (a,b):
	wynik = float(a)+float(b)
	return wynik

def odejmij(a,b):
	return a-b

pierwsza = input()
druga = input()
print (dodaj(pierwsza, druga))



