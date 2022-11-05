from dash import Dash, html
# from flask import Flask
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.layout import create_layout
from src.data.loader import load_raw_adidas_data

DATA_PATH = "./data/adidas_usa.csv"

def main() -> None: 
    # server = Flask(__name__)   
    # app = Dash(server=server)
    data = load_raw_adidas_data(DATA_PATH)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Floit Dashboard"
    app.layout = create_layout(app, data)
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__== "__main__":
    main()
    
