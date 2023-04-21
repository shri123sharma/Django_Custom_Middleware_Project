# def my_custom_decorator(view_func):
#     def wrapper(request, *args, **kwargs):
#         # Decorator logic
#         if hasattr(request, 'my_custom_decorator_applied') and request.my_custom_decorator_applied:
#             print("Decorator: Applied to view")
#             # Do something with the request before calling the view
#             # ...

#         response = view_func(request, *args, **kwargs)

#         # Do something with the response before returning it
#         # ...

#         return response
#     return wrapper

# from django.shortcuts import redirect
# from django.http import HttpResponse
# from django.shortcuts import redirect
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import user_passes_test

# def check_user_authenticated(user):
#     # import pdb;pdb.set_trace()
#     return user.is_authenticated

# def admin_required(view_func):
#     def wrapper(request, *args, **kwargs):
#         # import pdb;pdb.set_trace()
#         if request.user.is_authenticated:
#             if request.user.is_superuser:
#                 print('this admin user')
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('this is not an admin')
#         else:
            
#             return redirect('login_page')
#     return wrapper
