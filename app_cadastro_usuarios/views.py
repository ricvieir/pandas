from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')


# Salvar os dados da tela para o banco de dados
def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

# Exibir todos os usuários cadastrados em uma nova página
    #criando um dicionário de dados 
    usuarios = {
        'usuarios': Usuario.objects.all()
                        
    }
# Retornando os dados para a página de listagem de usuários
# o 'usuarios' no final da linha se refere ao dicionário de dados criado acima
    return render(request,'usuarios/usuarios.html', usuarios)