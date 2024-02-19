import argparse
import cv2
from pathlib import Path
from matplotlib import pyplot as plt
from typing import Union

class BoundingBoxVisualiser:
    """Class for visualising bounding boxes on images."""

    def __init__(self, image_path: Union[str, Path], label_path: Union[str, Path]):
        """
        Initialises the BoundingBoxVisualiser with the specified image and label paths.

        Args:
            image_path: The path to the image file.
            label_path: The path to the label file.
        """
        self.image_path = Path(image_path)
        self.label_path = Path(label_path)
        self.image = cv2.imread(str(self.image_path))
        if self.image is None:
            raise ValueError("Image could not be loaded. Please check the image path.")

    def draw_bounding_boxes(self) -> None:
        """Draws bounding boxes on the image based on the label file."""
        height, width, _ = self.image.shape

        with open(self.label_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            class_id, x_centre, y_centre, bbox_width, bbox_height = map(float, line.split())

            # Convert from relative to absolute coordinates
            x_centre, bbox_width = x_centre * width, bbox_width * width
            y_centre, bbox_height = y_centre * height, bbox_height * height

            # Calculate the top left corner
            x1, y1 = int(x_centre - bbox_width / 2), int(y_centre - bbox_height / 2)
            x2, y2 = int(x_centre + bbox_width / 2), int(y_centre + bbox_height / 2)

            # Draw the rectangle
            cv2.rectangle(self.image, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Blue rectangle with thickness 2

    def save_or_display_image(self, output_path: Union[str, Path], save: bool) -> None:
        """
        Saves or displays the image based on the user's preference.

        Args:
            output_path: The path where the image with drawn bounding boxes should be saved.
            save: A boolean indicating whether to save the image or display it.
        """
        if save:
            cv2.imwrite(str(output_path), self.image)
            print(f"Image saved to {output_path}")
        else:
            plt.imshow(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Visualise bounding boxes on images.')
    parser.add_argument('--image', help='The path to the image file.', required=True)
    parser.add_argument('--label', help='The path to the label file.', required=True)
    parser.add_argument('--output', help='The path where the image should be saved.', default='visualised_image.jpg')
    parser.add_argument('--save', action='store_true', help='Flag whether to save the image instead of displaying it.')

    args = parser.parse_args()

    visualiser = BoundingBoxVisualiser(args.image, args.label)
    visualiser.draw_bounding_boxes()
    visualiser.save_or_display_image(args.output, args.save)

"""
useage:

cd src

python visualize_bounding_boxes.py --image '../dataset_aug/train/images/9e36a476d14b2da360817b7d6724f074_jpg.rf.0467ca3c155d09a019303adae6eb8265_aug_12.jpg' --label '../dataset_aug/train/labels/9e36a476d14b2da360817b7d6724f074_jpg.rf.0467ca3c155d09a019303adae6eb8265_aug_12.txt'

"""
