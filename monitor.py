from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def status():
    return render_template("index.html")

@app.route("/config")
def config():
    return redirect(url_for('config_system'))

@app.route("/config/system")
def config_system():
    return render_template("config.html", tab="system")

@app.route("/config/network")
def config_network():
    return render_template("config.html", tab="network")

@app.route("/config/services")
def config_services():
    return render_template("config.html", tab="services")

@app.route("/config/api")
def config_api():
    return render_template("config.html", tab="api")

if __name__ == "__main__":
    app.run(debug=True)
