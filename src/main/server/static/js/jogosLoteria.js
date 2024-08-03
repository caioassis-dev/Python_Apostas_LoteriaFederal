
var botaoClick = document.getElementById("btnSortear");
const spinner = document.querySelector(".spinner-border");
const loading = document.querySelector(".btn-spinner");
var qtdSorteios = document.getElementById("entradaValor")
const dezSorteadas = document.getElementById('dezenSorteadas');

botaoClick.onclick = function() {

    spinner.style.display = 'block';
    loading.style.display = 'block';
    let valor = qtdSorteios.value

    console.log(valor)
    fetch(`http://127.0.0.1:3000/numeros?qtdSorteios=${valor}`) 
    .then(response => response.json())
    .then(data => {
        spinner.style.display = 'none';
        loading.style.display = 'none';
        dezSorteadas.style.display = 'block';
        const dezenasSorteadas = document.getElementById('sorteios');
        dezenasSorteadas.textContent = data.numbers.join(', ');;
    })
    .catch(error => {
        console.error('Erro na requisição:', error);
        spinner.style.display = 'none';
        loading.style.display = 'none';
    });
};


