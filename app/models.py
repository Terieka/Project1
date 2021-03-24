from . import db




class Properties(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Properties'

    property_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    Property_Title = db.Column(db.String(80))
    Description = db.Column(db.String(80))
    num_rooms = db.Column(db.String(80))
    num_bathrooms = db.Column(db.String(80))
    price=db.Column(db.String(80))
    property_type=db.Column(db.String(80))
    location=db.Column(db.String(80))
    photo=db.Column(db.String(80))



    def __init__(self, property_id, Property_Title, Description, num_rooms,num_bathrooms,price,property_type,location,photo):
        self.property_id=property_id
        self.Property_Title=Property_Title
        self.property_type=property_type
        self.Description=Description
        self.num_bathrooms=num_bathrooms
        self.num_rooms=num_rooms
        self.price=price
        self.location=location
        self.photo=photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.property_id)  # python 2 support
        except NameError:
            return str(self.property_id)  # python 3 support

   