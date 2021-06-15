from DB.app import db


class school(db.Model):
    __tablename__ = 'school'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    name = db.Column(db.String(45), unique=True, nullable=False)
    x = db.Column(db.DECIMAL(7, 4))
    y = db.Column(db.DECIMAL(7, 4))

    def __init__(self, name, id, x, y):
        self.id = id
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return 'id=%r, name=%r, x=%r, y=%r' % (self.id, self.name, self.x, self.y)
