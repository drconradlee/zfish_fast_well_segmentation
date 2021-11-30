# Fast well segmentation for Zebrafish Behaviour

Module + executable for segmenting wells for further video processing. The aim of the script is to compress raw avi files and crop multi-well videos into single well videos for tracking analysis. The code is optimized for compressing and processing multiple short videos. There is no speed advantage if you are processing a single large video file.

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
    <li> multiprocessing </li>
</ul>
  

<h2> Activating the environment </h2>
If you are running the script through the installed envionemnt, simply activate the environment and set the current directory.
<p> </p>

```
conda activate well_segmentation
```

<h2> Script Inputs </h2>
To run, simply input:
<p> </p>

```
python compress_and_seg.py -d <path_to_folder> -p 5 -min 100 -max 150 -f 2000 -n 16 -t 50
```

where:
<ul>
    <li> <strong> -f : </strong> reference frame </li> 
    <li> <strong> -min: </strong> estimated minimium well diameter in pixel </li> 
    <li> <strong> -max: </strong> estimate maxiumium well diameter in pixel </li> 
    <li> <strong> -d: </strong> directory of avi videos </li>
    <li> <strong> -p: </strong> padding in pixels desired around the well </li>
    <li> <strong> -n: target number of wells </li>
    <li><strong> -t: threshold between rows (important for non-rectalinear arrangement) </li>
</ul>

