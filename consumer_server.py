#Consumer server
import asyncio

from confluent_kafka import Consumer
#from confluent_kafka.admin import AdminClient, NewTopic

topic = 'com.udacity.sf.crime'

async def consume(topic_name):
    consumer = Consumer({
        'bootstrap.servers': 'PLAINTEXT://localhost:9092',
        'group.id': '0',
    })
    
    consumer.subscribe([topic_name])
    
    while True:
        messages = consumer.consume(5, timeout=1.0)
        print('Waiting')
        for message in messages:
            if message is None:
                print('No message recevied')
            elif message.error() is not None:
                print(f'Found error: {message.error()}')
            else:
                print(f'{message.value()}\n')
                
        await asyncio.sleep(1.0)
                
def run():
    try:
        asyncio.run(consume(topic))
        
    except KeyboardInterrupt as e:
        print("Exiting")
        
if __name__ == '__main__':
    run()
