import numpy as np

def convolve(image, kernel):
    image_height, image_width = image.shape
    kernel_size = kernel.shape[0]
    output_height = image_height - kernel_size + 1
    output_width = image_width - kernel_size + 1

    convolved_image = np.zeros((output_height, output_width), dtype=float)

    for i in range(output_height):
        for j in range(output_width):
            roi = image[i:i+kernel_size, j:j+kernel_size]
            elementwise_mult = np.multiply(roi, kernel)
            convolved_pixel = np.sum(elementwise_mult)
            convolved_image[i, j] = convolved_pixel

    return convolved_image