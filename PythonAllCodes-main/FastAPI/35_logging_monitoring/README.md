# Production Logging and Monitoring

This project demonstrates professional logging, monitoring, and observability patterns essential for backend engineers in production environments.

## Features

### Structured Logging
- **JSON Format**: All logs are structured in JSON format for easy parsing
- **Request Correlation**: Every request gets a unique ID for tracing
- **Context Enrichment**: Logs include user context, timing, and metadata
- **Multiple Log Levels**: Support for DEBUG, INFO, WARNING, ERROR levels

### Request Tracking
- **Automatic Middleware**: Logs all incoming requests and responses
- **Performance Timing**: Tracks request duration in milliseconds
- **Error Tracking**: Captures and logs exceptions with stack traces
- **Headers**: Adds request ID and response time to response headers

### Metrics Collection
- **Request Metrics**: Total requests, errors, response times
- **Endpoint Analytics**: Per-endpoint statistics and error rates
- **Health Monitoring**: System uptime and health status
- **Real-time Updates**: Metrics updated in real-time

### Monitoring Endpoints
- **Health Check**: `/health` - System health and basic metrics
- **Detailed Metrics**: `/metrics` - Comprehensive application metrics
- **Log Management**: `/admin/log-level` - Dynamic log level changes

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload

# Access the API documentation
# http://localhost:8000/docs
```

## Log Output Examples

### Request Logging
```json
{
  "timestamp": "2024-01-15T10:30:45.123456",
  "level": "INFO",
  "logger": "backend_api",
  "message": "Request started: GET /users/123",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "method": "GET",
  "url": "http://localhost:8000/users/123",
  "client_ip": "127.0.0.1",
  "user_agent": "curl/7.68.0",
  "endpoint": "GET /users/123"
}
```

### Error Logging
```json
{
  "timestamp": "2024-01-15T10:30:45.987654",
  "level": "ERROR",
  "logger": "backend_api",
  "message": "Request failed: GET /users/123",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "status_code": 404,
  "duration_ms": 45.67,
  "exception": {
    "type": "HTTPException",
    "message": "User not found",
    "traceback": ["..."]
  }
}
```

## Key Endpoints

### Health and Monitoring
- `GET /health` - Health check with metrics
- `GET /metrics` - Detailed application metrics
- `POST /admin/log-level` - Change log level dynamically

### Business Endpoints (with logging)
- `GET /users/{user_id}` - Get user with comprehensive logging
- `POST /users` - Create user with audit logging
- `GET /logging-examples` - Demonstrate logging patterns

### Testing Endpoints
- `GET /simulate-error?error_type=validation` - Test error logging

## Best Practices Demonstrated

### 1. Structured Logging
- Use JSON format for machine-readable logs
- Include correlation IDs for request tracing
- Add context information (user ID, operation, etc.)

### 2. Request Lifecycle Tracking
- Log request start and completion
- Track performance metrics
- Capture errors with full context

### 3. Operation-Level Logging
- Use context managers for operation tracking
- Log business logic steps
- Include timing and context data

### 4. Error Handling
- Structured error logging with stack traces
- Error categorization and metrics
- Graceful error responses

### 5. Monitoring Integration
- Health check endpoints
- Metrics collection and exposure
- Real-time monitoring capabilities

## Production Considerations

### Log Management
- Use centralized logging (ELK Stack, Fluentd)
- Implement log rotation and retention policies
- Monitor log volume and performance impact

### Metrics and Alerting
- Integrate with Prometheus/Grafana
- Set up alerting for error rates and performance
- Monitor business metrics and SLAs

### Performance
- Asynchronous logging for high-throughput
- Sample logs in high-volume scenarios
- Balance detail vs. performance

### Security
- Sanitize sensitive data in logs
- Use secure log transmission
- Implement access controls for logs

## Learning Objectives

By studying this code, you'll learn:

1. **Structured Logging**: How to implement JSON-formatted logging
2. **Request Tracing**: Correlation IDs and request lifecycle tracking
3. **Metrics Collection**: Application performance and business metrics
4. **Error Handling**: Comprehensive error logging and tracking
5. **Monitoring**: Health checks and metrics endpoints
6. **Production Patterns**: Real-world logging and monitoring practices

This is essential knowledge for backend engineers working in production environments where observability and monitoring are critical for system reliability and debugging.