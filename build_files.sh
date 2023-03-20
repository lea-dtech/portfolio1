
echo "Build Start"
pip3 install db-sqlite3
echo $PYTHONPATH
export PYTHONPATH=”/usr/local/lib/python3.9/site-packages:$PYTHONPATH”
python3.9 -m pip install -r requirements.txt
echo "Migration start"
python3.9 manage.py makemigrations
python3.9 manage.py migrate
echo "Migration End"
python3.9 manage.py collectstatic --noinput --clear
echo "Build End"