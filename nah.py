from datetime import datetime, timedelta
from flask import Flask, render_template
import random

app = Flask(__name__)

# This variable stores the time when the random string was last generated
last_generated = datetime.now()

# This variable stores the current random string
current_string = ""

# This function generates a new random string
def generate_string():
    global current_string

    # Use the current time as the seed for the random number generator
    random.seed(datetime.now())

    # Generate a random string of length 8
    current_string = "".join(random.choices(string.ascii_lowercase, k=8))

# This route displays the current random string
@app.route("/")
def index():
    # Check if the random string needs to be regenerated
    global last_generated
    if (datetime.now() - last_generated) > timedelta(minutes=20):
        generate_string()
        last_generated = datetime.now()

    return render_template("index.html", random_string=current_string)

if __name__ == "__main__":
    app.run()
