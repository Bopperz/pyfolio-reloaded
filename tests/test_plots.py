# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 07:55:00 2024

@author: james
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from pyfolio_reloaded.src import pyfolio as pf
import unittest
from unittest.mock import MagicMock, Mock, call

def main():
    unittest.main()

class Testpyfolio_reloaded(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        
        FILE = 'backtest_data.xlsx'
        
        mod_path = Path(__file__).parent
        file_path = (mod_path / 'test_data/' / FILE).resolve()
        
        cls.df = pd.read_excel(file_path, sheet_name=['returns', 'positions', 'transactions', 'gross_lev'], index_col=0)
        cls.returns = cls.df['returns'].squeeze()
        cls.positions = cls.df['positions']
        cls.transactions = cls.df['transactions']
        cls.gross_lev = cls.df['gross_lev']
        
    def setUp(self):
        pass
    
    def show_image(self, picture):
        #work around as images dont show in spyder
        from PIL import Image
        import datetime as dt

        filename = r'C:\tmp\backtrader_results_' + dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        picture.savefig(fname=filename, dpi=200)
        Image.open(filename+'.png').show()
    
    def test_create_full_tear_sheet(self):
        
        fig = pf.create_full_tear_sheet(returns=self.returns,
                                        positions=self.positions,
                                        transactions=self.transactions,
                                        estimate_intraday=False,
                                        set_context=False,
                                        )

    def test_create_simple_tear_sheet(self):
        
        fig = pf.create_simple_tear_sheet(returns=self.returns,
                                          positions=self.positions,
                                          transactions=self.transactions,
                                          estimate_intraday=False,
                                          set_context=False,
                                          )
        
    def test_create_returns_tear_sheet(self):
        
        fig = pf.create_returns_tear_sheet(returns=self.returns,
                                            positions=self.positions,
                                            transactions=self.transactions,
                                            return_fig=False,
                                            )


if __name__ == '__main__':
    unittest.main()