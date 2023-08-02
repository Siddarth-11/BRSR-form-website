from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from database import listed_entity_data, bussiness_activites, products_services, plants_located_data, market_served_data, company_details_data, Comm_ComplaintsGrievances, Investers_ComplaintsGrievances, Shareholders_ComplaintsGrievances, Emp_ComplaintsGrievances, Customer_ComplaintsGrievances, partners_ComplaintsGrievances, others_ComplaintsGrievances, entity_overview_data, landing_page_data, insert_employee_data, management_process_disclosure_data

app = Flask(__name__, static_folder='templates')

app.config['SECRET_KEY'] = 'db_connection_string'
app.config[
  'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hw6o2s2nl54tzv0q18gv:pscale_pw_DviKRaHOfLWrqzmobgg23XK372GPwDv7XF3wsAxRAW2@aws.connect.psdb.cloud/brsr_form?charset=utf8mb4&ssl_ca=/etc/ssl/cert.pem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password_hash = db.Column(db.String(128), nullable=False)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)


@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
      flash('Please enter both username and password.', 'error')
    else:
      existing_user = User.query.filter_by(username=username).first()
      if existing_user:
        flash('Username already exists. Please choose a different one.',
              'error')
      else:
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))

  return render_template('register.html')


@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
      session['user_id'] = user.id
      flash('Login successful!', 'success')
      return redirect(url_for('dashboard'))
    else:
      flash('Invalid username or password. Please try again.', 'error')

  return render_template('login.html')


@app.route('/dashboard')
def dashboard():
  if 'user_id' in session:
    user = User.query.get(session['user_id'])
    return f"Welcome, {user.username}! This is your dashboard."
  else:
    flash('You need to log in first.', 'error')
    return redirect(url_for('login'))


def logout():
  session.pop('user_id', None)
  flash('You have been logged out.', 'info')
  return redirect(url_for('login'))


@app.route("/landing.html")
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


@app.route("/Section_B.html")
def SecB():
  return render_template('Section_B.html')


@app.route("/Section_C.html")
def SecC():
  return render_template('Section_C.html')


@app.route("/db", methods=['post'])
def input0():
  name = request.form.to_dict()
  landing_page_data(name)
  return render_template('mainpage.html', application=name)


@app.route("/inputdb", methods=['post'])
def input1():
  name = request.form.to_dict()
  listed_entity_data(name)
  return render_template('products.html', application=name)


@app.route("/productdb", methods=['POST'])
def input2():
  name = request.form.to_dict()
  bussiness_activites(name)
  products_services(name)
  return render_template('operations.html', application=name)


@app.route("/operationsdb", methods=['POST'])
def input3():
  name = request.form.to_dict()
  plants_located_data(name)
  market_served_data(name)
  return render_template('employees.html', application=name)


@app.route("/HSAdb", methods=['POST'])
def input4():
  name = request.form.to_dict()
  company_details_data(name)
  return render_template('TAD.html', application=name)


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
  return render_template('Section_B.html', application=name)


@app.route("/Employeesdb", methods=['POST'])
def input6():
  name = request.form.to_dict()
  insert_employee_data(name)
  return render_template('HSA.html', application=name)


@app.route("/Section_Bdb", methods=['POST'])
def input7():
  name = request.form.to_dict()
  print()
  management_process_disclosure_data(name)
  return render_template('Section_C.html', application=name)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
