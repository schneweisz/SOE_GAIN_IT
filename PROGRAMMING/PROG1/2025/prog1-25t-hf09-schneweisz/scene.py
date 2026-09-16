import os

def load_scene(filename):
    """Loads the script of a scene and returns the speaking order of the characters.

    Args:
        filename (str): Path to a textfile containing the script of a scene.

    Returns:
        A list containing the name of the speaking character for each speech.

    Raises:
        FileNotFoundError: The file was not found.
    """
    names = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                line = line.strip()
                if line.isupper() and (i == 0 or lines[i - 1].strip() == ""):
                    names.append(line)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")
    return names