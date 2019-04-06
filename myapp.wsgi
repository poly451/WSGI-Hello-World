# from: https://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html
# This goes in /var/www/wsgi-scripts/

def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
    
# The following goes in your httpd.conf file (/etc/httpd/conf/httpd.conf -- or something like that!)
# If you're not sure where it is, try: $sudo find / -name "httpd.conf"

WSGIScriptAlias /myapp /var/www/wsgi-scripts/myapp.wsgi

<Directory "var/www/wsgi-scripts">
<IfVersion < 2.4>
  Order allow,deny
  Allow from all
</IfVersion>
<IfVersion >= 2.4>
  Require all granted
</IfVersion>
</Directory>
