from dash import Dash, html
# from flask import Flask
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.layout import create_layout

# server = Flask(__name__)   
# app = Dash(server=server)
# app.title = "Floit Dashboard"
# app.layout = create_layout(app)
# app.run_server(port=5000)

def main() -> None: 
    # server = Flask(__name__)   
    # app = Dash(server=server)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Floit Dashboard"
    app.layout = create_layout(app)
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__== "__main__":
    main()
    
