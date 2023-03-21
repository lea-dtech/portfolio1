
echo "Build Start"
pip install db-sqlite3
export PYTHONPATH=”/usr/local/lib/python3.9/site-packages:$PYTHONPATH”
# yarn add sqlite sqlite-dev sqlite3
# sqlite-dev libsqlite3-dev 
python3.9 -m pip install -r requirements.txt
# echo "Migration start"
# python3.9 manage.py makemigrations
# python3.9 manage.py migrate
# echo "Migration End"
python3.9 manage.py collectstatic --noinput --clear
echo "Build End"

# echo "Installing docker"
# yarn add docker
# yarn add docker-compose
# echo "Build Start"
# docker build -t django_web:latest .
# docker-compose up -d
# echo "Build End"