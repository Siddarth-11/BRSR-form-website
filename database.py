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
     "GrievanceRedressalMechanism" : info['n32'] ,
      "GrievanceRedressPolicyLink" : info['n33'] ,
    "NumComplaintsFiledCurrentYear" : info['n34'] ,
    "NumComplaintsPendingCurrentYear" : info['n35'] ,
    "RemarksCurrentYear" : info['n36'],
      "NumComplaintsFiledPreviousYear" : info['n37'] ,
      "NumComplaintsPendingPreviousYear" : info['n38'] ,
      "RemarksPreviousYear" : info['n39'] 
    }) 

def others_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text("insert into others_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)")

  conn.execute(query , {
     "GrievanceRedressalMechanism" : info['n30'] ,
      "GrievanceRedressPolicyLink" : info['n41'] ,
    "NumComplaintsFiledCurrentYear" : info['n42'] ,
    "NumComplaintsPendingCurrentYear" : info['n43'] ,
    "RemarksCurrentYear" : info['n44'],
      "NumComplaintsFiledPreviousYear" : info['n45'] ,
      "NumComplaintsPendingPreviousYear" : info['n46'] ,
      "RemarksPreviousYear" : info['n47'] 
    }) 
    
def landing_page_data(info):
  with engine.connect() as conn:
    query = text("insert into landing_page (report_id , begin_period , end_period) values (:report_id , :begin_period , :end_period)")

    conn.execute(query , {
     "report_id" : info['report_id'],
     "begin_period" : info['begin_period'],
     "end_period" : info['end_period']
   })

def entity_overview_data(info):
  with engine.connect() as conn:
    query = text("insert into entity_overview (MaterialIssue1 , RiskOpportunity1 , Rationale1 , Approach1 , FinancialImplications1, MaterialIssue2 , RiskOpportunity2 , Rationale2 , Approach2 , FinancialImplications2) values (:s1 , :s2 , :s3 , :s4 , :s5, :s6 , :s7 , :s8 ,:s9 , :s10)")

    conn.execute(query , {
     "s1": info['MaterialIssue1'],
     "s2": info['RiskOpportunity1'],
     "s3": info['Rationale1'],
     "s4": info['Approach1'],
     "s5": info['FinancialImplications1'],
     "s6": info['MaterialIssue2'],
     "s7": info['RiskOpportunity2'],
     "s8": info['Rationale2'],
     "s9": info['Approach2'],
     "s10": info['FinancialImplications2']
  })

