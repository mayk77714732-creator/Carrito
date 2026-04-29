from flask import Flask, render_template, request, redirect

app = Flask(__name__)

contactos = []
contador_id = 1

@app.route('/')
def index():
    return render_template('index.html', contactos=contactos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    global contador_id

    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        celular = request.form['celular']

        contactos.append({
            'id': contador_id,
            'nombre': nombre,
            'correo': correo,
            'celular': celular
        })

        contador_id += 1
        return redirect('/')

    return render_template('agregar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    contacto = next((c for c in contactos if c['id'] == id), None)

    if request.method == 'POST':
        contacto['nombre'] = request.form['nombre']
        contacto['correo'] = request.form['correo']
        contacto['celular'] = request.form['celular']
        return redirect('/')

    return render_template('editar.html', contacto=contacto)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    global contactos
    contactos = [c for c in contactos if c['id'] != id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
