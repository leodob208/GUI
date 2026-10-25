from pathlib import Path

import cv2


def read_image(filename: str):
    image_path = Path(__file__).resolve().parent / filename
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")
    return image


def main():
    dog = read_image("dog.jpeg")
    dog_gray = cv2.cvtColor(dog, cv2.COLOR_BGR2GRAY)
    flower = read_image("flower.jpeg")

    cv2.imshow("Gray Dog", dog_gray)
    cv2.imshow("Original Image", flower)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
