📞 Analisador de Ligações – Streamlit

Repositório destinado ao software criado para ajudar no gerenciamento de ligações gravadas.

Este projeto foi desenvolvido para atender uma necessidade real: facilitar a organização e análise das ligações recebidas diariamente. O sistema lê múltiplos arquivos CSV contendo informações de Data/Hora e Origem das ligações, transforma esses dados em uma tabela clara e estruturada, e exibe quantas vezes cada número telefonou em cada data — tudo de forma automática.

O aplicativo foi construído em Python + Streamlit, com foco em simplicidade e facilidade de uso para pessoas que não têm familiaridade com ferramentas de linha de comando.

🚀 Funcionalidades

Upload de múltiplos arquivos CSV simultaneamente

Leitura automática das colunas Data/Hora e Origem

Remoção da parte da hora, considerando apenas dia/mês/ano

Contagem de chamadas por número e por data

Geração de uma tabela dinâmica (pivot) com contagem por dia

Coluna Total por número

Download dos resultados em CSV

Arquivo .bat para execução com um clique

🖥 Como rodar

Instale as dependências:

pip install -r requirements.txt


Execute o aplicativo:

python -m streamlit run app.py


Ou simplesmente clique no arquivo iniciar.bat incluído no projeto.

📂 Estrutura

app.py — código principal do sistema

iniciar.bat — inicializador simples para abrir o sistema com um clique

requirements.txt — lista de dependências

README.md — este arquivo

Se quiser, também posso gerar um ícone, um instalador, ou melhorar esse README com badges, imagens ou GIF demonstrando o funcionamento.
