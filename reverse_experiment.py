from __future__ import division

import torch.nn as nn

from models.vanilla import Controller
from tasks.reverse import ReverseTask

read_size = 1
task = ReverseTask(min_length=1,
                   mean_length=10,
                   std_length=2,
                   max_length=12,
                   learning_rate=0.01,  # Must be 0.01
                   l2_weight=0.01,
                   batch_size=10,
                   read_size=read_size,
                   cuda=False,
                   epochs=100,
                   model_type=Controller,
                   criterion=nn.CrossEntropyLoss(),
                   verbose=True)

task.run_experiment()
