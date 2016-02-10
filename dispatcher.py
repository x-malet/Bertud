# from __future__ import print_function

try:
    import queue
except ImportError:
    import Queue as queue
import Pyro4
from Pyro4.util import SerializerBase
from workitem import Workitem


# For 'workitem.Workitem' we register a deserialization hook to be able to get these back from Pyro
SerializerBase.register_dict_to_class("workitem.Workitem", Workitem.from_dict)


class DispatcherQueue(object):
    def __init__(self):
        self.workqueue = queue.Queue()
        self.resultqueue = queue.Queue()

    def putWork(self, item):
        self.workqueue.put(item)

    def getWork(self, timeout=5):
        try:
            return self.workqueue.get(block=True, timeout=timeout)
        except queue.Empty:
            raise ValueError("no items in queue")

    def putResult(self, item):
        self.resultqueue.put(item)
        # print type(item)

    def getResult(self, timeout=5):
        try:
            return self.resultqueue.get(block=True, timeout=timeout)
        except queue.Empty:
            raise ValueError("no result available")

    def workQueueSize(self):
        return self.workqueue.qsize()

    def resultQueueSize(self):
        return self.resultqueue.qsize()

    def updateWorkerUsage(self, workerName, cpu_usage, ram_usage):
        print workerName, cpu_usage, ram_usage

    def test(self):
        return "Hello, it's me."

# main program

# Pyro4.Daemon.serveSimple({
#     DispatcherQueue(): "example.distributed.dispatcher"
# })

Pyro4.Daemon.serveSimple(
    {
        DispatcherQueue(): "example.distributed.dispatcher"
    },
    ns=True, verbose=True, host="10.0.63.66")

# Declare this explicitly later on