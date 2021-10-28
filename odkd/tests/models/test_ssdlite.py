import torch
from odkd.models.ssdlite import (
    Detect,
    ssd_lite
)


def test_detect(config, priors, localization, confidence):
    detect = Detect(config, priors)
    output = detect(localization, confidence)
    print(output.shape)
    assert output.shape == torch.Size(
        [config['batch_size'], config['num_classes'], config['topK'], 5])


def test_vgg16_ssdlite(config, input_tensor, priors, localization, confidence):
    ssdlite = ssd_lite('vgg16', config)
    test_localization, test_confidence, test_priors = ssdlite(input_tensor)
    print(test_localization.shape, test_confidence.shape, test_priors.shape)
    assert test_localization.shape == localization.shape
    assert test_confidence.shape == confidence.shape
    assert test_priors.shape == priors.shape


def test_mobilenetv2_ssdlite(config, input_tensor, priors, localization, confidence):
    ssdlite = ssd_lite('mobilenetv2', config)
    test_localization, test_confidence, test_priors = ssdlite(input_tensor)
    print(test_localization.shape, test_confidence.shape, test_priors.shape)
    assert test_localization.shape == localization.shape
    assert test_confidence.shape == confidence.shape
    assert test_priors.shape == priors.shape
