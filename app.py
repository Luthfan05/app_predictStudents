import streamlit as st
import pandas as pd
import joblib

# Load model
with open("model.joblib", "rb") as f:
    model = joblib.load(f)

st.title("Prediksi Status Mahasiswa")

# Fungsi untuk encode
def encode(label, category):
    if category == "marital_status":
        marital_status_values = {
            "Single": 1, 
            "Married": 2, 
            "Widowed": 3, 
            "Divorced": 4, 
            "Facto union": 5, 
            "Legally separated": 6
        }
        return marital_status_values.get(label, -1)
        
    elif category == "application_mode":
        application_mode_values = {
            "1st phase - general contingent": 1,
            "Ordinance No. 612/93": 2,
            "1st phase - special contingent (Azores Island)": 5,
            "Holders of other higher courses": 7,
            "Ordinance No. 854-B/99": 10,
            "International student (bachelor)": 15,
            "1st phase - special contingent (Madeira Island)": 16,
            "2nd phase - general contingent": 17,
            "3rd phase - general contingent": 18,
            "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
            "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
            "Over 23 years old": 39,
            "Transfer": 42,
            "Change of course": 43,
            "Technological specialization diploma holders": 44,
            "Change of institution/course": 51,
            "Short cycle diploma holders": 53,
            "Change of institution/course (International)": 57
        }
        return application_mode_values.get(label, -1)
    
    elif category == "course":
        course_values = {
            "Biofuel Production Technologies": 33,
            "Animation and Multimedia Design": 171,
            "Social Service (evening attendance)": 8014,
            "Agronomy": 9003,
            "Communication Design": 9070,
            "Veterinary Nursing": 9085,
            "Informatics Engineering": 9119,
            "Equinculture": 9130,
            "Management": 9147,
            "Social Service": 9238,
            "Tourism": 9254,
            "Nursing": 9500,
            "Oral Hygiene": 9556,
            "Advertising and Marketing Management": 9670,
            "Journalism and Communication": 9773,
            "Basic Education": 9853,
            "Management (evening attendance)": 9991
        }
        return course_values.get(label, -1)
    
    elif category == 'attendance':
        attendance_value = {
            'evening' : 0,
            'daytime' : 1
            }
        return attendance_value.get(label, -1)

    elif category == "previous_qualification":
        previous_qualification_values = {
            "Secondary education": 1,
            "Higher education - bachelor's degree": 2,
            "Higher education - degree": 3,
            "Higher education - master's": 4,
            "Higher education - doctorate": 5,
            "Frequency of higher education": 6,
            "12th year of schooling - not completed": 9,
            "11th year of schooling - not completed": 10,
            "Other - 11th year of schooling": 12,
            "10th year of schooling": 14,
            "10th year of schooling - not completed": 15,
            "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
            "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
            "Technological specialization course": 39,
            "Higher education - degree (1st cycle)": 40,
            "Professional higher technical course": 42,
            "Higher education - master (2nd cycle)": 43
        }
        return previous_qualification_values.get(label, -1)

    elif category == "nationality":
        nationality_values = {
            "Portuguese": 1,
            "German": 2,
            "Spanish": 6,
            "Italian": 11,
            "Dutch": 13,
            "English": 14,
            "Lithuanian": 17,
            "Angolan": 21,
            "Cape Verdean": 22,
            "Guinean": 24,
            "Mozambican": 25,
            "Santomean": 26,
            "Turkish": 32,
            "Brazilian": 41,
            "Romanian": 62,
            "Moldova (Republic of)": 100,
            "Mexican": 101,
            "Ukrainian": 103,
            "Russian": 105,
            "Cuban": 108,
            "Colombian": 109
        }
        return nationality_values.get(label, -1)

    elif category == "parent_qualification":
        parent_qualification_values = {
            "Secondary Education - 12th Year of Schooling or Eq.": 1,
            "Higher Education - Bachelor's Degree": 2,
            "Higher Education - Degree": 3,
            "Higher Education - Master's": 4,
            "Higher Education - Doctorate": 5,
            "Frequency of Higher Education": 6,
            "12th Year of Schooling - Not Completed": 9,
            "11th Year of Schooling - Not Completed": 10,
            "Other - 11th Year of Schooling": 12,
            "10th Year of Schooling": 14,
            "General commerce course": 18,
            "Basic Education 3rd Cycle (9th/10th/11th Year)": 19,
            "Technical-professional course": 22,
            "Higher Education - Master (2nd cycle)": 43,
            "Professional higher technical course": 42,
            "Higher Education - Doctorate (3rd cycle)": 44
        }
        return parent_qualification_values.get(label, -1)
    
    elif category == "occupation":
        occupation_values = {
            "Student": 0,
            "Representatives of the Legislative Power and Executive Bodies": 1,
            "Specialists in Intellectual and Scientific Activities": 2,
            "Intermediate Level Technicians and Professions": 3,
            "Administrative staff": 4,
            "Personal Services, Security and Safety Workers": 5,
            "Farmers and Skilled Workers in Agriculture": 6,
            "Skilled Workers in Industry, Construction": 7,
            "Unskilled Workers": 9,
            "Armed Forces Professions": 10,
            "Health professionals": 122,
            "Teachers": 123,
            "Specialists in information and communication technologies (ICT)": 125,
            "Intermediate level science and engineering technicians": 131
        }
        return occupation_values.get(label, -1)

    elif category == "gender":
        return 1 if label == "Male" else 0

    elif category == "status":
        return 1 if label == "Yes" else 0

    return -1


