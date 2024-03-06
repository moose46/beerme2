"""
realpython.com this file is renamed to flask_app.py
"""

from flask import Flask, render_template

from bets import betting_summary

app = Flask(__name__)


# https://alien-gadget-305416.ue.r.appspot.com/p
@app.route("/")
def index():
    # pick the winners
    for r in betting_summary.list_of_individual_bets:
        r.the_winner()

    # Use a breakpoint in the code line below to debug your script.

    return render_template(
        "beer.html",
        betting_summary=betting_summary,
        coolers=betting_summary.total_beers_owed,
    )


# to run this server, python main.py 5000
if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8089, debug=True)
    app.run(host="127.0.0.1", port=5000, debug=True)
    # app.run(debug=True)
