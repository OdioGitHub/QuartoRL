from gym.envs.registration import register

register(
    id='quarto-v0',
    entry_point='gym_quarto.envs:QuartoEnv',
)