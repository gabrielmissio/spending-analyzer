def paginate_by_validation(message):
    if(message["multiValueQueryStringParameters"] is None):
     return 10
  
    payload = message["multiValueQueryStringParameters"]
    if ("paginate_by" in payload):
      if(int(message["multiValueQueryStringParameters"]["paginate_by"][0]) != 0):
        return int(message["multiValueQueryStringParameters"]["paginate_by"][0])

    return 10

def page_validation(message):
    if(message["multiValueQueryStringParameters"] is None):
      return 1
    payload = message["multiValueQueryStringParameters"]
    if ("page" in payload):
      if(int(message["multiValueQueryStringParameters"]["page"][0]) != 0):
        return int(message["multiValueQueryStringParameters"]["page"][0])
    
    return 1