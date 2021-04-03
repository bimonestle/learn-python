# Use find and string slicing to extract the portion of the string
# after the colon character and then use the float function to convert
# the extracted string into a floating point number.

code = 'X-DSPAM-Confidence:0.8475'

floatPos = code.find(":") + 1
floatNumb = float(code[floatPos:])
print(floatNumb)
print(type(floatNumb))