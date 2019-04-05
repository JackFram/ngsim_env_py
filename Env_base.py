# Zhihao Zhang
# ngsim_env_py Env_base class, it will be inherited by its children


class Env_base:
    def __init__(self, env_params: dict):
        self.env_params = env_params

    def step(self, action):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    # no idea how to declare those two for now
    # Base.reset(env::Env;kwargs...) = error("Not implemented")
    # Base.reset(env::Env, dones::Union{Vector{Bool}, Nothing}; kwargs...) = reset(env;kwargs...)

    def observation_space_spec(self):
        raise NotImplementedError

    def action_space_spec(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def obs_name(self):
        raise NotImplementedError

    def vectorized(self):
        return False

    def num_envs(self):
        return 1

