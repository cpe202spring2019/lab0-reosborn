def weight_on_planets():
   # write your code here
   weight = input("What do you weigh on earth?")
   mars = .38 * int(weight)
   jupiter = 2.34 * int(weight)
   print(' ')
   print("On Mars you would weigh {mars} pounds.")
   print("On Jupiter you would weigh {jupiter} pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()
