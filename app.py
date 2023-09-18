from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def serve_pixel():
    # Lire l'image depuis le disque et la servir
    return send_file('im.png', mimetype='image/png')

if __name__ == '__main__':
         app.run()

