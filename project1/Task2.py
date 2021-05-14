"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

class Solution:
    def __init__(self, calls):
        self.calls = calls
        self.max_call_time = 0
        self.max_caller = ''
        self.phonenr_call_length = dict()

    def calc_call(self, phone_number, call_duration):
        total_phonenr_duration = self.phonenr_call_length.get(phone_number, 0) + call_duration

        if total_phonenr_duration > self.max_call_time:
            self.max_call_time = total_phonenr_duration
            self.max_caller = phone_number
        
        self.phonenr_call_length[phone_number] = total_phonenr_duration

    def print_max_caller(self):
        for call in self.calls:
            self.calc_call(call[0], int(call[3]))
            self.calc_call(call[1], int(call[3]))

        print(f'{self.max_caller} spent the longest time, {self.max_call_time} seconds, on the phone during September 2016.')

solution = Solution(calls)
solution.print_max_caller()