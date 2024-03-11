stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below

'''
The only valid characters in scientific notation are the digits 0-9, the letters E and x, the period symbol ., the hyphen symbol -, and the caret symbol ^. No spaces are allowed in the string.
There should be no more than one period (.), multiply symbol (x), or caret symbol (^) in the input string.
The exponent should be a valid integer (no floats allowed).
'''
valid = True
count = [0,0,0]
for i in stdform:
  if not(i in "0123456789Ex.-^"):
    valid = False
  if i == ".":
    count[0] += 1
  elif i == "x":
    count[1] += 1
  elif i == "^":
    count[2] += 1
  if count[0] > 1 or count[1] > 1 or count[2] > 1:
    valid = False

if valid: 
  mantissa = ""
  exponent = ""
  E = 0
  for i in range(len(stdform)):
    if E == 0:
      if stdform[i:i+4] == "x10^":
        E = 1
      else:
        mantissa = mantissa + stdform[i]
    elif E < 4:
      E = E + 1
    else:
      exponent = exponent + stdform[i]  
  if "." in exponent:
    valid = False 

if valid:
  print("This number in E notation is "+mantissa+"E"+exponent+".")
else:
  print("Error converting to scientific E notation.")