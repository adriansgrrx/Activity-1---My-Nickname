# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

# Hello Sir. Dan! My nickname is Eds!
# I will be using for loops and if statements for this program

# This pattern will be my reference
# * * * *  * * *     * * * 
# *        *    *   *  
# *        *     *  *   
# * * *    *     *   * * * 
# *        *     *        *   
# *        *    *         *   
# * * * *  * * *     * * * 

for i in range(10):
    if i == 4:
        print(" ", end="")
    elif i==7:
        print("    ", end="")
    print("* ", end="")