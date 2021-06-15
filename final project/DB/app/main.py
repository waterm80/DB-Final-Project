from io import SEEK_CUR
from os import write
from flask import *
from sqlalchemy.orm import query
from . import app, db
from .model.school import school
from .model.bus_stop import bus_stop
from .model.medical_institution import medical_institution
from .model.building import building
from .model.coordinate import coordinate
from sqlalchemy import *
from .form.view_form import *
from .distance import distance
import matplotlib.pyplot as plt


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/price', methods=['GET', 'POST'])
def price():
    form = Form1()
    if form.validate_on_submit():
        return redirect(url_for('display_price', name=form.name.data, range=form.range.data))
    return render_template('price.html', form=form)


@app.route('/price_result/<name>/<range>')
def display_price(name, range):
    target = coordinate.query.filter_by(name=name).first()
    building_list = building.query.all()
    building_near_list = []
    for item in building_list:
        if(name != item.name):
            tmp = coordinate.query.filter_by(name=item.name).first()
            if(float(distance(target.x, target.y, tmp.x, tmp.y)) <= float(range)):
                building_near_list.append(item.id)
    building_query = building.query.filter(building.id.in_(building_near_list))
    return render_template('result_price.html', data=building_query)


@app.route('/information', methods=['GET', 'POST'])
def information():
    form = Form7()
    if form.validate_on_submit():
        return redirect(url_for('display_single', name=form.name.data))
    return render_template('information.html', form=form)


@app.route('/single_result/<name>')
def display_single(name):
    query = building.query.filter_by(name=name).all()
    return render_template('result_single.html', data=query)


@app.route('/compare', methods=['GET', 'POST'])
def compare():
    form = Form2()
    if form.validate_on_submit():
        return redirect(url_for('display_compare', name1=form.name1.data, name2=form.name2.data))
    return render_template('compare.html', form=form)


@app.route('/compare_result/<name1>/<name2>')
def display_compare(name1, name2):
    query1 = building.query.filter_by(name=name1).first()
    query2 = building.query.filter_by(name=name2).first()
    return render_template('result_compare.html', data1=query1, data2=query2)


@app.route('/inrange', methods=['GET', 'POST'])
def inrange():
    form = Form1()
    if form.validate_on_submit():
        return redirect(url_for('display_mul', name=form.name.data, range=form.range.data))
    return render_template('inrange.html', form=form)


@app.route('/range_result/<name>/<range>')
def display_mul(name, range):
    target = coordinate.query.filter_by(name=name).first()
    school_list = school.query.all()
    bus_list = bus_stop.query.all()
    medical_list = medical_institution.query.all()
    sch_near_list = []
    bus_near_list = []
    medical_near_list = []
    for item in school_list:
        if(float(distance(target.x, target.y, item.x, item.y)) <= float(range)):
            sch_near_list.append(item.id)
    for item in bus_list:
        if(float(distance(target.x, target.y, item.x, item.y)) <= float(range)):
            bus_near_list.append(item.id)
    for item in medical_list:
        if(float(distance(target.x, target.y, item.x, item.y)) <= float(range)):
            medical_near_list.append(item.id)
    sch_query = school.query.filter(school.id.in_(sch_near_list))
    bus_query = bus_stop.query.filter(bus_stop.id.in_(bus_near_list))
    medical_query = medical_institution.query.filter(
        medical_institution.id.in_(medical_near_list))
    return render_template('result_multi.html', name=name, sch_data=sch_query, bus_data=bus_query, medical_data=medical_query)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = Form4()
    if form.validate_on_submit():
        cur = db.session.query(func.max(building.id)).scalar()+1
        Building = building(id=cur, name=form.name.data, address=form.address.data, land_area=form.land_area.data, floor_no=form.floor_no.data, floor_total=form.floor_total.data,
                            type=form.type.data, total_area=form.total_area.data, room=form.room.data, parlor=form.parlor.data, bath=form.bath.data, total_price=form.total_price.data, price_per=form.price_per.data,
                            parking_space_area=form.parking_space_area.data, parking_space_price=form.parking_space_price.data, balcony_area=form.balcony_area.data, elevator=form.elevator.data)
        db.session.add(Building)
        db.session.commit()
        return '新增成功'
    return render_template('add.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = Form5()
    if form.validate_on_submit():
        query = building.query.filter_by(
            name=form.name.data, floor_no=form.floor_no.data, address=form.address.data).first()
        if query == None:
            return '查無此建案，請重新輸入'
        db.session.delete(query)
        db.session.commit()
        return '刪除成功'
    return render_template('delete.html', form=form)


@app.route('/rate', methods=['GET', 'POST'])
def rate():
    form = Form7()
    if form.validate_on_submit():
        target = coordinate.query.filter_by(name=form.name.data).first()
        avg = db.session.query(func.avg(building.price_per)).filter_by(
            name=form.name.data).one()
        school_list = school.query.all()
        bus_list = bus_stop.query.all()
        medical_list = medical_institution.query.all()
        sum = 0
        for item in school_list:
            if(float(distance(target.x, target.y, item.x, item.y)) <= 1):
                sum += 3
        for item in bus_list:
            if(float(distance(target.x, target.y, item.x, item.y)) <= 0.5):
                sum += 1
        for item in medical_list:
            if(float(distance(target.x, target.y, item.x, item.y)) <= 2):
                sum += 2
        return render_template('result_rate.html', name=form.name.data, sum=sum, price=avg[0], CP=round(sum/avg[0]*1000, 2))
    return render_template('rate.html', form=form)


if __name__ == '__main__':
    app.debug = True
    app.run()
