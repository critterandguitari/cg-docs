---
title: Tapey
date: 2020-01-10
tags:
  - Sampler
  - Link Enabled
  - Looper
  - Sample Player
---


# Tapey


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/C4_lJigBvKc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Sampler, Link Enabled, Looper, Sample Player

**[Download Patch](https://patchstorage.com/wp-content/uploads/2026/04/Tapey-69f12286076f7.zip)**

Recorded samples are pitched across they keyboard. Sample playback emulates a tape player with pitch & speed warble and ramping start and stop speeds.

## Details

WHAT IS THIS PATCH?  
Tapey records a sample. The sample can be played by any key. The sample pitch is relative to the key's note. There are playback controls that emulate a tape player's ramping up to speed (and down from it) and warble. After sample is recorded, create and store sequences.  
The sample record length is only limited by available storage space on the Organelle's microSD card (or USB drive if you are using that for patch storage.)

HOW DO I USE THIS PATCH?  
There is one patch 'page' with the following controls:  
• Input Vol: controls volume of incoming signal.  
• Tune: Transpose tuning +/- two octaves.   
• Ramp Time: Sets how long it takes sample to get up to speed on keypress and back down to 0 when key is released.  
• Warble: Adds variability to playback pitch/speed.

The page also shows incoming BPM (if MIDI clock or Link Session present) and the current sequence and sequence state.

Additional patch controls are available from the ‘Aux Menu.’ The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux.

To select a Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The following Aux commands are available on the Left Column:  
Seq:Play/Stop - Plays or Stops selected sequence

Rec:Off/Armd - Controls Sequence Recording:  
  • When selected, Sequence is first Record Armed (Enabled). LED will be Pink. Sequencer is waiting for knob adjustment, key press or incoming MIDI note.  
  • When knob adjusted, key pressed or MIDI Note received, Recording starts. LED is Red.  
  • To end recording, press Aux (new seq begins looping immediately). LED will be Green and flash White on quarter note.

Dub:Off/On – Overdub on top of existing sequence. Counts in 3 Sec before starting recording. To end recording, press Aux and sequence begins looping immediately.

Undo – Reverts Sequence to previous state. If this command says 'Undid' you cannot 'undo' further.

Latch: Off/On - Toggles between playing segments after releasing keys or not.

The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record to. Changing sequence slot will change the number that precedes the command in the Left column.

There are five controls available in the Right column:  
Rec: When selected, it is record enabled and a X will appear in that cell and the LED will turn pink. When a loud enough sound is played, the recording will start and the LED will turn red. An Aux press will end the recording. Please note: if you’re using the Organelle’s mic for audio input, you will want to press and release the ‘Rec’ command button (upper C#) within 350 milliseconds. (You should release the Aux key when you release the Rec key as well.) Otherwise, the key release may cross the audio level threshold and trigger recording start and capture the key sound in the recording.

Mode: Mono/Poly. Controls how many samples can be played at once. If in Poly, it is 8-note polyphony. If in Mono, the Ramp controls glide between notes.

Cur: Selects the current sample by incrementing by one file. Will cycle back to '1' when it reaches the end of the list. Note: a new recording will automatically be selected as the current sample and so the number displayed will be incorrect after new recording. It will be correct once you select this command again.

Revrse: On/Off. Toggles between playing sample forwards or backwards.

Monitr: Toggles the audio monitor On/Off. Helpful if you want to hear your audio through the Organelle before, during, and/or after recording.

If you like a recorded sample or sequence, don’t forget to ‘Save’ in the Storage menu.

TECH SPECS:  
Foot Switch also controls sample record enable and record stop.

Link enabled for syncing with other devices on a shared wireless network.

MIDI Start and Stop commands will start sequencers. Grid notes are sent out as MIDI notes.

Fun Idea:  
You can record a sequence of just Warble and/or Ramp adjustment (no notes) and while it plays back you can play notes that get warbled by the sequence (a non-static warble setting for even more warble!).
