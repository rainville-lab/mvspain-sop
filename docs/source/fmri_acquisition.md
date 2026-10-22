# fMRI session

## Overview of fMRI data acquisition procedure



## Days before the session

- [ ] Send a reminder to the participant with the template email, and ask to complete dépistage-UNF.


- Make sure to ask the person not to wear nail polish or articifial nails



#### Physio/Biopac

- [ ] Check the notes of the EEG session to be aware of any information that could be related to the physiological signal. For example, for the skin conductance, a participant might be non-reponsder. In such a case, do not try to record the skin conductance activity (TBD). If it has been noted that the PPG quality was affected by poor circulation, do the PPG setup, but do not spend to much time troubleshooting the quality of that modality.

#### Prepration of the material

Gather all necessary equipment for the experiment:
- [ ] Digitimer 
...

-[ ] Gel


## Before the participant arrives - In the prep room

#### Physio/biopac

- [ ] Place the electrodes and the gel on the table in the prep room
    - [ ] Nuprep gel (EMG)
    - [ ] Alcohol bottle (EMG)
    - [ ] SignaGel (EMG)
    - [ ] 5 EL508 electrodes (EMG)
    - [ ] Isotonic gel (EDA)
    - [ ] 2 EL509 electrodes (EDA)
- [ ] Cut the bottom of two of the EL508 electrodes.


## Before the participant arrives - In the back room

#### Physio/Biopac
- [ ] In the back room in which the BIOPAC's amplifiers are, make sure the settings are at the right values on the amplifiers as per the table below.

| Parameters | EDA100C | PPG100C | EMG100C |
| :- | - | - | - |
| Gain | 2 | 100 | 2000 |
| LP | 10 | 10 | 500 |
| HP/100Hz HP | DC | 0.5 | Off |
| HP | DC | DC | 10 | 

![[images/biopac_amplifiers_setup.jpg]]

- [ ] On the HTL100C module, make sure that the cables for Psychopy, the TTL, and the digitimer are connected to channel 4, 5 and 8 respectively. Also make sure that if there are any other amplifier connected that are not in used (e.g., ECG100C), make sure that they are not set on those channels.

| HTL100C | Psychopy  | TTL | Digitimer |
| :- | - | - | - |
| Channel | 4 | 5 | 8 |

- [ ] Make sure the right channel is specified on each amplifier as per the channel below.

|  | EDA100C | PPG100C | EMG100C |  
| :- | - | - | - |
| Channel | 16 | 2 | 9 |


==To do: Verify the ACQ template and that the channels correspond==

![[images/biopac_channels_top_view.jpg]]


- [ ] Turn on the BIOPAC system.


## Before the participant arrives - In the control room

#### Digitimer setup

==list material for pain stimulation==

==List connexions schema==

- [ ] Pass the Digitimer cable in the waveguide

#### Psychopy computer

- [ ] code setup

- Open the reference list (annexe?) for the scripts to run

#### Acqkowledge computer

- Open template
- ==Make sure the filename matches the date (TDB)==

- make sure to display acq PC on the projector in the MRI room

- [ ] On the Acqknowledge computer, open the template in Acqknowledge.
==confirm template location and name when final==


#### Sensimetric

To deliver the auditory stimuli, an MRI-compatible earphone system is used ([Sensimetric]).

==todo insert imsge sound system==
- [ ] Make sure that the sound system is on and that the red light indicates A


## Before the participant arrives - In the MRI room

#### Physio/Biopac

- [ ] Unroll the EDA cable, place it properly on the ground, and put the extremety on the countertop with a sandbag on top.
- [ ] Unroll the PPG cable, place it properly on the ground, and put the extremety on the countertop with a sandbag on top.

#### Sensimetric

- [ ] Take the sensimetric out of the case, and bring it in the MRI room.
- [ ] Unroll the grey cable on the pannel in the back of the room. And bring it to the counter top in the front of the room. Do not forget to put a sandbag on the cable to make sure it does not fall on the ground.
- [ ] Connect the blue extremity of the Sensimetric with the blue extremity of the cable. Do the same with the red extremity.
- [ ] Remove the earplugs from the plastic bag and screw them to both heads. It is very important to screw them instead of just pushing them in. In the later case, you risk damaging the plastic part.

#### Digitimer

- [ ] Connect the filter and stimulation electrodes to the Digitimer cable passing through the waveguide

#### Other material
- [ ] Sandbag for hip stabilization
- [ ] Get a blanket out 
- [ ] Opt. the antenne RF


## During the setup - In the prep room 

#### Participant interactions
- [ ] Complete safety screening
- [ ] Give MRI-compatible short and slippers, key for locker


#### Physio/Biopac

- [ ] If the participant has nail polish on their right index, ask if they are confortable to remove it.
- [ ] Ask the participant to wash their hands with WATER ONLY
- [ ] Add some isotonic gel on the EL509 electrodes and place them on the palm on the right hand as shown in the figure below. Make sure to put some pressure on all sides of the electrodes to make sure the adhesive part properly makes contact with the skin.

![[images/physio_montage.png]]


## During the setup - In the control room


#### Acqkowledge computer

- [ ] Press play/start on the recording
- [ ] Make sure the filename is saved and corresponds to the correct date-time


#### Psychopy PC 



#### Sensimetric
- [ ] Plug the cable of the sound system in the psychopy computer. Press the button on the left to turn it on. Make sure the volume is not too loud to beginning with (button on the right).
- [ ] Turn on the intercom system using the switch on the left of the device.

