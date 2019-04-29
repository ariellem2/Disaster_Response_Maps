from flask import Flask, request, session, g, redirect, \
    url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/mapbox_js')
def mapbox_js():
    return render_template(
        'mapbox_js.html',
        ACCESS_KEY=sk.eyJ1IjoiYXJpZWxsZW1pcm8iLCJhIjoiY2p1dmZuY2hxMDE2bTRkc2sybTlsdmhrciJ9.V-vxV9-E0NW1YOfC923rUQ
    )
