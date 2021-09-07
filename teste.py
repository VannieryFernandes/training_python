myAge = 16

def runThisBaby(x,y):
	print("Olá, meu nome é: ", x, "Tenho", y, "Anos, e esses sao os meus produtos: ")
	myGoods = ['Bola', 'Caneta', 'Chapeu']
	i = 0
	while i < len(myGoods):
	    print(i)
	    i += 1

try:
    print("Welcome to my program")
    myName = 'Baiard'
    myName.replace('i','Y')
except ValueError:
    print(ValueError)
runThisBaby(myName, myAge)
