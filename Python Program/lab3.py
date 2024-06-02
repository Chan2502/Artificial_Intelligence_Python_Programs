framesize = int(input("Enter number of frames : "))
sent = 0
while True:
    for i in range(framesize):
        print("from", sent, "has been transmitted.")
        sent += 1
        if sent == framesize:
            break
    ack = int(input("\nPlease enter the last acknowledgement received.\n"))
    if ack == framesize:
        break
    else:
        sent = ack
