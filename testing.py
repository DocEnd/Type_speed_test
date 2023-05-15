import time
#
# class Timer():
#     def __init__(self):
#         self.start_time = None
#         self.end_time = None
#         self.now_time = time.time()
#         self.passed_time = 0
#
#     def go_time(self):
#         self.start_time = time.time()
#
#     def calculate_time(self):
#         self.passed_time = self.now_time - self.start_time
#         print(self.passed_time)
#
#     def play_time_on(self, seconds_to_go):
#         if self.passed_time < seconds_to_go:
#             return True
#         else:
#             return False

time_now = time.time()
time_to_stop = time_now + 10
while time.time() < time_to_stop:
    print("go")
