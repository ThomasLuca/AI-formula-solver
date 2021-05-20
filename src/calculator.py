import math


class Calculator:
    def __init__(self, formula):
      self.formula = formula

    def calculateX(self):
      seperated = self.separate(self.formula)
      a, b, c = self.extractABC(seperated)
      print(f"a: {a}, b: {b}, c: {c}")
      
      D =  pow(b, 2) - 4*a*c 
      if D < 0:
        print("Roots are complex")
      else:
        x1 = (-b + math.sqrt(abs(D))) / (2*a)
        x2 = (-b - math.sqrt(abs(D))) / (2*a)
        print(f"X1 = {x1}")
        print(f"X2 = {x2}")

    
    def separate(self, f):
      separated = []
      temp = ""

      for i in range(len(f)):
          c = f[i]
          if c == "-" or c == "+":
            if temp != '':
              separated.append(temp)
            separated.append(c)
            temp = ""
          elif i == len(f)-1:
            temp += c
            separated.append(temp)
          else:
            temp += c
      
      if '' in separated:
        separated.remove('')
      print(separated)
      return separated
      
    def extractABC(self, seperated):
      a, b, c = (0, 0, 0)
      sym = ''
      for e in seperated:
          if "X²" in e:
              if len(e) == 2:
                  a = int(sym + '1')
              else:
                  a = int(sym + e.replace("X²", ""))
          elif "X" in e:
              if len(e) == 1:
                  b = int(sym + '1')
              else:
                b = int(sym + e.replace("X", ""))
              sym = ""
          elif e == '-' or e == '+':
              sym = e
          else:
              c = int(sym + e)
      return (a, b, c)
