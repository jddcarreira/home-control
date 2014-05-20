import web
import serial

urls = (
    '/', 'index',
    '/lighton', 'lighton',
    '/lightoff', 'lightoff',
    '/sensors', 'sensors'
)

ser = serial.Serial('/dev/ttyACM0', 9600)


class index:
    def GET(self):
        return "<h1>GET AWAY!!!</h1>"


class lighton:
    def GET(self):
        ser.write('1')
        return True


class lightoff:
    def GET(self):
        ser.write('0')
        return False


class sensors:
    def GET(self):
        values = ser.readline()
        return values


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


