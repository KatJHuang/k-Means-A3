import numpy as np
import tensorflow as tf


def loadData():
	data = np.load("data2D.npy")
	return data

def splitData(data):
	train = data[:7000, :]
	validation = data[7000:10000, :]
	return train, validation

data = loadData()
train, validation = splitData(data)


