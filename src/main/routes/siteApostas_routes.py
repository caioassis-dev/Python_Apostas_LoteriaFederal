import webbrowser
from flask import jsonify, Blueprint, request, render_template
from src.controllers.get_bets import ultimos_60_numeros
import pdb

apostas_routes_bp = Blueprint("apostas_routes", __name__)


@apostas_routes_bp.route("/sorteios")
def index():
    return render_template('jogosLoteria.html')

@apostas_routes_bp.route("/numeros", methods=["GET"])
def get_bets_numbers():
    try:
        qtdSorteios = int(request.args.get("qtdSorteios", 15)) 
        listaDezenas, listaFrequenciaElementos = ultimos_60_numeros(qtdSorteios)
        return jsonify({"numbers": listaDezenas})
    except Exception as e:
        return jsonify({"error": str(e)})