# Noise-image-generator
Simple tool to generate noise images that can be used for testing image-based AI or anything else. 

## Background

There are some Advantages of Testing an image-absed AI with with Noise-Only Images:

- **Classification Separation Assessment:** If the model makes reliable predictions on noise images, it could indicate that it is not effectively separating classes and may yield false positives. This draws attention to possible weaknesses in the model architecture or training dataset.

- **Model Robustness:** Testing with images that consist only of noise can help determine how robust the model is against non-informative data. A well-trained model should be able to distinguish between noise and actual objects. If the model makes incorrect predictions on such images, it may indicate potential overfitting or inadequate generalization.

- **Threshold Development:** Such tests can help in defining thresholds and confidence criteria. If a model performs well in detecting objects but fails to make reliable predictions with noise-only images, it can help in determining when an object should be regarded as detected.

- **Evaluation of Preprocessing Techniques:** You can also assess how well preprocessing and augmentation techniques support the model. 

## Features

The Code generates and saves monochrome, RGB, multi and hyperpsectral images including the following features:

- Setting width, height and nummber of channels / bands.
- Setting number of images to generate
- Setting destination for saing the images
- Saving the images as numpy arraytogether with the resulting PNG / TIFF file 

## Installation

1. Clone the repository or just donload the nig.py file.
2. Execute the nig.py file in a terminal:
 ```bash
python nig.py
