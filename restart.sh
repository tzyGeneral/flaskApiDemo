uwsgi --stop ./uwsgi.pid
sleep 1
git pull
sleep 1
git submodule update
sleep 1
uwsgi --ini uwsgi.ini --safe-pidfile ./uwsgi.pid
sleep 5