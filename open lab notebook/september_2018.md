reading & studying: bayes, mathemactical notation

ansl: overhauling and adapting "aint_no_sound_loud_enough" exp
- adding gui for easy access of runs
- cleaning up and adapting PEP8
- removed unnecessary global declarations
- changed stimuli calls to relative paths and changed folder structure
- exchanged if-statement structure, which previously was used to differ between settings, to function statements
         -> simplifying structure into general function, which simply takes setting as keyword input
- changed range to (0, 14), instead of (0, 13), so that all stimuli are presented
- generating new stimuli (sampling rate 48800, 30dbz and scaled up in 10dbz steps (as proposed [here](https://forum.audacityteam.org/viewtopic.php?t=2364) and [here](https://www.asha.org/policy/gl2005-00014.htm))
- using[AudioSegment](https://github.com/jiaaro/pydub/blob/master/API.markdown) to scale down amplitude in steps of 10dBFS
           
updating distro to 18.04, including complete system overhaul
