#!/bin/bash

echo curl http://127.0.0.1:5000/car/1
curl http://127.0.0.1:5000/car/1
echo ""
echo curl http://127.0.0.1:5000/car/
curl http://127.0.0.1:5000/car/
echo ""
echo curl -d '{"make":"Seat", "model":"Cordoba", "year":"2003"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/avgprice
curl -d '{"make":"Seat", "model":"Cordoba", "year":"2003"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/avgprice
echo ""
echo curl -d '{"make":"Seat", "model":"Cordoba", "year":"2003", "chassis_id":"12345F"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/car
curl -d '{"make":"Seat", "model":"Cordoba", "year":"2003", "chassis_id":"12345F"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/car