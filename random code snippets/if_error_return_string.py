

def get_error_string(error_code):
    '''
        # Return constants
        WRONG_FORMAT = -5 # Value error
        FILENOTFOUND = -404
        UNKNOWN_ERROR = -1
        UNSUCCESSFUL = 0 # No error, but search yealded no results
        SUCCESS = 1
    '''
    if error_code == 0:
        return 'Nothing was found (no error)'
    elif error_code == -1:
        return 'Unknown error, program needs debugging!'
    elif errod_code == -5:
        return 'Líklega slegið inn rangt format á dags (Value Error)'
    elif error_code = -404:
        return 'Fann ekki skrá! Vinsamlegast athugaðu gagnabankann'
    else:
        return 'Success, why are you printing this out?!?'
