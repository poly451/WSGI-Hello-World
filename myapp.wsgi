# from: https://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html
# This goes in /var/www/wsgi-scripts/

def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
    

