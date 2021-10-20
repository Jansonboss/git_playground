import pandas as pd
from time import sleep
import pytorch_lightning as pl 

class myModel(pl.LightningModule):

	def __init__(self):
		super().__init__()
	
	def training_step(self):
		pass

	def validation_step(self, *args, **kwargs) -> Optional[STEP_OUTPUT]:
		pass