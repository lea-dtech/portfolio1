
echo "Build Start"
yum install python3
python3.9 -m pip install -r requirements.txt
echo "Migration start"
python3.9 manage.py makemigrations
python3.9 manage.py migrate
echo "Migration End"
python3.9 manage.py collectstatic --noinput --clear
echo "Build End"