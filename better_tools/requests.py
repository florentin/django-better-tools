# http://djangosnippets.org/snippets/2336/
import inspect
from django.http import HttpRequest

def get_request(max_depth=10, request_name=None): #request_name='request'
    """
    Go back in time and fetch the request object
    """
    f = inspect.currentframe()
    requests = []
    depth = 0
    while not requests and f.f_back is not None and depth < max_depth:
        f = f.f_back
        if request_name:
            if request_name in f.f_locals:
                requests.append((request_name, f.f_locals[request_name]))
        else:
            for var, val in f.f_locals.iteritems():
                if isinstance(val, HttpRequest):
                    requests.append((var, val))
        depth += 1
    
    if depth == max_depth:
        raise Exception("Can't find the request object.")
    
    if not requests:
        request = None
    elif len(requests) == 1:
        request = requests[0][1]
    else:
        for var, val in requests:
            if var == 'request':
                request = val
        if request is None:
            request = requests[0][1]
    return request
