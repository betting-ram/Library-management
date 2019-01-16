from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied

# def admin_only(view_func):
#    def wrap(request, *args, **kwargs):
#        if request.role == "python":
#            return view_func(request, *args, **kwargs)
#        else:
#            return HttpResponseRedirect(reverse('login'))
#    return wrap

