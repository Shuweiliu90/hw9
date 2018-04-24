from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

@app.route('/')
def quote():
    server='My server'
    with open('inspiration.txt') as fp:
        num = random.randrange(1,10,1)
        quote = fp.readlines()[num]

    return render_template(
            'Quote.html',
            quote = quote,
            server = server
            )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
