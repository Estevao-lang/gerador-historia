# Gerador de Currículo usando Flask

Este é um aplicativo web simples construído com Flask que permite aos usuários gerar um currículo em formato PDF (curriculum vitae) com base nas informações fornecidas. O PDF gerado inclui detalhes do usuário, habilidades e informações educacionais.

## Recursos

- Interface web amigável para inserir detalhes pessoais e educacionais.
- Seleção de habilidades a partir de uma lista predefinida.
- Geração dinâmica de um currículo em PDF com base nas informações fornecidas.
- Geração de PDF utilizando as bibliotecas `reportlab` e `xhtml2pdf`.

## Pré-requisitos

Antes de executar a aplicação, certifique-se de ter o seguinte instalado:

- Python 3.x
- Flask
- Reportlab
- xhtml2pdf

Você pode instalar os pacotes necessários usando o seguinte comando:

```bash
pip install Flask reportlab xhtml2pdf
```

## Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/your-username/curriculum-generator.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd curriculum-generator
   ```

3. Execute a aplicação Flask:

   ```bash
   python app.py
   ```

4. Abra seu navegador da web e vá para [http://127.0.0.1:5000/](http://127.0.0.1:5000/) para acessar a aplicação.

## Uso

1. Preencha os campos obrigatórios na página web.
2. Selecione habilidades a partir da lista predefinida.
3. Clique no botão "Gerar PDF".
4. A aplicação gerará dinamicamente um currículo em PDF com base nas informações fornecidas.
5. Faça o download do PDF gerado com o nome de arquivo "curriculum.pdf".

## Estrutura do Projeto

- `app.py`: Script da aplicação Flask contendo rotas e lógica de geração de PDF.
- `templates/`: Diretório contendo templates HTML para as páginas web.

## Bibliotecas Utilizadas

- Flask: Framework web para Python.
- Reportlab: Biblioteca para geração de PDF.
- xhtml2pdf: Biblioteca para converter HTML para PDF.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
