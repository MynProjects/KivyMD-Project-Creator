import utils
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

utils.load_kv("tab_one.kv")


class TabOne(FloatLayout, MDTabsBase):
    """
    Tab Item One.
    """
