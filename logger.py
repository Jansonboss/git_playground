import pandas as pd
import pytorch_lightning as pl
import torch



class myLogger(pl.LightningModule):
    
    def __init__(self):
        super().__init__()
    
    def loaded_optimizer_states_dict(self):
        return super().loaded_optimizer_states_dict
        
    def what_the_heck(self):
        return "nothing is more important than time"

    def training_epoch_end(self, outputs) -> None:
        return super().training_epoch_end(outputs)

    def some_testing_hooks(self):
        for i in range(10):
            print(10)
    
    def training_step(self, *args, **kwargs) -> STEP_OUTPUT:
        return super().training_step(*args, **kwargs)
            
    def validation_epoch_end(self, ouputs) -> None:
        pass
    
    @property
    def configure_optimizers(self) -> None:
        optimizer = torch.optim.Adam(self.parameters(), lr = 0.001)
