from DB.app import db


class building(db.Model):
    __tablename__ = 'building'
    id = db.Column(db.String(25), primary_key=True,
                   nullable=False)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    land_area = db.Column(db.DECIMAL(5, 2))
    floor_no = db.Column(db.String(10))
    floor_total = db.Column(db.String(10))
    type = db.Column(db.String(45))
    total_area = db.Column(db.DECIMAL(5, 2))
    room = db.Column(db.Integer)
    parlor = db.Column(db.Integer)
    bath = db.Column(db.Integer)
    total_price = db.Column(db.Integer)
    price_per = db.Column(db.Integer)
    parking_space_area = db.Column(db.DECIMAL(4, 2))
    parking_space_price = db.Column(db.Integer)
    balcony_area = db.Column(db.DECIMAL(4, 2))
    elevator = db.Column(db.String(3))

    def __init__(self, id, name, address, land_area, floor_no, floor_total,  type, total_area,
                 room, parlor, bath, total_price, price_per, parking_space_area,
                 parking_space_price, balcony_area, elevator):
        self.id = id
        self.name = name
        self.address = address
        self.land_area = land_area
        self.floor_no = floor_no
        self.floor_total = floor_total
        self.type = type
        self.total_area = total_area
        self.room = room
        self.parlor = parlor
        self.bath = bath
        self.total_price = total_price
        self.price_per = price_per
        self.parking_space_area = parking_space_area
        self.parking_space_price = parking_space_price
        self.balcony_area = balcony_area
        self.elevator = elevator

    def __repr__(self):
        return 'id=%r, name=%r, address=%r, land_area=%r, floor_no=%r, floor_total=%r, type=%r, total_area=%r, room=%r, parlor=%r, bath=%r, total_price=%r, price_per=%r, \
        parking_space_area=%r, parking_space_price=%r, balcony_area=%r, elevator=%r' \
        % (self.id, self.name, self.address, self.land_area, self.floor_no, self.floor_total, self.type, self.total_area, self.room, self.parlor, self.bath, self.total_price,
            self.price_per, self.parking_space_area, self.parking_space_price, self.balcony_area, self.elevator)
