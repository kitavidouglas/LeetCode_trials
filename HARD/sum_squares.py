import sys
from io import StringIO

def main():
    input_data = sys.stdin.read().splitlines()
    
    def process_cases(index, cases_left):
        if cases_left == 0:
            return
        
        x = int(input_data[index])  # Number of integers in this test case
        numbers = map(int, input_data[index + 1].split())  # Read numbers

        def sum_squares(remaining_numbers, total):
            if not remaining_numbers:
                print(total)  # Print the computed sum
                return
            
            head, *tail = remaining_numbers
            sum_squares(tail, total + (head * head if head >= 0 else 0))

        sum_squares(list(numbers), 0)
        process_cases(index + 2, cases_left - 1)

    process_cases(1, int(input_data[0]))

if __name__ == "__main__":
    # Simulating input for testing
    sys.stdin = StringIO("2\n4\n3 -1 1 14\n5\n9 6 -53 32 16")
    main()
