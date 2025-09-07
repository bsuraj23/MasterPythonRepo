try:
    raise RuntimeError("Manually raised error")
except RuntimeError as e:
    print("Caught error:", e)
