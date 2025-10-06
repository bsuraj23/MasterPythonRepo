import multiprocessing
import time
import os

def square_numbers():
    """Function to calculate squares with process information"""
    process_name = multiprocessing.current_process().name
    process_id = os.getpid()
    
    print(f"[{process_name}] Starting with PID: {process_id}")
    
    for i in range(5):  # Increased range for better demonstration
        result = i * i
        print(f"[{process_name}] Square of {i} is {result}")
        time.sleep(0.5)  # Reduced sleep time for faster execution
    
    print(f"[{process_name}] Completed all calculations")

def demonstrate_multiprocessing():
    """Main function to demonstrate multiprocessing"""
    print(f"Main process PID: {os.getpid()}")
    print("=" * 50)
    
    # Create processes with custom names
    p1 = multiprocessing.Process(target=square_numbers, name="SquareCalculator-1")
    p2 = multiprocessing.Process(target=square_numbers, name="SquareCalculator-2")
    
    # Display process information before starting
    print("Process Information:")
    print(f"Process 1: {p1.name}, PID: {p1.pid}, Alive: {p1.is_alive()}")
    print(f"Process 2: {p2.name}, PID: {p2.pid}, Alive: {p2.is_alive()}")
    print("=" * 50)
    
    # Record start time
    start_time = time.time()
    
    # Start processes
    print("Starting processes...")
    p1.start()
    p2.start()
    
    # Display process information after starting
    print(f"Process 1: {p1.name}, PID: {p1.pid}, Alive: {p1.is_alive()}")
    print(f"Process 2: {p2.name}, PID: {p2.pid}, Alive: {p2.is_alive()}")
    print("=" * 50)
    
    # Wait for processes to complete
    print("Waiting for processes to complete...")
    p1.join()
    print(f"Process 1 ({p1.name}) finished with exit code: {p1.exitcode}")
    
    p2.join()
    print(f"Process 2 ({p2.name}) finished with exit code: {p2.exitcode}")
    
    # Calculate total execution time
    end_time = time.time()
    execution_time = end_time - start_time
    
    print("=" * 50)
    print(f"Main process: All subprocesses completed in {execution_time:.2f} seconds")
    print(f"Process 1 final state - Alive: {p1.is_alive()}, Exit code: {p1.exitcode}")
    print(f"Process 2 final state - Alive: {p2.is_alive()}, Exit code: {p2.exitcode}")

if __name__ == "__main__":
    # This guard is essential for multiprocessing on Windows
    demonstrate_multiprocessing()