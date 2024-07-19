
def set_error_msg(request,msg):
    request.session['error_msg'] = msg
    return request

def unset_error_msg(request):
    request.session['error_msg'] = ""
    return request