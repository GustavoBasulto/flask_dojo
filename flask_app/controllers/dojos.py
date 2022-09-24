from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo


@app.route("/dojos")
def dojos(): 
    return render_template("index.html", dojos=Dojo.get_all())
    
@app.route("/agregar_dojo/procesar", methods=["POST"])
def agregar_dojo_procesar():
    data = {
        "nombre": request.form["nombre"]
    }
    Dojo.save(data)
    flash(f"exito al agregar el dojo {data['nombre']}", "success")
    return redirect("/dojos")

    
@app.route('/dojos/<int:id>')
def dojo_details(id):
    data = {
        'dojo_id': id
    }
    dojo_ninjas = Dojo.get_dojo_ninjas(data)
    if dojo_ninjas:
        return render_template('dojos.html', dojo=dojo_ninjas)
    else:
        flash("Dojo no posee Ninjas", "warning")
        return redirect('/dojos')