# Columns in api_logs.csv  

timestamp - date and time when the API request was recorded  
endpoint - API resource endpoint that was called  
status_code - HTTP response code returned by the API (e.g., 200, 404, 500)  
response_time_ms - response time of the API request in milliseconds  
service_name - name of the service or microservice handling the request  

# Columns in cart_abandonment.csv

user_id - unique identifier of the user who abandoned the cart  
cart_id - unique identifier of the shopping cart  
abandonment_time - date and time when the cart was abandoned  
items_in_cart - number of items left in the cart at abandonment  
total_value - total monetary value of the items left in the cart  
