reading & studying: bayes, mathemactical notation, markdown, LaTeX

ansl: overhauling and adapting "aint_no_sound_loud_enough" exp
- adding gui for easy access of runs
- cleaning up and adapting PEP8
- removed unnecessary global declarations
- changed stimuli calls to relative paths and changed folder structure
- exchanged if-statement structure, which previously was used to differ between settings, to function statements
         -> simplifying structure into general function, which simply takes setting as keyword input
- changed range to (0, 14), instead of (0, 13), so that all stimuli are presented
- generating new stimuli (sampling rate 48800, 30dbz and scaled up in 10dbfs steps (as proposed [here](https://forum.audacityteam.org/viewtopic.php?t=2364) and [here](https://www.asha.org/policy/gl2005-00014.htm))
- using[AudioSegment](https://github.com/jiaaro/pydub/blob/master/API.markdown) to scale down amplitude in steps of 10dBFS
- changed [script](https://github.com/M-earnest/audiometry_mri/blob/master/scripts_stimulation/ansl.py) to directly call already created stimuli, instead of using psychopy to scale volume
  -> new scripts:
         - [stimuli creation](https://github.com/M-earnest/audiometry_mri/blob/master/ansl_stimuli_creation.ipynb)
                  - tutorial on how to create stimuli using audacity and how to a number of sounds scaled by specific volume
         - [data cleaning and analysis](https://github.com/M-earnest/audiometry_mri/blob/master/ansl_analysis.ipynb)
                  - basic cleaning and statistical analysis of raw data
                  - plotting for different settings on singlie subject basis
                  - _pending_: analysis of mri-noise
                           -> how to pick specific frequencies from fft output and translate power to dBFS
                  - _pending_: analysis on group level
         - implementing necessary [questionnaires](https://github.com/M-earnest/audiometry_mri/tree/master/questionnaires
           and feedback in psychopy 
- testing first pilot:
         - creation of protocols for mri-sequencies and general testing procedure
         - changing range of stimuli presentation to include silent stimuli at the end/beginning of sequences to allow for
           more reaction time
         - ranomising order of stimuli presentation?


updating distro to 18.04, including complete system overhaul


