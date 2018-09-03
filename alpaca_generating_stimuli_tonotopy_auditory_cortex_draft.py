%matplotlib inline
import scipy
import matplotlib.pyplot as plt
import numpy as np
import time
import random
from __future__ import division #so 1/2 = 0.5, not 1/2=0

from IPython.display import Audio, Image
import librosa
import seaborn


# create your white noise

# duration for white noise -> still up to debate what would
# be the most efficient and appropriate for experimental setup
dur_noise=30
sr = 24400 # set sampling rate

#freq in hz -> placeholder: not sure what would be apropriate here
freq=np.arange(10,10000,dur_noise*sr)

def erb(f):

    ''' define equivalent rectangular bandwith (ERB) for given frequency in hz
        → minimize variation inf hearing tresholds between
        frequencies and participants.
        adapted from matlab:
        http://www.ee.ic.ac.uk/hp/staff/dmb/voicebox/doc/voicebox/frq2erb.html '''

    # erb=11.17268*sign(frq).*log(1+46.06538*g./(g+14678.49));
    u=[6.23**-6, 93.39**-3, 28.52] # u=[6.23e-6 93.39e-3 28.52]
    p=[-14678.5, -311.9] # p=sort(roots(u))
    a=11.17 # a=1e6/(6.23*(p(2)-p(1)))
    c=-14678.5 # c=p(1)
    k=676170.42 # k = p(1) - p(1)^2/p(2)
    h=47.065 # h=p(1)/p(2)

    # define bandwith for every frequency in freq-var (here 10 - 10000)
    erb=[]
    bnd=[]
    for element in freq:
        g=np.absolute(element)
        erb1=11.17268*np.sign(element)*scipy.log(1+46.06538*g/(g+14678.49))
        erb.append(erb1)
        bnd1=np.polyval(u,g)
        bnd.append(bnd1)
    return erb, bnd

# call function
erb, bnd= erb(freq)

# randomly pick out of calculated freq-range to set gaussian white noise?
# placeholder: not sure what to pick as mean here
samples = (np.random.normal(5000,bnd, dur_noise*sr))

# display white noise
display(Audio(samples,rate=sr))
plt.figure(figsize=(35,5))
plt.plot(samples)


# create pure tones

sr = 24400 # samplingrate
dur = 0.19 #duration of pure tone in seconds
amp= 0.24 # set amplitude
phi=scipy.pi//2 # set phase shift

# construct array for pure tone presentation
t = scipy.linspace(0, dur, dur*sr, endpoint=False)
# dur of ramps = twice of what is actually needed, will be sliced later
dur_ramp= 0.04
t_ramp = scipy.linspace(0.0,dur_ramp,dur_ramp*sr)


# define list of nominal frequencies in hz
nominal_frequencies=[200.0, 338.8, 573.8, 971.9
                    , 1646.2, 2788.4, 4723.1, 8000.0]

timeline=np.arange(t.size)/sr # define timeline for plotting

