# Importando e Manipulando Dados

## Sobre o Projeto

Importando e Manipulando Dados é um projeto desenvolvido em Python com o objetivo de praticar técnicas de importação, tratamento, análise e visualização de dados utilizando bibliotecas amplamente utilizadas no mercado de dados.

A aplicação realiza a leitura de um arquivo CSV contendo informações de movimentação de estoque, efetua o tratamento dos dados, gera análises estatísticas e produz gráficos interativos para facilitar a interpretação das informações.

Além das análises realizadas diretamente no terminal, o projeto também gera um arquivo HTML contendo visualizações interativas criadas com Plotly.

---

## Tecnologias Utilizadas

* Python
* Pandas
* Plotly Express

---

## Tratamento dos Dados

Antes das análises, foi realizado o tratamento da coluna **PREÇO UNITÁRIO**, convertendo seus valores para formato numérico e tratando possíveis inconsistências através da função `pd.to_numeric()`.

---

## Análises Realizadas

O sistema realiza diversas consultas sobre os dados, entre elas:

### Estoque Atual

* Soma total das movimentações registradas.

### Estoque por Loja

* Quantidade total movimentada por cada loja.

### Estoque por Categoria

* Quantidade total movimentada por categoria de produto.

### Estoque por Loja e Categoria

* Análise combinada entre lojas e categorias.

### Movimentações por Tipo

* Entradas
* Saídas
* Devoluções

### Quantidade de Entradas, Saídas e Devoluções

* Filtragem e agrupamento dos registros para identificar o volume de cada tipo de movimentação.

---

## Visualizações Geradas

O projeto utiliza a biblioteca Plotly Express para criar gráficos interativos:

* Estoque por Loja
* Estoque por Categoria
* Estoque por Loja e Categoria
* Entradas, Saídas e Devoluções

Todos os gráficos podem ser explorados de forma interativa, permitindo zoom, filtros e visualização detalhada dos dados.

---

## Exportação para HTML

Além da exibição dos gráficos durante a execução do programa, o projeto permite exportar gráficos interativos para arquivos HTML utilizando Plotly.

Exemplo:

```text
grafico_entradas_saidas_devolucoes.html
```

Esse arquivo pode ser aberto em qualquer navegador sem necessidade de executar o código novamente.

---

## Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/mcscarpa/manipulando-dados.git
```

### 2. Acesse a pasta do projeto

```bash
cd manipulando-dados
```

### 3. Instale as dependências

```bash
pip install pandas

pip install plotly.express
```

### 4. Execute o programa

```bash
python manipulacaoDados.py
```

---
por @mcscarpa
