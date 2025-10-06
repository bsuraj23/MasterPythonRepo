import multiprocessing
import time
import os

def task(name, delay):
    print(f"Process {name} starting with PID: {os.getpid()}")
    time.sleep(delay)
    print(f"Process {name} finished!")
    return f"Result from {name}"

def demonstrate_process_methods():
    # Create a process
    process = multiprocessing.Process(target=task, args=("Worker-1", 2))
    
    # Pre-start methods and properties
    print("=== PRE-START METHODS ===")
    print(f"Process created: {process}")
    print(f"Process name: {process.name}")
    print(f"Process PID (before start): {process.pid}")  # Will be None
    print(f"Process is alive: {process.is_alive()}")     # Will be False
    print(f"Process daemon status: {process.daemon}")
    print(f"Process exitcode (before start): {process.exitcode}")  # Will be None
    
    # Start the process
    print("\n=== STARTING PROCESS ===")
    process.start()
    print(f"Process started: {process}")
    
    # Post-start methods and properties
    print("\n=== POST-START METHODS ===")
    print(f"Process PID (after start): {process.pid}")
    print(f"Process is alive: {process.is_alive()}")     # Will be True
    print(f"Process exitcode (while running): {process.exitcode}")  # Will be None
    
    # Wait for process to complete
    print("\n=== JOINING PROCESS ===")
    process.join()
    
    # Post-completion methods
    print("\n=== POST-COMPLETION METHODS ===")
    print(f"Process finished: {process}")
    print(f"Process is alive: {process.is_alive()}")     # Will be False
    print(f"Process exitcode (after completion): {process.exitcode}")  # Will be 0 for success
    print(f"Process PID (after completion): {process.pid}")

def demonstrate_process_with_timeout():
    print("\n" + "="*50)
    print("DEMONSTRATING PROCESS WITH TIMEOUT")
    print("="*50)
    
    process = multiprocessing.Process(target=task, args=("Worker-2", 3))
    process.start()
    
    # Join with timeout
    process.join(timeout=1)  # Wait only 1 second
    
    if process.is_alive():
        print("Process is still running after timeout")
        print("Terminating process...")
        process.terminate()
        process.join()  # Wait for termination to complete
        print(f"Process terminated with exitcode: {process.exitcode}")

if __name__ == "__main__":
    print(f"Main process PID: {os.getpid()}")
    demonstrate_process_methods()
    demonstrate_process_with_timeout()
