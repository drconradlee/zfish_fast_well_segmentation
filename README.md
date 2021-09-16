# Fast well segmentation for Zebrafish Behaviour

Module + executable for segmenting wells for further video processing. Script includes compression of raw avi files, video preprocessing, well identification and automated cropping for single well videos. 

<h2> Installation </h2>
You can install all required packages by creating an environment with all dependencies with the included `environment.yml` file.
<p> </p>

```
conda env create -f environment.yml -n well_segmentation
```

<p> </p>
<p> Alternatively, you can install each depedencies individually: </p>
<ul>
    <li> numpy </li> 
    <li> argparse </li> 
    <li> opencv </li> 
    <li> ffmpeg-python </li>
</ul>
  

<h2> Activating the environment </h2>
If running you are script throught installed envionemnt, simply activate the environment
<p> </p>

```
conda activate well_segmentation
```

<h2> Script Inputs </h2>
To run, simply input:
<p> </p>

```
python compress_and_seg.py -p <path_to_folder> -n 16 -f 0.1 -c auto -tt circle -pp <path_to_json_params> 
```

where:
<ul>
    <li> <strong> -n : </strong> number of wells </li> 
    <li> <strong> -min: </strong> estimated minimium well diameter in pixel </li> 
    <li> <strong> -max: </strong> estimate maxiumium well diameter in pixel </li> 
    <li> <strong> -d: </strong> directory of avi videos </li>
    <li> <strong> -p: </strong> padding in pixels desired around the well </li>
</ul>

