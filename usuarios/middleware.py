from django.shortcuts import redirect

class RedirecionarMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica se a URL é /usuarios/logar/ e se o parâmetro 'usuario' está vazio
        if request.path == '/usuarios/entrar/' and not request.GET.get('usuario'):
            return redirect('/home/')

        response = self.get_response(request)
        return response
