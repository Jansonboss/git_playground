import pandas as pd
import pytorch_lightning as pl

class myLogger(pl.LightningModule):
    
    def __init__(self):
        super().__init__()
    
    def loaded_optimizer_states_dict(self):
        return super().loaded_optimizer_states_dict
        
    def what_the_heck(self):
        return "nothing is more important than time"

def main()