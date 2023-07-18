from flask import Flask, render_template, jsonify, request
from database import engine, load_data_from_db, store_trial_data

app = Flask(__name__)
'''
def load_from_db():
  with engine.connect() as conn:
    result = conn.execute("select * from brsr_form.listed_entity")
    data = []
    for row in result.all():
      data.append(dict(row))
      return data
'''
'''
@app.route("/<id>")
def load_db(id):
  load = load_data_from_db(id)
  return jsonify(load)
'''


@app.route(
  "/", )
def main_page():
  return render_template('mainpage.html')


@app.route("/DOE.html")
def main_page1():
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


@app.route("/HSA.html")
def HSA():
  return render_template('HSA.html')


@app.route("/TDC.html")
def TDC():
  return render_template('TAD.html')


@app.route("/trial.html")
def trial():
  return render_template("trial.html")


# data = request.args
# return jsonify(list(data))


@app.route("/inputdb", methods=['post'])
def input():
  name = request.form.to_dict()
  store_trial_data(name)
  return render_template('Form_submitted.html', application=name)


'''
@app.route("/input", methods=["POST" , "GET"])
def send_to_db():
  data = request.form
  return jsonify(list(data))
'''

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
