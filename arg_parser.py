import argparse

def add_model_specific_args(self):
	parser = argparse.ArgumentParser(description='VAE MNIST Example')
	parser.add_argument('--batch-size', type=int, default=128, metavar='N',
						help='input batch size for training (default: 128)')
	parser.add_argument('--epochs', type=int, default=10, metavar='N',
						help='number of epochs to train (default: 10)')
	parser.add_argument('--quick-test', type=bool, default=False,
						help='tried compiling your stupid code (default False)')
	self.args = parser.parse_args()
	