text = 'X-DSPAM-Confidence:     0.8475'
colPos = text.find(':')
numb = text[colPos+1 :].strip()
floatNumb = float(numb)
print(floatNumb)