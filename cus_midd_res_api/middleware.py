from django.utils.deprecation import MiddlewareMixin
import json

class CustomApiMiddleware(MiddlewareMixin):
    
    def __init__(self, get_response):
        self.get_response = get_response

    def process_response(self, request, response):
        import pdb;pdb.set_trace()
        response_data = response.content.decode('utf-8')
        data=json.loads(response_data) 
        if data: 
          for key, value in data.items():
            print(f"{key}: {value}")

    