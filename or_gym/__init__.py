import os
import sys
import warnings

import gymnasium as gym
from gymnasium import error

from or_gym.version import VERSION as __version__
from or_gym.utils import *

from gymnasium.core import Env, Wrapper, ObservationWrapper, ActionWrapper, RewardWrapper
from gymnasium.envs import spec, register
from or_gym.envs import classic_or, finance, supply_chain


def make(id, **kwargs):
    env_cls = create_env(id)
    return env_cls(**kwargs)
