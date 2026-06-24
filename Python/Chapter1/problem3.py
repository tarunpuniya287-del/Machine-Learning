import os

def list_directory_contents(directory_path):
  directory_path = 'Desktop'
  """
  Prints the contents of a given directory.

  Args:
    directory_path: The path to the directory.
  """
  try:
    for filename in os.listdir("/"):
      file_path = os.path.join(directory_path, filename)
      print(filename)
  except FileNotFoundError:
    print(f"Directory '{directory_path}' not found.")

if __name__ == "__main__":
  directory_to_list = input("Enter the directory path: ")
  list_directory_contents(directory_to_list)