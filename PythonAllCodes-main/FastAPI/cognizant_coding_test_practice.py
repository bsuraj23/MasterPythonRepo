"""
Cognizant Python Coding Test Practice
=====================================

This file contains practice problems similar to what you might face
in Cognizant's technical interview coding round.
"""

import time
import os

class CognizantCodingTest:
    def __init__(self):
        self.problems_solved = 0
        self.total_problems = 10
        
    def display_header(self):
        print("=" * 60)
        print("🏢 COGNIZANT PYTHON CODING TEST PRACTICE")
        print("=" * 60)
        print("Instructions:")
        print("- Solve each problem step by step")
        print("- Write clean, readable code")
        print("- Test your solutions with different inputs")
        print("- Explain your approach")
        print("=" * 60)
    
    def problem_1(self):
        """Basic String Manipulation"""
        print("\n📝 Problem 1: String Manipulation")
        print("-" * 40)
        print("Write a function that takes a string and returns:")
        print("1. Number of vowels")
        print("2. Number of consonants") 
        print("3. String reversed")
        print("4. String with first letter of each word capitalized")
        
        def analyze_string(text):
            vowels = "aeiouAEIOU"
            vowel_count = sum(1 for char in text if char in vowels)
            consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
            reversed_text = text[::-1]
            capitalized = text.title()
            
            return {
                'vowels': vowel_count,
                'consonants': consonant_count,
                'reversed': reversed_text,
                'capitalized': capitalized
            }
        
        # Test the function
        test_string = "Welcome to Cognizant"
        result = analyze_string(test_string)
        print(f"\nInput: '{test_string}'")
        print(f"Results: {result}")
        
        print("\n✅ Expected approach:")
        print("- Iterate through string once")
        print("- Count vowels and consonants")
        print("- Use slicing for reversal")
        print("- Use built-in title() method")
        
    def problem_2(self):
        """List Operations"""
        print("\n📝 Problem 2: List Operations")
        print("-" * 40)
        print("Given a list of numbers, write functions to:")
        print("1. Find the second largest number")
        print("2. Remove duplicates while maintaining order")
        print("3. Find pairs that sum to a target value")
        
        def find_second_largest(numbers):
            if len(numbers) < 2:
                return None
            unique_nums = sorted(list(set(numbers)), reverse=True)
            return unique_nums[1] if len(unique_nums) >= 2 else None
        
        def remove_duplicates_ordered(numbers):
            result = []
            for num in numbers:
                if num not in result:
                    result.append(num)
            return result
        
        def find_pairs_with_sum(numbers, target):
            pairs = []
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                        pairs.append((numbers[i], numbers[j]))
            return pairs
        
        # Test the functions
        test_list = [5, 2, 8, 2, 9, 1, 5, 4]
        target = 10
        
        print(f"\nInput list: {test_list}")
        print(f"Second largest: {find_second_largest(test_list)}")
        print(f"Remove duplicates: {remove_duplicates_ordered(test_list)}")
        print(f"Pairs that sum to {target}: {find_pairs_with_sum(test_list, target)}")
        
    def problem_3(self):
        """Mathematical Calculations"""
        print("\n📝 Problem 3: Mathematical Functions")
        print("-" * 40)
        print("Write functions for:")
        print("1. Check if a number is prime")
        print("2. Generate Fibonacci series")
        print("3. Calculate factorial")
        print("4. Find GCD of two numbers")
        
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        def fibonacci(n):
            if n <= 0:
                return []
            elif n == 1:
                return [0]
            elif n == 2:
                return [0, 1]
            
            fib_series = [0, 1]
            for i in range(2, n):
                fib_series.append(fib_series[-1] + fib_series[-2])
            return fib_series
        
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Test the functions
        test_num = 17
        print(f"\n{test_num} is prime: {is_prime(test_num)}")
        print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
        print(f"Factorial of 5: {factorial(5)}")
        print(f"GCD of 48 and 18: {gcd(48, 18)}")
        
    def problem_4(self):
        """Dictionary and Data Processing"""
        print("\n📝 Problem 4: Data Processing")
        print("-" * 40)
        print("Given employee data, write functions to:")
        print("1. Find employees by department")
        print("2. Calculate average salary by department")
        print("3. Find highest paid employee")
        
        employees = [
            {'name': 'Alice', 'dept': 'IT', 'salary': 75000},
            {'name': 'Bob', 'dept': 'Finance', 'salary': 65000},
            {'name': 'Charlie', 'dept': 'IT', 'salary': 80000},
            {'name': 'Diana', 'dept': 'HR', 'salary': 60000},
            {'name': 'Eve', 'dept': 'IT', 'salary': 70000},
            {'name': 'Frank', 'dept': 'Finance', 'salary': 72000}
        ]
        
        def find_by_department(employees, dept):
            return [emp for emp in employees if emp['dept'] == dept]
        
        def avg_salary_by_dept(employees):
            dept_salaries = {}
            for emp in employees:
                dept = emp['dept']
                if dept not in dept_salaries:
                    dept_salaries[dept] = []
                dept_salaries[dept].append(emp['salary'])
            
            return {dept: sum(salaries) / len(salaries) 
                   for dept, salaries in dept_salaries.items()}
        
        def highest_paid(employees):
            return max(employees, key=lambda emp: emp['salary'])
        
        # Test the functions
        print(f"\nIT employees: {find_by_department(employees, 'IT')}")
        print(f"Average salary by department: {avg_salary_by_dept(employees)}")
        print(f"Highest paid employee: {highest_paid(employees)}")
        
    def problem_5(self):
        """Class Design"""
        print("\n📝 Problem 5: Object-Oriented Programming")
        print("-" * 40)
        print("Design a Bank Account class with:")
        print("1. Account number, holder name, balance")
        print("2. Deposit and withdraw methods")
        print("3. Transaction history")
        print("4. Account validation")
        
        class BankAccount:
            def __init__(self, account_number, holder_name, initial_balance=0):
                self.account_number = account_number
                self.holder_name = holder_name
                self.balance = initial_balance
                self.transaction_history = []
                
            def deposit(self, amount):
                if amount > 0:
                    self.balance += amount
                    self.transaction_history.append(f"Deposited: ${amount}")
                    return True
                return False
            
            def withdraw(self, amount):
                if 0 < amount <= self.balance:
                    self.balance -= amount
                    self.transaction_history.append(f"Withdrawn: ${amount}")
                    return True
                return False
            
            def get_balance(self):
                return self.balance
            
            def get_statement(self):
                return self.transaction_history
            
            def __str__(self):
                return f"Account {self.account_number}: {self.holder_name}, Balance: ${self.balance}"
        
        # Test the class
        account = BankAccount("12345", "John Doe", 1000)
        print(f"\nInitial: {account}")
        
        account.deposit(500)
        print(f"After deposit: {account}")
        
        account.withdraw(200)
        print(f"After withdrawal: {account}")
        
        print(f"Transaction history: {account.get_statement()}")
        
    def problem_6(self):
        """Pattern Printing"""
        print("\n📝 Problem 6: Pattern Printing")
        print("-" * 40)
        print("Write functions to print different patterns:")
        
        def print_triangle(n):
            print("1. Right Triangle:")
            for i in range(1, n + 1):
                print('* ' * i)
        
        def print_pyramid(n):
            print("\n2. Pyramid:")
            for i in range(1, n + 1):
                spaces = ' ' * (n - i)
                stars = '* ' * i
                print(spaces + stars)
        
        def print_number_pattern(n):
            print("\n3. Number Pattern:")
            for i in range(1, n + 1):
                for j in range(1, i + 1):
                    print(j, end=' ')
                print()
        
        # Test pattern functions
        n = 5
        print_triangle(n)
        print_pyramid(n)
        print_number_pattern(n)
        
    def problem_7(self):
        """File Processing"""
        print("\n📝 Problem 7: File Operations")
        print("-" * 40)
        print("Write functions to:")
        print("1. Count words in a file")
        print("2. Find most frequent word")
        print("3. Count lines and characters")
        
        # Create sample file
        sample_text = """
        Welcome to Cognizant Technology Solutions.
        We are a leading provider of information technology,
        consulting and business process services.
        Cognizant is committed to helping clients transform
        their business models and stay ahead of the competition.
        """
        
        filename = "sample_text.txt"
        with open(filename, 'w') as f:
            f.write(sample_text)
        
        def analyze_file(filename):
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                    lines = content.strip().split('\n')
                    words = content.lower().split()
                    
                    # Count statistics
                    line_count = len([line for line in lines if line.strip()])
                    word_count = len(words)
                    char_count = len(content)
                    
                    # Find most frequent word
                    word_freq = {}
                    for word in words:
                        clean_word = ''.join(c for c in word if c.isalnum())
                        if clean_word:
                            word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
                    
                    most_frequent = max(word_freq, key=word_freq.get) if word_freq else None
                    
                    return {
                        'lines': line_count,
                        'words': word_count,
                        'characters': char_count,
                        'most_frequent_word': most_frequent,
                        'frequency': word_freq.get(most_frequent, 0) if most_frequent else 0
                    }
            except FileNotFoundError:
                return "File not found"
        
        result = analyze_file(filename)
        print(f"\nFile analysis results: {result}")
        
        # Clean up
        if os.path.exists(filename):
            os.remove(filename)
        
    def problem_8(self):
        """Error Handling"""
        print("\n📝 Problem 8: Exception Handling")
        print("-" * 40)
        print("Write a calculator with proper error handling:")
        
        class Calculator:
            @staticmethod
            def divide(a, b):
                try:
                    result = a / b
                    return f"Result: {result}"
                except ZeroDivisionError:
                    return "Error: Cannot divide by zero"
                except TypeError:
                    return "Error: Invalid input types"
            
            @staticmethod
            def square_root(n):
                try:
                    if n < 0:
                        raise ValueError("Cannot calculate square root of negative number")
                    return f"Square root of {n}: {n ** 0.5}"
                except ValueError as e:
                    return f"Error: {e}"
            
            @staticmethod
            def factorial(n):
                try:
                    if not isinstance(n, int) or n < 0:
                        raise ValueError("Factorial requires non-negative integer")
                    result = 1
                    for i in range(1, n + 1):
                        result *= i
                    return f"Factorial of {n}: {result}"
                except ValueError as e:
                    return f"Error: {e}"
        
        calc = Calculator()
        print(f"\n10 ÷ 2 = {calc.divide(10, 2)}")
        print(f"10 ÷ 0 = {calc.divide(10, 0)}")
        print(f"Square root of 16 = {calc.square_root(16)}")
        print(f"Square root of -4 = {calc.square_root(-4)}")
        print(f"Factorial of 5 = {calc.factorial(5)}")
        print(f"Factorial of -3 = {calc.factorial(-3)}")
        
    def problem_9(self):
        """Data Validation"""
        print("\n📝 Problem 9: Data Validation")
        print("-" * 40)
        print("Write functions to validate:")
        print("1. Email address")
        print("2. Phone number")
        print("3. Password strength")
        
        import re
        
        def validate_email(email):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            return bool(re.match(pattern, email))
        
        def validate_phone(phone):
            # Remove all non-digits
            digits_only = re.sub(r'\D', '', phone)
            return len(digits_only) == 10
        
        def validate_password(password):
            if len(password) < 8:
                return False, "Password must be at least 8 characters"
            if not re.search(r'[A-Z]', password):
                return False, "Password must contain uppercase letter"
            if not re.search(r'[a-z]', password):
                return False, "Password must contain lowercase letter"
            if not re.search(r'\d', password):
                return False, "Password must contain a number"
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                return False, "Password must contain special character"
            return True, "Password is strong"
        
        # Test validation functions
        test_cases = [
            ("john@cognizant.com", "9876543210", "Pass@123"),
            ("invalid-email", "123", "weak"),
            ("test@domain.com", "+91 98765-43210", "Strong@Pass123")
        ]
        
        for email, phone, password in test_cases:
            print(f"\nTesting: {email}, {phone}, {password}")
            print(f"Email valid: {validate_email(email)}")
            print(f"Phone valid: {validate_phone(phone)}")
            is_valid, msg = validate_password(password)
            print(f"Password: {msg}")
        
    def problem_10(self):
        """Algorithm Implementation"""
        print("\n📝 Problem 10: Search and Sort Algorithms")
        print("-" * 40)
        print("Implement basic algorithms:")
        print("1. Binary search")
        print("2. Bubble sort")
        print("3. Linear search")
        
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        def bubble_sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr
        
        def linear_search(arr, target):
            for i, value in enumerate(arr):
                if value == target:
                    return i
            return -1
        
        # Test algorithms
        unsorted_array = [64, 34, 25, 12, 22, 11, 90]
        sorted_array = sorted(unsorted_array)
        target = 25
        
        print(f"\nUnsorted array: {unsorted_array}")
        print(f"Sorted array: {bubble_sort(unsorted_array.copy())}")
        print(f"Linear search for {target}: {linear_search(unsorted_array, target)}")
        print(f"Binary search for {target}: {binary_search(sorted_array, target)}")
    
    def run_all_problems(self):
        """Run all practice problems"""
        self.display_header()
        
        problems = [
            self.problem_1, self.problem_2, self.problem_3, self.problem_4,
            self.problem_5, self.problem_6, self.problem_7, self.problem_8,
            self.problem_9, self.problem_10
        ]
        
        for i, problem in enumerate(problems, 1):
            try:
                problem()
                self.problems_solved += 1
                print(f"\n✅ Problem {i} completed successfully!")
            except Exception as e:
                print(f"\n❌ Problem {i} failed: {e}")
            
            if i < len(problems):
                input("\nPress Enter to continue to next problem...")
        
        print(f"\n🎉 Practice session completed!")
        print(f"Problems solved: {self.problems_solved}/{self.total_problems}")
        print("\n💡 Tips for actual interview:")
        print("- Explain your approach before coding")
        print("- Write clean, readable code")
        print("- Test with examples")
        print("- Handle edge cases")
        print("- Ask clarifying questions")

if __name__ == "__main__":
    # Run the practice test
    test = CognizantCodingTest()
    
    print("Choose an option:")
    print("1. Run all problems")
    print("2. Run specific problem")
    print("3. View problem list")
    
    try:
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            test.run_all_problems()
        elif choice == "2":
            problem_num = int(input("Enter problem number (1-10): "))
            if 1 <= problem_num <= 10:
                problem_method = getattr(test, f"problem_{problem_num}")
                test.display_header()
                problem_method()
            else:
                print("Invalid problem number!")
        elif choice == "3":
            test.display_header()
            print("Available problems:")
            problems = [
                "1. String Manipulation",
                "2. List Operations", 
                "3. Mathematical Functions",
                "4. Data Processing",
                "5. Object-Oriented Programming",
                "6. Pattern Printing",
                "7. File Operations",
                "8. Exception Handling",
                "9. Data Validation",
                "10. Search and Sort Algorithms"
            ]
            for problem in problems:
                print(problem)
        else:
            print("Invalid choice!")
            
    except ValueError:
        print("Invalid input! Please enter a number.")
    except KeyboardInterrupt:
        print("\nPractice session interrupted. Good luck!")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("\n🚀 Best of luck with your Cognizant interview!")