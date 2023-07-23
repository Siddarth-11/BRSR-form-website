from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['db_connection_string']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from brsr_form.listed_entity"))

  result_dicts = []
  for row in result.all():
    result_dicts.append(list(row))

  print(result_dicts)

def listed_entity_data(info):
  with engine.connect() as conn:
    query = text("INSERT INTO listed_entity(cin, year_of_incorporation, corporate_address, email, telephone, website, financial_year, stock_exchange, paid_up_capital, contact_person_telephone, contact_person_email, reporting_boundary) VALUES(:cin, :year_of_incorporation, :corporate_address, :email, :telephone, :website, :financial_year, :stock_exchange, :paid_up_capital, :contact_person_telephone, :contact_person_email, :reporting_boundary)")

    conn.execute(query,{
                 "cin" : info['cin'],
                 "year_of_incorporation" : info['year_of_incorporation'],
                 "corporate_address" : info['corporate_address'],
                 "email" : info['email'],
                 "telephone" : info['telephone'],
                 "website" : info['website'],
                 "financial_year" : info['financial_year'],
                 "stock_exchange" : info['stock_exchange'],
                 "paid_up_capital" : info['paid_up_capital'],
                 "contact_person_telephone" : info['contact_person_telephone'],
                 "contact_person_email" : info['contact_person_email'],
                 "reporting_boundary" : info['reporting_boundary']})


def bussiness_activites(info):
  with engine.connect() as conn:
    query = text("INSERT INTO BusinessActivities (DescriptionOfMainActivity_1,DescriptionOfBusinessActivity_1,TurnoverPercentage_1,DescriptionOfMainActivity_2,DescriptionOfBusinessActivity_2,TurnoverPercentage_2) VALUES (:DescriptionOfMainActivity_1,:DescriptionOfBusinessActivity_1,:TurnoverPercentage_1,:DescriptionOfMainActivity_2,:DescriptionOfBusinessActivity_2,:TurnoverPercentage_2)")

    conn.execute(query , {
     "DescriptionOfMainActivity_1" : info['main_Activity_1'] ,
    "DescriptionOfBusinessActivity_1" : info['bussiness_Acitvity_1'] ,
    "TurnoverPercentage_1" : info['turnover_1'] ,
    "DescriptionOfMainActivity_2" : info['main_Activity_2'] ,
    "DescriptionOfBusinessActivity_2" : info['bussiness_Acitvity_2'] ,
    "TurnoverPercentage_2" : info['turnover_2']})

def products_services(info):
  with engine.connect() as conn:
    query = text("insert into ProductsServices (ProductServiceDescription_1,NICCode_1 ,TurnoverPercentage_1 ,ProductServiceDescription_2 ,NICCode_2 ,TurnoverPercentage_2 ,ProductServiceDescription_3 ,NICCode_3 ,TurnoverPercentage_3) values (:ProductServiceDescription_1,:NICCode_1 ,:TurnoverPercentage_1 ,:ProductServiceDescription_2 ,:NICCode_2 ,:TurnoverPercentage_2 ,:ProductServiceDescription_3 ,:NICCode_3 ,:TurnoverPercentage_3)")

    conn.execute(query , {
     "ProductServiceDescription_1" : info['P/S_1'] ,
    "NICCode_1" : info['nic_number_1'] ,
    "TurnoverPercentage_1" : info['turnover_contributed_1'] ,
    "ProductServiceDescription_2" : info['P/S_2'] ,
    "NICCode_2" : info['nic_number_2'] ,
    "TurnoverPercentage_2" : info['turnover_contributed_2'],
    "ProductServiceDescription_3" : info['P/S_3'] ,
    "NICCode_3" : info['nic_number_3'] ,
    "TurnoverPercentage_3" : info['turnover_contributed_3']
    })


def plants_located_data(info):
  with engine.connect() as conn:
    query = text("insert into plants_located (national_no_of_plants,national_no_of_offices,national_total_locations,international_no_of_plants,international_no_of_offices,international_total_locations) values (:national_no_of_plants,:national_no_of_offices,:national_total_locations,:international_no_of_plants,:international_no_of_offices,:international_total_locations)")

    conn.execute(query , {
     "national_no_of_plants" : info['national_1'] ,
    "national_no_of_offices" : info['national_2'] ,
    "national_total_locations" : info['national_3'] ,
    "international_no_of_plants" : info['international_1'] ,
    "international_no_of_offices" : info['international_2'] ,
    "international_total_locations" : info['international_3']
    })

def market_served_data(info):
  with engine.connect() as conn:
    query = text("insert into market_served (national_locations,international_locations,exports_contribution,customer_types) values (:national_locations,:international_locations,:exports_contribution,:customer_types)")

    conn.execute(query , {
     "national_locations" : info['national_locations'] ,
    "international_locations" : info['international_locations'] ,
    "exports_contribution" : info['exports_contribution'] ,
    "customer_types" : info['customer_types']
    })

