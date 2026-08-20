from flask import Flask
from flask_cors import CORS
from database import db
from controllers.curso_controller import curso_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.url_map.strict_slashes = False
    app.config['SQLALCHEMY_DATABASE_URI'] = '' # inserir credenciais do banco de dados
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registro do Blueprint de Cursos
    app.register_blueprint(curso_bp, url_prefix='/api/cursos')

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)