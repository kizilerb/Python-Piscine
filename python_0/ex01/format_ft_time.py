import time

now_sec = time.time()
now_date = time.ctime(now_sec).split()
print("Seconds since January 1, 1970:", f"{now_sec:,.4f}", "or", f"{now_sec:.2e}", "in scientific notation")
print(now_date[1], now_date[2], now_date[4])
