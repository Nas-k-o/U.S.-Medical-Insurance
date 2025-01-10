from flask import Flask, render_template, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import os
import mysql.connector

# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",          # Replace with your database host
            user="root",               # Replace with your MySQL username
            password="root",           # Replace with your MySQL password
            database="usmi"            # Replace with your database name
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Fetch data from the STUDY table
def fetch_study_data():
    connection = connect_to_database()
    if connection:
        query = "SELECT * FROM STUDY"
        study_df = pd.read_sql(query, connection)
        connection.close()
        return study_df
    else:
        print("Failed to connect to the database.")
        return pd.DataFrame()

# Initialize Flask app
app = Flask(__name__)

# Load study data into a DataFrame
studyDataFrame = fetch_study_data()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user', methods=["POST", "GET"])
def user():
    if request.method == "POST":
        # Get the data from the form
        age = int(request.form['age'])
        gender = request.form['gender']
        bmi = float(request.form['bmi'])
        n_children = int(request.form['children'])
        region = request.form['region']
        smoker = request.form['smoker']

        # Gender cost calculation
        g_cost = 1 if gender.lower() == "male" else 0
        s_cost = 1 if smoker.lower() == "yes" else 0

        # Estimate the cost
        cost = 250 * age - 128 * g_cost + 370 * bmi + 425 * n_children + 24000 * s_cost - 12500

        # Save user data to the database
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            insert_query = """
                INSERT INTO USER_INSURANCE (age, sex, bmi, children, smoker, region, charges)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (age, gender, bmi, n_children, smoker, region, cost)
            cursor.execute(insert_query, values)
            connection.commit()
            cursor.close()
            connection.close()

        return render_template("user_input.html", cost=cost)
    return render_template("user_input.html")

@app.route('/main', methods=["GET", "POST"])
def main():
    context = {"view": None}  # Default view

    if request.method == "POST":
        if "age" in request.form:
            context["view"] = "age"
            context["avg_age"] = round(studyDataFrame["age"].mean(), 2)
        elif "gender" in request.form:
            context["view"] = "gender"
            gender_counts = studyDataFrame["sex"].value_counts()
            context["male"] = gender_counts.get('male', 0)
            context["female"] = gender_counts.get('female', 0)
        elif "bmi" in request.form:
            context["view"] = "bmi"
            context["avg_bmi"] = round(studyDataFrame["bmi"].mean(), 2)
        elif "children" in request.form:
            context["view"] = "children"
            context["avg_children"] = round(studyDataFrame["children"].mean(), 2)
        elif "smoker" in request.form:
            context["view"] = "smoker"
            smoker_counts = studyDataFrame["smoker"].value_counts()
            context["non_smoker"] = smoker_counts.get('no', 0)
            context["smoker"] = smoker_counts.get('yes', 0)
        elif "region" in request.form:
            context["view"] = "region"
            context["region_counts"] = studyDataFrame["region"].value_counts().to_dict()
        elif "charges" in request.form:
            context["view"] = "charges"
            context["avg_charge"] = round(studyDataFrame["charges"].mean(), 2)

    return render_template("main.html", **context)

@app.route('/region_stats', methods=["GET", "POST"])
def region_stats():
    context = {"view": "region_stats"}

    if request.method == "POST":
        region_data = studyDataFrame.groupby('region').agg(
            avg_age=('age', 'mean'),
            avg_bmi=('bmi', 'mean'),
            avg_children=('children', 'mean'),
            avg_charges=('charges', 'mean'),
            smoker_count=('smoker', lambda x: (x == 'yes').sum()),
            non_smoker_count=('smoker', lambda x: (x == 'no').sum())
        ).reset_index()

        context["region_data"] = region_data.to_dict(orient='records')

    return render_template("region_stats.html", **context)

@app.route('/download_region_stats', methods=["GET"])
def download_region_stats():
    region_data = studyDataFrame.groupby('region').agg(
        avg_age=('age', 'mean'),
        avg_bmi=('bmi', 'mean'),
        avg_children=('children', 'mean'),
        avg_charges=('charges', 'mean'),
        smoker_count=('smoker', lambda x: (x == 'yes').sum()),
        non_smoker_count=('smoker', lambda x: (x == 'no').sum())
    ).reset_index()

    csv_path = 'region_stats.csv'
    region_data.to_csv(csv_path, index=False)

    plt.figure(figsize=(10, 6))
    plt.bar(region_data['region'], region_data['avg_charges'], color='skyblue')
    plt.title('Average Charges per Region')
    plt.xlabel('Region')
    plt.ylabel('Average Charges')

    image_path = 'region_stats_graph.png'
    plt.savefig(image_path)

    zip_path = 'region_stats.zip'
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(csv_path)
        zipf.write(image_path)

    os.remove(csv_path)
    os.remove(image_path)

    return send_file(zip_path, as_attachment=True, download_name="region_stats.zip", mimetype='application/zip')

@app.route('/info')
def info():
    return render_template("info.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
