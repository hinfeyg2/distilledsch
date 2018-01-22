from app import db, Car
import datetime


db.create_all()

with open('data/distilledsch_data.csv', 'rt', encoding='utf-8') as file:
	next(file)
	for line in file:
		make, model, year, chassis_id, _id, last_updated, price = line.strip().split(',')
		parsed_datetime = datetime.datetime.strptime(last_updated, '%Y-%m-%d %H:%M:%S')
		car = Car(make=make, model=model, year=year, chassis_id=chassis_id, id=_id, last_updated=parsed_datetime, price=price)
		db.session.add(car)

db.session.commit()