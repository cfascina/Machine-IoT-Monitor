zookeeper-init:
	cd kafka_*/ && sudo bin/zookeeper-server-start.sh config/zookeeper.properties

kafka-init:
	cd kafka_*/ && sudo bin/kafka-server-start.sh config/server.properties

kafka-stop:
	cd kafka_*/ && sudo bin/kafka-server-stop.sh

topic-create:
	cd kafka_*/ && sudo bin/kafka-topics.sh --create --topic sensors-data --bootstrap-server localhost:9092

data-generator:
	python3 data_generator.py