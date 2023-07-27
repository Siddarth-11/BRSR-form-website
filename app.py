from flask import Flask, render_template, request
from database import listed_entity_data,bussiness_activites,products_services, plants_located_data, market_served_data, company_details_data,Comm_ComplaintsGrievances,Investers_ComplaintsGrievances,Shareholders_ComplaintsGrievances,Emp_ComplaintsGrievances,Customer_ComplaintsGrievances,partners_ComplaintsGrievances,others_ComplaintsGrievances,entity_overview_data, landing_page_data , insert_employee_data

app = Flask(__name__)

@app.route("/")
def main_page():
  return render_template('landing_page.html')


@app.route("/DOE.html")
def DOE():
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


@app.route("/db", methods=['post'])
def input0():
  name = request.form.to_dict()
  landing_page_data(name)
  return render_template('landing_page.html', application=name)


@app.route("/inputdb", methods=['post'])
def input1():
  name = request.form.to_dict()
  listed_entity_data(name)
  return render_template('mainpage.html', application=name )

@app.route("/productdb", methods=['POST'])
def input2():
  name = request.form.to_dict()
  bussiness_activites(name)
  products_services(name)
  return render_template('products.html', application=name )

@app.route("/operationsdb", methods=['POST'])
def input3():
  name = request.form.to_dict()
  plants_located_data(name)
  market_served_data(name)
  return render_template('operations.html', application=name )

@app.route("/HSAdb", methods=['POST'])
def input4():
  name = request.form.to_dict()
  company_details_data(name)
  return render_template('HSA.html', application=name )

@app.route("/TADdb", methods=['POST'])
def input5():
  name = request.form.to_dict()
  Comm_ComplaintsGrievances(name)
  Investers_ComplaintsGrievances(name)
  Shareholders_ComplaintsGrievances(name)
  Emp_ComplaintsGrievances(name)
  Customer_ComplaintsGrievances(name)
  partners_ComplaintsGrievances(name)
  others_ComplaintsGrievances(name)
  entity_overview_data(name)
  return render_template('TAD.html', application=name )

@app.route("/Employeesdb", methods=['POST'])
def input6():
  name = request.form.to_dict()
  insert_employee_data(name)
  return render_template('employees.html', application=name )

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