# Input dari user
marital_status = st.selectbox("**Marital Status**", ["Single", "Married", "Widowed", "Divorced", "Facto union", "Legally separated"])
# Application Mode
application_mode = st.selectbox("**Application Mode**", options=[
    "1st phase - general contingent",
    "Ordinance No. 612/93",
    "1st phase - special contingent (Azores Island)",
    "Holders of other higher courses",
    "Ordinance No. 854-B/99",
    "International student (bachelor)",
    "1st phase - special contingent (Madeira Island)",
    "2nd phase - general contingent",
    "3rd phase - general contingent",
    "Ordinance No. 533-A/99, item b2) (Different Plan)",
    "Ordinance No. 533-A/99, item b3 (Other Institution)",
    "Over 23 years old",
    "Transfer",
    "Change of course",
    "Technological specialization diploma holders",
    "Change of institution/course",
    "Short cycle diploma holders",
    "Change of institution/course (International)"
])
st.markdown("**Application order**")
application_order = st.slider("0 - first choice; and 9 - last choice", 0, 9)

# Course
course = st.selectbox("**Course**", [
    "Biofuel Production Technologies",
    "Animation and Multimedia Design",
    "Social Service (evening attendance)",
    "Agronomy",
    "Communication Design",
    "Veterinary Nursing",
    "Informatics Engineering",
    "Equinculture",
    "Management",
    "Social Service",
    "Tourism",
    "Nursing",
    "Oral Hygiene",
    "Advertising and Marketing Management",
    "Journalism and Communication",
    "Basic Education",
    "Management (evening attendance)"
])

attendance = st.selectbox("**Daytime/evening attendance**", ["daytime", "evening"])

previous_qualification = st.selectbox("**Previous qualification**", [
    "Secondary education",
    "Higher education - bachelor's degree",
    "Higher education - degree",
    "Higher education - master's",
    "Higher education - doctorate",
    "Frequency of higher education",
    "12th year of schooling - not completed",
    "11th year of schooling - not completed",
    "Other - 11th year of schooling",
    "10th year of schooling",
    "10th year of schooling - not completed",
    "Basic education 3rd cycle (9th/10th/11th year) or equiv.",
    "Basic education 2nd cycle (6th/7th/8th year) or equiv.",
    "Technological specialization course",
    "Higher education - degree (1st cycle)",
    "Professional higher technical course",
    "Higher education - master (2nd cycle)"
]
)

previous_qualification_grade = st.number_input("**Previous qualification (grade)**", min_value=0.0, max_value=200.0, step=0.1)

# Nationality
nationality = st.selectbox(
    "**Nacionality**", 
    options=[
        "Portuguese", "German", "Spanish", "Italian", "Dutch", "English", "Lithuanian",
        "Angolan", "Cape Verdean", "Guinean", "Mozambican", "Santomean", "Turkish",
        "Brazilian", "Romanian", "Moldova (Republic of)", "Mexican", "Ukrainian",
        "Russian", "Cuban", "Colombian"
    ]
)

