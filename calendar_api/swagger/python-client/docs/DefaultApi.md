# swagger_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/GJSCRAVEIRO/Calendar/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_get**](DefaultApi.md#schedules_get) | **GET** /schedules | Get a list of all schedules
[**schedules_guard_guard_id_get**](DefaultApi.md#schedules_guard_guard_id_get) | **GET** /schedules/guard/{guardId} | Get schedules by guard ID
[**schedules_location_location_name_get**](DefaultApi.md#schedules_location_location_name_get) | **GET** /schedules/location/{locationName} | Get schedules by location name
[**schedules_post**](DefaultApi.md#schedules_post) | **POST** /schedules | Create a new schedule
[**schedules_schedule_id_delete**](DefaultApi.md#schedules_schedule_id_delete) | **DELETE** /schedules/{scheduleId} | Delete a schedule by ID
[**schedules_schedule_id_get**](DefaultApi.md#schedules_schedule_id_get) | **GET** /schedules/{scheduleId} | Get a specific schedule by ID
[**schedules_schedule_id_put**](DefaultApi.md#schedules_schedule_id_put) | **PUT** /schedules/{scheduleId} | Update a schedule by ID
[**schedules_switch_post**](DefaultApi.md#schedules_switch_post) | **POST** /schedules/switch | Switch a schedule between two guards

# **schedules_get**
> list[Schedule] schedules_get()

Get a list of all schedules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get a list of all schedules
    api_response = api_instance.schedules_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->schedules_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Schedule]**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_guard_guard_id_get**
> list[Schedule] schedules_guard_guard_id_get(guard_id)

Get schedules by guard ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
guard_id = 'guard_id_example' # str | 

try:
    # Get schedules by guard ID
    api_response = api_instance.schedules_guard_guard_id_get(guard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->schedules_guard_guard_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_id** | **str**|  | 

### Return type

[**list[Schedule]**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_location_location_name_get**
> list[Schedule] schedules_location_location_name_get(location_name)

Get schedules by location name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
location_name = 'location_name_example' # str | 

try:
    # Get schedules by location name
    api_response = api_instance.schedules_location_location_name_get(location_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->schedules_location_location_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**|  | 

### Return type

[**list[Schedule]**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_post**
> schedules_post(body)

Create a new schedule

Creates a new schedule entry for a guard, checking for conflicts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Schedule() # Schedule | 

try:
    # Create a new schedule
    api_instance.schedules_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->schedules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Schedule**](Schedule.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_id_delete**
> schedules_schedule_id_delete(schedule_id)

Delete a schedule by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
schedule_id = 'schedule_id_example' # str | 

try:
    # Delete a schedule by ID
    api_instance.schedules_schedule_id_delete(schedule_id)
except ApiException as e:
    print("Exception when calling DefaultApi->schedules_schedule_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_id_get**
> Schedule schedules_schedule_id_get(schedule_id)

Get a specific schedule by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
schedule_id = 'schedule_id_example' # str | 

try:
    # Get a specific schedule by ID
    api_response = api_instance.schedules_schedule_id_get(schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->schedules_schedule_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_id_put**
> schedules_schedule_id_put(body, schedule_id)

Update a schedule by ID

Updates an existing schedule, checking for conflicts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Schedule() # Schedule | 
schedule_id = 'schedule_id_example' # str | 

try:
    # Update a schedule by ID
    api_instance.schedules_schedule_id_put(body, schedule_id)
except ApiException as e:
    print("Exception when calling DefaultApi->schedules_schedule_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Schedule**](Schedule.md)|  | 
 **schedule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_switch_post**
> schedules_switch_post(body)

Switch a schedule between two guards

Allows the swapping of a specific schedule from one guard to another.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.SchedulesSwitchBody() # SchedulesSwitchBody | 

try:
    # Switch a schedule between two guards
    api_instance.schedules_switch_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->schedules_switch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SchedulesSwitchBody**](SchedulesSwitchBody.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

