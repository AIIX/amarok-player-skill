"""
Amarok Player Mycroft Skill.
"""

import os
from os.path import dirname
import dbus
import psutil
from adapt.intent import IntentBuilder
from mycroft.util.log import getLogger
from mycroft.skills.core import MycroftSkill, intent_handler

__author__ = 'aix'

LOGGER = getLogger(__name__)


class AmarokSkill(MycroftSkill):
    """
    Amarok Skill Class.
    """

    def __init__(self):
        """
        Initialization.
        """
        super(AmarokSkill, self).__init__(name="AmarokSkill")

    @intent_handler(IntentBuilder("AmarokPlayKeywordIntent")
                    .require("AmarokPlayKeyword").build())
    def handle_internals_amarok_play_skill_intent(self):
        """
        Amarok Play Music
        """
        self.speak_dialog("amarok.play")
        amarok_running = False

        for proc in psutil.process_iter():
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            if pinfo['name'] == 'amarok':
                amarok_running = True

        if amarok_running:
            def runplay():
                """
                Amarok Skip Run Then Play
                """
                bus = dbus.SessionBus()
                remote_object = bus.get_object("org.mpris.MediaPlayer2.amarok",
                                               "/org/mpris/MediaPlayer2")
                remote_object.Play(
                    dbus_interface="org.mpris.MediaPlayer2.Player")
            runplay()

        else:
            def runprocandplay():
                """
                Amarok Run First Then Play
                """
                os.system("amarok")
                bus = dbus.SessionBus()
                remote_object = bus.get_object("org.mpris.MediaPlayer2.amarok",
                                               "/org/mpris/MediaPlayer2")
                remote_object.Play(
                    dbus_interface="org.mpris.MediaPlayer2.Player")
                runprocandplay()

    @intent_handler(IntentBuilder("AmarokStopKeywordIntent")
                    .require("AmarokStopKeyword").build())
    def handle_internals_amarok_stop_skill_intent(self):
        """
        Amarok Stop Music
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.mpris.MediaPlayer2.amarok",
                                       "/org/mpris/MediaPlayer2")
        remote_object.Stop(
            dbus_interface="org.mpris.MediaPlayer2.Player")

        self.speak_dialog("amarok.stop")

    @intent_handler(IntentBuilder("AmarokNextKeywordIntent")
                    .require("AmarokNextKeyword").build())
    def handle_internals_amarok_next_skill_intent(self):
        """
        Amarok Next Song
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.mpris.MediaPlayer2.amarok",
                                       "/org/mpris/MediaPlayer2")
        remote_object.Next(
            dbus_interface="org.mpris.MediaPlayer2.Player")

        self.speak_dialog("amarok.next")

    @intent_handler(IntentBuilder("AmarokPreviousKeywordIntent")
                    .require("AmarokPreviousKeyword").build())
    def handle_internals_amarok_previous_skill_intent(self):
        """
        Amarok Previous Song
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.mpris.MediaPlayer2.amarok",
                                       "/org/mpris/MediaPlayer2")
        remote_object.Previous(
            dbus_interface="org.mpris.MediaPlayer2.Player")

        self.speak_dialog("amarok.previous")

    @intent_handler(IntentBuilder("AmarokPauseKeywordIntent")
                    .require("AmarokPauseKeyword").build())
    def handle_internals_amarok_pause_skill_intent(self):
        """
        Amarok Pause Song
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.mpris.MediaPlayer2.amarok",
                                       "/org/mpris/MediaPlayer2")
        remote_object.Pause(
            dbus_interface="org.mpris.MediaPlayer2.Player")

        self.speak_dialog("amarok.pause")

    def stop(self):
        """
        Mycroft Stop Function
        """
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.


def create_skill():
    """
    Mycroft Create Skill Function
    """
    return AmarokSkill()
