from math import exp, log, ceil

try :
	import mathplotlib as plt
except: 
	print("Erreur:la librairie matplotlib n'est pas installer! Veuillez l'installer pour bien ploter la fonction")

import os


os.system('clear')


print("Voici l'approximation de la racine pour la fonction 10x-9e^-x")
print("============================================================")
print("")

#affectation des valeurs 
#pour d autres test changer les differents valeurs
intervale = [0,2]
epsilone = 10**(-6)
M = 0.1
xo = 0.1

#l equation de la fonction f de x
def fx(x) :
	return 10 * x - 9 * exp(-x)




#l equation phi de x
#pour d autres test l equation peut etre changee
def phix(x) :
	return 9 * exp(-x) / 10


#la derivee de fx	
def fxprime(x) : 
	return 10 + 9 * exp(-x)


    
#calcul du nombre d iterationpour la methode des points fixes
def nbreIterationPtFixes () :
	n = (log(epsilone) - log(intervale[1] - intervale[0])) / log(M)
	n = ceil(n)
	return n
	
    
    
#calcul du nbre d'iterations pour la methode de dichotomie    
def nbreIterationDichotomie () :
	n = (log (intervale[1] - intervale[0]) - log(epsilone)) / log(2)
	n = ceil(n)
	return n



#calcul de la valeurs approchee pour la methode de dichotomie
def dichotomie () :
	n = nbreIterationDichotomie()
	for i in range (n) :
		a = intervale[0]
		b = intervale[1]
		if  fx(a) * fx((a+b)/2) > 0 :
			intervale[0] = (a+b)/2
		else :
			intervale[1] = (a+b)/2

	print("la valeur approchee de la racine par la methode de dichotomie vaut :", intervale[1], " et le nbre d iteration vaut : ", n)
 

#la methode des points fixes
def pointFixes (epsilone, xo) :
	x1 = phix(xo)
	xn = x1
	n = nbreIterationPtFixes()
	for i in range(1, n) :
		xn = phix(xn)
	print ("la valeur raprochee de la racine par la methode du pointfixe vaut : ", xn, "le nombre d iteration vaut ", n)
	

    
    
#la methode de newton, on calcul le nombre d iteration et on applique la formnule pour calculer les valeurs de xn
def newton() :
	xn = xo
	n = nbreIterationDichotomie()
	for i in range (n) :
		xn = xn - (fx(xn) / fxprime(xn))
	
	print ("la valeur raprochee de la racine par la methode de newton vaut : ", xn, " et le nbre d iteration vaut ", n)


#ici on peut test les differents fonctions pour voir leurs reaction	

print("l'intervale est de : ", intervale)
print("la valeur de M est de : ", M)
print("la valeur de x0 est de : ", xo)
print("la valeur de epsilone est de : ", epsilone)

#appel des fonction pour le calcul
newton()
pointFixes(epsilone, xo)
dichotomie()



#tracer de la courbe de l equation
try:
	#calcul de points pour la fonction
	x = range(-100, -100)
	y = fx(x)
	#plot de la fonction
	plt.plot(x,y)
	plt.show()
except :
	pass
	


