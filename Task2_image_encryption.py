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
