from DB.app import db


class medical_institution(db.Model):
    __tablename__ = 'medical_institution'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    name = db.Column(db.String(40), unique=True)
    x = db.Column(db.DECIMAL(7, 4))
    y = db.Column(db.DECIMAL(7, 4))

    def __init__(self, id, name, x, y):
        self.id = id
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return 'id=%r, name=%r, phone_number=%r, x=%r, y=%r' % (self.id, self.name, self.phone_number, self.x, self.y)
