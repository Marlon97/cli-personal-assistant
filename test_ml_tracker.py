from unittest import TestCase
import ml_tracker as ml
from dotenv import load_dotenv
import os


class MlTrackerTest(TestCase):
    """ml_tracker test case"""

    def setup_method(self, method=0):
        load_dotenv()
        self.WEB_DRIVER_PATH = os.environ['WEBDRIVERPATH']

    def test_get_item_price(self):
        self.assertGreater(ml.get_item_price('https://www.mercadolibre.com.mx/sony-playstation-5-825gb-standard-color-blanco-y-negro/p/MLM16171888', self.WEB_DRIVER_PATH), 0)

    def test_price_tracker_happy_path(self):
        self.assertEqual(ml.price_tracker('https://www.mercadolibre.com.mx/sony-playstation-5-825gb-standard-color-blanco-y-negro/p/MLM16171888', ">", 1, self.WEB_DRIVER_PATH)[0], True)

    def test_price_tracker_wrong_path(self):
        self.assertEqual(ml.price_tracker('https://www.mercadolibre.com.mx/sony-playstation-5-825gb-standard-color-blanco-y-negro/p/MLM16171888', "<", 1, self.WEB_DRIVER_PATH), False)
