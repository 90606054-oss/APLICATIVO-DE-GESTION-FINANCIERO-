from collections import defaultdict
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "finanzas-dashboard-2026"


def calcular_distribucion(ingreso):
    return {
        "Necesidades (50%)": ingreso * 0.50,
        "Deseos (30%)": ingreso * 0.30,
        "Ahorro Recomendado (20%)": ingreso * 0.20,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        accion = request.form.get("accion")

        if accion == "set_income":
            ingreso = float(request.form.get("ingreso", 0) or 0)
            session["ingreso_total"] = ingreso

        elif accion == "add_expense":
            descripcion = request.form.get("descripcion", "").strip()
            categoria = request.form.get("categoria", "otros")
            monto = float(request.form.get("monto", 0) or 0)

            if descripcion and monto > 0:
                gastos = session.setdefault("gastos_registrados", [])
                gastos.append({
                    "descripcion": descripcion,
                    "categoria": categoria,
                    "monto": round(float(monto), 2),
                })
                session["gastos_registrados"] = gastos

        elif accion == "clear_data":
            session.clear()

    ingreso_total = float(session.get("ingreso_total", 0) or 0)
    gastos = session.get("gastos_registrados", [])

    total_gastado = sum(float(gasto["monto"]) for gasto in gastos)
    capacidad_restante = ingreso_total - total_gastado

    distribucion = calcular_distribucion(ingreso_total) if ingreso_total > 0 else {}

    categorias = defaultdict(float)
    for gasto in gastos:
        categorias[gasto["categoria"]] += float(gasto["monto"])

    budget_plan = {k: round(v, 2) for k, v in distribucion.items()}
    category_data = {k: round(v, 2) for k, v in categorias.items()}

    return render_template(
        "index.html",
        ingreso_total=ingreso_total,
        gastos=gastos,
        total_gastado=round(total_gastado, 2),
        capacidad_restante=round(capacidad_restante, 2),
        budget_plan=budget_plan,
        category_data=category_data,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
