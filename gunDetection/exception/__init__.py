import sys

def error_msg(error, error_detail:sys):
    _,_, exc_tb = error_detail.exc_info()

    file_name= exc_tb.tb_frame.f_code.co_filename

    error_message = "Error in file: {0} at line number: {1} with error message: {2}".format(file_name, exc_tb.tb_lineno, error)

    return error_message


class AppException(Exception):
    def __init__(self, message, detail):
        super().__init__(message)
        self.message = error_msg(message, detail)

    def __str__(self):
        return self.message