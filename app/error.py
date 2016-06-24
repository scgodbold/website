from flask import render_template, request

from app import app


@app.errorhandler(404)
def page_not_found(e):
    print request.referrer
    return render_template('errors/404.html', prev=request.referrer), 404
