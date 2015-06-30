#!/usr/bin/env python

import os
from datetime import datetime
from subprocess import Popen

OBFUSCATOR_PROGRAM_PATH = 'pyobfuscate/pyobfuscate'
SOLUTION_MODULE_FILE_NAMES = ['main.py', 'packet_data.py', 'packet_analysis.py']

def ensure_output_directory():
    name = datetime.now().strftime('%d%m%Y_%H%M%S')
    if not os.path.exists(name):
        os.makedirs(name)
        return name
    return None 

def ensure_obfuscator_program():
    if (os.path.isfile(OBFUSCATOR_PROGRAM_PATH) and 
            os.access(OBFUSCATOR_PROGRAM_PATH, os.X_OK)):
        return OBFUSCATOR_PROGRAM_PATH
    return None
        
def ensure_solution_files():
    for file_name in SOLUTION_MODULE_FILE_NAMES:
        if not (os.path.isfile(file_name) and
                os.access(file_name, os.R_OK)):
            return None
    return SOLUTION_MODULE_FILE_NAMES

def obfuscate(obfuscator_program, file_name, output_directory_name):
    output_file_path = os.path.join(output_directory_name, file_name)
    with open(output_file_path, 'w') as output_file:
        process = Popen([obfuscator_program, file_name], stdout=output_file)
        process.wait()


obfuscator_program = ensure_obfuscator_program()
if obfuscator_program is None:
    print 'Coult not ensure obfuscator program (could not find executable)'

solution_files = ensure_solution_files()
if solution_files is None:
    print 'Could not ensure solution files (could not find files to read)'

output_directory_name = ensure_output_directory()
if output_directory_name is None:
    print 'Could not ensure output directory (directory already exists?)'

for file_name in solution_files:
    obfuscate(obfuscator_program, file_name, output_directory_name)
