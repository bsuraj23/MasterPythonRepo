#code to demo logging in python
import logging      
logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
# You can change the level to logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL
# Example log messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')    
logging.error('This is an error message')
logging.critical('This is a critical message')
# End of the logging demonstration code

# You can run this file directly to see the log messages in app.log
# or you can import this logging configuration in another Python script to use the logging functionality    
# Example of using logging in another script
import logging      
logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.info('Logging from another script')
logging.error('Error logged from another script')
logging.debug('Debug message from another script')
logging.warning('Warning from another script')
logging.critical('Critical issue from another script')
# You can check the app.log file to see all the log messages
# This is a simple demonstration of how to use logging in Python
# Logging helps in tracking events that happen when some software runs  
# It is very useful for debugging and monitoring applications
# Always remember to configure logging at the start of your script
