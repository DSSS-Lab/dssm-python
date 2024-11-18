import signal

from dssm_python.ssm import *
from ini_ssm import *

keep_running = True


def signal_handler(sig, frame):
    global keep_running
    print('Loop interrupted by Ctrl-C')
    keep_running = False


if __name__ == "__main__":
    if not init_ssm():
        print("failed to initialize ssm")
        exit(1)

    ssm_api = SSMBaseAPI(stream_name='intSsm', stream_id=1, data_size=ctypes.sizeof(IniSsm))

    if not ssm_api.create(5.0, 1.0):
        print("failed to create ssm api")
        exit(1)

    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl-C to stop the loop.')

    i = 1
    while keep_running:
        # for the sample_datastruct
        # arr = [i+1, i+2, i+3, i+4, i+5]
        # data = IniSsm(i, i, i + 1.0, (ctypes.c_int * 5) (*arr))

        data = IniSsm(i)
        ssm_api.__data__ = data
        if ssm_api.write():
            print(i)
        i += 1

        sleep_ssm(1)

    ssm_api.release()
    end_ssm()
