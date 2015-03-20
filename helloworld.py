from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    titulo = "tutoFlask"
    usuario = [{'nombre': 'Alejandro'},
				{'nombre': 'Miguel'},
				{'nombre': 'Mario'},
				{'nombre': 'Osmary'},
				{'nombre': 'Dachi'},
				{'nombre': 'Luis'},
				{'nombre': 'Aldo'}]
    return render_template('index.html',
                           titulo=titulo,
                           usuario=usuario)

if __name__ == '__main__':
    app.run(host='0.0.0.0')