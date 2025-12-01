import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analisador de Telefones", layout="centered")

st.title("📊 Analisador de Telefones por Data")
st.write("Envie arquivos CSV contendo as colunas **Data/Hora** e **Origem**.")

uploaded_files = st.file_uploader(
    "Selecione os arquivos CSV",
    type=["csv"],
    accept_multiple_files=True
)

if uploaded_files:
    lista_df = []

    for file in uploaded_files:
        df = pd.read_csv(file)
        df.columns = df.columns.str.lower()

        col_data = None
        col_origem = None

        for c in df.columns:
            if "data" in c:  # encontra "data" ou "data/hora"
                col_data = c
            if "origem" in c:
                col_origem = c

        if col_data is None or col_origem is None:
            st.error(f"🚫 Arquivo ignorado: {file.name} (faltam Data/Hora ou Origem)")
            continue

        # converte data/hora
        df[col_data] = pd.to_datetime(df[col_data], errors="coerce")
        df["data"] = df[col_data].dt.date

        df = df[["data", col_origem]].rename(columns={col_origem: "telefone"})
        lista_df.append(df)

    if lista_df:
        dados = pd.concat(lista_df, ignore_index=True)

        # agrupamento
        agrupado = (
            dados.groupby(["data", "telefone"])
            .size()
            .reset_index(name="ocorrencias")
        )

        # 🔥 GERA A TABELA PIVOTADA
        tabela_final = agrupado.pivot_table(
            index="telefone",
            columns="data",
            values="ocorrencias",
            fill_value=0
        )

        # Coluna total
        tabela_final["Total"] = tabela_final.sum(axis=1)

        # Ordena por total (opcional)
        tabela_final = tabela_final.sort_values("Total", ascending=False)

        st.subheader("Resultado Consolidado (por número e por data)")
        st.dataframe(tabela_final, use_container_width=True)

        # Download
        csv = tabela_final.to_csv().encode("utf-8")
        st.download_button(
            "📥 Baixar Resultado (CSV)",
            csv,
            "resultado_pivotado.csv",
            "text/csv"
        )

    else:
        st.warning("Nenhum arquivo válido foi enviado.")
