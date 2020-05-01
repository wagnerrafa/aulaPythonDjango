from django.shortcuts import render

# Create your views here.
def home(request):
      return render(request, 'index.php')

def conexao(request):
      return render(request, 'conexao.php')

def processa(request):
      return render(request, 'index.php')