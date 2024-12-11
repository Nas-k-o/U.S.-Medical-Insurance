from flask import Flask, render_template, request
import pandas as pd
# Initialize Flask app
app = Flask(__name__)

# Read the CSV data
studyDataFrame = pd.read_csv("insurance.csv")
userDataFrame = pd.read_csv("userInsurance.csv")

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
        cost = 250*age - 128*g_cost + 370*bmi + 425*n_children + 24000*s_cost - 12500

        # Save user data
        saveToCsv = {
            "age": age,
            "sex": gender,
            "bmi": bmi,
            "children": n_children,
            "smoker": smoker,
            "region": region,
            "charges": cost
        }

        # Append user data to CSV (you can also save to a database if needed)
        pd.DataFrame([saveToCsv]).to_csv("userInsurance.csv", index = False)

        return render_template("user_input.html", cost=cost)
    return render_template("user_input.html")

@app.route('/main', methods=["GET", "POST"])
def main():
    context = {"view": None}  # Default view

    # Reload the user data every time the page is accessed
    userDataFrame = pd.read_csv("userInsurance.csv")

    if request.method == "POST":
        # Determine which button was clicked and fetch data
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
            context["smoker_count"] = smoker_counts.get('yes', 0)
        elif "region" in request.form:
            context["view"] = "region"
            context["region_counts"] = studyDataFrame["region"].value_counts().to_dict()
        elif "charges" in request.form:
            context["view"] = "charges"
            context["avg_charge"] = round(studyDataFrame["charges"].mean(), 2)
        elif "compare" in request.form:
            context["view"] = "compare"
            if not userDataFrame.empty:
                user_data = userDataFrame.iloc[0]
                study_averages = {
                    "Age": round(studyDataFrame["age"].mean(), 2),
                    "BMI": round(studyDataFrame["bmi"].mean(), 2),
                    "Children": round(studyDataFrame["children"].mean(), 2),
                    "Charges": round(studyDataFrame["charges"].mean(), 2)
                }

                comparison_data = {
                    "User Age": user_data["age"],
                    "Average Age": study_averages["Age"],
                    "User BMI": user_data["bmi"],
                    "Average BMI": study_averages["BMI"],
                    "User Children": user_data["children"],
                    "Average Children": study_averages["Children"],
                    "User Charges": user_data["charges"],
                    "Average Charges": study_averages["Charges"]
                }

                context["comparison_data"] = comparison_data
            else:
                context["comparison_error"] = "No user data available for comparison."

    return render_template("main.html", **context)


    return render_template("main.html", **context)

@app.route('/region_stats', methods=["GET", "POST"])
def region_stats():
    context = {"view": "region_stats"}

    if request.method == "POST":
        # Calculate statistics for each region
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

if __name__ == '__main__':
    app.run(debug=True)
