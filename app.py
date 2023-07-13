from flask import Flask , render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def main_page():
  return render_template('mainpage.html')

@app.route("/PS.html")
def PS():
  return render_template('products.html')

@app.route("/Employees.html")
def employee():
  return render_template('employees.html')

@app.route("/Operations.html")
def operation():
  return render_template('operations.html')

@app.route("/input", methods = ['post'])
def send_to_db():
  data = request.form
  return render_template(form = data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
