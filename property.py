import pandas as pd
import pytorch_lightning as pl 
import torch.optim as optim

from time import sleep

class myModel(pl.LightningModule):

	def __init__(self):
		super().__init__()
	
	def training_step(self):
		pass
	
	def validation_step(self, *args, **kwargs):
		return super().validation_step(*args, **kwargs)

	def on_epoch_start(self):
		return super().on_epoch_start()	

	def configure_optimizers(self):
		return optim.Adam(self.parameters(), 0.001)