**First volume test (after prep in MRI room is done)**
- [ ] On the Siemens intercom, press the Listen buttom.
- [ ] On the Sensimetric intercom, press the blue circle in the middle to speak.
> Instructions :speech_balloon: 
> Hi [name of the participant],
> We will soon be ready to start scanning, but first can you hear me properly in both ears?

> We will launch a mock scan with audio sample of the psychologist talking. This will simulate the level of noise during the next hour.
> I want you to pay attention to the audio, to make sure you hear well. It will last 30 seconds.
[Make the adjustments if needed]
> Perfect!
- ==To DO : implement in psychoPY and coordinate with André to know what is the dummy scan length==

## During the setup - In the MRI room

#### Sensimetric

- [ ] Once the participant is in a supine position but before connecting the EDA leads to the electrodes and placing the PPG transducer, bring the sensimetric to the participant, making sure that the Y part is place just under the participant's chin. Instruct to participant on how to place the earplugs.
> Instructions :speech_balloon: 
Now I'm going to ask you to put the earplugs in your ear. You will have to first squeeze the foam tips. Holding the colored plastic heads, insert the earplugs in your ear, and wait for 10 to 15 seconds until to foam expend again. Please to do not pull on the cable, and do not twist the plastic heads.
[Give the participant the earplugs and wait until they have inserted them.]
Does it feel confortable?

#### Physio/Biopac
- [ ] Place the cable under a sandbag placed on the moving part of the MRI table.

- [ ] After the participant has placed the earplugs in their ears, clip the EDA leads on the electrodes making sure that the wires are pointing towards the front of the MRI room.
- [ ] To make sure that the EDA signal is recording properly, first check the amplitude of the waveform. Usually, the skin conductance will vary between 5 and 20 microsiemens.
- [ ] Then, ask the participant to take a deep breath and hold it for a few seconds. This should cause an increase in the skin conductance.
> Troubleshooting :warning: 
> 1. Make sure the leads are properly attached to the electrodes: you can try to reclip the leads.
> 2. Check if the electrodes are properly adhering to the skin: if not,  add two pieces of tape on each side of the electrode.  
> 3. Check if there is enough gel: you will have to remove the gel on the participant's skin with some brown paper, and place the new electrodes.
> 4. If after those verifications the signal is out of the normal fluctuating range (5 to 20 microsiemens), change the gain on the EDA amplifier (TBD).

- [ ] Place the PPG on the right index of the participant, making sure the wire is pointing towards the front of the room (see figure above).
> Instructions :speech_balloon: 
> I will now attach a sensor on your index finger. It will feel a little bit tight, but it should not be too tight. Does it feel ok?
- [ ] To make sure the PPG signal is ok, look at the recorded waveform. You should see a consistant fluctuation. The systolic peak should be clearly visible, and you might also see the diastolic peak. 
> Troubleshooting :warning:
> If you don't see a consistent waveform when the participant is not moving:
> 1. Replace the strap on PPG sensor: the strap might be too loose or too tight.
> 
> If the PPG signal has a low amplitude
> 1. Check if the sensor is too tight as that might result in low perfusion.
> 2. Ask the participant if ther are too cold. Give them a blanket if it is the case.
> 
> If the waveform looks like it is "fading out"
> 1. If the participant has some nail polish, and was not confortable removing it, or has artificial nails, just write it down in the scanning notes, and continue with the rest of the setup.
> 2. Make sure the sensor is placed at the right position on the finger.

==add EMG== 

#### Digitimer electrodes 
- [ ] connect Digitimer electrodes


## Begining the experiment - In the control room
Once participant is set up in the MRI room 

**Task instructions**
> Instructions :speech_balloon: 
> TBD

#### Psychopy
```
Command to run dummy run script
```


```
Command to run dummy run script
```


## During the task - In the control room

#### Physio/Biopac

Each run, make sure that we see :
- [ ] TTL 
- [ ] Psychopy
- [ ] Digitimer

#### Acqkowledge (oscilloscope) monitoring 

What to look at...

In case of... wait until the run is done to do adjustment 

#### Psychopy computer

- [ ] Make sure the log is running properly (onset of evetns, and shocks)

> [!Warning] Important
Press ==TDB== keybord key to tell the program to be in a ready state.



### After the session

#### Digitimer 
- unplug the cables..etc


#### Sensimetric
- [ ] Ask the participant to remove the earplugs, and bring them to the countertop. Place a sandbag on top of the cable.
- [ ] Using some brown paper, **unscrew** the foam tips from the sensimetric and throw them in the garbage.
- [ ] Unplug the Sensimetric from the cable. Using a desinfecting wipe, gently wipe the extremities of the Sensimetric. Place the Sensimetric back in its case.
- [ ] Roll the grey cable using the over-under technique and place it back on the back pannel.
Volume calibration and adjustment!

#### Experimental log

>[!important]
> Complete the experimental log on github with relevant notes and information
> Note the temperature inside the scanning room!


## After the session

Do the debriefing interview

>[!important]
>- Save the qualitative data to ___
>- Save the physiological data to ___

##### Material and ressources check
- [ ] Count the number of remaining electrodes
    - Define the treshold (e.g. 10 packages)
- [ ] Check how many clean MRI-compatible shorts there are
- [ ] 

---

### Biopac

Multiple peripheral physiological measurements are recorded using MP160 MRI-compatible systems.



### Before the participants arrives - In the back room

### Before the participants arrives - In the control room




### During the setup - In the prep room

### During the setup - In the control room

### During the setup - In the MRI room

### After the experiment

This section explains how to put the equipment away.
- [ ] XX 
put
This section explains what to pay attention to in terms of the physiological signals, and what to write in the scanning notes.
- [ ] XX
