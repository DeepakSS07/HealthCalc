import os
import shutil
import random

def split_dataset(source_dir, dest_dir, train_split=0.7, val_split=0.15, test_split=0.15):
    """
    Splits the dataset into train, validation, and test sets.

    Parameters:
        source_dir (str): The directory containing all the images.
        dest_dir (str): The directory where the split datasets will be saved.
        train_split (float): Proportion of images to be used for training.
        val_split (float): Proportion of images to be used for validation.
        test_split (float): Proportion of images to be used for testing.
    """
    assert train_split + val_split + test_split == 1, "Splits must sum to 1"

    classes = [d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))]

    for cls in classes:
        class_dir = os.path.join(source_dir, cls)
        images = os.listdir(class_dir)
        random.shuffle(images)
        
        train_size = int(len(images) * train_split)
        val_size = int(len(images) * val_split)
        test_size = len(images) - train_size - val_size

        train_images = images[:train_size]
        val_images = images[train_size:train_size + val_size]
        test_images = images[train_size + val_size:]

        # Create directories for each split
        os.makedirs(os.path.join(dest_dir, 'train', cls), exist_ok=True)
        os.makedirs(os.path.join(dest_dir, 'val', cls), exist_ok=True)
        os.makedirs(os.path.join(dest_dir, 'test', cls), exist_ok=True)

        # Move the images
        for img in train_images:
            shutil.move(os.path.join(class_dir, img), os.path.join(dest_dir, 'train', cls, img))
        
        for img in val_images:
            shutil.move(os.path.join(class_dir, img), os.path.join(dest_dir, 'val', cls, img))
        
        for img in test_images:
            shutil.move(os.path.join(class_dir, img), os.path.join(dest_dir, 'test', cls, img))

    print("Dataset has been split into train, validation, and test sets.")

# Example usage:
source_directory = 'images'  # The directory where the scraped images are stored
destination_directory = 'dataset'  # The directory where the split datasets will be saved

split_dataset(source_directory, destination_directory, train_split=0.7, val_split=0.15, test_split=0.15)
