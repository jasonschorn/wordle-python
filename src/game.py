import pygame as pg

import src.assets.definitions as df
from src.event_manager import EventManager
from src.state_manager import StateManager

# -------------------------------------------------------------------------------------------------
#
#
__all__ = ['Game']


# -------------------------------------------------------------------------------------------------
#   Game
#
class Game:

    def __init__(self):
        pg.init()
        self.canvas = pg.display.set_mode(df.ScreenDimensions)
        self.clock = pg.time.Clock()

        self.event_manager = EventManager()
        self.state_manager = StateManager(self.canvas, self.event_manager)

    # -------------------------------------------------------------------------------------------------
    #   Run
    #
    def run(self):
        pg.init()
        self.initialize()

        while True:
            self.clock.tick(df.Fps)
            self.canvas.fill(df.BgColor)
            self.event_manager.parse()
            self.update()

            pg.display.flip()

    # -------------------------------------------------------------------------------------------------
    #   Update
    #
    def update(self):
        if self.state_manager.cur_state.name == "Initial":
            self.state_manager.cur_state.render(self.canvas)
        else:
            self.state_manager.cur_state.render(self.canvas, self.state_manager)

    # -------------------------------------------------------------------------------------------------
    #   Initialize
    #
    def initialize(self):
        # -------------------------------------------------------------------------------------------------
        #   Registers all alpha keys and used pygame events
        #       K_RETURN, K_BACKSPACE, K_ESCAPE, KEYDOWN, MOUSEBUTTONUP, MOUSEMOTION
        #
        self.event_manager.register_events()  # Get random Wordle word
        #
        #   Required to come after initializing all game-specific events since it sets
        #   the Initial state game button mouse over and mouse up listeners
        #
        self.state_manager.set_initial_state("Initial")
