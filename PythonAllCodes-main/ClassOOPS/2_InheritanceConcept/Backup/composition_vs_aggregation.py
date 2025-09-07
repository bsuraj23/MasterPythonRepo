# Composition vs Aggregation
# Composition: Strong ownership
class Heart: pass
class Human:
    def __init__(self):
        self.heart = Heart()

# Aggregation: Weak ownership
class Department: pass
class Employee:
    def __init__(self, dept):
        self.dept = dept
