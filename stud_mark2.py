# ========== STUDENT SYSTEM ==========

# Student Name: Anurag
# Math: 85
# Science: 72
# English: 91
# Python: 88

# Total = 336
# Percentage = 84%
# Grade = B
# Result = PASS

# Student name
# Roll number
# 4–5 subject marks

# Total
# Percentage
# Grade
# Pass/Fail


# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# <60    → Fail

def res_check(mat, sci, eng, pyt):
    total = mat + sci + eng + pyt
    percentage = total / 400 * 100 
    if percentage >= 90 and percentage <= 100:
           
        print("Grade A")
        return "Pass"
    elif percentage >= 80 and percentage <= 89:
        print("Grade B")
        return "Pass"

    elif percentage >= 70 and percentage <= 79:
            print("Grade C")
            return "Pass"
    elif percentage >= 60 and percentage <= 79:
                print("Grade D")
                return "Pass"
    else:
          return "Fail"
 
    
while True:
      name = input("Please enter your name: ")
      mat = int(input("Enter maths score: "))
      if mat > 100 or mat < 0:
            print("Enter Valid Input")
            break
      sc = int(input("Enter science score: "))
      if sc > 100 or mat < 0:
                  print("Enter Valid Input")
                  break
      en = int(input("Enter english score: "))
      if en > 100 or mat < 0:
                  print("Enter Valid Input")
                  break
      py = int(input("Enter python score: "))
      if py > 100 or mat < 0:
                  print("Enter Valid Input")
                  break
      i = res_check(mat,sc,en,py)
      print(f"{name} you are {i}.")

      
      

