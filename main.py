import web
from giacpy import giac

urls = (
    '/giac', 'index'
)


class index:
    def POST(self):
        try:
            webData = web.data().decode("utf-8")
            result = str(giac(str(webData)))
            return result
        except:
            pass
        return "undefined"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
