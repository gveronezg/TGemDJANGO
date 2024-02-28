// Verifica se o campo de usuário está vazio
document.addEventListener('DOMContentLoaded', function() {
    const usuarioInput = document.querySelector('[name="usuario"]');
    const loginForm = document.getElementById('loginForm');

    if (!usuarioInput.value.trim()) {
        // Redireciona automaticamente para a URL /home/
        window.location.href = '/home/';
    }

    // Adiciona um evento ao formulário para verificar novamente antes do envio
    loginForm.addEventListener('submit', function(event) {
        if (!usuarioInput.value.trim()) {
            // Cancela o envio do formulário se o campo de usuário estiver vazio
            event.preventDefault();
            window.location.href = '/home/';
        }
    });
});