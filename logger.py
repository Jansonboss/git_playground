import pandas as pd
import pytorch_lightning as pl

class myLogger(pl.LightningModule):
    
    def __init__(self):
        super().__init__()
        
    def logger(self):
        return super().logger