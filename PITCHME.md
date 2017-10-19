### Prometheus

- inspired by Google's Borgmon (cousin to Kubernetes)
- Cloud Native Computing Foundation
- numerical timeseries based monitoring system


+++
The name comes from Greek mythology, Prometheus was a Titan who took fire from the gods and gave it to humans.
![Fire](promAssets/promFire.jpeg)

+++
### Components

UNIX ethos
  - 'DOTADIW'
  - ecosystem - work well with other tools

![PromArch](promAssets/prom_architecture.svg)
---

#### Prometheus
- core service
- pull metrics from assets
  - application code
  - exporter
  - from push gateway




---

#### AlertManager
- clearing house for alerts

---

#### Exporters

+++

##### Prometheus Exporters
Databases
Hardware
Messaging systems
Storage
APIs, Logging, Miscellaneous...

---
Exporters

Databases | Hardware/OS |	Storage	| APIs |	Misc	| Software exposing Prom metrics	| Messaging |	HTTP |	Logging
------------ |------------ |------------ |------------ |------------ |------------
Aerospike  | apcupsd  | Ceph  | AWS ECS  | BIGIP  | Ceph | Kafka consumer group  | Apache  | Google's mtail log data extractor			
ClickHouse  | IoT Edison  | Gluster  | AWS Health  | BIND  | Collectd | Kafka ZooKeeper  | HAProxy  __(official)__ | Grok 			
Consul  __(official)__ | IPMI  | Hadoop HDFS FSImage  | AWS SQS  | Blackbox  __(official)__ | CRG Roller Derby Scoreboard __(client lib)__	 | NATS  | Nginx metric library				
CouchDB  | knxd  | Lustre  | Cloudflare  | BOSH  | Etcd  __(client lib)__	 | NSQ  | Nginx VTS 				
ElasticSearch  | Node/system metrics  __(official)__ | ScaleIO  | DigitalOcean  | cAdvisor | FreeBSD Kernel | RabbitMQ  | Passenger 				
Memcached  __(official)__ | Ubiquiti UniFi 	 | | Docker Cloud  | Dovecot  | Kubernetes  __(client lib)__	 | RabbitMQ Management Plugin  | Tinyproxy 				
MongoDB 		| | | Docker Hub  | Jenkins  | Linkerd | Mirth Connect  | Varnish 				
MSSQL server 		| | | GitHub  | Kemp LoadBalancer  | Netdata | MQTT blackbox  | WebDriver 				
MySQL server  __(official)__		| | | InstaClustr  | Meteor JS web framework  | Pretix						
OpenTSDB Exporter		| | | Mozilla Observatory  | Minecraft  module | Quobyte  __(client lib)__							
PgBouncer 		| | | OpenWeatherMap  | PHPFPM  | RobustIRC						
PostgreSQL 		| | | Pagespeed  | PowerDNS  | SkyDNS  __(client lib)__							
ProxySQL 		| | | Rancher  | Process  | Telegraf						
Redis 		| | | Speedtest  | rTorrent  | Weave Flux						
RethinkDB 		| |	| | Script 							
SQL query result set metrics 			| | | | Shield 							
Tarantool metric library			|| | | SMTP/Maildir MDA blackbox prober			
| | | |   Transmission 							
| | | |   Unbound 							
| | | |   Xen 					

---

##### Prometheus Exporters in use

  - Node/system metrics exporter __(official)__
  - Memcached exporter __(official)__
  - MySQL server exporter __(official)__
  - HAProxy exporter __(official)__
  - Blackbox exporter __(official)__
  - cAdvisor
  - redis
  - Forensiq Pixel (custom)

+++

### Links and contact

list of exporters
- https://prometheus.io/docs/instrumenting/exporters/

guidelines on writing exporters
- https://prometheus.io/docs/instrumenting/writing_exporters/

Michael Bubb
- slack \@mbubb
