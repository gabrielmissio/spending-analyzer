class Page:

  def __init__(self, current_page, paginate_by, url):
    self.__current_page = current_page
    self.__paginate_by = paginate_by
    self.__all_rows = 0
    self.__url = url

  def get_url(self):
    return self.__url

  def set_all_rows(self, rows):
    self.__all_rows = rows
  
  def get_all_rows(self):
    return self.__all_rows

  def get_page_count(self):
    num_pages = self.__all_rows/self.__paginate_by
    num_pages_int = int(num_pages)
    if(num_pages_int == 0):
      return int(1)
    if(num_pages%num_pages_int == 0):
      return int(num_pages)
    
    return int(num_pages + 1)

  def get_current_page(self):
    return self.__current_page

  def get_paginate_by(self):
    return self.__paginate_by

  def get_next_page(self):
    url_next_page = None
    if(self.check_next_page()):
      next = str(self.__current_page + 1)
      url_next_page = "{}?page={}&paginate_by={}".format(self.__url, next, self.__paginate_by)#self.__url
    return url_next_page

  def get_previous_page(self):
    url_previous_page = None
    if(self.check_previous_page()):
      previous = str(self.__current_page - 1)
      url_previous_page = "{}?page={}&paginate_by={}".format(self.__url, previous, self.__paginate_by)#self.__url
    return url_previous_page

  def check_next_page(self):
    return (self.__current_page + 1 <= self.get_page_count())
  
  def check_previous_page(self):
    return (self.__current_page - 1 >= 1)

  def __str__(self):
    return "current_page: {}, paginate_by: {}, all_rows: {}, url: {}".format(self.__current_page, self.__paginate_by, self.__all_rows, self.__url)