# aqui importo uma biblioteca nativa do Python
import webbrowser 
# e aqui importo minha biblioteca
import load 

pagina = 'www.google.com'
# executo uma função contida em minha biblioteca
load.url(pagina)


import webbrowser

def url(destino):
	varURL = destino
	print (varURL)
	webbrowser.open(varURL, new=0, autoraise=True)
