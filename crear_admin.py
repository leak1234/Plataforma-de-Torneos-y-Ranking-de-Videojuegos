from app import create_app,db
from app.usuarios.models import Usuario

app=create_app()

with app.app_context():

    admin=Usuario(
        usuario="admin",
        correo="admin@gmail.com",
        password="123456",
        rol="admin",
        estado="Activo"
    )

    db.session.add(admin)
    db.session.commit()

    print("Admin creado correctamente")