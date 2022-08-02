from flask import render_template, request, redirect, url_for, flash
from werkzeug import exceptions
from datetime import datetime
from url_shortener.models import ShortUrls
from url_shortener import app, db
from random import choice
import string

def gen_short_id(num_of_chars: int):
	return ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_of_chars))

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		url = request.form['url']
		short_id = request.form['shortened_id']

		if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
			flash('Shortened ID already exists!')
			return redirect(url_for('index'))
		if not url:
			flash('Please enter a URL!')
			return redirect(url_for('index'))
		if not short_id:
			short_id = gen_short_id(5)

		new_url = ShortUrls(original_url=url, short_id=short_id, created_at=datetime.utcnow())
		db.session.add(new_url)
		db.session.commit()

		short_url = request.host_url + short_id
  
		return render_template('index.html', short_url=short_url)

	return render_template('index.html')

@app.route('/<short_id>')
def redirect_to_url(short_id):
	link = ShortUrls.query.filter_by(short_id=short_id).first()
	if link:
		return redirect(link.original_url)
	else:
		raise exceptions.NotFound()

@app.errorhandler(exceptions.NotFound)
def handle_404(e):
    return render_template('errors/404.html'), 404