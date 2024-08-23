# FlashLearn

FlashLearn is a flashcard application designed to help users learn French vocabulary. The app displays flashcards with Fench words and their English translations on the back, allowing users to test their knowledge.

## Features

- **Flashcards**: Display French words and their English translations.
- **Word Removal**: Mark words as learned and remove them from the word list.
- **Random Word Selection**: Pick a random word from the list each time a new word is requested.

## Requirements

- Python 3.x
- `customtkinter`
- `pyglet`
- `Pillow`
- `pandas`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Abtin0/FlashLearn.git
    ```

2. Navigate to the project directory:
    ```bash
    cd FlashLearn
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```


## Usage


1. Run the application
    ```bash
    python main.py
    ```

2. The application window will open. Use the buttons to interact with the flashcards:
    - **Show Back**: Flip the card to show the French word.
    - **Correct**: Mark the current word as learned and remove it from the list.
    - **Wrong**: Show a new word.

## Customization

- **Fonts**: The application uses the `Giphurs ExtraBlack` font. You can change the font by replacing the font file, and changing the file name in `main.py`.

## Acknowledgements

- [CustomTkinter](https://github.com/peperka/customtkinter) for Tkinter widgets.
- [Pyglet](https://pyglet.org/) for font handling.
- [Pillow](https://pillow.readthedocs.io/en/stable/) for image processing.
- [Pandas](https://pandas.pydata.org/) for data handling.

