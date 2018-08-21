1 - 20 August:
- studying: claculus, music theory, sound engineering with python, bayes on coursera
- assisting in tnac and hoaf experiments

- working futher on alpaca script for generating sound bursts:
  - improved edge detetcion loop by switching from numpy sin, cos etc. to scipy version
  - added timeline variable for more intuitive plotting (instead of samples as x-axis)
  - packaged pure tone loop into function and implemented fail-safe loop, which triggers if one or more sound were 
    dropped during creation
  - implemented one loop that checks for total length of each pure tone and prints a warning if a sound is below a certain
    threshold length -> threshold still needs theoretical foundation (e.g. practicality vs. theoretical boundaries)
                     -> possibilty of implenting a fail-safe as mentionend above
  - defined frequency range as one semitone above or below each fundamental frequency (freq_range=int(i//1.06),int(i*1.06))
  - created loop that randomly picks a frequency out of the given range and feeds it forward to the pure tone function
  - created loop that writes produced tones into a labeld dictionary for easy access
    -> atm pseudorandomisation of stimuli is achieved by simply shuffling the order of said dictionary 
      -> looking into balancing transition probabilites
      
  - extended gaussian white noise for background presentation:
    -> randomising frequency at every sample point
    -> adapted formula for ERBF from VOICEBOX speech processing toolbox for MATLAB into python
    -> simply added said filter to white noise
    -> amplitude corrected signal so that amp max = 0.24
    
- still need to look into actual volume control via python and if there would be any distortion, when presenting
  experiment over mrt-compatible headphones, as well as finding an apropriate base frequency for the white noise 
  or finding out if that is even necessary
