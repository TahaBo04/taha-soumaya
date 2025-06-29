from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Memory for the /moments section
user_memories = []

# Memory for the /promise section
her_promise_text = ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/pictures")
def pictures():
    return render_template("pictures.html")

@app.route("/moments", methods=["GET", "POST"])
def moments():
    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")
        if title and text:
            user_memories.append({"title": title, "text": text})
        return redirect("/moments")
    return render_template("moments.html", user_memories=user_memories)

@app.route("/promise", methods=["GET", "POST"])
def promise():
    global her_promise_text
    if request.method == "POST":
        her_promise_text = request.form.get("her_promise")
        return redirect("/promise")
    return render_template("promise.html", her_promise=her_promise_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

