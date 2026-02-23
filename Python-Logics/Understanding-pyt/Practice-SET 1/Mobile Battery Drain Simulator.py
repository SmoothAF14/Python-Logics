bpm = int(input())
battery = 100
minutes  = 0
while battery > 0:
    battery -= bpm
    minutes += 1    
print(minutes)