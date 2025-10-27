from abc import ABC, abstractmethod
import src.assets.definitions as df
import pygame as pg
import sys

# -------------------------------------------------------------------------------------------------
#
#
__all__ = ["EventManager"]


# -------------------------------------------------------------------------------------------------
#
#
class EventListener(ABC):

    @abstractmethod
    def alert(self, *args):
        pass


# -------------------------------------------------------------------------------------------------
#
#
class EventManager:

    def __init__(self):
        self.listeners = {}

    # ---------------------------------------------------------------------------------------------
    #   Register Events
    #
    def register_events(self):
        """
            Register all applicable events that can occur on the game

                Alpha_keymap    -> keys/value K_A = 97 ... K_Z = 122

                Alt_keymap      -> key/value K_RETURN, K_BACKSPACE, K_ESCAPE, K_MOUSEBUTTONUP, K_KEYDOWN
        """
        for event in df.alpha_keymap.values():
            self.listeners[event]: dict = []

        for event in df.used_pygame_events.values():
            self.listeners[event]: dict = []

    # ---------------------------------------------------------------------------------------------
    #   Subscribe
    #
    def subscribe(self, event_type, handler):
        self.listeners[event_type].append(handler)

    # ---------------------------------------------------------------------------------------------
    #   Unsubscribe
    #
    def unsubscribe(self, event_type, handler):
        self.listeners[event_type].remove(handler)

    # ---------------------------------------------------------------------------------------------
    #   Notify
    #
    def notify(self, event_type, *args):
        for handler in self.listeners[event_type]:
            handler.handle_it(*args)

    # ---------------------------------------------------------------------------------------------
    #   Parse
    #
    def parse(self):
        """
        Parse the event loop and notify all respective listeners
        """
        mouse_pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key in df.alpha_keymap.values() or event.key in df.used_pygame_events.values():
                    self.notify(event.key, chr(event.key))
                else:
                    pass

            if event.type == pg.MOUSEBUTTONUP:
                self.notify(pg.MOUSEBUTTONUP, mouse_pos)

            if event.type == pg.MOUSEMOTION:
                self.notify(pg.MOUSEMOTION, mouse_pos)

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