def insert_employee_data(info):
    with engine.connect() as conn:
        
        employees_query = text("INSERT INTO Employees (Permanent,permanent_male1, permanent_female1, permanent_male2,permanent_female2, other_than_permanent, other_than_permanent_male1, other_than_permanent_female1, other_than_permanent_male2,other_than_permanent_female2,total_employees, total_male1,total_female1,total_male2 , total_female2) VALUES (:permanent, :permanent_male1, :permanent_female1, :permanent_male2, :permanent_female2,other_than_permanent,:other_than_permanent_male1,:other_than_permanent_female1,:other_than_permanent_male2,:other_than_permanent_female2, :total_employees, :total_male1, :total_female1, :total_male2 , :total_female2)")

        conn.execute(employees_query, {
            "permanent": info['a1'],
            "permanent_male1": info["a2"],
            "permanent_female1": info["a3"],
            "permanent_male2": info["a4"],
            "permanent_female2": info["a5"],
            "other_than_permanent": info["a6"],
            "other_than_permanent_male1": info["a7"],
            "other_than_permanent_female1": info["a8"],
            "other_than_permanent_male2": info["a9"],
            "other_than_permanent_female2": info["a10"],
            "total_employees": info["a11"],
            "total_male1": info["a12"],
            "total_female1": info["a13"],
            "total_male2": info["a14"],
            "total_female2": info["a15"]
             })

        workers_query = text("INSERT INTO Workers (Permanent,permanent_male1, permanent_female1, permanent_male2,permanent_female2, other_than_permanent, other_than_permanent_male1, other_than_permanent_female1, other_than_permanent_male2,other_than_permanent_female2,total_employees, total_male1,total_female1,total_male2 , total_female2) VALUES (:permanent, :permanent_male1, :permanent_female1, :permanent_male2, :permanent_female2,other_than_permanent,:other_than_permanent_male1,:other_than_permanent_female1,:other_than_permanent_male2,:other_than_permanent_female2, :total_employees, :total_male1, :total_female1, :total_male2 , :total_female2)")

        conn.execute(workers_query, {
            "permanent": info['a16'],
            "permanent_male1": info["a17"],
            "permanent_female1": info["a18"],
            "permanent_male2": info["a19"],
            "permanent_female2": info["a20"],
            "other_than_permanent": info["a21"],
            "other_than_permanent_male1": info["a22"],
            "other_than_permanent_female1": info["a23"],
            "other_than_permanent_male2": info["a24"],
            "other_than_permanent_female2": info["a25"],
            "total_employees": info["a26"],
            "total_male1": info["a27"],
            "total_female1": info["a28"],
            "total_male2": info["a29"],
            "total_female2": info["a30"]
        })

        differently_abled_employees_query = text("INSERT INTO DifferentlyAbledEmployees (Permanent,permanent_male1, permanent_female1, permanent_male2,permanent_female2, other_than_permanent, other_than_permanent_male1, other_than_permanent_female1, other_than_permanent_male2,other_than_permanent_female2,total_employees, total_male1,total_female1,total_male2 , total_female2) VALUES (:permanent, :permanent_male1, :permanent_female1, :permanent_male2, :permanent_female2,other_than_permanent,:other_than_permanent_male1,:other_than_permanent_female1,:other_than_permanent_male2,:other_than_permanent_female2, :total_employees, :total_male1, :total_female1, :total_male2 , :total_female2)")

        conn.execute(differently_abled_employees_query, {
            "permanent": info['a31'],
            "permanent_male1": info["a32"],
            "permanent_female1": info["a33"],
            "permanent_male2": info["a34"],
            "permanent_female2": info["a35"],
            "other_than_permanent": info["a36"],
            "other_than_permanent_male1": info["a37"],
            "other_than_permanent_female1": info["a38"],
            "other_than_permanent_male2": info["a39"],
            "other_than_permanent_female2": info["a40"],
            "total_employees": info["a41"],
            "total_male1": info["a42"],
            "total_female1": info["a43"],
            "total_male2": info["a44"],
            "total_female2": info["a45"]
        })
      
        differently_abled_workers_query = text("INSERT INTO DifferentlyAbledWorkers (Permanent,permanent_male1, permanent_female1, permanent_male2,permanent_female2, other_than_permanent, other_than_permanent_male1, other_than_permanent_female1, other_than_permanent_male2,other_than_permanent_female2,total_employees, total_male1,total_female1,total_male2 , total_female2) VALUES (:permanent, :permanent_male1, :permanent_female1, :permanent_male2, :permanent_female2,other_than_permanent,:other_than_permanent_male1,:other_than_permanent_female1,:other_than_permanent_male2,:other_than_permanent_female2, :total_employees, :total_male1, :total_female1, :total_male2 , :total_female2)")

        conn.execute(differently_abled_workers_query, {
            "permanent": info['a46'],
            "permanent_male1": info["a47"],
            "permanent_female1": info["a48"],
            "permanent_male2": info["a49"],
            "permanent_female2": info["a50"],
            "other_than_permanent": info["a51"],
            "other_than_permanent_male1": info["a52"],
            "other_than_permanent_female1": info["a53"],
            "other_than_permanent_male2": info["a54"],
            "other_than_permanent_female2": info["a55"],
            "total_employees": info["a56"],
            "total_male1": info["a57"],
            "total_female1": info["a58"],
            "total_male2": info["a59"],
            "total_female2": info["a60"]
        })

        women_participation_query = text("INSERT INTO WomenParticipation (Board_of_Directors_Total, Board_of_Directors_Female1,  Board_of_Directors_Female2,Key_Management_Personnel_Total, Key_Management_Personnel_Female1, Key_Management_Personnel_Female2) VALUES (:board_of_directors_total, :board_of_directors_female1, :board_of_directors_female2,:key_management_personnel_total, :key_management_personnel_female1 , :key_management_personnel_female2)")

        conn.execute(women_participation_query, {
            "board_of_directors_total": info["a61"],
            "board_of_directors_female1": info["a62"],
            "board_of_directors_female2": info["a63"],
            "key_management_personnel_total": info["a64"],
            "key_management_personnel_female1": info["a65"],
            "key_management_personnel_female2": info["a66"]
        })

        pe_turnover_rate_query = text("INSERT INTO PE_TurnoverRatePermanent (PE_fy_current_1, PE_fy_current_2, PE_fy_current_3, PE_fy_previous_1, PE_fy_previous_2, PE_fy_previous_3, PE_fy_year_prior_1, PE_fy_year_prior_2, PE_fy_year_prior_3) VALUES (:PE_fy_current_1, :PE_fy_current_2, :PE_fy_current_3, :PE_fy_previous_1, :PE_fy_previous_2, :PE_fy_previous_3, :PE_fy_year_prior_1, :PE_fy_year_prior_2, :PE_fy_year_prior_3)")

        conn.execute(pe_turnover_rate_query, {
            "PE_fy_current_1": info["a67"],
            "PE_fy_current_2": info["a68"],
            "PE_fy_current_3": info["a69"],
            "PE_fy_previous_1": info["a70"],
            "PE_fy_previous_2": info["a71"],
            "PE_fy_previous_3": info["a72"],
            "PE_fy_year_prior_1": info["a73"],
            "PE_fy_year_prior_2": info["a74"],
            "PE_fy_year_prior_3": info["a75"]
        })

        pw_turnover_rate_query = text("INSERT INTO PW_TurnoverRatePermanent (PW_fy_current_1, PW_fy_current_2, PW_fy_current_3, PW_fy_previous_1, PW_fy_previous_2, PW_fy_previous_3, PW_fy_year_prior_1, PW_fy_year_prior_2, PW_fy_year_prior_3) VALUES (:PW_fy_current_1, :PW_fy_current_2, :PW_fy_current_3, :PW_fy_previous_1, :PW_fy_previous_2, :PW_fy_previous_3, :PW_fy_year_prior_1, :PW_fy_year_prior_2, :PW_fy_year_prior_3)")

        conn.execute(pw_turnover_rate_query, {
            "PW_fy_current_1": info["a76"],
            "PW_fy_current_2": info["a77"],
            "PW_fy_current_3": info["a78"],
            "PW_fy_previous_1": info["a79"],
            "PW_fy_previous_2": info["a80"],
            "PW_fy_previous_3": info["a81"],
            "PW_fy_year_prior_1": info["a82"],
            "PW_fy_year_prior_2": info["a83"],
            "PW_fy_year_prior_3": info["a84"]
        })  