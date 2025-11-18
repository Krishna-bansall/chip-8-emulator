import multiprocessing, time

def tick_check():
    tick = 0
    while True:
        tick += 1
        print(tick)

# tick_check()

if __name__ == '__main__':
    # Start bar as a process
    p = multiprocessing.Process(target=tick_check)
    p.start()

    # Wait for 10 seconds or until process finishes
    p.join(1)
    
    if p.is_alive():
        print ("running... let's kill it...")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()
