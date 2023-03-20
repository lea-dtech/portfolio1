
echo "Build Start"
yum install sqlite-devel -y
python3.9 -m pip install -r requirements.txt
echo "Migration start"
python3.9 manage.py makemigrations
python3.9 manage.py migrate
echo "Migration End"
python3.9 manage.py collectstatic --noinput --clear
echo "Build End"