def company_details_data(info):
  with engine.connect() as conn:
    query = text("insert into CompanyDetails (Name,Relationship ,SharePercentage,ParticipatesInBusinessResponsibility ,CSRApplicable,TurnoverInRs,NetWorthInRs) values (:Name,:Relationship ,:SharePercentage,:ParticipatesInBusinessResponsibility ,:CSRApplicable,:TurnoverInRs,:NetWorthInRs)")

    conn.execute(query , {
     "Name" : info['Name'] ,
    "Relationship" : info['Relationship'] ,
    "SharePercentage" : info['SharePercentage'] ,
    "ParticipatesInBusinessResponsibility" : info['ParticipatesInBusinessResponsibility'],
      "CSRApplicable" : info['CSRApplicable'] ,
      "TurnoverInRs" : info['TurnoverInRs'] ,
      "NetWorthInRs" : info['NetWorthInRs'] 
    })   

'''
def load_data_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from brsr_form.listed_entity where id = 1"))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return list(rows[0])
'''
def Comm_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text("insert into Comm_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)")

    conn.execute(query , {
     "GrievanceRedressalMechanism" : info['GrievanceRedressalMechanism'] ,
      "GrievanceRedressPolicyLink" : info['GrievanceRedressPolicyLink'] ,
    "NumComplaintsFiledCurrentYear" : info['NumComplaintsFiledCurrentYear'] ,
    "NumComplaintsPendingCurrentYear" : info['NumComplaintsPendingCurrentYear'] ,
    "RemarksCurrentYear" : info['RemarksCurrentYear'],
      "NumComplaintsFiledPreviousYear" : info['NumComplaintsFiledPreviousYear'] ,
      "NumComplaintsPendingPreviousYear" : info['NumComplaintsPendingPreviousYear'] ,
      "RemarksPreviousYear" : info['RemarksPreviousYear'] 
    })   

def Investers_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text("insert into Investers_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)")

    conn.execute(query , {
     "GrievanceRedressalMechanism" : info['n0'] ,
      "GrievanceRedressPolicyLink" : info['n1'] ,
    "NumComplaintsFiledCurrentYear" : info['n2'] ,
    "NumComplaintsPendingCurrentYear" : info['n3'] ,
    "RemarksCurrentYear" : info['n4'],
      "NumComplaintsFiledPreviousYear" : info['n5'] ,
      "NumComplaintsPendingPreviousYear" : info['n6'] ,
      "RemarksPreviousYear" : info['n7'] 
    }) 

def Shareholders_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text("insert into Shareholders_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)")

    conn.execute(query , {
     "GrievanceRedressalMechanism" : info['n8'] ,
      "GrievanceRedressPolicyLink" : info['n9'] ,
    "NumComplaintsFiledCurrentYear" : info['n10'] ,
    "NumComplaintsPendingCurrentYear" : info['n11'] ,
    "RemarksCurrentYear" : info['n12'],
      "NumComplaintsFiledPreviousYear" : info['n13'] ,
      "NumComplaintsPendingPreviousYear" : info['n14'] ,
      "RemarksPreviousYear" : info['n15'] 
    }) 

def Emp_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text("insert into Emp_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)")

    conn.execute(query , {
     "GrievanceRedressalMechanism" : info['n16'] ,
      "GrievanceRedressPolicyLink" : info['n17'] ,
    "NumComplaintsFiledCurrentYear" : info['n18'] ,
    "NumComplaintsPendingCurrentYear" : info['n19'] ,
    "RemarksCurrentYear" : info['n20'],
      "NumComplaintsFiledPreviousYear" : info['n21'] ,
      "NumComplaintsPendingPreviousYear" : info['n22'] ,
      "RemarksPreviousYear" : info['n23'] 
    }) 

def Customer_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text("insert into Customer_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)")

    conn.execute(query , {
     "GrievanceRedressalMechanism" : info['n24'] ,
      "GrievanceRedressPolicyLink" : info['n25'] ,
    "NumComplaintsFiledCurrentYear" : info['n26'] ,
    "NumComplaintsPendingCurrentYear" : info['n27'] ,
    "RemarksCurrentYear" : info['n28'],
      "NumComplaintsFiledPreviousYear" : info['n29'] ,
      "NumComplaintsPendingPreviousYear" : info['n30'] ,
      "RemarksPreviousYear" : info['n31'] 
    }) 

def partners_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text("insert into partners_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)")

    conn.execute(query , {
     "GrievanceRedressalMechanism" : info['n31'] ,
      "GrievanceRedressPolicyLink" : info['n32'] ,
    "NumComplaintsFiledCurrentYear" : info['n33'] ,
    "NumComplaintsPendingCurrentYear" : info['n34'] ,
    "RemarksCurrentYear" : info['n35'],
      "NumComplaintsFiledPreviousYear" : info['n36'] ,
      "NumComplaintsPendingPreviousYear" : info['n37'] ,
      "RemarksPreviousYear" : info['n38'] 
    }) 

def others_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text("insert into others_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)")

    conn.execute(query , {
     "GrievanceRedressalMechanism" : info['n39'] ,
      "GrievanceRedressPolicyLink" : info['n40'] ,
    "NumComplaintsFiledCurrentYear" : info['n41'] ,
    "NumComplaintsPendingCurrentYear" : info['n42'] ,
    "RemarksCurrentYear" : info['n43'],
      "NumComplaintsFiledPreviousYear" : info['n44'] ,
      "NumComplaintsPendingPreviousYear" : info['n45'] ,
      "RemarksPreviousYear" : info['n46'] 
    }) 
