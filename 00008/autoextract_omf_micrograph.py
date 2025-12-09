"""
   Copyright 2025 Samarthya Lykamanuella

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
# Obtaining the OMF file of OOMMF simulations at a specific DataTable coordinate.
# This file is downloaded from https://github.com/nanofisika/kuliah/blob/main/00008.
# Created by Samarthya Lykamanuella (youtube.com/@nanofisika) on 2025-12-09.
# Visit my GitHub page on https://github.com/samarlyka ^^.

import math
import odt2csv
import os
import pandas as pd
import subprocess as sp


def get_closest_item_index(a: pd.DataFrame, b: pd.DataFrame, val_a: float, val_b: float):
    """ Assuming both `a` and `b` dataframes have the same size, returns the index of item
    that corresponds the most to the closest values of `val_a` in `a` and `val_b` in `b`. """
    list_of_differences = []
    for i in range(len(a)):
        diff_a = math.fabs(val_a - a[i])
        diff_b = math.fabs(val_b - b[i])
        diff_sum = diff_a + diff_b  # --- the closest item to some number has the lowest absolute difference.
        list_of_differences.append({'diff_a': diff_a, 'diff_b': diff_b, 'diff_sum': diff_sum, 'index': i})
    
    # Sorted! Return a single value.
    return sorted(list_of_differences, key=lambda c: c['diff_sum'])[0]['index']

def get_all_omf(
    coordinates: list,  # --- must be a list of tuples.
    x_col: str,
    y_col: str,
    omf_dir: str,
    odt_file: str,
    oommf_path: str,
    out_dir: str,
    convert_omf2png: bool=False,
    add_xy_suffix: bool=True,  # --- whether to suffix the output filename with the X-Y coordinate.
    omf2png_config: str='',  # --- the path to the avf2ppm config file.
    odt2csv_parser_behavior: str='new',
    iterator_column: str='Oxs_TimeDriver::Iteration',
):
    print(f'Reading from {odt_file}...')
    print(f'x-Column: {x_col}, y-Column: {y_col}, it-Column: {iterator_column}, odt2csv-parser-behavior: {odt2csv_parser_behavior}')
    
    # Converting ODT to CSV.
    odt2csv.convert(odt_file, parser_behavior=odt2csv_parser_behavior)
    
    # Read the CSV.
    csv_file = odt_file.replace('.odt', '.csv') if odt_file.endswith('.odt') else odt_file + '.csv'
    df = pd.read_csv(csv_file)
    
    # Parsing the columns.
    data_x = df[x_col]
    data_y = df[y_col]
    it = df[iterator_column]
    
    # Parsing the list of OMF files.
    data_omf = [{'it': int(l.replace('.omf', '').split('-')[-1]), 'name': l} for l in os.listdir(omf_dir) if l.endswith('.omf')]
    data_omf_it_only = [l['it'] for l in data_omf]
    
    for i in range(len(coordinates)):
        # The iteration number that matches the current X-Y coordinate.
        coor_x, coor_y = coordinates[i][0], coordinates[i][1]
        name_suffix = f'{coor_x}-{coor_y}'
        id_coord = get_closest_item_index(data_x, data_y, coor_x, coor_y)
        now_it = it[id_coord]
        
        # Get the closest OMF file closest to this iteration number.
        id_omf = get_closest_item_index(data_omf_it_only, data_omf_it_only, now_it, now_it)
        now_omf_filename = data_omf[id_omf]['name']
        
        # Obtain the matching OMF file.
        target_micrograph = omf_dir + os.sep + now_omf_filename
        
        # Copies the OMF file.
        s_n, s_x = os.path.splitext(target_micrograph)
        target_omf_copy_name = f'{os.path.basename(s_n)}_{name_suffix}{s_x}' if add_xy_suffix else f'{s_n}{s_x}'
        target_omf_copy_path = out_dir + os.sep + target_omf_copy_name
        sp.getstatusoutput(f'copy "{target_micrograph}" "{target_omf_copy_path}"')
        
        # Converts OMF to PNG.
        if convert_omf2png:
            # Preparing the OOMMF command.
            # The subprocess command to convert OMF to PNG.
            theconfig = '' if omf2png_config.strip().__len__() == 0 else '-config ' + omf2png_config
            omf2png_command = f'tclsh {oommf_path} avf2ppm -format PNG -f {theconfig} -ipat '
            
            # Converting the OMF file to PNG.
            target_png = target_micrograph[:-3] + 'png' if target_micrograph.endswith('.omf') else target_micrograph + '.png'
            sp.getstatusoutput(omf2png_command + target_micrograph)
            
            # Copies the PNG file.
            s_n, s_x = os.path.splitext(target_png)
            target_png_copy_name = f'{os.path.basename(s_n)}_{name_suffix}{s_x}' if add_xy_suffix else f'{s_n}{s_x}'
            target_png_copy_path = out_dir + os.sep + target_png_copy_name
            sp.getstatusoutput(f'copy "{target_png}" "{target_png_copy_path}"')
        
        # Do the necessary logging.
        print('=' * 25)
        print(f'Coordinate                  ::: {coordinates[i]} {(x_col, y_col)}')
        print(f'Matching Iteration No.      ::: {now_it}')
        print(f'Matching OMF File           ::: {target_micrograph}')
        print(f'OMF File Copied to          ::: {target_omf_copy_path} (Exists? {os.path.exists(target_omf_copy_path)})')
        if convert_omf2png:
            print(f'PNG File Copied to          ::: {target_png_copy_path} (Exists? {os.path.exists(target_png_copy_path)})')


if __name__ == '__main__':
    """ You only ever need to change this section of the script. """
    get_all_omf(
        coordinates=[
            (7.8e-8, 7.8e-8),
            (1.52e-7, 1.52e-7),
        ],
        x_col = 'Oxs_TimeDriver::Simulation time',
        y_col = 'Oxs_TimeDriver::Simulation time',
        omf_dir = r"C:\euphoberia\nife\oommf\02509.00013\run\25nm3",
        odt_file = r"C:\euphoberia\nife\oommf\02509.00013\run\25nm3\sim.odt",
        oommf_path = r"C:\euphoberia\fept\oommf\v2.1a2\oommf.tcl",
        out_dir = r"C:\Users\huskarl\Documents\Temp\waktu",
        convert_omf2png = True,
    )
    
# Good bye
exit()