def frequency_range(nominal_frequencies):

    ''' varying nominal frequencies in range of 1 semitone
    x¹²=2
    x=2**(1/12)=1.0594630943593 '''

    range_frequencies=[]
    for i in nominal_frequencies:
        for f in range(4):
            frequency=int(i//1.06),int(i*1.06)
            range_frequencies.append(frequency)
    return range_frequencies

def pick_frequency(range_frequencies):

    ''' randomly pick a freq in the specified range '''

    counter1=0
    random_frequency=[]
    for i in range_frequencies:

        random_pick=random.randint((*range_frequencies[counter1]))
        random_frequency.append(random_pick)
        counter1+=1
        print('freq_range='+str(i)+'; picked freq='+str(random_pick))
    return random_frequency


# sine evelope -> helps with reshaping of ramps
def sine_envelope(t):
    return np.square(scipy.sin((1.0)*np.pi*t/t[-1])) #t[-1] = last value


def create_sounds(random_frequency):

    ''' function fitting onset and offset ramps to sounds,
        plot and output sounds and append sounds to a list'''

    # create list to append to
    list_sounds=[]
    for f in random_frequency:
        # create your pure tone for each frequency rand_freq
        pure_tone =(amp*scipy.sin(2.0*np.pi*f*t+phi))

        # define onset ramp
        onset_r=(amp*scipy.cos(2*scipy.pi*f*(t_ramp)))

        # multiply it by sine envelope
        onset = sine_envelope(t_ramp)*onset_r

        # uncomment to plot your tones for visual inspection
        #plt.figure(figsize=(100,5))
        #plt.plot(timeline,pure_tone)
        #plt.xlabel('Amplitude')
        #plt.ylabel('time')
        #plt.title('Frequency='+str(f))


        # split your ramp into onset - offset ramp
        split_ramp=np.split(onset,2)
        onset_split = split_ramp[0]
        offset_split = split_ramp[1]

        # plot onset ramp
        #plt.figure(figsize=(100,4))
        #plt.plot(timeline,onset_split)
        #plt.xlabel('Amplitude')
        #plt.ylabel('time')
        #plt.title('Frequency='+str(f))

        # plot offset ramp
        #plt.figure(figsize=(100,4))
        #plt.plot(timeline,offset_split)
        #plt.xlabel('Amplitude')
        #plt.ylabel('time')
        #plt.title('Frequency='+str(f))


        # create counter to have a condition on when to advance in the loop
        counter=0
        onset_pure_offset= []

        for i in range(len(pure_tone[0:500])):
            # find closest aproximation of overlapping points between maximum
            # of onset ramp and pure tone array
            # to minimise clicking sounds at transition
            if (np.round(pure_tone[i],decimals=2) ==
                np.round(np.amax(onset_split),decimals=2)
                and counter==0):

                # append cut onset ramp to list
                onset_pure_offset.append(onset_split[0:(np.argmax(onset_split))])

                # append onset matched pure tone
                onset_pure_offset.append(pure_tone[i:])

                # cocncatenate tone
                sound= scipy.concatenate(onset_pure_offset)
                counter+=1

                for i in range(len(sound)-1,0,-1):
                    # repeat step for offset ramp
                    if (np.round(sound[i],decimals=2) ==
                        np.round(np.amax(offset_split),decimals=2)
                        and counter==1):

                        sound=sound[0:i]
                        sound=np.append([sound],
                                        [offset_split[np.argmax(offset_split):]])

                        # plot finished tone
                        #plt.figure(figsize=(100,5))
                        #plt.xlabel('Amplitude')
                        #plt.ylabel('time')
                        #plt.title('Frequency='+str(f))
                        #plt.plot(timeline,sound)
                        #plt.title('Frequency='+str(f))
                        #display(Audio(sound, rate=sr))

                        print(str(f)+': length of sound= '+str(len(sound)))
                        # append tone to list of tones
                        list_sounds.append(sound)
                        counter+=1
                        break


    # create failsafe for unexpected problems in the sound creation
    # check if the list of sounds is complete
    restart=True
    while restart:
        if len(list_sounds)!=32:
            # if len of list sounds is not 32 rerun create sounds function
            print(len(list_sounds))
            print('WARNING! dropped tone during creation -> rerunning loop!')

            range_frequencies=frequency_range(nominal_frequencies)
            random_frequency=pick_frequency(range_frequencies)
            list_sounds=create_sounds(random_frequency)
            restart=True
            print(len(list_sounds))
        elif len(list_sounds)==32:
            restart=False

    # print a warning if the length of certain sounds doesn't match  criteria
    counter_f=0
    for i in list_sounds:
        counter_f+=1
        if len(i)<5450:
            print('WARNING! sound '+str(counter_f)
                    + ' is shorter than usual length')


    return list_sounds

# call functions
range_frequencies=frequency_range(nominal_frequencies)
random_frequency=pick_frequency(range_frequencies)
list_sounds=create_sounds(random_frequency)



# create dictionary for easy acces of sounds'''

twohundred_hz=[]
threethreeeight_hz=[]
fiveseventhree_hz=[]
ninesevenone_hz=[]
onesixfoursix_hz=[]
twoseveneighteight_hz=[]
fourseventwothree_hz=[]
eightthousand_hz=[]

# append data from list_sounds
for i in range(32):
    if i <= 3:
        sound=list_sounds[i]
        twohundred_hz.append(sound)
    elif i <=7:
        sound=list_sounds[i]
        threethreeeight_hz.append(sound)
    elif i <=11:
        sound=list_sounds[i]
        fiveseventhree_hz.append(sound)
    elif i <=15:
        sound=list_sounds[i]
        ninesevenone_hz.append(sound)
    elif i <=19:
        sound=list_sounds[i]
        onesixfoursix_hz.append(sound)
    elif i <=23:
        sound=list_sounds[i]
        twoseveneighteight_hz.append(sound)
    elif i <=27:
        sound=list_sounds[i]
        fourseventwothree_hz.append(sound)
    elif i <=32:
        sound=list_sounds[i]
        eightthousand_hz.append(sound)

# write dictionary combining keywords with sound data
grouped_sound={'twohundred_hz':twohundred_hz
                ,'threethreeeight_hz':threethreeeight_hz
                ,'fiveseventhree_hz':fiveseventhree_hz
                ,'ninesevenone_hz':ninesevenone_hz
                ,'onesixfoursix_hz':onesixfoursix_hz
                ,'twoseveneighteight_hz':twoseveneighteight_hz
                ,'eightthousand_hz':eightthousand_hz}



# short demo of how exp could sound like

# set autoplay to True, for examination purposes
for x in range(1):

    display(Audio(samples,rate=sr, autoplay=False)) # white noise
    for i in range(4):
        time.sleep(1)
        display(Audio(twohundred_hz[i],rate=sr,autoplay=False)) # pure tone
    for i in range(4):
        time.sleep(1)
        display(Audio(ninesevenone_hz[i],rate=sr,autoplay=False)) # pure tone
    for i in range(4):
        time.sleep(1)
        display(Audio(onesixfoursix_hz[i],rate=sr,autoplay=False)) # pure tone
    for i in range(4):
        time.sleep(1)
        display(Audio(fiveseventhree_hz[i],rate=sr,autoplay=False)) # pure tone
