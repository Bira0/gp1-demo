from flask import Flask, request, session, render_template_string
import random

app = Flask(__name__)
app.secret_key = "gp1-demo" # nosec B105

def add_numbers(a, b):
    return a + b
    
def check_guess(guess, target):
    if guess < target:
        return "low"
    if guess > target:
        return "high"
    return "correct"

HTML = """
<!doctype html>
<title>High or Low Game</title>
<style>
body { font-family: Arial; text-align: center; padding: 40px; background: #f4f4f4; }
.card { background: white; max-width: 500px; margin: auto; padding: 30px; border-radius: 12px; }
input, button { padding: 10px; margin: 8px; }
img { width: 220px; border-radius: 10px; margin-top: 15px; }
</style>

<div class="card">
{% if state == "play" %}
  <h1>High or Low</h1>
  <p>Guess a number from 1 to 10</p>
  <p>Tries left: {{ tries }}</p>
  <form method="post">
    <input type="number" name="guess" min="1" max="10" required>
    <button type="submit">Guess</button>
  </form>
  <p>{{ message }}</p>

{% elif state == "win" %}
  <h1>🎉 Congratulations! 🎉</h1>
  <p>You guessed the number {{ target }}.</p>
  <img src="https://c.tenor.com/2C-iqDjJmnMAAAAd/tenor.gif">
  <form method="get"><button name="reset" value="1">Play Again</button></form>

{% else %}
  <h1>😢 You Lose</h1>
  <p>The number was {{ target }}.</p>
  <form method="get"><button name="reset" value="1">Try Again</button></form>
{% endif %}
</div>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.args.get("reset") == "1" or "target" not in session:
        session["target"] = random.randint(1, 10)  # nosec B311
        session["tries"] = 3

    message = ""
    state = "play"

    if request.method == "POST":
        guess = int(request.form["guess"])
        target = session["target"]
        session["tries"] -= 1

        result = check_guess(guess, target)

        if result == "correct":
            state = "win"
        elif session["tries"] == 0:
            state = "lose"
        elif result == "low":
            message = "Too low"
        else:
            message = "Too high"

    if session["tries"] == 0 and request.method != "POST":
        state = "lose"

    return render_template_string(
        HTML,
        state=state,
        tries=session["tries"],
        message=message,
        target=session["target"]
    )

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8080)  # nosec B104