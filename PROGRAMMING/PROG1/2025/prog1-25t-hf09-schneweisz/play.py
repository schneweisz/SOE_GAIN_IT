import os
from scene import load_scene

def load_play(directory):
    """Loads the scenes of a play from the given directory.

    Args:
        directory: Path to the directory which contains the scenes.

    Returns:
        A dict where the keys are the scene names (filename without ext.), values are
        lists containing the names of the speaking characters.

    Raises:
        FileNotFoundError: The directory was not found. 
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' was not found.")
    
    play = {}
    for filename in os.listdir(directory):
        parts = filename.split(".")
        if parts[-1] == "txt":
            scene = parts[0]
            scene_path = os.path.join(directory, filename)
            play[scene] = load_scene(scene_path)
    return play


def get_speech_count(play):
    """Counts the total number of speeches in all scenes of a play.

    Args:
        play: Scene names and character names.

    Returns:
        The total number of speeches.
    """
    return sum(len(names) for names in play.values())