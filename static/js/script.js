
function showStep(stepId) {
    const steps = document.getElementsByClassName('step');
    for (let i = 0; i < steps.length; i++) {
        steps[i].style.display = 'none';
    }
    document.getElementById(stepId).style.display = 'block';
}

function nextStep(nextStepId) {
    showStep(nextStepId);
}

function previousStep(previousStepId) {
    showStep(previousStepId);
}

function submitForm() {
    // Aqui você pode adicionar a lógica para enviar o formulário
    alert('Formulário enviado!');
}

showStep('step1'); // Mostra a primeira etapa inicialmente

function showStep(stepId) {
    const steps = document.getElementsByClassName('step');
    for (let i = 0; i < steps.length; i++) {
        steps[i].style.display = 'none';
    }
    document.getElementById(stepId).style.display = 'block';
}

function nextStep(nextStepId) {
    showStep(nextStepId);
}

function previousStep(previousStepId) {
    showStep(previousStepId);
}

function submitForm() {
    // Aqui você pode adicionar a lógica para enviar o formulário
    alert('Formulário enviado!');
}

showStep('step1'); // Mostra a primeira etapa inicialmente



$(document).ready(function () {
    $('#data-nascimento').datepicker({
        dateFormat: 'dd/mm/yy',
        changeMonth: true,
        changeYear: true,
        yearRange: '1900:2050'
    });
});

// Adiciona a máscara ao campo de entrada
$(document).ready(function () {
    $('#celular').mask('(99) 99999-9999');
});


function mostrarPeriodos() {
    var nivel = document.getElementById("nivel").value;
    var periodoSelect = document.getElementById("periodo");
    var semestreSelect = document.getElementById("semestre");
    var cursoSelect = document.getElementById("curso");
    var labelPeriodo = document.getElementById("labelPeriodo");
    var labelSemestre = document.getElementById("labelSemestre");
    var labelCurso = document.getElementById("labelCurso");

    if (nivel === "medio" || nivel === "tecnico") {
        periodoSelect.innerHTML = `
  <option value="">Selecione um período</option>
  <option value="Manhã">Manhã</option>
  <option value="Tarde">Tarde</option>
  <option value="Noite">Noite</option>
  <option value="Integral">Integral</option>
`;
        semestreSelect.style.display = "none";
        cursoSelect.style.display = "none";
        labelSemestre.style.display = "none";
        labelCurso.style.display = "none";
        labelPeriodo.style.display = "block";
        periodoSelect.style.display = "block";
    } else if (nivel === "graduacao" || nivel === "especializacao") {
        periodoSelect.innerHTML = `
  <option value="">Selecione um período</option>
  <option value="Diurno">Diurno</option>
  <option value="Noturno">Noturno</option>
`;
        semestreSelect.innerHTML = `
  <option value="">Selecione um semestre</option>
  <option value="1º ao 3º Semestre">1º ao 3º Semestre</option>
  <option value="3º ao 6º Semestre">3º ao 6º Semestre</option>
  <option value="6º ao 10º Semestre">7º ao 10º Semestre</option>
`;
        cursoSelect.style.display = "block";
        labelCurso.style.display = "block";
        semestreSelect.style.display = "block";
        labelSemestre.style.display = "block";
        labelPeriodo.style.display = "block";
        periodoSelect.style.display = "block";
    } else {
        labelPeriodo.style.display = "none";
        periodoSelect.style.display = "none";
        labelSemestre.style.display = "none";
        semestreSelect.style.display = "none";
        labelCurso.style.display = "none";
        cursoSelect.style.display = "none";
    }
}




function formatPhoneNumber(input) {
    // Remove any non-digit characters
    let phoneNumber = input.value.replace(/\D/g, '');

    // Apply the mask (XX) XXXXX-XXXX
    if (phoneNumber.length <= 2) {
        phoneNumber = phoneNumber.replace(/^(\d{0,2})/, '($1');
    } else if (phoneNumber.length <= 7) {
        phoneNumber = phoneNumber.replace(/^(\d{0,2})(\d{0,5})/, '($1) $2');
    } else {
        phoneNumber = phoneNumber.replace(/^(\d{0,2})(\d{0,5})(.*)/, '($1) $2-$3');
    }

    // Set the formatted value back to the input field
    input.value = phoneNumber;
}
function showFeedback(message) {
    const feedbackDiv = document.getElementById('feedback');
    feedbackDiv.textContent = message;
    feedbackDiv.style.display = 'block';
}

function hideFeedback() {
    const feedbackDiv = document.getElementById('feedback');
    feedbackDiv.style.display = 'none';
}

const form = document.querySelector('form');
form.addEventListener('submit', function () {
    showFeedback('Gerando currículo... Por favor, aguarde.');
});

const downloadButton = document.getElementById('download-button');
downloadButton.addEventListener('click', function () {
    hideFeedback();
});


