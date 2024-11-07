# Documentação do Script de Configuração de Geradores Solares

Este script automatiza a configuração de geradores de energia solar com base em produtos disponíveis em estoque, gerando uma lista de geradores configurados semanalmente e enviando um e-mail com o número de geradores configurados.

## Estrutura e Funcionamento do Código

### 1. Importação de Bibliotecas
O script usa `pandas` para manipulação de dados, `random` para geração de IDs únicos, e `FPDF` para a criação de um PDF com o relatório para o time de marketing.

### 2. Definição dos Dados de Estoque
Os dados de produtos são definidos como uma lista de dicionários com detalhes sobre categoria, ID, potência e nome do produto.

### 3. Filtragem dos Produtos por Categoria
Os produtos são classificados em três DataFrames separados (`painéis`, `inversores` e `controladores`) com base na coluna "Categoria".

### 4. Configuração dos Geradores
O código itera sobre cada combinação possível de painel, inversor e controlador. Para cada combinação que satisfaça a regra de compatibilidade (potências iguais), um gerador é configurado e adicionado à lista `geradores`.

Cada gerador recebe:
   - Um ID único gerado aleatoriamente.
   - Uma lista de IDs e nomes de produtos componentes do gerador.
   - Uma quantidade de cada componente.

### 5. Exportação dos Dados dos Geradores
Após a configuração, o DataFrame `df_geradores` é criado e exportado para o arquivo `geradores_configurados_completo.csv`.

### 6. Criação do PDF de Relatório
A função `criar_pdf_email` gera um PDF (`email_para_marketing.pdf`) com o conteúdo de um e-mail de resumo semanal.

### 7. Exemplo de Uso
No final do script, a função `criar_pdf_email` é chamada com o número de geradores configurados, e o DataFrame de geradores é exportado como CSV.

## Estrutura de Arquivos

- `geradores_configurados_completo.csv`: Arquivo com detalhes dos geradores configurados.
- `email_para_marketing.pdf`: PDF contendo o resumo de geradores para o e-mail.
- `script.py`: Código-fonte do script.

## Instruções de Manutenção

1. **Atualização de Estoque**: Ao adicionar novos produtos, insira-os na lista `dados` com os mesmos campos usados nos registros existentes.
2. **Alteração de Regras de Compatibilidade**: Caso a regra de compatibilidade de potência mude, ajuste a linha `if painel['Potencia em W'] == inversor['Potencia em W'] == controlador['Potencia em W']` na configuração dos geradores.
3. **Modificação no Layout do PDF**: Para personalizar o PDF, ajuste o conteúdo da função `criar_pdf_email`, alterando o título, corpo ou estrutura.
4. **Integração com Banco de Dados**: Para um estoque atualizado automaticamente, substitua a lista `dados` por uma consulta ao banco de dados.
