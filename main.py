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
"""
@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/age')
def age():
    avg_age = studyDataFrame["age"].mean()
    return render_template("age.html", avg_age=round(avg_age, 2))

@app.route('/gender')
def gender():
    gender_counts = studyDataFrame["sex"].value_counts()
    male = gender_counts.get('male', 0)
    female = gender_counts.get('female', 0)
    return render_template("gender.html", male=male, female=female)

@app.route('/bmi')
def bmi():
    avg_bmi = studyDataFrame["bmi"].mean()
    return render_template("bmi.html", avg_bmi=round(avg_bmi, 2))

@app.route('/children')
def children():
    avg_children = studyDataFrame["children"].mean()
    return render_template("children.html", avg_children=round(avg_children, 2))

@app.route('/smoker')
def smoker():
    smoker_counts = studyDataFrame["smoker"].value_counts()
    non_smoker = smoker_counts.get('no', 0)
    smoker_count = smoker_counts.get('yes', 0)
    return render_template("smoker.html", non_smoker=non_smoker, smoker=smoker_count)

@app.route('/region')
def region():
    region_counts = studyDataFrame["region"].value_counts()
    return render_template("region.html", region_counts=region_counts)

@app.route('/charges')
def charges():
    avg_charge = studyDataFrame["charges"].mean()
    return render_template("charges.html", avg_charge=round(avg_charge, 2))

@app.route('/additional', methods=["GET", "POST"])
def additional():
    if request.method == "POST":
        choice = int(request.form['choice'])
        if choice == 1:
            # Calculate average charge for the region of the user
            avgRegion = studyDataFrame.groupby("region").charges.mean()
            user_region = userDataFrame.region[0]
            avg = avgRegion.get(user_region, 0)
            return render_template("additional.html", region_avg=round(avg, 2))
        elif choice == 2:
            # Calculate average charge for the user's gender
            gender_count = studyDataFrame.groupby("sex").charges.mean()
            user_gender = userDataFrame.sex[0]
            avg = gender_count.get(user_gender, 0)
            return render_template("additional.html", gender_avg=round(avg, 2))
        elif choice == 3:
            # Calculate average charge for a region (user can input region)
            selected_region = request.form['region']
            avg_charge = studyDataFrame[studyDataFrame["region"] == selected_region]["charges"].mean()
            return render_template("additional.html", region_avg=round(avg_charge, 2))
        else:
            return render_template("additional.html", error="Invalid choice")
    return render_template("additional.html")

@app.route('/compare')
def compare():
    # Here we assume you would want to compare the user's data to the study data
    user_data = userDataFrame.iloc[0]
    comparison_data = {
        "Age": user_data['age'],
        "Gender": user_data['sex'],
        "BMI": user_data['bmi'],
        "Children": user_data['children'],
        "Smoker": user_data['smoker'],
        "Region": user_data['region'],
        "Charges": user_data['charges']
    }
    return render_template("compare.html", comparison_data=comparison_data)
"""
@app.route('/main', methods=["GET", "POST"])
def main():
    context = {"view": None}  # Default view

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

if __name__ == '__main__':
    app.run(debug=True)
