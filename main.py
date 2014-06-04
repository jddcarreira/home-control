import web
import serial

urls = (
    '/', 'index',
    '/lighton', 'lighton',
    '/lightoff', 'lightoff',
    '/temp', 'temp',
    '/light', 'light'
)

ser = serial.Serial('/dev/ttyACM0', 9600)


class index:
    def GET(self):
        return "<h1>GET AWAY!!!</h1>"


class lightoff:
    def GET(self):
        ser.write('0')
        return False


class lighton:
    def GET(self):
        ser.write('1')
        return True


class light:
    def GET(self):
        ser.write('4')
        light = ser.readline()
        return light


class temp:
    def GET(self):
        ser.write('3')
        temp = ser.readline()
        return temp


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


