from server_errors import OK, NotFound, ServerError, status


if __name__ == "__main__":
    error_list = [OK(), NotFound(), ServerError()]

    for err in error_list:
        print(status(err))
