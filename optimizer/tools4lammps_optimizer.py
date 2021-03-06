from optimizer import Optimizer
from broker.task import Task
import logging

class T4l_optimizer(Optimizer):

    def __init__(self, config):
        super(T4l_optimizer, self).__init__(config)

    def pre_optimize_task(self, task):
        """if a task has requires pre-optimization
           search for id in the config json
        """
        if task.already_pre_optimized:
            return

        task.already_pre_optimized = True

        if task.id in self.config:
            entry = self.config[task.id]
            if entry["pre"] == "":
                logging.info("Nothing to optimize for task {}".format(task.id))
                return
            logging.info("Calling optimization method {} for task {}".format(entry["pre"],
                                                                             task.id))
            getattr(self, entry["pre"])()

    def post_optimize_task(self, task):
        """if a task has requires pre-optimization
           search for id in the config json
        """
        if task.already_post_optimized:
            return

        task.already_post_optimized = True

        if task.id in self.config:
            entry = self.config[task.id]
            if entry["post"] == "":
                logging.info("Nothing to optimize for task {}".format(task.id))
                return
            logging.info("Calling optimization method {} for task {}".format(entry["post"],
                                                                             task.id))
            getattr(self, entry["post"])()

    def pre_optimize_t4l(self):
        pass

    def post_optimize_t4l(self):
        pass