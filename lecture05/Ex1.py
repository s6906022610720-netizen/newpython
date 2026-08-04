def is_armstrong(n):
    # แปลงตัวเลขเป็น string เพื่อหาจำนวนหลัก และดึงเลขแต่ละหลักออกมาง่ายๆ
    s = str(n)
    power = len(s)
    
    # คำนวณผลรวมของเลขแต่ละหลักยกกำลังด้วยจำนวนหลัก
    total = sum(int(digit) ** power for digit in s)
    
    # ส่งคืนค่า True ถ้าผลรวมเท่ากับตัวเลขเดิม
    return total == n


# --- ทดสอบการใช้งานตามโจทย์ ---
print(is_armstrong(153))   # Output: True
print(is_armstrong(9474))  # Output: True
print(is_armstrong(123))   # Output: False