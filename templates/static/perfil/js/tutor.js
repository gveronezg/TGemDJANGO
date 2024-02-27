// Função para carregar municípios ao alterar o estado
function carregarMunicipios() {
    const estadoSelect = document.getElementById('estadoSelect');
    const municipioSelect = document.getElementById('municipioSelect');
    const estadoSelecionado = estadoSelect.value;

    // Faça uma requisição AJAX para obter os municípios do estado selecionado
    fetch(`https://servicodados.ibge.gov.br/api/v1/localidades/estados/${estadoSelecionado}/distritos`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro na requisição');
            }
            return response.json();
        })
        .then(data => {
            console.log('Dados da API:', data);

            // Ordenar municípios em ordem alfabética
            data.sort((a, b) => a.nome.localeCompare(b.nome));

            // Limpe os municípios existentes
            municipioSelect.innerHTML = "";

            // Adicione os novos municípios ao select
            data.forEach(municipio => {
                const option = document.createElement('option');
                option.value = municipio.id;
                option.text = municipio.nome;
                municipioSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Erro na requisição:', error);
        });
}

// Adicione um ouvinte de eventos para chamar a função ao alterar o estado
estadoSelect.addEventListener('change', carregarMunicipios);

// Adicione um ouvinte para carregar os estados assim que a página for carregada
document.addEventListener('DOMContentLoaded', function () {
    const estadoSelect = document.getElementById('estadoSelect');

    // Faça uma requisição AJAX para obter os estados
    fetch('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro na requisição');
            }
            return response.json();
        })
        .then(estados => {
            console.log('Estados:', estados);

            // Ordenar municípios em ordem alfabética
            estados.sort((a, b) => a.nome.localeCompare(b.nome));

            // Adicione os estados ao select
            estados.forEach(estado => {
                const option = document.createElement('option');
                option.value = estado.sigla;
                option.text = estado.nome;
                estadoSelect.appendChild(option);
            });

            // Selecione o estado Acre e carregue os municípios ao iniciar a página
            estadoSelect.value = 'AC';
            carregarMunicipios();
        })
        .catch(error => {
            console.error('Erro na requisição:', error);
        });
});