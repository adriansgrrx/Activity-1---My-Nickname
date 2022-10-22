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

print()

for j in range(13):
    if j==0 or j==7 or j==10 or j==12:
        print("* ", end="")
    print(" ", end="")

print()

for k in range(14):
    if k==0 or k==7 or k==11 or k==12:
        print("* ", end="")
    print(" ", end="")

print()

for l in range(8):
    if l==3:
        print("   ", end="")
    elif l==4:
        print("    ", end="")
    elif l==5:
        print("  ", end="")

    print("* ", end="")

print()