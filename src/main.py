from src.customcsv import parse_to_array
from src.task import random_select_sample, extract_sample
from src.classifier import nn


dataset = parse_to_array('iris.data')
sample = random_select_sample(dataset, 80)

extract_sample(sample, dataset)

nn(sample, dataset)