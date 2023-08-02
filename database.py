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
    query = text(
      "INSERT INTO listed_entity(cin, year_of_incorporation, corporate_address, email, telephone, website, financial_year, stock_exchange, paid_up_capital, contact_person_telephone, contact_person_email, reporting_boundary) VALUES(:cin, :year_of_incorporation, :corporate_address, :email, :telephone, :website, :financial_year, :stock_exchange, :paid_up_capital, :contact_person_telephone, :contact_person_email, :reporting_boundary)"
    )

    conn.execute(
      query, {
        "cin": info['cin'],
        "year_of_incorporation": info['year_of_incorporation'],
        "corporate_address": info['corporate_address'],
        "email": info['email'],
        "telephone": info['telephone'],
        "website": info['website'],
        "financial_year": info['financial_year'],
        "stock_exchange": info['stock_exchange'],
        "paid_up_capital": info['paid_up_capital'],
        "contact_person_telephone": info['contact_person_telephone'],
        "contact_person_email": info['contact_person_email'],
        "reporting_boundary": info['reporting_boundary']
      })


def bussiness_activites(info):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO BusinessActivities (DescriptionOfMainActivity_1,DescriptionOfBusinessActivity_1,TurnoverPercentage_1,DescriptionOfMainActivity_2,DescriptionOfBusinessActivity_2,TurnoverPercentage_2) VALUES (:DescriptionOfMainActivity_1,:DescriptionOfBusinessActivity_1,:TurnoverPercentage_1,:DescriptionOfMainActivity_2,:DescriptionOfBusinessActivity_2,:TurnoverPercentage_2)"
    )

    conn.execute(
      query, {
        "DescriptionOfMainActivity_1": info['main_Activity_1'],
        "DescriptionOfBusinessActivity_1": info['bussiness_Acitvity_1'],
        "TurnoverPercentage_1": info['turnover_1'],
        "DescriptionOfMainActivity_2": info['main_Activity_2'],
        "DescriptionOfBusinessActivity_2": info['bussiness_Acitvity_2'],
        "TurnoverPercentage_2": info['turnover_2']
      })


def products_services(info):
  with engine.connect() as conn:
    query = text(
      "insert into ProductsServices (ProductServiceDescription_1,NICCode_1 ,TurnoverPercentage_1 ,ProductServiceDescription_2 ,NICCode_2 ,TurnoverPercentage_2 ,ProductServiceDescription_3 ,NICCode_3 ,TurnoverPercentage_3) values (:ProductServiceDescription_1,:NICCode_1 ,:TurnoverPercentage_1 ,:ProductServiceDescription_2 ,:NICCode_2 ,:TurnoverPercentage_2 ,:ProductServiceDescription_3 ,:NICCode_3 ,:TurnoverPercentage_3)"
    )

    conn.execute(
      query, {
        "ProductServiceDescription_1": info['P/S_1'],
        "NICCode_1": info['nic_number_1'],
        "TurnoverPercentage_1": info['turnover_contributed_1'],
        "ProductServiceDescription_2": info['P/S_2'],
        "NICCode_2": info['nic_number_2'],
        "TurnoverPercentage_2": info['turnover_contributed_2'],
        "ProductServiceDescription_3": info['P/S_3'],
        "NICCode_3": info['nic_number_3'],
        "TurnoverPercentage_3": info['turnover_contributed_3']
      })


def plants_located_data(info):
  with engine.connect() as conn:
    query = text(
      "insert into plants_located (national_no_of_plants,national_no_of_offices,national_total_locations,international_no_of_plants,international_no_of_offices,international_total_locations) values (:national_no_of_plants,:national_no_of_offices,:national_total_locations,:international_no_of_plants,:international_no_of_offices,:international_total_locations)"
    )

    conn.execute(
      query, {
        "national_no_of_plants": info['national_1'],
        "national_no_of_offices": info['national_2'],
        "national_total_locations": info['national_3'],
        "international_no_of_plants": info['international_1'],
        "international_no_of_offices": info['international_2'],
        "international_total_locations": info['international_3']
      })


def market_served_data(info):
  with engine.connect() as conn:
    query = text(
      "insert into market_served (national_locations,international_locations,exports_contribution,customer_types) values (:national_locations,:international_locations,:exports_contribution,:customer_types)"
    )

    conn.execute(
      query, {
        "national_locations": info['national_locations'],
        "international_locations": info['international_locations'],
        "exports_contribution": info['exports_contribution'],
        "customer_types": info['customer_types']
      })


