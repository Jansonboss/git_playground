import pandas as pd
import pytorch_lightning as pl

class myLogger(pl.LightningModule):
    
    def __init__(self):
        super().__init__()
    
    def loaded_optimizer_states_dict(self) -> dict:
        return super().loaded_optimizer_states_dict
        
    def logger(self):
        return super().logger
    

def main()