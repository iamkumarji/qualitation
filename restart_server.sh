#!/bin/bash
echo "Stopping any running Django servers..."
pkill -f "manage.py runserver"
sleep 2
echo "Starting Django server..."
cd /Users/shubham/Desktop/qualitation
source venv/bin/activate
python manage.py runserver
