from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

##########################################################
########################### 01 ###########################
##########################################################
@app.route('/')
def index():
    return render_template('index.html')


##########################################################
########################### 02 ###########################
##########################################################
# CRIANDO O DATAFRAME


# RENDERIZE OS VALORES DO DATAFRAME df EM UMA TABELA HTML DENTRO DA PÁGINA /table.html (CRIE UM HTML PARA ISSO)
@app.route('/table')
def table():

# Alterei a forma de execução do dataframe por ter uma melhor visualização 
    df = pd.DataFrame({
    'alunos': ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'],
    'notas': [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00]
})

# Desafio 1.4.2 - Renderizar o dataframe presente na linha 18 (do arquivo app.py) na página table.html
# Utilizei a função do Pandas de transformar um dataframe em algum formato que seja necessário. No caso foi utilizado para transforma em HTML
# Sendo assim inseri df.to_html e tirei o índice do dataframe com index=False.
    table_html = df.to_html(index=False)

# Ainda sobre o desafio 1.4.2, inseri dentro do arquivo table.html a variavel table*, sendo assim quando executar identificará que table é
# a tabela_html criada a partir do dataframe transformado em html.
#*table foi inserida no table.html e lá terá uma nota com número ¹ explicando a chave criada.
    return render_template('table.html', table=table_html)

# Desafio 1.4.1 - Identifique porque o projeto não está sendo executado no localhost:
# Resposta: O bloco abaixo é feito para executar o arquivo. Se o bloco não estiver dentro do arquivo o servidor Flask não irá iniciar.
# Como o arquivo estava sem este bloco, o projeto não identificou que devia ser executado e, portanto, não foi executado no localhost.
if __name__ == '__main__':
    app.run()
# Para o app.run() podemos inserir a opção de debug=True que irá trazer os erros e as atualizações do código em tempo real. 
# Utilizei durante o desenvolvimento do projeto em alguns momentos para entender melhor a função.
