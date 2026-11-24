
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv('citas_medicas.csv')

# Título del dashboard
st.title('Dashboard de Gestión de Citas Médicas')

# Gráfico de citas por especialidad
st.subheader('Citas por Especialidad')

fig1 = px.bar(
    df['especialidad'].value_counts(),
    labels={'value': 'Cantidad'}
)

st.plotly_chart(fig1)

# Gráfico del estado de las citas
st.subheader('Estado de las Citas')

fig2 = px.pie(
    df,
    names='estado'
)

st.plotly_chart(fig2)

# Preparar fechas
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month

# Agrupar citas por mes
citas_mes = df.groupby('mes').size().reset_index(name='cantidad')

# Gráfico de citas por mes
st.subheader('Citas por Mes')

fig3 = px.line(
    citas_mes,
    x='mes',
    y='cantidad',
    markers=True
)

st.plotly_chart(fig3)
