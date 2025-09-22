// Função para conversão de valores de reais para gramas de ouro
function conversor() {
    // Explicação sobre a conversão
    alert("O valor em gramas de ouro é calculado dividindo o valor em reais pelo preço de 1 grama de ouro. Exemplo: R$1000 dividido por R$312,50 resulta em aproximadamente 3,20 gramas.");

    // Captura o valor digitado pelo usuário
    let valorAtual = prompt("Digite o valor em reais que deseja converter para ouro:");

    // Verifica se a entrada é válida
    if (isNaN(valorAtual) || valorAtual.trim() === "") {
        alert("Por favor, insira um número válido.");
        return;
    }

    // Define o valor atual do ouro por grama (pode ser atualizado futuramente)
    const valorOuro = 312.50;

    // Calcula o valor convertido
    let valorEmOuro = valorAtual / valorOuro;

    // Exibe o resultado
    alert(`O valor de R$${valorAtual} equivale a ${valorEmOuro.toFixed(2)} gramas de ouro.`);
}

// Adiciona um evento ao botão para chamar a função de conversão
document.getElementById("convertBtn").addEventListener("click", conversor);