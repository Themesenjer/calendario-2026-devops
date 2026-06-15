from flask import Flask
import calendar

app = Flask(__name__)

@app.route("/")
def inicio():

    html = "<h1>Calendario 2026</h1>"

    for mes in range(1, 13):

        html += f"<h2>{calendar.month_name[mes]} 2026</h2>"
        html += f"<pre>{calendar.month(2026, mes)}</pre>"

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)