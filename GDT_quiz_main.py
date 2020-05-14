from pathlib import Path
import os

working_directory = Path.cwd()

gdt_flatness = {'name':'flatness',
                'image_file_name': 'flatness.png',
                'Type_of_tolerance': 'Form',
                'datum_required': "No"}

gdt_straightness = {'name':'straightness',
                'image_file_name': 'straightness.png',
                'Type_of_tolerance': 'Form',
                'datum_required': "No"}

print('done')