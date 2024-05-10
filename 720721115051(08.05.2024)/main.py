def roman_To_Int(s):
  m = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }
        
  output = 0
        
  for i in range(len(s)):
    if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
      output -= m[s[i]]
    else:
       output += m[s[i]]
  return output

print(roman_To_Int('III'))
print(roman_To_Int('LVIII'))
print(roman_To_Int('MCMXCIV'))