import wget
import os
import scipy.io
import numpy as np


def my_raw_denoiser(x):
    """TODO: Implement your own raw-RGB denoiser here."""
    return x.copy()


# Download input file, if needed.
url = 'https://competitions.codalab.org/my/datasets/download/7a9badd9-fffc-4e56-ba41-0c5e2a76e58a'
input_file = 'BenchmarkNoisyBlocksRaw.mat'
if os.path.exists(input_file):
    print(f'{input_file} exists. No need to download it.')
else:
    print('Downloading input file BenchmarkNoisyBlocksRaw.mat...')
    wget.download(url, input_file)
    print('Downloaded successfully.')

# Read inputs.
key = 'BenchmarkNoisyBlocksRaw'
inputs = scipy.io.loadmat(input_file)
inputs = inputs[key]
print(f'inputs.shape = {inputs.shape}')

# Denoising.
outputs = inputs.copy()
for i in range(inputs.shape[0]):
    for j in range(inputs.shape[1]):
        outputs[i, j, :, :] = my_raw_denoiser(inputs[i, j, :, :])
print(f'outputs.shape = {outputs.shape}')

# Save outputs to .mat file.
output_file = 'SubmitRaw.mat'
print(f'Saving outputs to {output_file}')
scipy.io.savemat(output_file, {'SubmitRaw': outputs})

# TODO: Submit the output file SubmitRaw.mat at 
# http://130.63.97.225/sidd/benchmark_submit.php

print('Done.')