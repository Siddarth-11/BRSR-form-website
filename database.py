from sqlalchemy import create_engine , text
#import os
#my_secret = os.environ['DB_CONNECTION_STR']
db_connection_string = "mysql+pymysql://2d830d13l459skh0o3u3:pscale_pw_Vie8hUHWvOX2FizocLq7WOmhhIOV6C1UC8xLfmAiZ5N@aws.connect.psdb.cloud/brsr_form?charset=utf8mb4"

engine = create_engine(
  db_connection_string, 
connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
}
)

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
                )

