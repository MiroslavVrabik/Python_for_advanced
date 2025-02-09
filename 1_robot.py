class Robot:

    # constructor
    def __init__(self, battery, arms_length):
        self.bat = battery
        self.arm_len = arms_length
        self.performed_until_control = 1000

    def step_forward(self):
        print("Robot stepped forward")
        self.performed_until_control -= 1
        print(f"Úkonů do kontroly: {self.performed_until_control}")

    def step_backward(self):
        print("Robot stepped backward")
        self.performed_until_control -= 1
        print(f"Úkonů do kontroly: {self.performed_until_control}")

# Tvoříme objekty podle classy

robot_1 = Robot(24, 0.6)
robot_2 = Robot(48, 0.5)
robot_3 = Robot(12, 0.2)
robot_4 = Robot(18, 0.3)

print(robot_1.bat)
print(robot_1.arm_len)
print(robot_1.performed_until_control)
robot_1.step_forward()
robot_1.step_backward()
robot_1.step_forward()
robot_1.step_backward()
robot_1.step_forward()
robot_1.step_backward()
robot_1.step_forward()
robot_1.step_backward()
robot_1.step_forward()
robot_1.step_backward()
print(robot_1.performed_until_control)

# print(robot_2.bat)
# print(robot_2.arm_len)
# print(robot_2.performed_until_control)
#
# print(robot_3.bat)
# print(robot_3.arm_len)
# print(robot_3.performed_until_control)
#
# print(robot_4.bat)
# print(robot_4.arm_len)
# print(robot_4.performed_until_control)