// Lista para armazenar os veículos
let veiculos = [];

// Função para adicionar veículo
document.getElementById('adicionar-veiculo').addEventListener('click', function() {
    const nome = document.getElementById('nome').value;
    const ano = document.getElementById('ano').value;
    const valorDiario = document.getElementById('valor-diario').value;
    const tipo = document.getElementById('tipo').value;
    const opcaoAdicional = document.getElementById('opcao-adicional').value;

    // Verifica se todos os campos estão preenchidos
    if (!nome || !ano || !valorDiario || !tipo || !opcaoAdicional) {
        alert('Por favor, preencha todos os campos.');
        return;
    }

    // Adiciona o veículo à lista
    veiculos.push({
        nome,
        ano,
        valorDiario,
        tipo,
        opcaoAdicional
    });

    alert('Veículo adicionado com sucesso!');
    document.getElementById('form-veiculo').reset();  // Limpa o formulário
});

// Função para calcular o aluguel
document.getElementById('calcular-aluguel').addEventListener('click', function() {
    if (veiculos.length === 0) {
        alert('Nenhum veículo adicionado.');
        return;
    }

    let resultado = 'Veículos cadastrados:<br>';
    veiculos.forEach((veiculo, index) => {
        resultado += `${index + 1}. ${veiculo.nome} (${veiculo.ano}) - Tipo: ${veiculo.tipo}, Valor Diário: R$ ${parseFloat(veiculo.valorDiario).toFixed(2)}, Combustível/Cilindrada: ${veiculo.opcaoAdicional}<br>`;
    });

    // Exibe a lista de veículos
    document.getElementById('resultado').innerHTML = resultado;
});
