import wget
import os
import scipy.io
import numpy as np


def my_srgb_denoiser(x):
    """TODO: Implement your own sRGB denoiser here."""
    return x.copy()


# Download input file, if needed.
url = 'https://competitions.codalab.org/my/datasets/download/0d8a1e68-155d-4301-a8cd-9b829030d719'
input_file = 'BenchmarkNoisyBlocksSrgb.mat'
if os.path.exists(input_file):
    print(f'{input_file} exists. No need to download it.')
else:
    print('Downloading input file BenchmarkNoisyBlocksSrgb.mat...')
    wget.download(url, input_file)
    print('Downloaded successfully.')

# Read inputs.
key = 'BenchmarkNoisyBlocksSrgb'
inputs = scipy.io.loadmat(input_file)
inputs = inputs[key]
print(f'inputs.shape = {inputs.shape}')

# Denoising.
outputs = inputs.copy()
for i in range(inputs.shape[0]):
    for j in range(inputs.shape[1]):
        outputs[i, j, :, :, :] = my_srgb_denoiser(inputs[i, j, :, :, :])
print(f'outputs.shape = {outputs.shape}')

# Save outputs to .mat file.
output_file = 'SubmitSrgb.mat'
print(f'Saving outputs to {output_file}')
scipy.io.savemat(output_file, {'SubmitSrgb': outputs})

# TODO: Submit the output file SubmitSrgb.mat at 
# http://130.63.97.225/sidd/benchmark_submit.php

print('Done.')