from flask import Flask, render_template, request, make_response, session
from io import BytesIO
from xhtml2pdf import pisa
import platform

# Verifica se o sistema é Windows
if platform.system() == 'Windows':
    import multiprocessing
    
    # Esta linha é necessária para evitar o erro relacionado ao módulo 'fcntl' no Windows
    multiprocessing.freeze_support()

app = Flask(__name__)
app.secret_key = 'vocacao'  # Defina uma chave secreta para a sessão

# Predefined list of skills
habilidades = [
    'comunicacao', 'trabalho-em-equipe', 'resolucao-de-problemas',
    'adaptabilidade', 'aprendizado-rapido', 'excel-basico', 'excel-intermediario',
    'excel-avancado', 'word-basico', 'word-intermediario', 'word-avancado',
    'logica-programacao', 'design-grafico', 'analise-de-dados', 'power-bi',
    'gestao-de-projetos', 'ingles-basico', 'ingles-intermediario', 'ingles-avancado',
    'espanhol-basico', 'espanhol-intermediario', 'espanhol-avancado'
]

def generate_pdf_from_html(html):
    buffer = BytesIO()
    pisa.CreatePDF(BytesIO(html.encode('utf-8')), dest=buffer)
    pdf_data = buffer.getvalue()
    buffer.close()
    return pdf_data

def validate_form_data(user_data):
    required_fields = ['nome', 'email', 'telefone', 'cep', 'bairro', 'cidade', 'estado', 'objetivos', 'area', 'instituicao_ensino', 'nivel', 'periodo', 'semestre', 'curso']

    for field in required_fields:
        if not user_data.get(field):
            return f'O campo {field} é obrigatório. Por favor, preencha todos os campos obrigatórios.'

    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    user_data = {
        'nome': request.form.get('nome', ''),
        'dataNascimento': request.form.get('dataNascimento', ''),
        'email': request.form.get('email', ''),
        'linkedin': request.form.get('linkedin', ''),
        'perfil': request.form.get('perfil', ''),
        'telefone': request.form.get('telefone', ''),
        'cep': request.form.get('cep', ''),
        'bairro': request.form.get('bairro', ''),
        'cidade': request.form.get('cidade', ''),
        'estado': request.form.get('estado', ''),
        'objetivos': request.form.get('objetivos', ''),
        'area': request.form.get('area', ''),
        'instituicao_ensino': request.form.get('instituicao_ensino', ''),
        'nivel': request.form.get('nivel', ''),
        'periodo': request.form.get('periodo', ''),
        'semestre': request.form.get('semestre', ''),
        'curso': request.form.get('curso', ''),
        'habilidades': [habilidade for habilidade in habilidades if habilidade in request.form]
    }

    validation_error = validate_form_data(user_data)
    if validation_error:
        return render_template('error.html', message=validation_error)

    session['user_data'] = user_data
    rendered_html = render_template('curriculum.html', user_data=user_data)
    pdf_data = generate_pdf_from_html(rendered_html)

    response = make_response(pdf_data)
    response.headers['Content-Disposition'] = 'attachment; filename=curriculum.pdf'
    response.headers['Content-Type'] = 'application/pdf'

    return response

if __name__ == '__main__':
    app.run(debug=True)
