reading & studying: bayes, mathemactical notation

ansl: overhauling and adapting "aint_no_sound_loud_enough" exp
- adding gui for easy access of runs
- cleaning up and adapting PEP8
- removed unnecessary global declarations
- changed stimuli calls to relative paths and changed folder structure
- exchanged if-statement structure, which previously was used to differ between settings, to function statements
         -> simplifying structure into either one function for each setting or writing general function, which simply
         takes setting as keyword for saving
- changed range of for loop to (0, 14), instead of (0, 13)
           
updating distro to 18.04, including complete system overhaul
