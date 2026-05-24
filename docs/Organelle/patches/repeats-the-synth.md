---
title: Repeats the Synth
date: 2021-11-21
tags:
  - Sequencer
  - Synthesizer
  - "Multi-Instrument"
---


# Repeats the Synth


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/nRAtoiW4E38" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Sequencer, Synthesizer, Multi-Instrument

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/11/Repeats-the-Synth.zip)**

Multisynth w/ polyphonic sequencer. Set note length and note repeat pattern within a bar, then set repeat pattern for that bar. Example: Low C key repeats every third 16th note, every other measure.

## Details

WHAT IS THIS PATCH?  
Build up melodies by setting how often a note repeats within one measure and then set how often the measure (aka 'bar') itself repeats. It is a pattern of patterns. By selecting a note on the keyboard, choosing a note division (32nd through whole), choosing a note repeat pattern (e.g. every note division, every fourth division, etc.), then selecting a bar repeat pattern (e.g. every bar, once every 7th bar, etc.), you can build up your melody from a single note to complex patterns of interlacing notes.

Once you have a pattern you like, update the synth settings or choose another synth that fits your pattern better. There are nine synth modes to choose from.

Update your pattern and/or synth settings whenever you want!

HOW DO I USE THIS PATCH?

A typical use case would be:

1. Select a note to play by pressing a keyboard key. Adjust the volume of that note.  
2. Start loop playback.  
3. Set the note division, note pattern, bar pattern and swing amount for that note.  
4. Set the global settings: transpose, note length, swing, and tempo.  
5. Adjust the synth settings.  
6. Save your settings.  
7. Revisit the above steps in any order as needed.

To do many of the steps above you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The Left column includes the following controls:   
Play/Pause: Starts/resets the 32-bar loop.  
Pattrn: Turns on the Pattern page.    
Global: Turns on the Global page.  
Synth: Turns on the Synth page.

The Right column includes the following control:  
Clear: Selecting this command will clear the Pattern. There is no undoing this.

Step 1: The default screen is a representation of the 24-key keyboard and a 32-bar counter. Pressing a key will preview a note one time and 'fill in' the key on screen layout. Repeatedly pressing the same key again will set the volume in the pattern of 100%, 50%, 25%, 0%, 25%, 50%, 100%..., and the visual key will be filled in accordingly: all the way filled for 100%, and no fill for 0%. The current key and volume will be displayed at the bottom of the screen.

Step 2: Hold aux button & press Low C# key or a connected Foot Switch to start and stop playback of the 32-bar loop. If playback is stopped, LED is pink and the bar counter reads '0'. If loop is playing, the LED is green. Playback always starts at beginning (bar 1). As notes get played, the on-screen keys flash for each individual trigger.   
   
Step 3: To set a key's note division, pattern, etc., you will need to use the ‘Note Edit’ menu. Hold Aux and press F# Key to enter the Pattern page. Long press a key to enter the Note Edit menu. If the loop is stopped you will hear a preview of that note as it loops for one measure at the current tempo. The LED will be white. If loop is playing, you will hear your note update according to settings - so if the bar repeat pattern is not 'often,' you will not hear your note update right away. The LED will flash between green and white.   
Turning knobs1-4 will edit the parameters. Adjusting the note & bar patterns (Knobs2 & 3) will display a grid with filled/white and unfilled/black cells. Filled = 'on'; Unfilled = 'off.'  A cell that is 'on' will trigger sample playback for that note division or bar. To exit the edit menu, press 'Aux.'

Step 4: Hold Aux and press G# Key to enter the Global page. Here you can set transposition, note length, swing, and tempo:  
Knob1: Sets the transposition of the keyboard notes.   
Knob2: Sets length for notes. This a relative adjustment. The notes will still start playing at their set interval (quarter, whole, etc.) but the length can be set to 0-100% of the set interval.   
Knob3: Add swing for all notes.  
Knob4: Sets tempo unless incoming MIDI clock or is present. If Link session is active, this knob will control Link tempo.

Step 5: Hold Aux and press A# Key to enter the Synth page.  
Knob1: Selects the Synth module.  
Knob2: Depends on Synth module selected on Knob1.  
Knob3: Depends on Synth module selected on Knob1.  
Knob4: Depends on Synth module selected on Knob1.

Step 6: Use the Organelle's 'Save' command in the Storage menu to save your work.

Step 7: Keep editing until your pattern, synth, tempo suit you!

_______

TECH SPECS:

MIDI clock is always sent out. Playback of loop waits for next beat. MIDI 'Start' and 'Stop' messages are sent out when loop is started/stopped. Incoming MIDI Start and Stop commands will start loop playback.

Link enabled for syncing with other devices on a shared wireless network.

Incoming MIDI Start and Stop commands will start sequencer.

_______

Fun Idea: Send a stream of MIDI notes to create a new hybrid rhythm...
