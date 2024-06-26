class OK:
    def __init__(self):
        self.code = 200
        self.message = "Request successful"


class NotFound:
    def __init__(self):
        self.code = 404
        self.message = "Page not found"


class ServerError:
    def __init__(self):
        self.code = 500
        self.message = "Internal Server Error"


def status(error_obj):
    return {
        "code": error_obj.code,
        "message": error_obj.message
    }
