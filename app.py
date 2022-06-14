from flask import Flask, jsonify, make_response, render_template
from buergerbot import fetch_months, extract_links, get_month_name

app = Flask(__name__)

services = [
    { 'id': 120702, 'name': 'Meldebescheinigung' },
    { 'id': 120686, 'name': 'Anmeldung' }
]

@app.route("/")
def get_home():
    return render_template('home.html', services=services)

@app.route("/<int:service>")
def get_service(service):
    html_data = ''
    months = fetch_months(service)
    for month in months:
        html_data += f'<h2>{get_month_name(month)}</h2>'
        links = extract_links(month)
        html_data += '<ul>'
        if links:
            html_data += '\n'.join([f'<li><a target=”_blank” href={link[1]}>{link[0]}</a></li>' for link in links])
        else:
            html_data += '\n(none)'
        html_data += '</ul>'

    return render_template('service.html', dates=html_data)

@app.errorhandler(404)
def resource_not_found(e):
    return render_template('404.html', title = '404'), 404

if __name__ == '__main__':
    app.run()