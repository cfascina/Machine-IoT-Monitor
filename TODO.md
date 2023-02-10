# TODO

[] Executar o producer por um tempo determinado.

[] Converter arquivos para .py.

[] No Makefile, fixar versão do Kafka para executar os comandos.

[x] Remover pacotes desnecessários de requirements.txt

[] Talvez seja necessário fazer as seguintes configurações:

Edit ´.env/pyvenv.cfg´ with the following:

```bash
include-system-site-packages = true
```

Edit ´kafka_2.13-3.3.2/config/server.properties´ with the following:

```bash
listeners=PLAINTEXT://localhost:9092
```
