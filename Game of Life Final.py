

print("""Rules:

~ If bacterium is dead but BOTH of its neighboring bacteria are alive, the bacterium becomes alive.
~ If bacterium is alive but BOTH of its neighboring bacteria are dead or alive, the bacterium dies.
~ An alive bacterium survives for the next generation if and only if it EXACTLY has one alive neighbor.

N.B: 1 means that the bacterium is alive and 0 means that it is dead.

Enjoy!
""")


string = str(input("Enter the bacterial string: "))
gen = int(input("Enter the number of genrations: "))

length  = len(string)

def replace(s, pos, b):
    s_1 = s[:pos]
    s_2 = s[pos+1:]
    s_final = s_1 + b + s_2
    return s_final

print()

string_li = [string]

count = 0
for i in range(gen):
    
    new_string = ""
    
    for j in range(length):
        element = string[j]
        li = []
        ### left and right determination
        
        if j == 0:
            left = "0"
        if j == length-1:
            right = "0"
        if j >= 0 and j < length-1:
            right = string[j+1]
        if j <= length-1 and j > 0:
            left = string[j-1]
            
        
        count_0 = 0
        count_1 = 0
        
        if left == "0":
            count_0 += 1
        else:
            count_1 += 1
        if right == "0":
            count_0 += 1
        else:
            count_1 += 1
            
        ### conditions for living
            
        if count_0 == 2:
            new = "0"
            
        if count_1 == 1 and element == "0":
            new = "0"
               
        if count_1 == 1 and element == "1":
            new = "1"
            
        if count_1 == 2 and element == "1":
            new = "0"
            
        if count_1 == 2 and element == "0":
            new = "1"

            
        new_string += new
        
    string = new_string
    print(string)
    print()
    
    if string not in string_li:
        string_li.append(string)
    elif string != length*"0":
        print("This pattern continues")
        print("Your bacteria survived through all the generations")
        break
    
    dead = "0" * length
    if string != dead:
        count += 1
    else:
        print("Your bacteria survived for:", count, "generation(s)")
        break
    if count == gen:
        print("Your bacteria survived through all the generations")
        alive_count = 0
        for k in string:
            if k == "1":
                alive_count += 1
                
        print("Number of bacteria alive:", alive_count)
        
