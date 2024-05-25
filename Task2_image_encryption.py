from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size # image size
    
    encrypted_pixels = []     # encrypt image pixel using XOR with the key
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple((pixel[i] ^ key[i % len(key)]) for i in range(3))
            encrypted_pixels.append(encrypted_pixel)
        #   print(f"Pixel at ({x}, {y}): {encrypted_pixel}") for print the pixel values
    
    # encrypted image
    encrypted_img = Image.new("RGB", (width, height))
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.jpg")
    print("Image encrypted successfully.")

def decrypt_image(encrypted_image_path, key, original_key): # check the provided key for decryption
    if key != original_key:
        print("Incorrect key! Unable to decrypt the image.")
        return False
    
    encrypted_img = Image.open(encrypted_image_path) # take the encrypted image for decryption
    width, height = encrypted_img.size
    
    decrypted_pixels = [] # decrypt image pixel using XOR with the same key which is used for encryption
    for y in range(height):
        for x in range(width):
            pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = tuple((pixel[i] ^ key[i % len(key)]) for i in range(3))
            decrypted_pixels.append(decrypted_pixel)
    # decrypted image
    decrypted_img = Image.new("RGB", (width, height))
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted_image.jpg")
    print("Image decrypted successfully.")
    return True

def main():
    print("Image Encryption and Decryption")
    image_path = input("Enter the path to the image file: ")
    key = tuple(map(int, input("Enter a key (3 integers separated by space): ").split())) # input the encryption key
    encrypt_image(image_path, key) #encrypt
    max_attempts = 3
    attempts = 0
    print("only 3 attempt is there for decrypt the image")
    while attempts < max_attempts:
        key_decrypt = tuple(map(int, input(f"Enter the key for decryption (3 integers separated by space) - Attempt {attempts + 1}/{max_attempts}: ").split()))
        if decrypt_image("encrypted_image.jpg", key_decrypt, key):
            break
        attempts += 1
        if attempts < max_attempts:
            print(f"Incorrect key. You have {max_attempts - attempts} attempt(s) left.")
        else:
            print("Maximum attempts reached. Unable to decrypt the image.")

if __name__ == "__main__":
    main()






"""
from PIL import Image
import numpy as np

def generate_random_image(image_shape, random_image_path):
    # Generate a random image with the same shape as the original image
    random_image_array = np.random.randint(0, 256, size=image_shape, dtype=np.uint8)
    random_image = Image.fromarray(random_image_array)
    random_image.save(random_image_path)
    print("Random image generated and saved.")

def encrypt_image(image_path, random_image_path, encrypted_image_path, key_value):
    # Open the original image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Open the random image
    random_img = Image.open(random_image_path)
    random_array = np.array(random_img)

    # Generate a key from the user input value
    key = np.full(img_array.shape, key_value, dtype=np.uint8)

    # Encrypt each pixel using XOR with the key and the random image
    encrypted_array = np.bitwise_xor(img_array, key ^ random_array)
    
    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save(encrypted_image_path)
    print("Image encrypted successfully.")

def decrypt_image(encrypted_image_path, random_image_path, decrypted_image_path, key_value):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_img)
    
    # Open the random image
    random_img = Image.open(random_image_path)
    random_array = np.array(random_img)

    # Generate a key from the user input value
    key = np.full(encrypted_array.shape, key_value, dtype=np.uint8)

    # Decrypt each pixel using XOR with the key and the random image
    decrypted_array = np.bitwise_xor(encrypted_array, key ^ random_array)
    
    # Convert the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_img.save(decrypted_image_path)
    print("Image decrypted successfully.")

def main():
    print("Image Encryption and Decryption using a Random Image and XOR")

    # Input the image path for encryption
    image_path = input("Enter the path to the image file: ")
    
    # Generate a random image with the same dimensions as the input image
    img = Image.open(image_path)
    random_image_path = "random_image.png"
    generate_random_image(np.array(img).shape, random_image_path)
    
    # Input the key value for encryption
    key_value_encrypt = int(input("Enter an integer key value for encryption (0-255): "))
    
    # Encrypt the image using the random image and the key value
    encrypted_image_path = "encrypted_image.png"
    encrypt_image(image_path, random_image_path, encrypted_image_path, key_value_encrypt)
    
    # Input the key value for decryption
    key_value_decrypt = int(input("Enter an integer key value for decryption (0-255): "))
    
    # Decrypt the image using the random image and the key value
    decrypted_image_path = "decrypted_image.png"
    decrypt_image(encrypted_image_path, random_image_path, decrypted_image_path, key_value_decrypt)

if __name__ == "__main__":
    main()
"""
"""
from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Get image size
    width, height = img.size
    
    # Encrypt each pixel using XOR with the key
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple((pixel[i] ^ key[i % len(key)]) for i in range(3))
            encrypted_pixels.append(encrypted_pixel)
        #   print(f"Pixel at ({x}, {y}): {encrypted_pixel}") for print the pixel values
    
    # Create a new image with the same size
    encrypted_img = Image.new("RGB", (width, height))
    encrypted_img.putdata(encrypted_pixels)
    
    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(encrypted_image_path, key, original_key):
    # Check if the provided key matches the original key
    if key != original_key:
        print("Incorrect key! Unable to decrypt the image.")
        return False

    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Get image size
    width, height = encrypted_img.size
    
    # Decrypt each pixel using XOR with the key
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = tuple((pixel[i] ^ key[i % len(key)]) for i in range(3))
            decrypted_pixels.append(decrypted_pixel)
    
    # Create a new image with the same size
    decrypted_img = Image.new("RGB", (width, height))
    decrypted_img.putdata(decrypted_pixels)
    
    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")
    return True

def main():
    print("Image Encryption and Decryption Tool")
    
    # Input the image path
    image_path = input("Enter the path to the image file: ")
    
    # Input the encryption key
    key = tuple(map(int, input("Enter a key (3 integers separated by space): ").split()))
    
    # Encrypt the image
    encrypt_image(image_path, key)
    
    # Allow the user up to 3 attempts to provide the correct decryption key
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        key_decrypt = tuple(map(int, input(f"Enter the key for decryption (3 integers separated by space) - Attempt {attempts + 1}/{max_attempts}: ").split()))
        if decrypt_image("encrypted_image.png", key_decrypt, key):
            break
        attempts += 1
        if attempts < max_attempts:
            print(f"Incorrect key. You have {max_attempts - attempts} attempt(s) left.")
        else:
            print("Maximum attempts reached. Unable to decrypt the image.")

if __name__ == "__main__":
    main()
"""
