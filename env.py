# Zhihao Zhang
# ngsim_env_py Env class, this is the class that create an environment for us


from debug_envs import DeterministicSingleStepDebugEnv


class Env:

    def __init__(self, env_id: str, env_params: dict):
        self.env_id = env_id
        self.env_params = env_params

    def make_env(self):
        try:
            if self.env_id == "DeterministicSingleStepDebugEnv":
                return DeterministicSingleStepDebugEnv(self.env_params)
            elif self.env_id == "NGSIMEnv":
                return NGSIMEnv(self.env_params)
            elif self.env_id == "VectorizedNGSIMEnv":
                return VectorizedNGSIMEnv(self.env_params)
            elif self.env_id == "MultiagentNGSIMEnv":
                return MultiagentNGSIMEnv(self.env_params)
            elif self.env_id == "MultiagentNGSIMEnvVideoMaker":
                return MultiagentNGSIMEnvVideoMaker(self.env_params)
            else:
                raise ValueError("We don't have a env with this name, try another one!")
        except Exception as error:
            print('Caught this error: ' + repr(error))


