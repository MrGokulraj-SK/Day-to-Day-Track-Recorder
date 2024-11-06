from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="todo"
)
cursor = db.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Extract form data
        wakeup = request.form.get("wakeup")
        meditation = request.form.get("meditation")
        exercise = request.form.get("exercise")
        english = request.form.get("english")
        technical = request.form.get("technical")
        knew_topic_tech = request.form.get("knew_topic_tech")
        placement = request.form.get("placement")
        knew_topic_placement = request.form.get("knew_topic_placement")
        tech_affairs = request.form.get("techaffairs")
        knew_topic_techaffairs = request.form.get("knew_topic_techaffairs")
        mern = request.form.get("mern")
        knew_topic_mern = request.form.get("knew_topic_mern")
        program = request.form.get("program")
        nofap = request.form.get("nofap")
        note = request.form.get("note")

        # Insert data into MySQL database
        sql = """INSERT INTO daily_activity (
            submission_time,wakeup, meditation, exercise, english, technical, knew_topic_tech,
            placement, knew_topic_placement, tech_affairs, knew_topic_techaffairs,
            mern, knew_topic_mern, program, nofap, note
        ) VALUES (CURRENT_TIMESTAMP(),%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        data = (
            wakeup, meditation, exercise, english, technical, knew_topic_tech,
            placement, knew_topic_placement, tech_affairs, knew_topic_techaffairs,
            mern, knew_topic_mern, program, nofap, note
        )

        cursor.execute(sql, data)
        db.commit()

        return redirect(url_for("index"))

    return render_template("index.html")


@app.route("/track_details", methods=["GET"])
def table_details():
    # Fetch data from the MySQL database
    cursor.execute("SELECT * FROM daily_activity")
    table_data = cursor.fetchall()

    return render_template("track_record.html", table_data=table_data)


if __name__ == "__main__":
    app.run(debug=True)
