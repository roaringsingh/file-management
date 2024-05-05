import os
from moviepy.editor import VideoFileClip

def convert_mov_to_mp4(input_file, output_folder):
  """
  Converts a single .mov file to .mp4

  Args:
      input_file (str): Path to the input .mov file
      output_folder (str): Path to the output folder
  """
  filename = os.path.splitext(os.path.basename(input_file))[0]
  output_path = os.path.join(output_folder, filename + ".mp4")

  try:
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_path)
    print(f"Converted {input_file} to {output_path}")
  except Exception as e:
    print(f"Error converting {input_file}: {e}")

def convert_all_mov_in_dir(directory, output_folder):
  """
  Loops through a directory and converts all .mov files to .mp4

  Args:
      directory (str): Path to the directory containing .mov files
      output_folder (str): Path to the output folder
  """
  for filename in os.listdir(directory):
    if filename.endswith(".mov") or filename.endswith(".MOV"):
      input_file = os.path.join(directory, filename)
      convert_mov_to_mp4(input_file, output_folder)

if __name__ == "__main__":
  # Replace with your directory path containing .mov files
  directory = "/mnt/roaringsingh/Entertainment/Personal/Test"

  # Replace with your desired output folder
  output_folder = "/mnt/roaringsingh/Entertainment/Personal/test-converted"

  convert_all_mov_in_dir(directory, output_folder)

