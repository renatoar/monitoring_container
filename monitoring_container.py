import time
import requests
from pymongo import MongoClient
from datetime import datetime
client = MongoClient('192.168.50.20:17017')['container_monitoring']['metricas']

mins = 0
#URL base
base = "http://192.168.50.10:9090/api/v1/query?query="
#query CPU Usage
URL_cpu = 'rate(container_cpu_user_seconds_total{image!=\"\"}[5m])*100'
URL_mem = 'rate(container_memory_usage_bytes{image!=\"\"}[5m])'
URL_tx = 'rate(container_network_transmit_bytes_total{image!=\"\"}[5m])'
URL_rx = 'rate(container_network_receive_bytes_total{image!=\"\"}[5m])'
while mins != 10:
    r = requests.get(url = base + URL_cpu)
    j = requests.get(url = base + URL_mem)
    p = requests.get(url = base + URL_tx)
    q = requests.get(url = base + URL_rx)
    dados_cpu = r.json()
    dados_mem = j.json()
    dados_nettx = p.json()
    dados_netrx = q.json()
    qtd_containers = len(dados_cpu["data"]["result"])
    array_containers = []
    for x in range(0, qtd_containers) :
        timestamp = datetime.fromtimestamp(dados_cpu["data"]["result"][x]["value"][0])
        timestampStr = timestamp.strftime("%d-%b-%Y - %H:%M:%S")
        name_container = dados_cpu["data"]["result"][x]["metric"]["name"]
        id_container = dados_cpu["data"]["result"][x]["metric"]["id"]
        cpu_usage = format(float(dados_cpu["data"]["result"][x]["value"][1]), '.2f') + " %"
        mem_usage = format(float(dados_mem["data"]["result"][x]["value"][1]), '.2f') + " MB"
        byte_tx = dados_nettx["data"]["result"][x]["value"][1] + " Bs"
        byte_rx = dados_netrx["data"]["result"][x]["value"][1] + " Bs"
        
        resposta = client[timestampStr].insert_one({'timestap': timestampStr, 'name_container': name_container, 'id_container': id_container, 'cpu_usage': cpu_usage, 'mem_usage' : mem_usage, 'byte_tx': byte_tx, 'byte_rx': byte_rx})
        print(resposta)

    time.sleep(15)
    mins += 1