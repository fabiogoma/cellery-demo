Run RabbitMQ
docker run -d --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

Start Celery cluster
celery -A tasks worker --loglevel=INFO -n worker1@fedora
celery -A tasks worker --loglevel=INFO -n worker2@fedora
celery -A tasks worker --loglevel=INFO -n worker3@fedora

Install dependencies
pip install -r requirements.txt

Run bot
source venv/bin/activate
python bot.py