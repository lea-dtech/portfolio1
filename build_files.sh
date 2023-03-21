
echo "Build Start"
yarn add mysql-libmysqlclient
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