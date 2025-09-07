import subprocess

# This works on Linux/macOS. On Windows, use ["cmd", "/c", "dir"]
result = subprocess.run(["ls"], capture_output=True, text=True)

print("Files and Folders:")
print(result.stdout)
