def impar_par(n:int):
    """
    # n % 2 == 0  par
    # n % 2 != 0  impar

    """
    
    for number_range in range(n):
        #verificando se par
        if(number_range % 2==0):
           print(str(number_range)+" é par")
        # caso contrario impar
        else:
            print(str(number_range)+" é impar")

impar_par(30)
