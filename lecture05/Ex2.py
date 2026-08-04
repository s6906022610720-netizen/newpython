def is_prime(num):
    # """ฟังก์ชันเช็คว่า num เป็นจำนวนเฉพาะหรือไม่"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    # """ฟังก์ชันสร้าง String ของจำนวนเฉพาะที่ไม่เกิน n"""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(str(num))
    
    # นำจำนวนเฉพาะมารวมกันด้วย ", "
    return ", ".join(primes)


# --- ทดสอบการใช้งานตามโจทย์ ---
print(generate_primes(10)) # Output: "2, 3, 5, 7"
print(generate_primes(20)) # Output: "2, 3, 5, 7, 11, 13, 17, 19"
print(generate_primes(1))  # Output: ""
print(generate_primes(2))  # Output: "2"