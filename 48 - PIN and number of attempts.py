# Write your solution here
attempts = 0
correct_pin = 4321
while True:
    pin = int(input("PIN:"))
    attempts += 1
    if pin != correct_pin:
        print("Wrong")
    else:
        break
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
