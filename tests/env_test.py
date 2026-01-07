#!usr/bin/env python

'''
Tests to ensure environments load and basic functionality
is satisfied.
'''

import or_gym
from or_gym.envs.env_list import ENV_LIST
import traceback

def pytest_generate_tests(metafunc):
    idlist = []
    argvalues = []
    for scenario in metafunc.cls.scenarios:
        idlist.append(scenario[0])
        items = scenario[1].items()
        argnames = [x[0] for x in items]
        argvalues.append([x[1] for x in items])
    metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")

class TestEnv:
    scenarios = [(i, {'config': {'env_name': i}}) for i in ENV_LIST]

    def _build_env(self, env_name):
        env = or_gym.make(env_name)
        return env

    def test_make(self, config):
        # Ensures that environments are instantiated
        env_name = config['env_name']
        try:
            _ = self._build_env(env_name)
            success = True
        except Exception as e:
            tb = e.__traceback__
            success = False
        assert success, ''.join(traceback.format_tb(tb))

    def test_episode(self, config):
        # Run 100 episodes and check observation space
        env_name = config['env_name']
        EPISODES = 100
        env = self._build_env(env_name)
        for ep in range(EPISODES):
            reset_result = env.reset()
            if isinstance(reset_result, tuple):
                state = reset_result[0]
            else:
                state = reset_result
            while True:
                assert env.observation_space.contains(state), \
                    f"State out of range of observation space: {state}"
                action = env.action_space.sample()
                step_result = env.step(action)
                if len(step_result) == 5:
                    state, reward, terminated, truncated, info = step_result
                    done = terminated or truncated
                else:
                    state, reward, done, info = step_result
                if done:
                    break
        
        assert done
