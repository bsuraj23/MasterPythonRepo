import subprocess

# This works on Linux/macOS. On Windows, use ["cmd", "/c", "dir"]
result = subprocess.run(["ls"], capture_output=True, text=True)

print("Files and Folders:")
print(result.stdout)
if __name__ == "__main__":
    # This guard is essential for multithreading  on Windows
    result = subprocess.run(["ls"], capture_output=True, text=True)

    #TODO: Add your code here