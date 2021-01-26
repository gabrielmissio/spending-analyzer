from datetime import datetime

def get_date_now():
    data_atual = datetime.now()
    data_atual = data_atual.strftime("%Y-%m-%d %H:%M:%S") + '.000'
    return datetime.now()

def format_datetime(data_atual):
    data_atual = data_atual.strftime("%Y-%m-%d %H:%M:%S") + '.000'
    return data_atual