# Container para monitoramento de containers

Este container coleta as informações abaixo de todos os containers em um cluster Docker Swarm em que ele está rodando e os armazena em um banco de dados.

- Data e hora atual
- Ip dos hosts
- ID dos containers
- Nome dos containers
- Uso de CPU por cada container
- Uso de memória por cada container
- Quantidade de Bytes transferidos pela rede
- Quantidade de Bytes recebidos pela rede

***Aplicação parte integrante do projeto https://github.com/renatoar/prometheus_monitor_project.git
