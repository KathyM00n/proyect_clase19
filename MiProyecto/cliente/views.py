from django.shortcuts import render

app_name = "Clientes"
# Create your views here.
def index(request):
    return render(request, "cliente/index_cliente.html")

