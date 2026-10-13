# kitchen-helper-app
Aplicação em Python para pesquisa de receitas e geração de listas de compras via API Spoonacular
🍳 Kitchen Helper

Uma aplicação desktop simples e intuitiva desenvolvida em Python que ajuda os utilizadores a encontrar receitas personalizadas com base no seu tipo de dieta e nos ingredientes disponíveis, gerando automaticamente uma lista de compras consolidada.

📌 Funcionalidades

🔍 Pesquisa Personalizada: Procura receitas com base na dieta (ex: vegan, keto, gluten free) e em ingredientes específicos.

📖 Detalhes e Modo de Preparação: Apresenta a lista completa de ingredientes e as instruções de confeção de cada prato.

🛒 Gerador de Lista de Compras: Consolida automaticamente todos os ingredientes das receitas encontradas numa lista pronta a usar.

🎨 Interface Gráfica (GUI): Interface amigável e acessível desenvolvida com Tkinter.

🛠️ Tecnologias Utilizadas

Linguagem: Python 3

Interface Gráfica: tkinter

Comunicação HTTP: requests

API REST Externa: Spoonacular API via RapidAPI

🚀 Como Executar o Projeto

Pré-requisitos

Certifica-te de que tens o Python instalado no teu sistema.

1. Clonar o repositório

git clone https://github.com/TEU-UTILIZADOR/kitchen-helper-app.git
cd kitchen-helper-app


2. Instalar as dependências

Instala a biblioteca necessária para realizar os pedidos HTTP:

pip install requests


3. Configurar a Chave de API

Cria uma conta gratuita na RapidAPI.

Subscreve o plano gratuito da Spoonacular API.

Copia a tua X-RapidAPI-Key.

Abre o ficheiro do projeto (app.py ou app_nova.py) e cola a tua chave na variável:

API_KEY = "SUA_CHAVE_API_AQUI"


4. Executar a aplicação

python app.py


(No Windows, também podes executar através de py app.py)

📄 Licença

Este projeto é de código aberto e está disponível para fins educacionais e de demonstração.
