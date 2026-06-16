from flask import Flask
import calendar

app = Flask(__name__)

VERSION = "3.0.0"

@app.route("/")
def inicio():

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>

        <title>Calendario 2026</title>

        <style>

            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f9;
                margin: 20px;
            }}

            h1 {{
                text-align: center;
                color: #2c3e50;
            }}

            h2 {{
                text-align: center;
                color: #34495e;
            }}

            #reloj {{
                text-align: center;
                font-size: 28px;
                font-weight: bold;
                color: #27ae60;
                margin-bottom: 30px;
            }}

            .contenedor {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
            }}

            .mes {{
                background: white;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.2);
            }}

            pre {{
                font-size: 14px;
            }}

        </style>

    </head>

    <body>

        <h1>📅 Calendario 2026</h1>
        <h2>Versión {VERSION}</h2>

        <div id="reloj"></div>

        <div class="contenedor">
    """

    for mes in range(1, 13):

        html += f"""
        <div class="mes">
            <h3>{calendar.month_name[mes]}</h3>
            <pre>{calendar.month(2026, mes)}</pre>
        </div>
        """

    html += """
        </div>

        <script>

        function actualizarHora() {

            const ahora = new Date();

            const opciones = {
                timeZone: 'America/Guayaquil',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit'
            };

            document.getElementById('reloj').innerHTML =
                'Hora de Quito, Ecuador: ' +
                ahora.toLocaleTimeString('es-EC', opciones);

        }

        setInterval(actualizarHora, 1000);
        actualizarHora();

        </script>

    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)