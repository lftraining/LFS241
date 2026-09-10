import json
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

sys.stdout = sys.stderr


def u_repr(obj):
    if isinstance(obj, dict):
        return '{' + ', '.join('%s: %s' % (u_repr(k), u_repr(v))
                               for k, v in obj.items()) + '}'
    elif isinstance(obj, str):
        return "u'%s'" % obj.replace("'", "\\'")
    elif isinstance(obj, list):
        return '[' + ', '.join(u_repr(i) for i in obj) + ']'
    else:
        return repr(obj)


class AlertHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        data = json.loads(self.rfile.read(content_len))

        print("Received %u %s alerts:" % (len(data["alerts"]), data["status"]))

        print("\tGrouping labels:")
        for k, v in data['groupLabels'].items():
            print("\t\t%s = %s" % (k, u_repr(v)))

        print("\tCommon labels:")
        for k, v in data['commonLabels'].items():
            print("\t\t%s = %s" % (k, u_repr(v)))

        print("\tCommon annotations:")
        for k, v in data['commonAnnotations'].items():
            print("\t\t%s = %s" % (k, u_repr(v)))

        print("\t\tAlert details:")
        for idx, alert in enumerate(data['alerts']):
            print("\t\t\tAlert %u:" % idx)
            print("\t\t\t\tLabels: %s" % u_repr(alert['labels']))
            print("\t\t\t\tAnnotations: %s" % u_repr(alert['annotations']))

        self.send_response(200)
        self.end_headers()


if __name__ == '__main__':
    httpd = HTTPServer(('', 9595), AlertHandler)
    print("Listening on port 9595...")
    httpd.serve_forever()
