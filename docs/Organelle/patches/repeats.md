---
title: Repeats
date: 2021-04-30
tags:
  - Rhythm
  - Rhythm Maker
  - Drum Machine
  - Sample Player
  - Link Enabled
---


# Repeats


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/dx1Gf0lj6ME" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Rhythm, Rhythm Maker, Drum Machine, Sample Player, Link Enabled

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/05/Repeats-1.zip)**

Rhythm Building patch. Choose one of 24 samples, set repeat pattern within a measure, then set repeat pattern for that measure. E.G,: snare repeats every third 16th note, every other measure.

## Details

WHAT IS THIS PATCH?  
Build up rhythms by setting how often a sample repeats within one measure and then set how often the measure (aka 'bar') itself repeats. It is a pattern of patterns. By selecting a sample from keyboard, choosing a note division (32nd through whole), choosing a note repeat pattern (e.g. every note division, every fourth division, 'on' for two divisions in a row then 'off' for one, etc.), then selecting a bar repeat pattern (e.g. every bar, once every 7th bar, etc.), you can build up your beat from a single note to a complex patterns between samples.

HOW DO I USE THIS PATCH?

A typical use case would be:

1. Select a sample to play by selecting a key. Adjust the volume of that sample.  
2. Start loop playback.  
3. Set the note division, note pattern, bar pattern and swing amount for that sample.  
4. Set the global sample 'shift,' length, and speed.  
5. Set the tempo.  
6. Save your settings.  
7. Revisit the above steps in any order as needed.

Step 1: The default screen is a representation of the 24-key keyboard and a bar counter. Pressing a key will preview a sample one time and 'fill in' the key on screen layout. Repeatedly pressing the same key again will set the volume in the pattern of 100%, 50%, 25%, 0%, 25%, 50%, 100%..., and the visual key will be filled in accordingly: all the way filled for 100%, and no fill for 0%. The current key and volume will be displayed at the bottom of the screen.

Step 2: Pressing Aux button or a connected Foot Switch starts and stops playback of the 32-bar loop. If playback is stopped, LED is pink and the bar counter reads '0'. If loop is playing, the LED is green. Playback always starts at beginning (bar 1). As samples get played, the on-screen keys flash for each individual trigger.   
   
Step 3: To set a key's note division, pattern, etc., you will need to use the ‘Sample Edit’ menu. Long press a key to enter this edit menu for that key. If the loop is stopped you will hear a preview of that sample as it loops for one measure at the current tempo. The LED will be white. If loop is playing, you will hear your sample update according to settings - so if the bar repeat pattern is not 'often,' you will not hear your sample update right away. The LED will flash between green and white.   
Turning knobs1-4 will edit the parameters. Adjusting the note & bar patterns (Knobs2 & 3) will display a grid with filled/white and unfilled/black cells. Filled = 'on'; Unfilled = 'off.'  A cell that is 'on' will trigger sample playback for that note division or bar. To exit the edit menu, press 'Aux.'

Steps 4 & 5: Back on the default screen, adjustments to Knobs1-4 will be displayed at the bottom of the screen. They are:

Knob1: Sets the sample 'shift'. It moves the samples up to the next key while keeping the pattern for the key. This is a way to change the 'vibe' of the rhythm but the 'hits' remain in place in time. Turning the knob up to +24 will bring you back to the beginning.   
   
Knob2: Sets playback length for all samples.

Knob3: Sets playback speed for all samples.

Knob4: Sets tempo unless incoming MIDI clock or Link session is present.

Step 6: Use the Organelle's 'Save' command in the Storage menu to save your work.

_______

TECH SPECS:

MIDI clock is always sent out. Playback of loop waits for next beat. MIDI 'Start' and 'Stop' messages are sent out when loop is started/stopped. Incoming MIDI Start and Stop commands will start loop playback.

Link enabled for syncing with other devices on a shared wireless network.

Incoming MIDI Start and Stop commands will start sequencer.

_______

Fun Idea: Swap in your own samples!  
Fun Idea: Send a stream of MIDI notes to create a new hybrid rhythm...
