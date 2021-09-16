# Fast Well segmentation for zebrafish behaviour

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
    <b>
    <li> openCV </li> 
    <li> argparse </li> 
    <li> numpy </li> 
    <li> ffmpeg-python </li>
    </b>
</ul>
  

<h2> Activating environment </h2>
If running you are script throught installed envionemnt, simply activate the environment
<p> </p>

```
conda activate well_segmentation
```

<h2> Script Inputs </h2>
To run, simply input:
```
python compress_and_seg.py -p <path_to_folder> -n 16 -f 0.1 -c auto -tt circle -pp <path_to_json_params> 
```
where:
<ul>
    <b>
    <li> openCV </li> 
    <li> argparse </li> 
    <li> numpy </li> 
    <li> ffmpeg-python </li>
    </b>
</ul>

