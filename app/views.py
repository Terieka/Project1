"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from app import db
from flask import render_template, request, redirect, url_for
from .forms import AddProperty
from app.models import Properties


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Terieka Henry")

@app.route('/property')
def add_property():
    form=AddProperty()

    if request.method=='POST' and form.validate_on_submit():
        prop= Properties(property_id=property_id,Property_Title=form.Property_Title.data,Description=form.Description.data,num_rooms=form.num_rooms.data,num_bathrooms=form.num_bathrooms.data,price=form.price.data,property_type=form.property_type.data,location=form.location.data,photo=form.photo.data )
        db.session.add(prop)
        db.session.commit()
        quit()
        return redirect (url_for('properties'))
        flash("Property Sucessfully added")


    return render_template ('property.html',form=form)


@app.route('/properties')
def properties():
    return render_template('properties.hmtl')

@app.route()
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
