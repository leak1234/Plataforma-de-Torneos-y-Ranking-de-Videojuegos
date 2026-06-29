from flask import render_template,request,redirect,url_for,session,flash
from app import db
from app.usuarios import bp_usuarios
from app.usuarios.models import Usuario


@bp_usuarios.route("/")
def index():

    if session.get("usuario_rol")!="admin":
        return redirect(url_for("bp_core.index"))

    usuarios=Usuario.query.all()

    return render_template("usuarios/index.html",usuarios=usuarios)



@bp_usuarios.route("/create",methods=["GET","POST"])
def create():

    if session.get("usuario_rol")!="admin":
        return redirect(url_for("bp_core.index"))


    if request.method=="POST":

        usuario=Usuario(
            usuario=request.form.get("usuario"),
            correo=request.form.get("correo"),
            password=request.form.get("password"),
            rol=request.form.get("rol"),
            estado="Activo"
        )


        db.session.add(usuario)
        db.session.commit()

        flash("Usuario creado","success")

        return redirect(url_for("bp_usuarios.index"))


    return render_template("usuarios/create.html")



@bp_usuarios.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):

    if session.get("usuario_rol")!="admin":
        return redirect(url_for("bp_core.index"))


    usuario=Usuario.query.get_or_404(id)


    if request.method=="POST":

        usuario.usuario=request.form.get("usuario")
        usuario.correo=request.form.get("correo")
        usuario.rol=request.form.get("rol")
        usuario.estado=request.form.get("estado")

        db.session.commit()

        flash("Usuario actualizado","success")

        return redirect(url_for("bp_usuarios.index"))


    return render_template("usuarios/editar.html",usuario=usuario)



@bp_usuarios.route("/eliminar/<int:id>")
def eliminar(id):

    if session.get("usuario_rol")!="admin":
        return redirect(url_for("bp_core.index"))


    usuario=Usuario.query.get_or_404(id)

    db.session.delete(usuario)

    db.session.commit()

    flash("Usuario eliminado","danger")

    return redirect(url_for("bp_usuarios.index"))



@bp_usuarios.route("/login",methods=["GET","POST"])
def login():

    if request.method=="POST":

        usuario=Usuario.query.filter_by(
            correo=request.form.get("correo"),
            password=request.form.get("password")
        ).first()


        if usuario:

            session["usuario_id"]=usuario.id_usuario
            session["usuario_nombre"]=usuario.usuario
            session["usuario_rol"]=usuario.rol


            return redirect(url_for("bp_core.index"))


        flash("Correo o contraseña incorrectos","danger")


    return render_template("usuarios/login.html")



@bp_usuarios.route("/registro",methods=["GET","POST"])
def registro():

    if request.method=="POST":

        nuevo=Usuario(
            usuario=request.form.get("usuario"),
            correo=request.form.get("correo"),
            password=request.form.get("password"),
            rol="usuario",
            estado="Activo"
        )


        db.session.add(nuevo)
        db.session.commit()


        flash("Registro exitoso","success")


        return redirect(url_for("bp_usuarios.login"))


    return render_template("usuarios/registro.html")



@bp_usuarios.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("bp_core.index"))