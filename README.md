# Midi Rhythm Generator

A project for converting 3D `.pdb` files into `.mid` files.

## Project Initialization:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the necessary dependencies by running:
   `pip install -r requirements.txt`

## Instructions:

1. Go to [HMDB](https://hmdb.ca/) (or any database that includes 3D PDB data).
2. Search for a metabolite (drug, hormone, protein, etc.).
3. Click on the metabolite, scroll down to the Structure section, and click "3D PDB".
4. Click "Download".
5. Put the `.pdb` file in the root directory of this project.
6. Run `python generate_pdb.py`, and the script will convert the `.pdb` file(s) into `.mid` file(s) with the same name.
