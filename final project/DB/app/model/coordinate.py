from DB.app import db


class coordinate(db.Model):
    __tablename__ = 'coordinate'
    name = db.Column(db.String(50), primary_key=True, nullable=False)
    x = db.Column(db.DECIMAL(7, 4))
    y = db.Column(db.DECIMAL(7, 4))

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return 'name=%r, x=%r, y=%r' % (self.name, self.x, self.y)
