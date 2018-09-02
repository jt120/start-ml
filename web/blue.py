from flask import Flask, url_for
from simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

@app.route('/hello/')
def hello():
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        print(url)
    return 'hello'