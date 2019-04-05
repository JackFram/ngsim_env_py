# Zhihao Zhang
# ngsim_env_py debug_envs class, this is the DeterministicSingleStepDebugEnv class

from Env_base import Env_base


class DeterministicSingleStepDebugEnv(Env_base):
    def __init__(self, envs_params: dict):
        super(DeterministicSingleStepDebugEnv, self).__init__(envs_params)

    def step(self, action: int):
        assert action == 1 or action == 2
        return 0, action, True, dict()

    def reset(self):
        return 0

    def observation_space_spec(self):
        return [i for i in range(1)], "Discrete"

    def action_space_spec(self):
        return [i for i in range(2)], "Discrete"

    def obs_name(self):
        return 'No name'

    def render(self):
        pass
