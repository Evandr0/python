import webbrowser

def url(destino):
	varURL = destino
	print (varURL)
	webbrowser.open(varURL, new=0, autoraise=True)
