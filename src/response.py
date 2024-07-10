from typing import Union

class Response:
    def __init__(self, success: bool, message: str, data: Union[dict, list] = {}):
        self.success = success
        self.message = message
        self.data = data

    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data
        }
