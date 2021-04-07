# Run RabbitMQ
```shell
docker run -d --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

# Create a virtual environment
```shell
python3.8 -m venv venv
```

# Install dependencies
```shell
source venv/bin/activate
pip install -r requirements.txt
```

# Start Celery cluster
```shell
celery -A tasks worker --loglevel=INFO -n worker1@fedora
celery -A tasks worker --loglevel=INFO -n worker2@fedora
celery -A tasks worker --loglevel=INFO -n worker3@fedora
```

# Run bot
```shell
source venv/bin/activate
python bot.py
```