# Port Scanner in Python

# imports psutil and time packages
import psutil
import time

def formatBytes(bytesAmount):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytesAmount < 1024:
            return f"{bytesAmount:.2f} {unit}"
        bytesAmount /= 1024
    return f"{bytesAmount:.2F} TB"


# main function for the network monitor
def networkMonitor():
    print("Starting Network Monitor... \nPress CTRL+C to stop.\n")


    oldStats = psutil.net_io_counters()

    # while loop that loops and updates 
    # the display of the stats every 1 second
    while True:
        time.sleep(1)
        newStats = psutil.net_io_counters()
        # calculates the speeds
        bytesSent = newStats.bytes_sent - oldStats.bytes_sent
        bytesRecv = newStats.bytes_recv - oldStats.bytes_recv

        oldStats = newStats

        # Prints the network stats in real time
        print("=" * 40)
        print(f"Upload Speed    : {formatBytes(bytesSent)}/s")
        print(f"Download Speed  : {formatBytes(bytesRecv)}/s")
        print(f"Total Sent      : {formatBytes(newStats.bytes_sent)}")
        print(f"Total Recieved  : {formatBytes(newStats.bytes_recv)}")


# stops the program when you press CTRL+C

if __name__ == "__main__":
    try:
        networkMonitor()
    except KeyboardInterrupt:
        print("\nNetwork Monitor Stopped")