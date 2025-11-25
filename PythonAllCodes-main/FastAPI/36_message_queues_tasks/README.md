# Message Queues and Background Tasks

This project demonstrates asynchronous processing, message queues, and background task patterns essential for scalable backend applications.

## Features

### Task Queue System
- **Priority-based Queue**: Tasks are processed based on priority (Critical > High > Medium > Low)
- **Task Status Tracking**: Real-time status updates (Pending, Processing, Completed, Failed, Retrying)
- **Automatic Retries**: Failed tasks are automatically retried with exponential backoff
- **Worker Management**: Configurable number of concurrent workers

### Background Task Types
- **Email Tasks**: Asynchronous email sending with SMTP integration
- **Report Generation**: Long-running report generation with progress tracking
- **Batch Processing**: Process large datasets in the background
- **Generic Tasks**: Flexible framework for any background operation

### Advanced Features
- **Task Cancellation**: Cancel pending tasks before processing
- **Bulk Operations**: Queue multiple tasks simultaneously
- **Webhook Integration**: External service integration via webhooks
- **Queue Monitoring**: Real-time statistics and health monitoring

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload

# Access the API documentation
# http://localhost:8000/docs
```

## API Examples

### Queue Email Task
```bash
curl -X POST "http://localhost:8000/tasks/email" \
  -H "Content-Type: application/json" \
  -d '{
    "to_email": "user@example.com",
    "subject": "Welcome!",
    "body": "Thank you for signing up!",
    "priority": "high"
  }'
```

### Queue Report Task
```bash
curl -X POST "http://localhost:8000/tasks/report" \
  -H "Content-Type: application/json" \
  -d '{
    "report_type": "user_activity",
    "user_id": 123,
    "parameters": {"period": "last_30_days"},
    "priority": "medium"
  }'
```

### Queue Batch Processing
```bash
curl -X POST "http://localhost:8000/tasks/batch" \
  -H "Content-Type: application/json" \
  -d '{
    "operation": "validate",
    "items": [
      {"id": 1, "name": "item_1"},
      {"id": 2, "name": "item_2"},
      {"id": 3, "name": "item_3"}
    ]
  }'
```

### Check Task Status
```bash
curl "http://localhost:8000/tasks/{task_id}"
```

### Get Queue Statistics
```bash
curl "http://localhost:8000/queue/stats"
```

## Key Concepts

### 1. Task Priorities
Tasks are processed based on priority levels:
- **Critical**: Immediate processing (payment confirmations, security alerts)
- **High**: Important but not critical (user notifications, order updates)  
- **Medium**: Regular tasks (email newsletters, routine reports)
- **Low**: Background maintenance (data cleanup, analytics)

### 2. Retry Strategy
Failed tasks are automatically retried with exponential backoff:
- 1st retry: 5 seconds
- 2nd retry: 15 seconds  
- 3rd retry: 60 seconds
- 4th retry: 300 seconds
- After 4 failures: Mark as permanently failed

### 3. Task Lifecycle
```
Queued → Pending → Processing → Completed
                     ↓
                  Failed → Retrying → Pending
                     ↓
              Permanently Failed
```

### 4. Worker Pattern
- Configurable number of concurrent workers
- Tasks are distributed among available workers
- Workers automatically pick up tasks from the queue
- Graceful handling of worker failures

## Production Considerations

### Message Queue Solutions
For production environments, replace the in-memory queue with:

#### Redis + Celery
```python
# celery_app.py
from celery import Celery

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def send_email_task(email_data):
    # Email sending logic
    pass
```

#### AWS SQS
```python
import boto3

sqs = boto3.client('sqs')

def queue_task(queue_url, message_body):
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message_body)
    )
    return response['MessageId']
```

#### RabbitMQ
```python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

def publish_task(queue_name, task_data):
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(task_data),
        properties=pika.BasicProperties(delivery_mode=2)
    )
```

### Monitoring and Observability
- **Metrics**: Task throughput, failure rates, queue depth
- **Logging**: Structured logs for task lifecycle events
- **Alerting**: Notifications for high failure rates or queue backlogs
- **Dashboard**: Real-time visualization of queue health

### Scaling Strategies
- **Horizontal Scaling**: Multiple worker instances
- **Vertical Scaling**: Increase worker count per instance
- **Load Balancing**: Distribute tasks across worker pools
- **Auto-scaling**: Dynamic worker scaling based on queue depth

## Learning Objectives

By studying this code, you'll learn:

1. **Asynchronous Processing**: How to handle long-running tasks without blocking requests
2. **Queue Management**: Priority-based task queuing and worker patterns
3. **Error Handling**: Retry strategies and failure management
4. **Task Monitoring**: Status tracking and queue statistics
5. **Production Patterns**: Scalable background task architectures

## Advanced Patterns

### Task Dependencies
```python
# Tasks that depend on other tasks
def process_order_workflow(order_id):
    # Step 1: Validate payment
    payment_task = queue_task("validate_payment", {"order_id": order_id})
    
    # Step 2: Update inventory (depends on payment)
    inventory_task = queue_task("update_inventory", {
        "order_id": order_id,
        "depends_on": payment_task.id
    })
    
    # Step 3: Send confirmation (depends on inventory)
    email_task = queue_task("send_confirmation", {
        "order_id": order_id,
        "depends_on": inventory_task.id
    })
```

### Dead Letter Queues
```python
# Handle permanently failed tasks
def handle_dead_letter(task_data):
    # Log the failure
    logger.error(f"Task permanently failed: {task_data}")
    
    # Notify administrators
    send_admin_alert(f"Task {task_data['id']} requires manual intervention")
    
    # Store for manual review
    store_failed_task(task_data)
```

### Task Scheduling
```python
from datetime import datetime, timedelta

def schedule_recurring_task():
    """Schedule tasks for future execution"""
    future_time = datetime.utcnow() + timedelta(hours=24)
    
    queue_task("daily_report", {
        "execute_at": future_time.isoformat(),
        "recurring": "daily"
    })
```

This example provides a solid foundation for understanding message queues and background task processing, essential skills for building scalable backend applications.