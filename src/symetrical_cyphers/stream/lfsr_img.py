from src.symetrical_cyphers.stream.lfsr import Lfsr
from PIL import Image
import numpy as np


class LfsrImg(Lfsr):
    def __init__(self, register, taps):
        super().__init__(register, taps)

    def generate_static_key(self, length):
        num = 0
        for _ in range(length):
            num *= 2
            num += self._generate_key_bit()
        return num

    def encrypt_color(self, color):
        key = self.generate_static_key(8)
        encrypted_color = color ^ key
        return encrypted_color

    def encrypt_pixel(self, img_from_array, x, y):
        R = img_from_array.getpixel((x, y))[0]
        G = img_from_array.getpixel((x, y))[1]
        B = img_from_array.getpixel((x, y))[2]

        newR = self.encrypt_color(R)
        newG = self.encrypt_color(G)
        newB = self.encrypt_color(B)
        return (newR, newG, newB)

    def encrypt_image(self, img, img_from_array):
        self.register = self.origin.copy()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                new_pixel = self.encrypt_pixel(img_from_array, x, y)
                img.putpixel((x, y), new_pixel)
        return img

    def decrypt_image(self, img, img_from_array):
        return self.encrypt_image(img, img_from_array)


if __name__ == '__main__':

    register = LfsrImg(register=[0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0,
                    1, 0, 0, 0, 1, 0, 0, 0, 0], taps=[16, 2])

    with Image.open('src/symetrical_cyphers/stream/images/secret.png').convert("RGB") as image:
        image.load()
    image_from_array = Image.fromarray(np.asarray(image), mode="RGB")
    register.encrypt_image(image, image_from_array)
    image.save('src/symetrical_cyphers/stream/images/encrypted_secret.png')

    with Image.open('src/symetrical_cyphers/stream/images/encrypted_secret.png').convert("RGB") as encrypted_image:
        encrypted_image.load()
    encrypted_image_from_array = Image.fromarray(
        np.asarray(encrypted_image), mode="RGB")
    register.encrypt_image(encrypted_image, encrypted_image_from_array)
    encrypted_image.save('src/symetrical_cyphers/stream/images/decrypted_secret.png')
