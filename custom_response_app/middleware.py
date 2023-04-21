from django.utils.deprecation import MiddlewareMixin

class ExampleMiddleware(MiddlewareMixin):
    
    def __init__(self, get_response):
        self.get_response = get_response

    def process_response(self, request, response):
        response_data = response.content.decode('utf-8')
        processed_response_data = self.process_response_data(response_data)
        response.content = processed_response_data.encode('utf-8')
        return response

    def process_response_data(self, data):
        processed_data = data
        return processed_data

# class MyCustomMiddleware(MiddlewareMixin):
#     def process_response(self, request, response):
#         import pdb;pdb.set_trace()
#         # response_content = response.content
#         print(response)
#         response_data = response.content.decode('utf-8')
#         processed_response_data = self.process_response_data(response_data)
#         response.content = processed_response_data.encode('utf-8')

#         return response
