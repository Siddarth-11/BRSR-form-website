from sqlalchemy import create_engine , text
import os

db_connection_string = os.environ['DB_CONNECTION_STR']

engine = create_engine(
  db_connection_string, 
connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
}
)

with engine.connect() as conn:
  result = conn.execute(text("select * from SecA_part1"))
  print(result.all())

