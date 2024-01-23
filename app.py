from flask import Flask, render_template, request, make_response
from reportlab.pdfgen import canvas

app = Flask(__name__)

# Predefined list of skills
habilidades = [
    'comunicacao', 'trabalho-em-equipe', 'resolucao-de-problemas',
    'adaptabilidade', 'aprendizado-rapido', 'excel', 'word',
    'logica-programacao', 'design-grafico', 'analise-de-dados',
    'gestao-de-projetos', 'ingles', 'espanhol'
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
        'telefone': request.form.get('telefone', ''),
        'cep': request.form.get('cep', ''),
        'logradouro': request.form.get('logradouro', ''),
        'numero': request.form.get('numero', ''),
        'complemento': request.form.get('complemento', ''),
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

    # Renderiza a página HTML com os dados do usuário
    rendered_html = render_template('curriculum.html', user_data=user_data)

    # Gera o PDF usando a biblioteca reportlab
    pdf_data = generate_pdf_from_html(rendered_html)

    # Cria uma resposta Flask com o PDF
    response = make_response(pdf_data)
    response.headers['Content-Disposition'] = 'attachment; filename=curriculum.pdf'
    response.headers['Content-Type'] = 'application/pdf'

    return response

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