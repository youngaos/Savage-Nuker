@echo off
echo Ejecutando el archivo Python...

python3 main.py

if errorlevel 1 (
    echo Error al ejecutar el archivo con python3. Intentando con python...
    python main.py
)

pause
