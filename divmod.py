def readable_time(seconds):
    m,s = divmod(seconds,60)
    h,m = divmod(m,60)
    
    return f'{h:02d}:{m:02d}:{s:02d}'

print(readable_time(600))