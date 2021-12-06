# Fast well segmentation for Zebrafish Behaviour

Module + executable for segmenting wells for further video processing. The aim of the script is to compress raw avi files and crop multi-well videos into single well videos for tracking analysis. The code is optimized for compressing and processing multiple short videos. There is no speed advantage if you are processing a single large video file.

<h2> Installation </h2>
You can install all required packages by creating an environment with all dependencies with the included `environment.yml` file.
<p> </p>

```
conda env create -f environment.yml -n well_segmentation
```

<p> </p>
 

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
python compress_and_seg.py -d <path_to_folder> -n 16 
```
If errors are encounters, other input variable are avaliable to fine tune the segmentation.
Where:
<ul>
    <li> <strong> -f : </strong> Reference frame </li> 
    <li> <strong> -min: </strong> Estimated minimium well diameter in pixel </li> 
    <li> <strong> -max: </strong> Estimated maxiumium well diameter in pixel </li> 
    <li> <strong> -d: </strong> Directory of avi videos </li>
    <li> <strong> -p: </strong> Padding in pixels desired around the well </li>
    <li> <strong> -t: </strong> Threshold hold between rows of wells </li>
</ul>

