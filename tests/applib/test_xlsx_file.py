import unittest
from applib.xlsx_file import XlsxFile
import logging
import os



class TestXlsxFile(unittest.TestCase):
    def test_add_row(self):
        filepath = 'test.xlsx'

        data = {
            'sku': '1023203', 
            'item': "NRM Peck'n'Lay Pellets 20kg", 
            'description': 'Key features\nPeck‘n’Lay® is specifically formulated with quality ingredients, balanced amino acids, energy, and calcium for good egg production and shell quality.\nNatural pigments from paprika and marigold are included to enhance yolk colour.\nEssential oils and organic acids aid in protecting against gut pathogens.\n  Feeding recommendation\n  Introduce Peck‘n’Lay® from approximately 1 week before the onset of lay, typically around 16 weeks of age. Allow ad-lib access to NRM Peck’n’Lay®. Hens can be expected to consume around 125 – 130g (approximately one cup or a good handful) per hen per day. If birds are given access to feeds other than Peck‘n’Lay®, provide ad-lib access to oyster shell grit to ensure good shell quality.\nAlways ensure birds have access to fresh, clean water\n  Ingredients selected from\n  Grain and grain by-products, plant proteins, vegetable oils, animal fats, enzymes, amino acids, limestone, mono or di-calcium phosphate, salt, sodium bicarbonate, vitamins and trace minerals, organic acids and plant extracts, and natural pigments.\n  Typical analysis (approximate on an as fed basis)\n  Crude Protein\n16.50%\nAvailable Lysine\n6.7g/kg (min)\nCalcium\n3.80%\n  Storage\n  Please ensure the product is stored in a cool, dry, and vermin-free environment.\nCaution: Do not feed any animal species other than those stipulated on the label.\n   ', 
            'size': 'Gross Width: 545mm Gross Depth: 315mm Gross Height: 155mm', 
            'weight': 'Net Weight: 20.0kg', 
            'rrp': '$33.90', 
            'discount_price': '$25.11', 
            'promotion_price': '$30.12',
        }

        logger = logging.getLogger(__name__)
        file = XlsxFile(filepath=filepath, logger=logger)
        file.add_row(data=data)
        lines = file.rows()
        self.assertTupleEqual(lines[0], tuple(data.keys()))
        self.assertTupleEqual(lines[1], tuple(data.values()))

        if os.path.exists(filepath):
            os.remove(filepath)

