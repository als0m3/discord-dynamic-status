import time
from services.apiCalls import setStatus
import multiprocessing as mp
from loops.animations import *


DEFAULT_PROCESS = "spaceInvader"


def loop(process_):
    try:
        print("process is", process_)
        percent = 0
        while(True):
            time.sleep(.5)

            percent, loading_string = globals()[process_](percent)
            setStatus(loading_string, "idle")
    except:
        print("process does not exist")


if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=loop, args=(DEFAULT_PROCESS,))
    p.start()
    while(True):
        input_ = input()
        print("Change process")
        p.terminate()
        p.join()
        p = ctx.Process(target=loop, args=(input_,))
        p.start()
