from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route("/ninjas")
def ninjas():
    dojos = Dojo.get_all()
    return render_template("agregar_ninja.html", dojos=dojos)

@app.route("/agregar_ninja/procesar", methods=["POST"])
def agregar_ninja_procesar():
    data = {
        "nombre": request.form["nombre"],
        "apellido" : request.form["apellido"],
        "edad" : request.form["edad"],
        "id_dojo":request.form["dojo"]
    }
    Ninja.save(data)
    flash(f"exito al agregar al ninja {data['nombre']}","success")
    return redirect(f"/dojos/{data['id_dojo']}")
