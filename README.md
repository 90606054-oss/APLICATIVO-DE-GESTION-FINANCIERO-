# APLICATIVO DE GESTION FINANCIERO

Aplicación web para gestionar ingresos y gastos personales con recomendaciones de presupuesto según la regla 50/30/20.

## Requisitos

- Python 3.10+
- pip

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
python app.py
```

Then open:

http://localhost:5000

## Funcionalidades

- Definir ingreso mensual
- Registrar gastos con descripción, categoría y monto
- Visualizar resumen financiero
- Ver recomendación de presupuesto en 50/30/20
- Revisar gastos por categoría en gráficos
- Limpiar historial de datos
