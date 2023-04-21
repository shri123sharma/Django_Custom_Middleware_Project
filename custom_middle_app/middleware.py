from .decorators import *

# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
  
#     def __call__(self, request):
       
#         print("before response")
#         request = self.process_request(request)

#         response = self.get_response(request)

#         print("After response")
        
#         return response
    
#     def process_request(self, request):
#             # Apply the decorator logic here
#             if request.user.is_authenticated:
#                 # Apply the decorator
#                 request.my_custom_decorator_applied = True

#             return request

# class CustomMiddleware:
    
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("before call Response")

#     def __call__(self, request):
#         response = self.get_response(request)
#         print("after call Response")
#         return response