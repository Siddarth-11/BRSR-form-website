from sqlalchemy import create_engine, text
#import os
#my_secret = os.environ['DB_CONNECTION_STR']
db_connection_string = "mysql+pymysql://v4roct5mdaikueazsv8c:pscale_pw_oRpbtfmznSeDuNE8Tn4OToU82crlTFXSsQobtsyhJQw@aws.connect.psdb.cloud/brsr_form?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from brsr_form.listed_entity"))

result_dicts = []
for row in result.all():
  result_dicts.append(list(row))

# print(result_dicts)
"""
def add_to_db(data):
  with engine.connect() as conn:
    query = text("INSERT INTO listed_entity(cin, name, year_of_incorporation, registered_office_address, corporate_address, email, telephone, website, financial_year, stock_exchange, paid_up_capital, contact_person_name, contact_person_telephone, contact_person_email, reporting_boundary) VALUES(:cin, :name, :year_of_incorporation, :registered_office_address, :corporate_address, :email, :telephone, :website, :financial_year, :stock_exchange, :paid_up_capital, :contact_person_name, :contact_person_telephone, :contact_person_email, :reporting_boundary)")

    conn.execute(query,
                cin = data['cin'],
                name = data['name'],
                year_of_incorporation = data['year_of_incorporation'],
                registered_office_address = data['registered_office_address'],
                corporate_address = data['corporate_address'],
                email = data['email'],
                telephone = data['telephone'],
                website = data['website'],
                financial_year = data['financial_year'],
                stock_exchange = data['stock_exchange'],
                paid_up_capital = data['paid_up_capital'],
                contact_person_name = data['contact_person_name'],
                contact_person_telephone = data['contact_person_telephone'],
                contact_person_email = data['contact_person_email'],
                reporting_boundary = data['reporting_boundary']
                )

"""


def load_data_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from brsr_form.listed_entity where id = 1"))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return list(rows[0])


def store_trial_data(data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO brsr_form.trial (Email_input, Tele_input, name_input) VALUES (siddarth, 12345, Sid)")
    
    conn.execute(query)
                  #{"email_input" : data['Email_input']},
                  #{"tele_input" : data['Tele_input']},
                  #{"Name_input" : data['name_input']})
