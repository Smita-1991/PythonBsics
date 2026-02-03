i=1

while i<=5:
    if i == 4:
        i = i + 1
        continue  ### Break on this step and continue to the next iteration
    if i==5:
        break   ##### Break on the current iteration not to execute the next iteration
    print(i)
    i = i + 1
