@echo off
title Analisador de Telefones
echo ================================
echo  Iniciando o sistema Streamlit...
echo ================================
echo.

REM Abre o navegador automaticamente
set BROWSER=chrome

REM Executa o streamlit
python -m streamlit run app.py

echo.
echo O sistema foi fechado.
pause