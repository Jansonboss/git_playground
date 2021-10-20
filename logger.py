import pandas as pd
import pytorch_lightning as pl

class myLogger(pl.LightningModule):
    
    def __init__(self):
        super().__init__()
    
    def loaded_optimizer_states_dict(self):
        return super().loaded_optimizer_states_dict
        
    def mylogger(self):
        from time import sleep
        for i in range(10): print(10)
        return super().logger
    

def main()