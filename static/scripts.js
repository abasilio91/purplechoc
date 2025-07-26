document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('dados-entrada');
    const saida = document.getElementById('saida');

window.addEventListener('load', function () {
    slider.value = slider.max;
    atualizaPosicaoHandler();
});

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(form);

        fetch('/processa', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                saida.textContent = data.resultado;
            })
            .catch(error => {
                saida.textContent = 'Erro ao processar.';
                console.error('Erro:', error);
            });
    });
});

const panel = document.getElementById('painel-opcoes');
function togglePanel() {
    panel.style.display = panel.style.display === 'none' ? 'block' : 'none';
};

const slider = document.getElementById('painel-tamanho')
const valor = document.getElementById('tamanho-valor')

function atualizaPosicaoHandler() {
    const sliderWidth = slider.offsetWidth
    const min = parseInt(slider.min)
    const max = parseInt(slider.max)
    const val = parseInt(slider.value)

    const percent = (val - min) / (max - min)
    const offset = percent * sliderWidth

    valor.textContent = val
    valor.style.left = `${offset}px`
}

slider.addEventListener('input', atualizaPosicaoHandler)
window.addEventListener('load', atualizaPosicaoHandler)