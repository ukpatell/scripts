import boto3
import json
import random
import time
import uuid

kinesis_client = boto3.client('kinesis', region_name='YOUR_REGION')

states = ['NY', 'CA', 'TX', 'FL', 'IL', 'WA', 'GA', 'OH', 'PA', 'AZ', 'MI', 'NC', 'VA', 'MA', 'CO', 'TN', 'IN', 'MO', 'WI', 'MN', 'OR', 'AL', 'SC', 'OK', 'KY']
pages = ['home', 'product', 'checkout', 'contact']

def generate_click():
    state = random.choice(states)
    page = random.choice(pages)
    customer_id = str(uuid.uuid4())  # Generates a random UUID
    time_spent = random.randint(1, 60)  # Generate random time spent (in seconds)
    timestamp = int(time.time())
    
    data = {
        'state': state,
        'page': page,
        'time_spent': time_spent,
        'timestamp': timestamp,
        'customer_id':customer_id,
    }
    
    return json.dumps(data)

# Simulate clickstream events
for _ in range(100):
    click_event = generate_click()
    print(click_event)
    response = kinesis_client.put_record(
        StreamName='STREAM_NAME',
        Data=click_event.encode('utf-8'),
        PartitionKey='1',
    )
    time.sleep(1)
