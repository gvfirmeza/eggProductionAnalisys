import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Ap1 Tic",
    page_icon="🥚",
    initial_sidebar_state="collapsed",
)

# Título do aplicativo
st.title('Análise da Produção de Ovos')


# csv 1


# Carregar o arquivo CSV
df = pd.read_csv('producaobrasiltodo.csv', encoding='utf-8')

st.write("""
### Produção no Brasil Todo (mil dúzias)
""")

# Corrigir o índice para usar os anos como eixo x
df.index = df['ano']

# Configurar o gráfico de linha com Altair e adicionar tooltip
line_chart = alt.Chart(df).mark_line(point=True).encode(
    x='ano:N',  # Usando o ano como eixo x
    y='valor:Q',
    tooltip=['ano:N', 'valor:Q']  # Adicionando tooltip
).properties(
    width=700,
    height=400,
).interactive()

st.altair_chart(line_chart)


# csv 2


# Carregar o arquivo CSV
df1 = pd.read_csv('csvexemplo.csv', encoding='utf-8')

st.write("""
### Maiores Produtoras
""")

# Exibir a tabela com os dados (opcional)
st.write(df1)


# csv 3


# Carregar o arquivo CSV
df2 = pd.read_csv('rankingempresas.csv')

st.write("""
### Ranking de Empresas por Ano Fiscal
""")

# Exibir a tabela com os dados (opcional)
st.write(df2)


# csv 4


st.write("""
## Produção por Estados do Nordeste
""")

# Carregar o arquivo CSV
df3 = pd.read_csv('producaoporestados.csv')

# Opção para selecionar o estado
state_options = ['Todos'] + list(df3['Estados'].unique())
selected_state = st.selectbox('Selecione um Estado', state_options)

# Filtrar o dataframe conforme a opção selecionada
if selected_state == 'Todos':
    filtered_df = df3
else:
    filtered_df = df3[df3['Estados'] == selected_state]

# Melt o dataframe filtrado para facilitar a plotagem
filtered_df_melt = filtered_df.melt(id_vars=['Estados', 'Ano'], var_name='Ano Producao', value_name='Producao')

# Configurar o gráfico de linha com Altair e adicionar tooltip
line_chart2 = alt.Chart(filtered_df_melt).mark_line(point=True).encode(
    x='Ano Producao:N',
    y='Producao:Q',
    color='Estados:N',
    tooltip=['Estados:N', 'Producao:Q']
).properties(
    width=700,
    height=400,
).interactive()

st.altair_chart(line_chart2)