# Mother's Qualification
mother_qualification = st.selectbox(
    "**Mother's qualification**", 
    options=[
        "Secondary Education - 12th Year of Schooling or Eq.",
        "Higher Education - Bachelor's Degree",
        "Higher Education - Degree",
        "Higher Education - Master's",
        "Higher Education - Doctorate",
        "Frequency of Higher Education",
        "12th Year of Schooling - Not Completed",
        "11th Year of Schooling - Not Completed",
        "Other - 11th Year of Schooling",
        "10th Year of Schooling",
        "General commerce course",
        "Basic Education 3rd Cycle (9th/10th/11th Year)",
        "Technical-professional course",
        "Professional higher technical course",
        "Higher Education - Master (2nd cycle)",
        "Higher Education - Doctorate (3rd cycle)"
    ]
)

# Father's Qualification
father_qualification = st.selectbox(
    "**Father's qualification**", 
    options=[
        "Secondary Education - 12th Year of Schooling or Eq.",
        "Higher Education - Bachelor's Degree",
        "Higher Education - Degree",
        "Higher Education - Master's",
        "Higher Education - Doctorate",
        "Frequency of Higher Education",
        "12th Year of Schooling - Not Completed",
        "11th Year of Schooling - Not Completed",
        "Other - 11th Year of Schooling",
        "10th Year of Schooling",
        "General commerce course",
        "Basic Education 3rd Cycle (9th/10th/11th Year)",
        "Technical-professional course",
        "Professional higher technical course",
        "Higher Education - Master (2nd cycle)",
        "Higher Education - Doctorate (3rd cycle)"
    ]
)
# Pilihan occupation
occupation_options = [
    "Student",
    "Representatives of the Legislative Power and Executive Bodies",
    "Specialists in Intellectual and Scientific Activities",
    "Intermediate Level Technicians and Professions",
    "Administrative staff",
    "Personal Services, Security and Safety Workers",
    "Farmers and Skilled Workers in Agriculture",
    "Skilled Workers in Industry, Construction",
    "Unskilled Workers",
    "Armed Forces Professions",
    "Health professionals",
    "Teachers",
    "Specialists in information and communication technologies (ICT)",
    "Intermediate level science and engineering technicians"
]

mother_occupation = st.selectbox("**Mother's occupation**", occupation_options)
father_occupation = st.selectbox("**Father's occupation**", occupation_options)
admission_grade = st.number_input("**Admission grade** (0 - 200)", min_value=0.0, max_value=200.0, step=0.1)
displaced = st.radio("**Displaced**", ["Yes", "No"], horizontal=True)
special_needs = st.radio("**Educational special needs**", ["Yes", "No"], horizontal=True)
debtor = st.radio("**Debtor**", ["Yes", "No"], horizontal=True)
tuition_paid = st.radio("**Tuition fees up to date**", ["Yes", "No"], horizontal=True)
gender = st.radio("**Gender**", ["Male", "Female"])
scholarship = st.radio("**Scholarship holder**", ["Yes", "No"], horizontal=True)
age_enrollment = st.number_input("**Age at enrollment**", min_value=16, max_value=100)
international = st.radio("**International Student**", ["Yes", "No"], horizontal=True)
units_credited = st.number_input("**Curricular units 1st sem (credited)**", min_value=0)
units_enrolled = st.number_input("**Curricular units 1st sem (enrolled)**", min_value=0)
units_evaluations = st.number_input("**Curricular units 1st sem (evaluations)**", min_value=0)
units_approved = st.number_input("**Curricular units 1st sem (approved)**", min_value=0)
cu_1st_grade = st.number_input("**Curricular units 1st sem (grade)**", min_value=0.0, max_value=20.0)
cu_1st_no_evaluation = st.number_input("**Curricular units 1st sem (without evaluations)**", min_value=0)
cu_2nd_credited = st.number_input("**Curricular units 2nd sem (credited)**", min_value=0)
cu_2nd_enrolled = st.number_input("**Curricular units 2nd sem (enrolled)**", min_value=0)
cu_2nd_evaluations = st.number_input("**Curricular units 2nd sem (evaluations)**", min_value=0)
cu_2nd_approved = st.number_input("**Curricular units 2nd sem (approved)**", min_value=0)
cu_2nd_grade = st.number_input("**Curricular units 2nd sem (grade)**", min_value=0.0, max_value=20.0)
cu_2nd_no_evaluation = st.number_input("**Curricular units 2nd sem (without evaluations)**", min_value=0)
unemployment_rate = st.number_input("**Unemployment rate**", min_value=0.0, step=0.1)
inflation_rate = st.number_input("**Inflation rate**")
gdp = st.number_input("**GDP**")


