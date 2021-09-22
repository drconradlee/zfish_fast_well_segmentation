# Import packages
import numpy as np
import os
import argparse
import multiprocessing
from ffmpeg_seg_comp import run_segmentation
from detect_and_export import detect_and_export

if __name__ == '__main__':
    # configure argument parser
    AP = argparse.ArgumentParser()
    AP.add_argument("-d",
                    "--folder_path",
                    required=True,
                    help="Folder path where the raw videos are located")
    AP.add_argument("-p",
                    "--padding",
                    required=True,
                    help="Pixel padding value",
                    default=5)
    AP.add_argument("-min",
                    "--min_well_size",
                    required=True,
                    help="Minimium well radius size in pixel",
                    default=100)
    AP.add_argument("-max",
                    "--max_well_size",
                    required=True,
                    help="Maximum well radius size in pixel",
                    default=150)
    AP.add_argument("-f",
                    "--sample_frame",
                    required=True,
                    help="Select sample frame",
                    default=2000)
    AP.add_argument("-n",
                    "--target_num_wells",
                    required=True,
                    help='Expected Number of wells',
                    default = 16)                                        
    ARGS = vars(AP.parse_args())
    directory = ARGS['folder_path']
    min_pad = int(ARGS['padding'])
    min_well = int(ARGS['min_well_size'])
    max_well = int(ARGS['max_well_size'])
    examine_frame = int(ARGS['sample_frame'])
    target_num_well = int(ARGS['target_num_wells'])

    # Run through the folder and get all the avi names
    file_list = [];
    for filename in os.listdir(directory):
        if filename.endswith(".avi"): 
            file_list.append(os.path.join(directory, filename))
            continue
        else:
            continue
    
    print(' ')
    print('Total AVI Files: ' + str(np.shape(file_list)[0]))
    print('###############################################')
    print(' ')
    print('Detecting Wells...')
    print('-----------------------------------------------')
    num_wells,all_coord = detect_and_export(file_list,examine_frame,min_well,max_well,min_pad,target_num_well)
    print(' ')
    print('CHECK WELL-DETECTION OUTPUT TO COMFIRM')
    print('###############################################')
    print(' ')
    print('Writing AVI Files...')
    print('-----------------------------------------------')

    # Segment Wells and export as avi
    target_dir = os.path.join(os.path.dirname(file_list[0]), 'well_videos')
    os.mkdir(target_dir)
    
    jobs = []    
    for file_num in np.arange(np.shape(all_coord)[0]):
        p = multiprocessing.Process(target=run_segmentation, args=(file_list,file_num,all_coord,num_wells))
        jobs.append(p)
        p.start()
    
        