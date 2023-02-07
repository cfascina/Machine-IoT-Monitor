# Machine Sensors Monitoring

[ ] Project Description.

## Set Up

1. Download [Kafka](https://kafka.apache.org/downloads) into the project directory.

2. Extract the **.tgz** and remove it:

    ```bash
    sudo tar -xzf kafka_*.tgz && rm kafka_*.tgz
    ```

3. Create the virtual environment and activate it:

    ```bash
    python3 -m venv .env && source .env/bin/activate
    ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Run

1. In **Terminal 1**, initialize Zookeeper (Kafka's Cluster Manager):

    ```bash
    make zookeeper-init
    ```

2. In **Terminal 2**, initialize Kafka:

    ```bash
    make kafka-init
    ```

    **Do not close Terminals 1 and 2. Open a new one to run the commands below.**

3. Create the topic:

    ```bash
    make topic-create
    ```
