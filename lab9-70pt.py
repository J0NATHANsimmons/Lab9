############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print "Celius to Farenheit calculator!"
print "Type your Celcius tempurature :"
userInput = int(raw_input()) *9 /5 +32
print "Your Farenheit tempurature is " + str(userInput) + "!"