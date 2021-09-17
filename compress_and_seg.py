# Import packages
import numpy as np
import cv2
import os
import argparse
import ffmpeg
from tqdm import tqdm
import multiprocessing

def run_segmentation(file_list,file_num,all_coord,num_wells):
    for well in np.arange(num_wells[file_num][0]):
        print(f'Running Well: {well+1}')
        try:
            stream = ffmpeg.input(file_list[file_num])
            stream = ffmpeg.filter(stream,'crop',\
                                   str(round(all_coord[file_num][well][0])),\
                                   str(round(all_coord[file_num][well][1])),\
                                   str(round(all_coord[file_num][well][2])),\
                                   str(round(all_coord[file_num][well][3])),\
                                  )
            
            target_dir = os.path.join(os.path.dirname(file_list[file_num]), 'well_videos')
            base_name = os.path.splitext(os.path.basename(file_list[file_num]))[0]
            target_file = os.path.join(target_dir,base_name + '_well_' + str(well+1) + '.avi')

            stream = ffmpeg.output(stream, target_file, **{'c:v': 'libx264rgb'},\
                                  preset='medium', crf=12, f='avi')
            stream = ffmpeg.overwrite_output(stream)
            ffmpeg.run(stream,capture_stdout=True, capture_stderr=True)
        except ffmpeg.Error as e:
            print('stdout:', e.stdout.decode('utf8'))
            print('stderr:', e.stderr.decode('utf8'))
            raise e

# Main script    
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
                    default=20)
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
    ARGS = vars(AP.parse_args())
    directory = ARGS['folder_path']
    min_pad = int(ARGS['padding'])
    min_well = int(ARGS['min_well_size'])
    max_well = int(ARGS['max_well_size'])
    examine_frame = int(ARGS['sample_frame'])

    # Run through the folder and get all the avi names
    file_list = [];
    for filename in os.listdir(directory):
        if filename.endswith(".avi"): 
            file_list.append(os.path.join(directory, filename))
            continue
        else:
            continue

    print('Total AVI Files: ' + str(np.shape(file_list)[0]))

    # Go thru each avi and define the video boundaries
    num_wells = []
    all_coord =[]
    for video in np.arange(np.shape(file_list)[0]):
        cap = cv2.VideoCapture(file_list[video])
        cap.set(1,examine_frame)
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                param1=50,param2=30,minRadius=min_well,maxRadius=max_well)
        circles = np.uint16(np.around(circles))
        num_wells.append(np.shape(circles[0,:,0]))

        print('Number of wells detected: ' + str(num_wells[video][0]))

        for i in circles[0,:]:
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)    
        img_out_name = os.path.splitext(file_list[video])[0] + '_well_detection.jpg'
        cv2.imwrite(img_out_name, frame)

        coord_lines = np.zeros((num_wells[video][0],4))
        for well in range(num_wells[video][0]):
            coord_lines[well][0] = (max(circles[0][:,2])+min_pad)*2
            coord_lines[well][1] = (max(circles[0][:,2])+min_pad)*2
            coord_lines[well][2] = circles[0][well][0]-(max(circles[0][:,2])+min_pad)
            coord_lines[well][3] = circles[0][well][1]-(max(circles[0][:,2])+min_pad)   

        all_coord.append(coord_lines)

    # Segment Wells and export as avi

    target_dir = os.path.join(os.path.dirname(file_list[0]), 'well_videos')
    os.mkdir(target_dir)

    jobs = []
    for file_num in tqdm(np.arange(np.shape(all_coord)[0])):
        p = multiprocessing.Process(target=run_segmentation, args=(file_list,file_num,all_coord,num_wells))
        jobs.append(p)
        p.start()