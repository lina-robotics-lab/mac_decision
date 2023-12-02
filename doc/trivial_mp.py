from multiprocessing import Process, Array, Lock, Manager
import sys
sys.path.append('/home/mht/PycharmProjects/mac_decision')
from src.SafeMaC.utils.visualizer_simu import Visulizer
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

def run_visualizer(shared_list, lock):
    visu = Visulizer(shared_list, lock)
    visu.run()

if __name__ == '__main__':
    info('main line')
    shared_list = Manager().list([0, 1, 2])
    lock = Lock()
    p = Process(target=run_visualizer, args=(shared_list, lock))
    p.start()
    p.join()
    # print(os.path.dirname(os.path.dirname(__file__)))