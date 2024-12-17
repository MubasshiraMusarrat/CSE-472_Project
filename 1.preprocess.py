import os
import csv
import random

# Define the path to the main folder containing the subfolders
main_folder = 'bdsl_data'

# Define the name of the CSV file where the data will be saved
csv_filename = 'video_paths_labels_with_train_test.csv'

# Initialize lists to hold train and test videos
train_videos = []
test_videos = []

# Loop through each subfolder in the main folder to collect video information
for label in os.listdir(main_folder):
    # Create the full path to the subfolder
    folder_path = os.path.join(main_folder, label)

    # Check if the path is indeed a directory
    if os.path.isdir(folder_path):
        label_videos = []
        # Loop through each file in the subfolder
        for video_name in os.listdir(folder_path):
            # Create the full path to the video
            video_path = os.path.join(folder_path, video_name)
            # Append video information to the label-specific list
            label_videos.append([video_path, video_name, label])

        # Shuffle the list for the current label to randomize the order of videos
        random.shuffle(label_videos)

        # Calculate the split index for an 80/20 distribution for the current label
        split_index = int(len(label_videos) * 0.8)

        # Split the videos into train and test for the current label
        train_videos_label = label_videos[:split_index]
        test_videos_label = label_videos[split_index:]

        # Append the split videos into the main train and test lists
        train_videos.extend(train_videos_label)
        test_videos.extend(test_videos_label)

# Open the CSV file in write mode
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # Write the header row
    csvwriter.writerow(['Video Path', 'Video Name', 'Label', 'Type'])

    # Write train videos with 'train' label
    for video in train_videos:
        csvwriter.writerow(video + ['train'])

    # Write test videos with 'test' label
    for video in test_videos:
        csvwriter.writerow(video + ['test'])

print(f"CSV file '{csv_filename}' has been created with video paths, labels, and train/test designation.")
