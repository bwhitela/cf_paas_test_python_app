from pprint import pformat


def application(environ, start_response):
    input = environ['wsgi.input']
    input_data = input.read()

    status = '200 OK'
    output = 'Environ dictionary:\n\n'
    output += pformat(environ)
    output += '\n\n\nPOST data:\n\n'
    output += input_data
    output += '\n'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
