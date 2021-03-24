from flask_wtf import FlaskForm
from wtforms import TextField,TextAreaField,SelectField,SubmitField,FileField,validators 
from wtforms.validators import DataRequired, Email
  
class AddProperty(FlaskForm):
    Property_Title = TextField('Property Title', [validators.Required()])
    Description = TextAreaField('Description', [validators.Required() ])
    num_rooms = TextField('No. of Rooms',[ validators.Required()])
    num_bathrooms = TextField('No. of Bathrooms', [validators.Required()])
    price = TextField('Price',[validators.required()])
    property_type = SelectField("Property Type",choices=['House' ,'Apartment','Town house','Studio Units','Cottage',"Beach Front"])
    location = TextField("Location", [validators.required()])
    photo = FileField('Photo',[validators.required()])
    submit = SubmitField ('Add Property')