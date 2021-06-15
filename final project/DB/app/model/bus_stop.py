from DB.app import db


class bus_stop(db.Model):
    __tablename__ = 'bus_stop'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    line = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    x = db.Column(db.DECIMAL(7, 4))
    y = db.Column(db.DECIMAL(7, 4))

    def __init__(self, id, line, name, x, y):
        self.id = id
        self.line = line
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return 'id=%r, line=%r, name=%r, , x=%r, y=%r' % (self.id, self.line, self.name, self.x, self.y)
