import subprocess

# Run a simple shell command
result = subprocess.run(["echo", "Hello from subprocess!"], capture_output=True, text=True)

print("Output:", result.stdout)
print("Exit code:", result.returncode)
result.kill()
