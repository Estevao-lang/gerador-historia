from flask import Flask, render_template, request, make_response, session, redirect, url_for
from reportlab.pdfgen import canvas
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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    user_data = {
        'nome': request.form.get('nome', ''),
        'dataNascimento': request.form.get('dataNascimento', ''),
        'email': request.form.get('email', ''),
         'github': request.form.get('github', ''),
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

    # Armazena user_data na sessão
    session['user_data'] = user_data

    # Renderiza a página HTML com os dados do usuário
    rendered_html = render_template('curriculum.html', user_data=user_data)

    # Gera o PDF usando a biblioteca reportlab
    pdf_data = generate_pdf_from_html(rendered_html)

    # Cria uma resposta Flask com o PDF
    response = make_response(pdf_data)
    response.headers['Content-Disposition'] = 'attachment; filename=curriculum.pdf'
    response.headers['Content-Type'] = 'application/pdf'

    return response

# Adicione user_data como argumento para a função render_template em 'itens.html'


def generate_pdf_from_html(html):
    from io import BytesIO
    from xhtml2pdf import pisa

    # Gera um buffer de BytesIO para armazenar o PDF
    buffer = BytesIO()

    # Converte o HTML para PDF
    pisa.CreatePDF(BytesIO(html.encode('utf-8')), dest=buffer)

    # Retorna os dados do buffer
    pdf_data = buffer.getvalue()
    buffer.close()

    return pdf_data

if __name__ == '__main__':
    app.run(debug=True)
