
import json
import datetime
import time

# Working URL
url = 'http://localhost:8080/ui'
# API Methods
status = 'v1/status'
system_monitoring = 'v1/system_monitoring'

# Status Code
OK_status_code = 200

# Generate DATA
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S ')
default_data_response_request = {'status': 'ok', 'timestamp': st}
data = json.dumps(default_data_response_request)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}