def is_prime(n):
    """
    Determine whether a number is prime.
    
    Args:
        n: An integer to check
        
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def main():
    try:
        num = int(input("Enter an integer: "))
        
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
            
    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()
