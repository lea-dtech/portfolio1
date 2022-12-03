
echo "Build Start"
python3.9 -m pip install -r requirements.txt
ech "Make Migration"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
echo "collect statics"
python3.9 manage.py collectstatic --noinput --clear
echo "Build End"