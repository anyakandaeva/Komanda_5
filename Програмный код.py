import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  SP1 = None
  SP3 = None
  SP4 = None
  SP5 = None
  ZL = None
  b = None
  dist = None
  err = None
  kpW = None
  l = None
  u = None
  v = None

  # Subprograms
  def schetchik(self,l, v):
    
    while True:
      self.b = brick.colorSensor("video2").read(2, 2)[2]
      print(brick.colorSensor("video2").read(2, 2))
      if self.b > 140:
        brick.motor("M1").powerOff()
        brick.motor("M2").powerOff()
        brick.motor("M3").powerOff()
        brick.motor("M4").powerOff()
        
        return
        
        break
      self.regulyator_stena()
      
  def regulyator_stena(self,):
    
    self.err = self.dist - brick.sensor("A1").read()
    self.u = self.kpW * self.err
    brick.motor("M1").setPower(int(60 + self.u))
    
    brick.motor("M2").setPower(int(60 - self.u))
    
    print(brick.sensor("A1").read())
    return
    
  def bez_korobki(self,):
    
    self.SP3 = 50
    self.SP4 = 0
    brick.motor("S5").setPower(-90)
    
    
    while self.SP3 > -30:
      script.wait(50)
      
      self.SP3 = self.SP3 - 1
      brick.motor("S3").setPower(self.SP3)
      
    
    while self.SP4 < 60:
      script.wait(50)
      
      self.SP4 = self.SP4 + 1
      brick.motor("S4").setPower(self.SP4)
      
    
    while self.SP3 < 90:
      script.wait(50)
      
      self.SP3 = self.SP3 + 1
      brick.motor("S3").setPower(self.SP3)
      
    
    while self.SP4 > 0:
      script.wait(50)
      
      self.SP4 = self.SP4 - 1
      brick.motor("S4").setPower(self.SP4)
      
    script.wait(1000)
    
    return
    
  def sbros(self,):
    
    self.SP4 = 90
    self.SP5 = -75
    self.SP1 = -40
    self.SP3 = 90
    
    while self.SP3 > 20:
      script.wait(50)
      
      self.SP3 = self.SP3 - 1
      brick.motor("S3").setPower(self.SP3)
      
    script.wait(1000)
    
    
    while self.SP5 > -90:
      script.wait(50)
      
      self.SP5 = self.SP5 - 1
      brick.motor("S5").setPower(self.SP5)
      
    
    while self.SP4 > 0:
      script.wait(50)
      
      self.SP4 = self.SP4 - 1
      brick.motor("S4").setPower(self.SP4)
      
    brick.motor("S2").setPower(-90)
    
    script.wait(1000)
    
    
    while self.SP3 < 50:
      script.wait(50)
      
      self.SP3 = self.SP3 + 1
      brick.motor("S3").setPower(self.SP3)
      
    script.wait(1000)
    
    brick.motor("S2").setPower(-90)
    
    script.wait(1000)
    
    brick.motor("S1").setPower(-90)
    
    script.wait(3000)
    
    return
    
  def zahvat(self,):
    
    self.SP4 = 0
    self.SP5 = -90
    brick.motor("S2").setPower(-40)
    
    brick.motor("S5").setPower(self.SP5)
    
    brick.motor("S1").setPower(-90)
    
    script.wait(1000)
    
    brick.motor("S3").setPower(60)
    
    
    while self.SP5 < -75:
      self.SP5 = self.SP5 + 1
      script.wait(50)
      
      brick.motor("S5").setPower(self.SP5)
      
    script.wait(3000)
    
    brick.motor("S1").setPower(-20)
    
    script.wait(1000)
    
    brick.motor("S5").setPower(-90)
    
    script.wait(1000)
    
    brick.motor("S3").setPower(0)
    
    
    while self.SP4 < 90:
      self.SP4 = self.SP4 + 1
      script.wait(50)
      
      brick.motor("S4").setPower(self.SP4)
      
    script.wait(3000)
    
    brick.motor("S3").setPower(90)
    
    return
    

  def execMain(self):

    
    brick.say("Я устааааал!")
    
    brick.configure("video2", "colorSensor")
    brick.colorSensor("video2").init(True)
    
    self.kpW = 1.6
    self.dist = 20
    self.v = 60
    self.ZL = 0
    self.zahvat()
    
    script.wait(1000)
    
    self.schetchik(0, self.v)
    
    brick.say("Кладу коробку")
    
    self.sbros()
    
    self.bez_korobki()
    
    brick.colorSensor("video2").stop();
    
    brick.stop()
    return

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
