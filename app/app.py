from flask import Flask, render_template

app = Flask(__name__)

######################### Rotas principais #########################


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def indexhome():
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


####################################################################
if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port)
