import pandas as pd
import random

dados = [ #Dados fornecidos, (Certificar-se de estar nesse formato)
  {
    "Categoria": "Painel Solar",
    "Id": 1001,
    "Potencia em W": 500,
    "Produto": "Painel Solar 500 W Marca A"
  },
  {
    "Categoria": "Painel Solar",
    "Id": 1002,
    "Potencia em W": 500,
    "Produto": "Painel Solar 500 W Marca B"
  },
  {
    "Categoria": "Painel Solar",
    "Id": 1003,
    "Potencia em W": 500,
    "Produto": "Painel Solar 500 W Marca C"
  },
  {
    "Categoria": "Controlador de carga",
    "Id": 2001,
    "Potencia em W": 500,
    "Produto": "Controlador de Carga 30A Marca E"
  },
  {
    "Categoria": "Controlador de carga",
    "Id": 2002,
    "Potencia em W": 750,
    "Produto": "Controlador de Carga 50A Marca E"
  },
  {
    "Categoria": "Controlador de carga",
    "Id": 2003,
    "Potencia em W": 1000,
    "Produto": "Controlador de Carga 40A Marca D"
  },
  {
    "Categoria": "Inversor",
    "Id": 3001,
    "Potencia em W": 500,
    "Produto": "Inversor 500W Marca D"
  },
  {
    "Categoria": "Inversor",
    "Id": 3002,
    "Potencia em W": 1000,
    "Produto": "Inversor 1000W Marca D"
  }
]

df = pd.DataFrame(dados) #Criação do DataFrame

# Separando os produtos em categorias
paineis = df[df['Categoria'] == 'Painel Solar']
inversores = df[df['Categoria'] == 'Inversor']
controladores = df[df['Categoria'] == 'Controlador de carga']

geradores = []

for i, painel in painéis.iterrows():
    for j, inversor in inversores.iterrows():
        for k, controlador in controladores.iterrows():
            if painel['Potencia em W'] == inversor['Potencia em W'] == controlador['Potencia em W']:
                # Gera um ID único para o gerador
                gerador_id = f"{random.randint(10000, 99999)}"

                # Adiciona a configuração do gerador à lista
                geradores.append({
                    "ID Gerador": gerador_id,
                    "Potência do Gerador": painel['Potencia em W'],
                    "ID Produto": [painel['Id'], inversor['Id'], controlador['Id']],
                    "Nome Produto": [painel['Produto'], inversor['Produto'], controlador['Produto']],
                    "Quantidade": [1, 1, 1]  # Ajuste de acordo com a necessidade
                })

df_geradores = pd.DataFrame(geradores) # Criação do DataFrame dos geradores
# Exibir todas as colunas
pd.set_option('display.max_columns', None)

# Exibir todas as linhas (use com cuidado em DataFrames grandes)
pd.set_option('display.max_rows', None)

# Exibir conteúdo completo de cada célula
pd.set_option('display.max_colwidth', None)

# Exibe o DataFrame completo
print(df_geradores)

from fpdf import FPDF

def criar_pdf_email(quantidade_geradores):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título do PDF
    pdf.cell(200, 10, txt="Relatório Semanal de Geradores Configurados", ln=True, align='C')
    pdf.ln(10)

    # Corpo do e-mail
    conteudo_email = (
        f"Prezados,\n\n"
        f"Nesta semana, foram configurados um total de {quantidade_geradores} geradores de energia solar.\n\n"
        "Abaixo segue o arquivo com a tabela detalhada de cada gerador e sua composição.\n\n"
        "Atenciosamente,\n\n"
        "Yure\nEquipe Técnica"
    )
    pdf.multi_cell(0, 10, conteudo_email)

    # Salva o PDF
    pdf.output("email_para_marketing.pdf")

# Exemplo de uso
criar_pdf_email(quantidade_geradores=3)

df_geradores.to_csv("geradores_configurados_completo.csv", index=False)
