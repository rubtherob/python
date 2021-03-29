'''
Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший
больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

'''


def get_key(dict_ip, value):
    for k, v in dict_ip.items():
        if v == value:
            return k


dict_ip={}

with open('nginx_logs.txt','r',encoding='utf-8') as log:
    for lines in log:
        ip=lines.split()[0]
        if ip in dict_ip.keys():
            dict_ip[ip] += 1
        else:
            dict_ip[ip] = 1


print('Гадюка спамер -',get_key(dict_ip,max(dict_ip.values())),'Целых ', max(dict_ip.values()),' запросов' )
log.close()