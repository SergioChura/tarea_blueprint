from flask import Blueprint, render_template

admin_bp = Blueprint('admin',__name__,url_prefix='/admin',template_folder='templates')

@admin_bp.route("/panel")
def panel():
    return "<h3>BIEVENIDO AL PANEL DE ADMINSTRACION: </h3>"


