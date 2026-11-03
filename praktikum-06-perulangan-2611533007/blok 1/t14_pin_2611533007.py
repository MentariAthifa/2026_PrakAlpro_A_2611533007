attempt_3007 = 1
MAX_ATTEMPTS_3007 = 3
correct_pin_3007 = "1234"
pin_3007 = input("Enter PIN: ")

while pin_3007 != correct_pin_3007 and attempt_3007 < MAX_ATTEMPTS_3007:
    print("Incorrect PIN")
    pin_3007 = input("Enter PIN: ")
    attempt_3007 += 1

if pin_3007 == correct_pin_3007:
    print("Access granted")
else:
    print("Account locked")