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

# Columns in clickstream.csv

user_id - unique identifier of the user  
timestamp - date and time when the user action was recorded  
page - the webpage or URL where the user interaction happened  
element_clicked - the specific element on the page that the user clicked  

# Columns session_tracking.csv

session_id - unique identifier of the user session  
user_id - unique identifier of the user  
start_time - date and time when the session started  
end_time - date and time when the session ended  
page_sequence - ordered list of pages visited during the session  
drop_off_page - the page where

# Columns user_feedback.csv

user_id - unique identifier of the user providing feedback  
timestamp - date and time when the feedback was submitted  
feedback_text - text content of the user’s feedback or comment  
rating - numeric score or rating given by the user (e.g., 1-5)  
