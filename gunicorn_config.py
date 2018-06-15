bind = '127.0.0.1:49153'
timeout = 600
max_requests = 2000
name = "tethys-gunicorn"
workers = 4
raw_env = [
          'HOME=/home/hydroapp'
          ]
log_level = 'debug'
accesslog = '/var/tethys_deploy/tethys/gunicorn/access.log'
errorlog = '/var/tethys_deploy/tethys/gunicorn/error.log'
capture_output = True
access_log_format = 'process%(p)s XFF%({X-Forwarded-For}i)s; %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