def company_details_data(info):
  with engine.connect() as conn:
    query = text(
      "insert into CompanyDetails (Name,Relationship ,SharePercentage,ParticipatesInBusinessResponsibility ,CSRApplicable,TurnoverInRs,NetWorthInRs) values (:Name,:Relationship ,:SharePercentage,:ParticipatesInBusinessResponsibility ,:CSRApplicable,:TurnoverInRs,:NetWorthInRs)"
    )

    conn.execute(
      query, {
        "Name":
        info['Name'],
        "Relationship":
        info['Relationship'],
        "SharePercentage":
        info['SharePercentage'],
        "ParticipatesInBusinessResponsibility":
        info['ParticipatesInBusinessResponsibility'],
        "CSRApplicable":
        info['CSRApplicable'],
        "TurnoverInRs":
        info['TurnoverInRs'],
        "NetWorthInRs":
        info['NetWorthInRs']
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
    query = text(
      "insert into Comm_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)"
    )

    conn.execute(
      query, {
        "GrievanceRedressalMechanism":
        info['GrievanceRedressalMechanism'],
        "GrievanceRedressPolicyLink":
        info['GrievanceRedressPolicyLink'],
        "NumComplaintsFiledCurrentYear":
        info['NumComplaintsFiledCurrentYear'],
        "NumComplaintsPendingCurrentYear":
        info['NumComplaintsPendingCurrentYear'],
        "RemarksCurrentYear":
        info['RemarksCurrentYear'],
        "NumComplaintsFiledPreviousYear":
        info['NumComplaintsFiledPreviousYear'],
        "NumComplaintsPendingPreviousYear":
        info['NumComplaintsPendingPreviousYear'],
        "RemarksPreviousYear":
        info['RemarksPreviousYear']
      })


def Investers_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text(
      "insert into Investers_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)"
    )

    conn.execute(
      query, {
        "GrievanceRedressalMechanism": info['n0'],
        "GrievanceRedressPolicyLink": info['n1'],
        "NumComplaintsFiledCurrentYear": info['n2'],
        "NumComplaintsPendingCurrentYear": info['n3'],
        "RemarksCurrentYear": info['n4'],
        "NumComplaintsFiledPreviousYear": info['n5'],
        "NumComplaintsPendingPreviousYear": info['n6'],
        "RemarksPreviousYear": info['n7']
      })


def Shareholders_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text(
      "insert into Shareholders_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)"
    )

    conn.execute(
      query, {
        "GrievanceRedressalMechanism": info['n8'],
        "GrievanceRedressPolicyLink": info['n9'],
        "NumComplaintsFiledCurrentYear": info['n10'],
        "NumComplaintsPendingCurrentYear": info['n11'],
        "RemarksCurrentYear": info['n12'],
        "NumComplaintsFiledPreviousYear": info['n13'],
        "NumComplaintsPendingPreviousYear": info['n14'],
        "RemarksPreviousYear": info['n15']
      })


def Emp_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text(
      "insert into Emp_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)"
    )

    conn.execute(
      query, {
        "GrievanceRedressalMechanism": info['n16'],
        "GrievanceRedressPolicyLink": info['n17'],
        "NumComplaintsFiledCurrentYear": info['n18'],
        "NumComplaintsPendingCurrentYear": info['n19'],
        "RemarksCurrentYear": info['n20'],
        "NumComplaintsFiledPreviousYear": info['n21'],
        "NumComplaintsPendingPreviousYear": info['n22'],
        "RemarksPreviousYear": info['n23']
      })


def Customer_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text(
      "insert into Customer_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)"
    )

    conn.execute(
      query, {
        "GrievanceRedressalMechanism": info['n24'],
        "GrievanceRedressPolicyLink": info['n25'],
        "NumComplaintsFiledCurrentYear": info['n26'],
        "NumComplaintsPendingCurrentYear": info['n27'],
        "RemarksCurrentYear": info['n28'],
        "NumComplaintsFiledPreviousYear": info['n29'],
        "NumComplaintsPendingPreviousYear": info['n30'],
        "RemarksPreviousYear": info['n31']
      })


def partners_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text(
      "insert into partners_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)"
    )

    conn.execute(
      query, {
        "GrievanceRedressalMechanism": info['n32'],
        "GrievanceRedressPolicyLink": info['n33'],
        "NumComplaintsFiledCurrentYear": info['n34'],
        "NumComplaintsPendingCurrentYear": info['n35'],
        "RemarksCurrentYear": info['n36'],
        "NumComplaintsFiledPreviousYear": info['n37'],
        "NumComplaintsPendingPreviousYear": info['n38'],
        "RemarksPreviousYear": info['n39']
      })


def others_ComplaintsGrievances(info):
  with engine.connect() as conn:
    query = text(
      "insert into others_ComplaintsGrievances (GrievanceRedressalMechanism,GrievanceRedressPolicyLink,NumComplaintsFiledCurrentYear,NumComplaintsPendingCurrentYear,RemarksCurrentYear,NumComplaintsFiledPreviousYear,NumComplaintsPendingPreviousYear,RemarksPreviousYear) values (:GrievanceRedressalMechanism,:GrievanceRedressPolicyLink,:NumComplaintsFiledCurrentYear,:NumComplaintsPendingCurrentYear,:RemarksCurrentYear,:NumComplaintsFiledPreviousYear,:NumComplaintsPendingPreviousYear,:RemarksPreviousYear)"
    )

  conn.execute(
    query, {
      "GrievanceRedressalMechanism": info['n30'],
      "GrievanceRedressPolicyLink": info['n41'],
      "NumComplaintsFiledCurrentYear": info['n42'],
      "NumComplaintsPendingCurrentYear": info['n43'],
      "RemarksCurrentYear": info['n44'],
      "NumComplaintsFiledPreviousYear": info['n45'],
      "NumComplaintsPendingPreviousYear": info['n46'],
      "RemarksPreviousYear": info['n47']
    })


def landing_page_data(info):
  with engine.connect() as conn:
    query = text(
      "insert into landing_page (report_id , begin_period , end_period) values (:report_id , :begin_period , :end_period)"
    )

    conn.execute(
      query, {
        "report_id": info['report_id'],
        "begin_period": info['begin_period'],
        "end_period": info['end_period']
      })


def entity_overview_data(info):
  with engine.connect() as conn:
    query = text(
      "insert into entity_overview (MaterialIssue1 , RiskOpportunity1 , Rationale1 , Approach1 , FinancialImplications1, MaterialIssue2 , RiskOpportunity2 , Rationale2 , Approach2 , FinancialImplications2) values (:s1 , :s2 , :s3 , :s4 , :s5, :s6 , :s7 , :s8 ,:s9 , :s10)"
    )

    conn.execute(
      query, {
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

    employees_query = text(
      "INSERT INTO Employees (Permanent,permanent_male1, permanent_female1, permanent_male2,permanent_female2, other_than_permanent, other_than_permanent_male1, other_than_permanent_female1, other_than_permanent_male2,other_than_permanent_female2,total_employees, total_male1,total_female1,total_male2 , total_female2) VALUES (:permanent, :permanent_male1, :permanent_female1, :permanent_male2, :permanent_female2,:other_than_permanent,:other_than_permanent_male1,:other_than_permanent_female1,:other_than_permanent_male2,:other_than_permanent_female2, :total_employees, :total_male1, :total_female1, :total_male2 , :total_female2)"
    )

    conn.execute(
      employees_query, {
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

    workers_query = text(
      "INSERT INTO Workers (Permanent,permanent_male1, permanent_female1, permanent_male2,permanent_female2, other_than_permanent, other_than_permanent_male1, other_than_permanent_female1, other_than_permanent_male2,other_than_permanent_female2,total_employees, total_male1,total_female1,total_male2 , total_female2) VALUES (:permanent, :permanent_male1, :permanent_female1, :permanent_male2, :permanent_female2,:other_than_permanent,:other_than_permanent_male1,:other_than_permanent_female1,:other_than_permanent_male2,:other_than_permanent_female2, :total_employees, :total_male1, :total_female1, :total_male2 , :total_female2)"
    )

    conn.execute(
      workers_query, {
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

    differently_abled_employees_query = text(
      "INSERT INTO DifferentlyAbledEmployees (Permanent,permanent_male1, permanent_female1, permanent_male2,permanent_female2, other_than_permanent, other_than_permanent_male1, other_than_permanent_female1, other_than_permanent_male2,other_than_permanent_female2,total_employees, total_male1,total_female1,total_male2 , total_female2) VALUES (:permanent, :permanent_male1, :permanent_female1, :permanent_male2, :permanent_female2,:other_than_permanent,:other_than_permanent_male1,:other_than_permanent_female1,:other_than_permanent_male2,:other_than_permanent_female2, :total_employees, :total_male1, :total_female1, :total_male2 , :total_female2)"
    )

    conn.execute(
      differently_abled_employees_query, {
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

    differently_abled_workers_query = text(
      "INSERT INTO DifferentlyAbledWorkers (Permanent,permanent_male1, permanent_female1, permanent_male2,permanent_female2, other_than_permanent, other_than_permanent_male1, other_than_permanent_female1, other_than_permanent_male2,other_than_permanent_female2,total_employees, total_male1,total_female1,total_male2 , total_female2) VALUES (:permanent, :permanent_male1, :permanent_female1, :permanent_male2, :permanent_female2,:other_than_permanent,:other_than_permanent_male1,:other_than_permanent_female1,:other_than_permanent_male2,:other_than_permanent_female2, :total_employees, :total_male1, :total_female1, :total_male2 , :total_female2)"
    )

    conn.execute(
      differently_abled_workers_query, {
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

    women_participation_query = text(
      "INSERT INTO WomenParticipation (Board_of_Directors_Total, Board_of_Directors_Female1,  Board_of_Directors_Female2,Key_Management_Personnel_Total, Key_Management_Personnel_Female1, Key_Management_Personnel_Female2) VALUES (:board_of_directors_total, :board_of_directors_female1, :board_of_directors_female2,:key_management_personnel_total, :key_management_personnel_female1 , :key_management_personnel_female2)"
    )

    conn.execute(
      women_participation_query, {
        "board_of_directors_total": info["a61"],
        "board_of_directors_female1": info["a62"],
        "board_of_directors_female2": info["a63"],
        "key_management_personnel_total": info["a64"],
        "key_management_personnel_female1": info["a65"],
        "key_management_personnel_female2": info["a66"]
      })

    pe_turnover_rate_query = text(
      "INSERT INTO PE_TurnoverRatePermanent (PE_fy_current_1, PE_fy_current_2, PE_fy_current_3, PE_fy_previous_1, PE_fy_previous_2, PE_fy_previous_3, PE_fy_year_prior_1, PE_fy_year_prior_2, PE_fy_year_prior_3) VALUES (:PE_fy_current_1, :PE_fy_current_2, :PE_fy_current_3, :PE_fy_previous_1, :PE_fy_previous_2, :PE_fy_previous_3, :PE_fy_year_prior_1, :PE_fy_year_prior_2, :PE_fy_year_prior_3)"
    )

    conn.execute(
      pe_turnover_rate_query, {
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

    pw_turnover_rate_query = text(
      "INSERT INTO PW_TurnoverRatePermanent (PW_fy_current_1, PW_fy_current_2, PW_fy_current_3, PW_fy_previous_1, PW_fy_previous_2, PW_fy_previous_3, PW_fy_year_prior_1, PW_fy_year_prior_2, PW_fy_year_prior_3) VALUES (:PW_fy_current_1, :PW_fy_current_2, :PW_fy_current_3, :PW_fy_previous_1, :PW_fy_previous_2, :PW_fy_previous_3, :PW_fy_year_prior_1, :PW_fy_year_prior_2, :PW_fy_year_prior_3)"
    )

    conn.execute(
      pw_turnover_rate_query, {
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


def management_process_disclosure_data(info):
  with engine.connect() as conn:

    query1 = text(
      "insert into NGRBC_Policy_Coverage(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query1, {
        "P1": info.get('z1', 0),
        "P2": info.get('z2', 0),
        "P3": info.get('z3', 0),
        "P4": info.get('z4', 0),
        "P5": info.get('z5', 0),
        "P6": info.get('z6', 0),
        "P7": info.get('z7', 0),
        "P8": info.get('z8', 0),
        "P9": info.get('z9', 0)
      })


'''
    query2 = text(
      "insert into A_Policy_Approval_Status(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query2, {
        "P1": info['z10'],
        "P2": info('z11'),
        "P3": info('z12'),
        "P4": info('z13'),
        "P5": info('z14'),
        "P6": info('z15'),
        "P7": info('z16'),
        "P8": info('z17'),
        "P9": info('z18')
      })

    query3 = text(
      "insert into Policy_Translation_Status(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query3, {
        "P1": info('z19'),
        "P2": info('z20'),
        "P3": info('z21'),
        "P4": info('z22'),
        "P5": info('z23'),
        "P6": info('z24'),
        "P7": info('z25'),
        "P8": info('z26'),
        "P9": info('z27')
      })

    query4 = text(
      "insert into B_Policy_Approval_Status(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query4, {
        "P1": info('z28'),
        "P2": info('z29'),
        "P3": info('z30'),
        "P4": info('z31'),
        "P5": info('z32'),
        "P6": info('z33'),
        "P7": info('z34'),
        "P8": info('z35'),
        "P9": info('z36')
      })

    query5 = text(
      "insert into Policy_Value_Chain_Extension(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query5, {
        "P1": info('z37'),
        "P2": info('z38'),
        "P3": info('z39'),
        "P4": info('z40'),
        "P5": info('z41'),
        "P6": info('z42'),
        "P7": info('z43'),
        "P8": info('z44'),
        "P9": info('z45')
      })

    query6 = text(
      "insert into Standards_Certifications_Mapping(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query6, {
        "P1": info('z46'),
        "P2": info('z47'),
        "P3": info('z48'),
        "P4": info('z49'),
        "P5": info('z50'),
        "P6": info('z51'),
        "P7": info('z52'),
        "P8": info('z53'),
        "P9": info('z54')
      })

    query7 = text(
      "insert into commitments_not_met(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query7, {
        "P1": info('z55'),
        "P2": info('z56'),
        "P3": info('z57'),
        "P4": info('z58'),
        "P5": info('z59'),
        "P6": info('z60'),
        "P7": info('z61'),
        "P8": info('z62'),
        "P9": info('z63')
      })

    query16 = text("insert into Governance_leadership_oversight(BRP_Highest_Authority, Has_Committee , Has_Committee_if_yes) values (:BRP_Highest_Authority , :Has_Committee , :Has_Committee_if_yes)")

    conn.execute(
      query16,{
        "BRP_Highest_Authority" : info('z64'),
        "Has_Committee": info('z65'),
        "Has_Committee_if_yes" : info('z66')
      })
    

    query8 = text(
      "insert into Policy_Performance_FollowUp(Review_By_P1,Review_By_P2,Review_By_P3,Review_By_P4,Review_By_P5,Review_By_P6,Review_By_P7,Review_By_P8,Review_By_P9, Frequency_P1,Frequency_P2,Frequency_P3,Frequency_P4,Frequency_P5,Frequency_P6,Frequency_P7,Frequency_P8,Frequency_P9) values (:Review_By_P1,:Review_By_P2,:Review_By_P3,:Review_By_P4,:Review_By_P5,:Review_By_P6,:Review_By_P7,:Review_By_P8,:Review_By_P9, :Frequency_P1,:Frequency_P2,:Frequency_P3,:Frequency_P4,:Frequency_P5,:Frequency_P6,:Frequency_P7,:Frequency_P8,:Frequency_P9)"
    )

    conn.execute(
      query8, {
        "Review_By_P1": info('z67'),
        "Review_By_P2": info('z68'),
        "Review_By_P3": info('z69'),
        "Review_By_P4": info('z70'),
        "Review_By_P5": info('z71'),
        "Review_By_P6": info('z72'),
        "Review_By_P7": info('z73'),
        "Review_By_P8": info('z74'),
        "Review_By_P9": info('z75'),
        "Frequency_P1": info('z76'),
        "Frequency_P2": info('z77'),
        "Frequency_P3": info('z78'),
        "Frequency_P4": info('z79'),
        "Frequency_P5": info('z80'),
        "Frequency_P6": info('z81'),
        "Frequency_P7": info('z82'),
        "Frequency_P8": info('z83'),
        "Frequency_P9": info('z84')
      })

    query9 = text(
      "insert into Statutory_Compliance(Review_By_P1,Review_By_P2,Review_By_P3,Review_By_P4,Review_By_P5,Review_By_P6,Review_By_P7,Review_By_P8,Review_By_P9, Frequency_P1,Frequency_P2,Frequency_P3,Frequency_P4,Frequency_P5,Frequency_P6,Frequency_P7,Frequency_P8,Frequency_P9) values (:Review_By_P1,:Review_By_P2,:Review_By_P3,:Review_By_P4,:Review_By_P5,:Review_By_P6,:Review_By_P7,:Review_By_P8,:Review_By_P9, :Frequency_P1,:Frequency_P2,:Frequency_P3,:Frequency_P4,:Frequency_P5,:Frequency_P6,:Frequency_P7,:Frequency_P8,:Frequency_P9)"
    )

    conn.execute(
      query9, {
        "Review_By_P1": info('z85'),
        "Review_By_P2": info('z86'),
        "Review_By_P3": info('z87'),
        "Review_By_P4": info('z88'),
        "Review_By_P5": info('z89'),
        "Review_By_P6": info('z90'),
        "Review_By_P7": info('z91'),
        "Review_By_P8": info('z92'),
        "Review_By_P9": info('z93'),
        "Frequency_P1": info('z94'),
        "Frequency_P2": info('z95'),
        "Frequency_P3": info('z96'),
        "Frequency_P4": info('z97'),
        "Frequency_P5": info('z98'),
        "Frequency_P6": info('z99'),
        "Frequency_P7": info('z100'),
        "Frequency_P8": info('z101'),
        "Frequency_P9": info('z102')
      })

    query10 = text(
      "insert into External_Assessment(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query10, {
        "P1": info('z103'),
        "P2": info('z104'),
        "P3": info('z105'),
        "P4": info('z106'),
        "P5": info('z107'),
        "P6": info('z108'),
        "P7": info('z109'),
        "P8": info('z110'),
        "P9": info('z111')
      })

    query11 = text(
      "insert into Materiality_Assessment(P1,P1_review,P2,P2_review,P3,P3_review,P4,P4_review,P5,P5_review,P6,P6_review,P7,P7_review,P8,P8_review,P9,P9_review) values (:P1,:P1_review,:P2,:P2_review,:P3,:P3_review,:P4,:P4_review,:P5,:P5_review,:P6,:P6_review,:P7,:P7_review,:P8,:P8_review,:P9,:P9_review)"
    )

    conn.execute(
      query11, {
        "P1": info('z112'),
        "P1_review": info('z113'),
        "P2": info('z114'),
        "P2_review": info('z115'),
        "P3": info('z116'),
        "P3_review": info('z117'),
        "P4": info('z118'),
        "P4_review": info('z119'),
        "P5": info('z120'),
        "P5_review": info('z121'),
        "P6": info('z122'),
        "P6_review": info('z123'),
        "P7": info('z124'),
        "P7_review": info('z125'),
        "P8": info('z126'),
        "P8_review": info('z127'),
        "P9": info('z128'),
        "P9_review": info('z129'),
      })

    query12 = text(
      "insert into Policy_Formulation_Status(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query12, {
        "P1": info('z130'),
        "P2": info('z131'),
        "P3": info('z132'),
        "P4": info('z133'),
        "P5": info('z134'),
        "P6": info('z135'),
        "P7": info('z136'),
        "P8": info('z137'),
        "P9": info('z138')
      })

    query13 = text(
      "insert into Resource_Availability(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query13, {
        "P1": info('z139'),
        "P2": info('z140'),
        "P3": info('z141'),
        "P4": info('z142'),
        "P5": info('z143'),
        "P6": info('z144'),
        "P7": info('z145'),
        "P8": info('z146'),
        "P9": info('z147')
      })

    query14 = text(
      "insert into Financial_Year_Plans(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query14, {
        "P1": info('z148'),
        "P2": info('z149'),
        "P3": info('z150'),
        "P4": info('z151'),
        "P5": info('z152'),
        "P6": info('z153'),
        "P7": info('z154'),
        "P8": info('z155'),
        "P9": info('z156')
      })

    query15 = text(
      "insert into any_other_reason(P1,P2,P3,P4,P5,P6,P7,P8,P9) values (:P1,:P2,:P3,:P4,:P5,:P6,:P7,:P8,:P9)"
    )

    conn.execute(
      query15, {
        "P1": info('z158'),
        "P2": info('z159'),
        "P3": info('z160'),
        "P4": info('z161'),
        "P5": info('z162'),
        "P6": info('z163'),
        "P7": info('z164'),
        "P8": info('z165'),
        "P9": info('z166')
      })
'''
