from django.shortcuts import render

def cart_home(request):
	#print(request.session)
	#print(dir(request.session)) # Metodo utilizado para visualizar os metodos disponiveis no objeto
	# request.session.set_expiry(300) # 5 minutos
	#key = request.session.session_key
	#print(key)
	#request.session['first_name'] = "Felipe"
	return render(request, "carts/home.html", {})
