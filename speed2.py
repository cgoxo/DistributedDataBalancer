import time
import os
class DiskSpeed:
    def __init__(self,drive):
        self.dr_name=drive
    
    def get_write_speed(self):
    
        st_to_write="faferfvjhgrf,bu,ferfreuu4fr37fbv,e8qlf83l8rqT@6ikg"
        start_timer=time.time()
        try:
            f=open('wrtcheck.txt','w')
            for k in range(0,100000):
                for q in st_to_write:
                    f.write(q)
            f.close()
            end_timer=time.time()
            size=os.stat("wrtcheck.txt")
            d=size.st_size//(end_timer-start_timer)
            os.remove('wrtcheck.txt')
            d=int(d)
            return (str(d))
        except:
            return "error"
                    
    
drive_name="/dev/sda2"
disk_speed=DiskSpeed(drive_name)

print ("Disk write speed for drive {0} is {1} bits/s".format(drive_name,disk_speed.get_write_speed()))

