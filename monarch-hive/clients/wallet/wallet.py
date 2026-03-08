
import hashlib,time,qrcode

class Wallet:

 def create_trade(self,amount,memo):

  payload=f"monarch:{amount}:{memo}:{int(time.time())}"

  h=hashlib.sha256(payload.encode()).hexdigest()

  img=qrcode.make(h)

  img.save("trade.png")

  print("QR generated")

if __name__=="__main__":

 Wallet().create_trade(1.0,"coffee")
