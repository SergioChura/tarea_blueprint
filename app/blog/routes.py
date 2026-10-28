from flask import Blueprint, render_template

blog_bp = Blueprint('blog',__name__,url_prefix='/blog',template_folder='templates')

@blog_bp.route("/")
def mostrar():
    return render_template('base.html')


@blog_bp.route("/titulo/<id>")
def mostrar_titulo(id):
    return "<h3>Este es el titulo de mi blog: "+id+" </h3>"
