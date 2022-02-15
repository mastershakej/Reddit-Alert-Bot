from sys import stdout
import time

class SleepHandler:
    @staticmethod
    def sleep(seconds):
        digits = len(str(seconds))
        seconds += 1
        for i in range(1, seconds):
            stdout.write('\r')
            if i % 4 == 0:
                stdout.write('Sleeping (' + str(seconds - i).zfill(digits) + ')')
            elif i % 4 == 1:
                stdout.write('Sleeping (' + str(seconds - i).zfill(digits) + ')')
            elif i % 4 == 2:
                stdout.write('Sleeping (' + str(seconds - i).zfill(digits) + ')')
            elif i % 4 == 3:
                stdout.write('Sleeping (' + str(seconds - i).zfill(digits) + ')')
            stdout.flush()
            time.sleep(1)
        stdout.write('\r')
        stdout.flush()