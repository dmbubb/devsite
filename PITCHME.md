### Prometheus

Monitoring framework

- developed by 2 ex-Google engineers at SoundCloud
- modeled on BorgMon.

(This makes Prometheus somewhat of a cousin to Kubernetes - a descendant of Borg.)

+++
The name comes from Greek mythology, Prometheus was a Titan who gave fire to humans.
![Fire](promAssets/promFire.jpeg)

+++
And this is the thanks he got...
![Chains](promAssets/prometheusInChains.jpg)

+++
### Components

---

#### Prometheus

---

#### AlertManager

---

#### Exporters

+++

##### Prometheus Exporters
Databases
  - Aerospike exporter
  - ClickHouse exporter
  - Consul exporter __(official)__
  - CouchDB exporter
  - ElasticSearch exporter
  - Memcached exporter __(official)__
  - MongoDB exporter
  - MSSQL server exporter
  - MySQL server exporter __(official)__
  - OpenTSDB Exporter
  - PgBouncer exporter
  - PostgreSQL exporter
  - ProxySQL exporter
  - Redis exporter
  - RethinkDB exporter
  - SQL query result set metrics exporter
  - Tarantool metric library


Hardware related
  - apcupsd exporter
  - IoT Edison exporter
  - IPMI exporter
  - knxd exporter
  - Node/system metrics exporter __(official)__
  - Ubiquiti UniFi exporter


Messaging systems
  - Kafka consumer group exporter
  - Kafka ZooKeeper exporter
  - NATS exporter
  - NSQ exporter
  - RabbitMQ exporter
  - RabbitMQ Management Plugin exporter
  - Mirth Connect exporter
  - MQTT blackbox exporter

Storage
  - Ceph exporter
  - Gluster exporter
  - Hadoop HDFS FSImage exporter
  - Lustre exporter
  - ScaleIO exporter

HTTP
  - Apache exporter
  - HAProxy exporter __(official)__
  - Nginx metric library
  - Nginx VTS exporter
  - Passenger exporter
  - Tinyproxy exporter
  - Varnish exporter
  - WebDriver exporter

APIs
  - AWS ECS exporter
  - AWS Health exporter
  - AWS SQS exporter
  - Cloudflare exporter
  - DigitalOcean exporter
  - Docker Cloud exporter
  - Docker Hub exporter
  - GitHub exporter
  - InstaClustr exporter
  - Mozilla Observatory exporter
  - OpenWeatherMap exporter
  - Pagespeed exporter
  - Rancher exporter
  - Speedtest exporter


Logging
  - Google's mtail log data extractor
  - Grok exporter


Other monitoring systems
  - Akamai Cloudmonitor exporter
  - AWS CloudWatch exporter __(official)__
  - Cloud Foundry Firehose exporter
  - Collectd exporter __(official)__
  - Google Stackdriver exporter
  - Graphite exporter __(official)__
  - Heka dashboard exporter
  - Heka exporter
  - InfluxDB exporter __(official)__
  - JavaMelody exporter
  - JMX exporter __(official)__
  - Munin exporter
  - Nagios / Naemon exporter
  - New Relic exporter
  - NRPE exporter
  - Pingdom exporter
  - scollector exporter
  - Sensu exporter
  - SNMP exporter __(official)__
  - StatsD exporter __(official)__


Miscellaneous
  - BIG-IP exporter
  - BIND exporter
  - Blackbox exporter __(official)__
  - BOSH exporter
  - cAdvisor
  - Dovecot exporter
  - Jenkins exporter
  - Kemp LoadBalancer exporter
  - Meteor JS web framework exporter
  - Minecraft exporter module
  - PHP-FPM exporter
  - PowerDNS exporter
  - Process exporter
  - rTorrent exporter
  - Script exporter
  - Shield exporter
  - SMTP/Maildir MDA blackbox prober
  - Transmission exporter
  - Unbound exporter
  - Xen exporter

##### Other Software exposing Prometheus metrics
  - Ceph
  - Collectd
  - CRG Roller Derby Scoreboard *
  - Etcd  *
  - FreeBSD Kernel
  - Kubernetes  *
  - Linkerd
  - Netdata
  - Pretix
  - Quobyte  *
  - RobustIRC
  - SkyDNS  *
  - Telegraf
  - Weave Flux

  \* _through Prometheus client library_

+++

### Links and contact

list of exporters
- https://prometheus.io/docs/instrumenting/exporters/

guidelines on writing exporters
- https://prometheus.io/docs/instrumenting/writing_exporters/

Michael Bubb
- slack \@mbubb
