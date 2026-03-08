
import random,time

class Sophia:

 def observe(self):
  return random.choice(["trade","market","weather"])

 def reason(self,event):

  if event=="trade":
   return "trade activity rising"

  return "network stable"

if __name__=="__main__":

 s=Sophia()

 while True:

  e=s.observe()

  print("Sophia insight:",s.reason(e))

  time.sleep(5)