# Encoding
encoded_marital_status = encode(marital_status, "marital_status")
encoded_application_mode = encode(application_mode, 'application_mode')
encoded_course = encode(course, 'course')
encoded_attendance = encode(attendance, "attendance")
encoded_previous_qualification = encode(previous_qualification, "previous_qualification")
encoded_nationality = encode(nationality, "nationality")
encoded_mother_qualification = encode(mother_qualification, "parent_qualification")
encoded_father_qualification = encode(father_qualification, "parent_qualification")
encoded_mother_occupation = encode(mother_occupation, "occupation_options")
encoded_father_occupation = encode(father_occupation, "occupation_options")
encoded_displaced = 1 if displaced == "Yes" else 0
encoded_special_needs = 1 if special_needs == "Yes" else 0
encoded_debtor = 1 if debtor == "Yes" else 0
encoded_tuition_paid = 1 if tuition_paid == "Yes" else 0
encoded_gender = encode(gender, "gender")
encoded_scholarship = 1 if scholarship == "Yes" else 0
encoded_international = 1 if international == "Yes" else 0


# Buat DataFrame sesuai urutan fitur pada model
input_df = pd.DataFrame([{
    'Marital status': encoded_marital_status,
    'Application mode': encoded_application_mode,
    'Application order': application_order,
    'Course': encoded_course,
    'Daytime/evening attendance': encoded_attendance,
    'Previous qualification': encoded_previous_qualification,
    'Previous qualification (grade)': previous_qualification_grade,
    'Nacionality': encoded_nationality,
    "Mother's qualification": encoded_mother_qualification,
    "Father's qualification": encoded_father_qualification,
    "Mother's occupation": encoded_mother_occupation,
    "Father's occupation": encoded_father_occupation,
    'Admission grade': admission_grade,
    'Displaced': encoded_displaced,
    'Educational special needs': encoded_special_needs,
    'Debtor': encoded_debtor,
    'Tuition fees up to date': encoded_tuition_paid,
    'Gender': encoded_gender,
    'Scholarship holder': encoded_scholarship,
    'Age at enrollment': age_enrollment,
    'International': encoded_international,
    'Curricular units 1st sem (credited)': units_credited,
    'Curricular units 1st sem (enrolled)': units_enrolled,
    'Curricular units 1st sem (evaluations)': units_evaluations,
    'Curricular units 1st sem (approved)': units_approved,
    'Curricular units 1st sem (grade)': cu_1st_grade,
    'Curricular units 1st sem (without evaluations)': cu_1st_no_evaluation,
    'Curricular units 2nd sem (credited)': cu_2nd_credited,
    'Curricular units 2nd sem (enrolled)': cu_2nd_enrolled,
    'Curricular units 2nd sem (evaluations)': cu_2nd_evaluations,
    'Curricular units 2nd sem (approved)': cu_2nd_approved,
    'Curricular units 2nd sem (grade)': cu_2nd_grade,
    'Curricular units 2nd sem (without evaluations)': cu_2nd_no_evaluation,
    'Unemployment rate': unemployment_rate,
    'Inflation rate': inflation_rate,
    'GDP': gdp
}])

# Prediksi
if st.button("Prediksi Status"):
    prediction = model.predict(input_df)[0]
    
    if prediction == 0:
        label = "Dropout"
    elif prediction == 1:
        label = "Graduate"
    elif prediction == 2:
        label = "Enrolled"
    else:
        label = "Tidak diketahui"

    st.subheader(f"Prediksi: {label}")