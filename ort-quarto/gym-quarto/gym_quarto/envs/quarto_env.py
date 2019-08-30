import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np


class QuartoEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):

    self.board = np.zeros((4,4))
    self.pieces = np.ones((15))

    self.reward_range = (0, 1)

    # la accion consiste en poner la ficha que nos da el oponente 
    # y seleccionar la ficha para el oponente, en el caso de jugar primero no hay ficha para colocar asi que deberia solo seleccionar la del oponente
    # se codifica en un array con 2 valores que pueden asumir un low y high
    # https://stackoverflow.com/questions/44404281/openai-gym-understanding-action-space-notation-spaces-box
    # acepta valores de 0 a 15 para la posicion en el tablero
    # y valores de 0 a 15 para seleccionar que pieza juega el oponente
    # self.action_space = spaces.Box(low=np.array([0, 0]), high=np.array([15, 15]))
    self.action_space = spaces.MultiDiscrete([16,16])

    # el observation space es un array con el tablero de 4x4 y otro de 1 dimension con las piezas que se pueden jugar
    # https://www.programcreek.com/python/example/97539/gym.spaces.Box 
    
    self.observation_space = spaces.Tuple([
            spaces.Box(low=0, high=16, shape=(4, 4), dtype=np.int), # este es el tablero de 4x4 0 es vacio de 1 a 16 son las posibles piezas
            spaces.Box(low=0, high=15, shape=(1,), dtype=np.int), # esta es la pieza que le toca jugar
            spaces.Box(low=0, high=1, shape=(16,), dtype=np.int) # lista de piezas que puede elejir segun index 0 a 15 // 1 esta 0 no esta
        ])

    a=1

  def step(self, action):
    a=1
  def reset(self):
    # aca se pone todo en 0, vacia el tablero y llena el stack de piezas para elegir
    # https://towardsdatascience.com/reinforcement-learning-with-openai-d445c2c687d2
    self.board = self.board.fill(16)
    self.pieces = self.pieces.fill(1)
    

    a=1
  def render(self, mode='human', close=False):
    a=1
  def close(self):
    a=1