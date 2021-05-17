from os import sep
import warnings
warnings.filterwarnings('ignore')
import numpy as np


class Calculator:
    def __init__(self, formula):
      self.formula = formula

    def calculateX(self):
      seperated = self.separate(self.formula)
      print(seperated)
      print(self.extractABC(seperated))
    
    def separate(self, f):
      separated = []
      temp = ""

      for i in range(len(f)):
          c = f[i]
          if c == "-" or c == "+" or i == len(f)-1:
              separated.append(temp)
              separated.append(c)
              temp = ""
          else:
              temp += c
      
      if '' in separated:
        separated.remove('')

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
      return [a, b, c]

    # def calcroots(self, numbers):
    #   coeff.append(numbers[0]).append(numbers[4]).append(numbers[7])
    #   return np.roots(coeff)