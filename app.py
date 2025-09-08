from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_average(marks):
    return sum(marks) / len(marks)

def find_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        name = request.form["name"]
        marks = [
            int(request.form["sub1"]),
            int(request.form["sub2"]),
            int(request.form["sub3"]),
            int(request.form["sub4"]),
            int(request.form["sub5"])
        ]
        avg = calculate_average(marks)
        grade = find_grade(avg)
        result = {
            "name": name,
            "average": round(avg, 2),
            "grade": grade
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
