from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ceva_secret_key"

USERS = {
    "admin": {
        "password": "Ceva2026",
        "role": "admin"
    },
    "agent": {
        "password": "agent123",
        "role": "agent"
    }
}


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = USERS.get(username)

        if user and user["password"] == password:
            session["username"] = username
            session["role"] = user["role"]

            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect("/")

    return render_template(
        "index.html",
        username=session["username"],
        role=session["role"]
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)