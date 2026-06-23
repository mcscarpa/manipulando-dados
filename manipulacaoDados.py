import pandas as pd
import plotly.express as px

pd.read_csv("Análise de Estoque.csv", sep=";")

base = pd.read_csv("Análise de Estoque.csv", sep=";")


#Fazendo tratamento na coluna PREÇO UNITÁRIO
base["PREÇO UNITÁRIO"] = pd.to_numeric(base["PREÇO UNITÁRIO"], errors="coerce")

# Fazendo consultas simples
print(base)
print(base.info())
print(base.head(10))
print(base[["ID LOJA", "PREÇO UNITÁRIO"]])

# # ANÁLISES

# Estoque Atual
print(base["MOVIMENTAÇÃO"].sum())

# # Estoque por loja
print(base.groupby("ID LOJA")["MOVIMENTAÇÃO"].sum())

# # Estoque por categoria
print(base.groupby("CATEGORIA")["MOVIMENTAÇÃO"].sum())

# # Estoque por loja e categoria
print(base.groupby(["ID LOJA", "CATEGORIA"])["MOVIMENTAÇÃO"].sum())
print(base.groupby("TIPO")["MOVIMENTAÇÃO"].sum())

# # Quantidade de devoluções
print(base[base["TIPO"] == "DEVOLUÇÃO"].groupby("TIPO").sum())

# # Quantidade de entradas
print(base[base["TIPO"] == "ENTRADA"].groupby("TIPO").sum())

# # Quantidade de saídas
print(base[base["TIPO"] == "SAÍDA"].groupby("TIPO").sum())


# GRÁFICOS

# Gráfico Estoque por Loja
px.histogram(base, x="ID LOJA", y="MOVIMENTAÇÃO", text_auto=True, color="ID LOJA").show()

#Gráfico Estoque por Categoria
px.histogram(base, x="CATEGORIA", y="MOVIMENTAÇÃO", text_auto=True, color="CATEGORIA").show()

#Gráfico Estoque por Loja Categoria
px.histogram(base, x=["CATEGORIA","ID LOJA"], y="MOVIMENTAÇÃO", text_auto=True, color="CATEGORIA").show()

# Gráfico de Entradas, Saídas e Devoluções
px.histogram(base, x="TIPO", y="MOVIMENTAÇÃO", text_auto=True, color="TIPO").show()

# Gerando arquivo HTML
gec = px.histogram(base, x=["TIPO","ID LOJA"], y="MOVIMENTAÇÃO", text_auto=True, color="TIPO")
gec.write_html("grafico_entradas_saidas_devolucoes.html")