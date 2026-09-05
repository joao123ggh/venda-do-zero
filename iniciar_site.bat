@echo off
chcp 65001 >nul
title Servidor Venda do Zero - FAÇA SUA PRIMEIRA VENDA DO ZERO

echo ======================================================================
echo    VENDA DO ZERO - LANDING PAGE PROFISSIONAL (FLASK + PYTHON)
echo ======================================================================
echo.

:: 1. Localizar executável do Python
set PYTHON_CMD=

:: Verifica se python está no PATH
python --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python
    goto :PYTHON_OK
)

:: Verifica py launcher
py --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=py
    goto :PYTHON_OK
)

:: Verifica diretório padrão do instalador de usuário
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set PYTHON_CMD="%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    goto :PYTHON_OK
)

:: Procura em qualquer versão instalada em AppData
for /d %%D in ("%LOCALAPPDATA%\Programs\Python\Python*") do (
    if exist "%%D\python.exe" (
        set PYTHON_CMD="%%D\python.exe"
        goto :PYTHON_OK
    )
)

echo [ERRO] Python não foi encontrado no sistema!
echo Por favor, instale o Python através do site oficial: https://www.python.org/
echo ou execute no PowerShell: winget install Python.Python.3.12
echo.
pause
exit /b 1

:PYTHON_OK
echo [1/3] Python detectado com sucesso!
%PYTHON_CMD% --version
echo.

echo [2/3] Verificando dependencias necessarias (Flask)...
%PYTHON_CMD% -m pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo [AVISO] Ocorreu uma pendencia com o pip, continuando a inicializacao...
) else (
    echo Dependencias verificadas com sucesso!
)
echo.

echo [3/3] Iniciando o servidor Flask e abrindo o navegador...
echo.
echo ======================================================================
echo  >> SITE RODANDO EM: http://127.0.0.1:5000
echo  >> Para encerrar o servidor, feche esta janela ou aperte CTRL+C.
echo ======================================================================
echo.

%PYTHON_CMD% server.py

pause
