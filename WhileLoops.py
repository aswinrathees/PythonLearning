# Introduction to While Loops

temp = 10

while temp < 20:
    temp += 1                         # Increment the temperature by 1
    if temp == 15:
        #break                        # Break the loop when temperature reaches 15
        #continue                     # Skip the rest of the loop when temperature reaches 15
        pass                          # Do nothing when temperature reaches 15
    print("Current temperature:", temp)  # Print the current temperature
print("Loop ended at temperature:", temp)  # This will print the final temperature after the loop ends