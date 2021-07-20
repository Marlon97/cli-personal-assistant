from unittest import TestCase
import cli


class CliTest(TestCase):
    """cli test case"""
    def test_draw_menu_screen(self):
        self.assertEqual(type(cli.drawMenuScreen()), str)

    def test_draw_config_screen(self):
        self.assertEqual(type(cli.drawConfigScreen()), str)

    def test_draw_help_screen(self):
        self.assertEqual(type(cli.drawHelpScreen()), str)
