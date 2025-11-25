"""
Message Queues and Background Tasks

This module demonstrates asynchronous processing, message queues, and background tasks
essential for scalable backend applications.
"""

from fastapi import FastAPI, BackgroundTasks, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Dict, List, Optional, Any
import asyncio
import json
import time
import uuid
from datetime import datetime, timedelta
from enum import Enum
import smtplib
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI(
    title="Message Queues & Background Tasks",
    description="Asynchronous processing and background task patterns"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Task Status Enum
class TaskStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"

# Task Priority Enum
class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

# Models
class EmailTask(BaseModel):
    to_email: EmailStr
    subject: str
    body: str
    priority: TaskPriority = TaskPriority.MEDIUM

class ReportTask(BaseModel):
    report_type: str
    user_id: int
    parameters: Dict[str, Any] = {}
    priority: TaskPriority = TaskPriority.LOW

class TaskResult(BaseModel):
    task_id: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    retry_count: int = 0
    priority: TaskPriority

class QueueStats(BaseModel):
    total_tasks: int
    pending_tasks: int
    processing_tasks: int
    completed_tasks: int
    failed_tasks: int
    queue_size: int

# In-memory task storage (use Redis/RabbitMQ/Celery in production)
class TaskQueue:
    def __init__(self):
        self.tasks: Dict[str, TaskResult] = {}
        self.pending_queue: List[str] = []
        self.processing_queue: List[str] = []
        self.max_workers = 3
        self.workers_busy = 0
        self.retry_delays = [5, 15, 60, 300]  # Exponential backoff
    
    def add_task(self, task_data: Dict[str, Any], priority: TaskPriority = TaskPriority.MEDIUM) -> str:
        """Add a new task to the queue"""
        task_id = str(uuid.uuid4())
        now = datetime.utcnow()
        
        task_result = TaskResult(
            task_id=task_id,
            status=TaskStatus.PENDING,
            created_at=now,
            updated_at=now,
            priority=priority
        )
        
        self.tasks[task_id] = task_result
        
        # Insert based on priority
        if priority == TaskPriority.CRITICAL:
            self.pending_queue.insert(0, task_id)
        elif priority == TaskPriority.HIGH:
            # Insert after other critical tasks
            insert_pos = 0
            for i, tid in enumerate(self.pending_queue):
                if self.tasks[tid].priority != TaskPriority.CRITICAL:
                    insert_pos = i
                    break
            else:
                insert_pos = len(self.pending_queue)
            self.pending_queue.insert(insert_pos, task_id)
        else:
            self.pending_queue.append(task_id)
        
        logger.info(f"Task {task_id} added to queue with priority {priority}")
        return task_id
    
    def get_next_task(self) -> Optional[str]:
        """Get the next task from queue"""
        if not self.pending_queue or self.workers_busy >= self.max_workers:
            return None
        
        task_id = self.pending_queue.pop(0)
        self.processing_queue.append(task_id)
        self.tasks[task_id].status = TaskStatus.PROCESSING
        self.tasks[task_id].updated_at = datetime.utcnow()
        self.workers_busy += 1
        
        return task_id
    
    def complete_task(self, task_id: str, result: Dict[str, Any]):
        """Mark task as completed"""
        if task_id in self.processing_queue:
            self.processing_queue.remove(task_id)
        
        self.tasks[task_id].status = TaskStatus.COMPLETED
        self.tasks[task_id].result = result
        self.tasks[task_id].updated_at = datetime.utcnow()
        self.workers_busy = max(0, self.workers_busy - 1)
        
        logger.info(f"Task {task_id} completed successfully")
    
    def fail_task(self, task_id: str, error: str):
        """Mark task as failed and potentially retry"""
        if task_id in self.processing_queue:
            self.processing_queue.remove(task_id)
        
        task = self.tasks[task_id]
        task.error = error
        task.retry_count += 1
        task.updated_at = datetime.utcnow()
        self.workers_busy = max(0, self.workers_busy - 1)
        
        # Retry logic
        if task.retry_count <= len(self.retry_delays):
            task.status = TaskStatus.RETRYING
            delay = self.retry_delays[min(task.retry_count - 1, len(self.retry_delays) - 1)]
            logger.info(f"Task {task_id} failed, retrying in {delay} seconds (attempt {task.retry_count})")
            
            # Schedule retry (in production, use Celery countdown or Redis delayed queue)
            asyncio.create_task(self._retry_task(task_id, delay))
        else:
            task.status = TaskStatus.FAILED
            logger.error(f"Task {task_id} failed permanently after {task.retry_count} attempts")
    
    async def _retry_task(self, task_id: str, delay: int):
        """Retry a failed task after delay"""
        await asyncio.sleep(delay)
        if self.tasks[task_id].status == TaskStatus.RETRYING:
            self.pending_queue.insert(0, task_id)  # High priority for retries
            self.tasks[task_id].status = TaskStatus.PENDING
            self.tasks[task_id].updated_at = datetime.utcnow()
    
    def get_stats(self) -> QueueStats:
        """Get queue statistics"""
        status_counts = {status: 0 for status in TaskStatus}
        for task in self.tasks.values():
            status_counts[task.status] += 1
        
        return QueueStats(
            total_tasks=len(self.tasks),
            pending_tasks=status_counts[TaskStatus.PENDING],
            processing_tasks=status_counts[TaskStatus.PROCESSING],
            completed_tasks=status_counts[TaskStatus.COMPLETED],
            failed_tasks=status_counts[TaskStatus.FAILED],
            queue_size=len(self.pending_queue)
        )

# Global task queue
task_queue = TaskQueue()

# Background task functions
async def send_email_task(task_id: str, email_data: EmailTask):
    """Background task to send email"""
    try:
        logger.info(f"Sending email to {email_data.to_email}")
        
        # Simulate email sending delay
        await asyncio.sleep(2)
        
        # In production, use real SMTP or email service (SendGrid, AWS SES)
        # smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        # smtp_server.starttls()
        # smtp_server.login(username, password)
        # smtp_server.send_message(msg)
        # smtp_server.quit()
        
        result = {
            "email_sent": True,
            "recipient": email_data.to_email,
            "subject": email_data.subject,
            "sent_at": datetime.utcnow().isoformat()
        }
        
        task_queue.complete_task(task_id, result)
        
    except Exception as e:
        task_queue.fail_task(task_id, str(e))

async def generate_report_task(task_id: str, report_data: ReportTask):
    """Background task to generate report"""
    try:
        logger.info(f"Generating {report_data.report_type} report for user {report_data.user_id}")
        
        # Simulate report generation
        await asyncio.sleep(5)
        
        # Mock report generation
        if report_data.report_type == "user_activity":
            report_content = {
                "user_id": report_data.user_id,
                "total_logins": 45,
                "last_login": datetime.utcnow().isoformat(),
                "active_sessions": 2
            }
        elif report_data.report_type == "sales":
            report_content = {
                "total_sales": 15678.90,
                "orders_count": 123,
                "period": "last_30_days"
            }
        else:
            report_content = {"message": "Generic report generated"}
        
        result = {
            "report_generated": True,
            "report_type": report_data.report_type,
            "user_id": report_data.user_id,
            "content": report_content,
            "generated_at": datetime.utcnow().isoformat()
        }
        
        task_queue.complete_task(task_id, result)
        
    except Exception as e:
        task_queue.fail_task(task_id, str(e))

async def process_batch_task(task_id: str, batch_data: Dict[str, Any]):
    """Background task for batch processing"""
    try:
        items = batch_data.get("items", [])
        operation = batch_data.get("operation", "process")
        
        logger.info(f"Processing batch of {len(items)} items with operation: {operation}")
        
        processed_items = []
        failed_items = []
        
        for i, item in enumerate(items):
            try:
                # Simulate processing each item
                await asyncio.sleep(0.1)
                
                if operation == "validate":
                    # Simulate validation
                    if item.get("id", 0) % 10 == 0:
                        failed_items.append({"item": item, "error": "Validation failed"})
                    else:
                        processed_items.append({"item": item, "status": "valid"})
                        
                elif operation == "transform":
                    # Simulate transformation
                    transformed = {**item, "processed_at": datetime.utcnow().isoformat()}
                    processed_items.append(transformed)
                    
                else:
                    processed_items.append({"item": item, "status": "processed"})
                    
            except Exception as item_error:
                failed_items.append({"item": item, "error": str(item_error)})
        
        result = {
            "batch_processed": True,
            "operation": operation,
            "total_items": len(items),
            "successful": len(processed_items),
            "failed": len(failed_items),
            "processed_items": processed_items,
            "failed_items": failed_items,
            "processed_at": datetime.utcnow().isoformat()
        }
        
        task_queue.complete_task(task_id, result)
        
    except Exception as e:
        task_queue.fail_task(task_id, str(e))

# Task worker
async def task_worker():
    """Background worker to process tasks"""
    while True:
        task_id = task_queue.get_next_task()
        
        if task_id:
            task_data = task_queue.tasks[task_id]
            logger.info(f"Worker processing task {task_id}")
            
            # In production, task data would include the actual task payload
            # For this demo, we'll simulate different task types
            task_type = task_id.split('-')[0] if '-' in task_id else 'unknown'
            
            try:
                if task_type == 'email':
                    # Simulate email task
                    email_data = EmailTask(
                        to_email="user@example.com",
                        subject="Test Email",
                        body="This is a test email"
                    )
                    await send_email_task(task_id, email_data)
                    
                elif task_type == 'report':
                    # Simulate report task
                    report_data = ReportTask(
                        report_type="user_activity",
                        user_id=123
                    )
                    await generate_report_task(task_id, report_data)
                    
                elif task_type == 'batch':
                    # Simulate batch task
                    batch_data = {
                        "operation": "validate",
                        "items": [{"id": i, "name": f"item_{i}"} for i in range(10)]
                    }
                    await process_batch_task(task_id, batch_data)
                    
                else:
                    # Generic task processing
                    await asyncio.sleep(1)
                    task_queue.complete_task(task_id, {"message": "Task completed"})
                    
            except Exception as e:
                task_queue.fail_task(task_id, str(e))
        else:
            # No tasks available, wait before checking again
            await asyncio.sleep(1)

# Start background worker
@app.on_event("startup")
async def start_background_worker():
    """Start the background task worker"""
    asyncio.create_task(task_worker())
    logger.info("Background task worker started")

# API Endpoints

@app.post("/tasks/email", tags=["Tasks"])
def queue_email_task(email_data: EmailTask, background_tasks: BackgroundTasks):
    """Queue an email sending task"""
    
    # Add to our custom queue
    task_id = f"email-{task_queue.add_task(email_data.dict(), email_data.priority)}"
    
    # Also demonstrate FastAPI's built-in BackgroundTasks
    def log_email_queued():
        logger.info(f"Email task {task_id} was queued via BackgroundTasks")
    
    background_tasks.add_task(log_email_queued)
    
    return {
        "task_id": task_id,
        "message": "Email task queued successfully",
        "priority": email_data.priority
    }

@app.post("/tasks/report", tags=["Tasks"])
def queue_report_task(report_data: ReportTask):
    """Queue a report generation task"""
    
    task_id = f"report-{task_queue.add_task(report_data.dict(), report_data.priority)}"
    
    return {
        "task_id": task_id,
        "message": "Report generation task queued successfully",
        "estimated_completion": (datetime.utcnow() + timedelta(minutes=5)).isoformat()
    }

@app.post("/tasks/batch", tags=["Tasks"])
def queue_batch_task(batch_data: Dict[str, Any], priority: TaskPriority = TaskPriority.MEDIUM):
    """Queue a batch processing task"""
    
    task_id = f"batch-{task_queue.add_task(batch_data, priority)}"
    
    return {
        "task_id": task_id,
        "message": "Batch processing task queued successfully",
        "items_count": len(batch_data.get("items", []))
    }

@app.get("/tasks/{task_id}", response_model=TaskResult, tags=["Tasks"])
def get_task_status(task_id: str):
    """Get task status and result"""
    
    if task_id not in task_queue.tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task_queue.tasks[task_id]

@app.get("/tasks", tags=["Tasks"])
def list_tasks(status: Optional[TaskStatus] = None, limit: int = 50):
    """List all tasks with optional status filter"""
    
    tasks = list(task_queue.tasks.values())
    
    if status:
        tasks = [task for task in tasks if task.status == status]
    
    # Sort by created_at descending
    tasks.sort(key=lambda x: x.created_at, reverse=True)
    
    return {
        "tasks": tasks[:limit],
        "total": len(tasks),
        "filtered_by": status
    }

@app.get("/queue/stats", response_model=QueueStats, tags=["Monitoring"])
def get_queue_stats():
    """Get queue statistics"""
    return task_queue.get_stats()

@app.delete("/tasks/{task_id}", tags=["Tasks"])
def cancel_task(task_id: str):
    """Cancel a pending task"""
    
    if task_id not in task_queue.tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = task_queue.tasks[task_id]
    
    if task.status == TaskStatus.PENDING:
        if task_id in task_queue.pending_queue:
            task_queue.pending_queue.remove(task_id)
        task.status = TaskStatus.FAILED
        task.error = "Task cancelled by user"
        task.updated_at = datetime.utcnow()
        
        return {"message": "Task cancelled successfully"}
    
    elif task.status == TaskStatus.PROCESSING:
        return {"message": "Cannot cancel task that is currently processing"}
    
    else:
        return {"message": f"Task is already {task.status.value}"}

# Webhook simulation for external services
@app.post("/webhooks/task-complete", tags=["Webhooks"])
def task_completion_webhook(task_id: str, result: Dict[str, Any]):
    """Simulate webhook for external task completion"""
    
    # In production, this would be called by external services
    # like payment processors, image processing services, etc.
    
    if task_id in task_queue.tasks:
        task_queue.complete_task(task_id, result)
        return {"message": "Task marked as completed via webhook"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

# Bulk operations
@app.post("/tasks/bulk", tags=["Bulk Operations"])
def queue_bulk_tasks(tasks_data: List[Dict[str, Any]]):
    """Queue multiple tasks at once"""
    
    queued_tasks = []
    
    for i, task_data in enumerate(tasks_data):
        task_type = task_data.get("type", "generic")
        priority = TaskPriority(task_data.get("priority", "medium"))
        
        task_id = f"{task_type}-{task_queue.add_task(task_data, priority)}"
        queued_tasks.append({
            "task_id": task_id,
            "type": task_type,
            "priority": priority
        })
    
    return {
        "message": f"Queued {len(queued_tasks)} tasks successfully",
        "tasks": queued_tasks
    }

@app.get("/", tags=["Documentation"])
def root():
    """API documentation"""
    return {
        "service": "Message Queues & Background Tasks Demo",
        "features": [
            "Asynchronous task processing",
            "Priority-based queuing",
            "Task retry with exponential backoff",
            "Task status tracking",
            "Batch processing",
            "Webhook integration",
            "Queue monitoring and statistics"
        ],
        "task_types": [
            "Email sending",
            "Report generation", 
            "Batch processing",
            "Generic background tasks"
        ],
        "endpoints": {
            "queue_email": "POST /tasks/email",
            "queue_report": "POST /tasks/report", 
            "queue_batch": "POST /tasks/batch",
            "task_status": "GET /tasks/{task_id}",
            "list_tasks": "GET /tasks",
            "queue_stats": "GET /queue/stats",
            "cancel_task": "DELETE /tasks/{task_id}"
        },
        "production_alternatives": [
            "Celery with Redis/RabbitMQ",
            "AWS SQS/Lambda",
            "Google Cloud Tasks",
            "Azure Service Bus",
            "Apache Kafka"
        ]
    }