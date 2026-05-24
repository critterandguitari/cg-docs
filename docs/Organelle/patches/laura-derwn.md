---
title: Laura Derwn
date: 2023-01-20
tags:
  - Pitch Shift
  - Effect
  - Vibrato
---


# Laura Derwn


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/bRw4m8FdkHE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Pitch Shift, Effect, Vibrato

**[Download Patch](https://patchstorage.com/wp-content/uploads/2023/01/Laura-Derwn-63cb048b53d5e.zip)**

Pitch ramping effect with tempo sync.

## Details

Laura Derwn makes your sound go 'derwn' or 'derrrwwwwnnn' to a user-set semitone below the actual pitch. It is an effect similar to the sound of stopping a record on a turntable. The patch has a tempo aspect which controls the rate at which the pitch ramps down and then back up, and then back down, and then up, and so on!

There are two main pages of parameters: Ramp and Tempo.

The Ramp page has settings for the following:  
1. Which semitone to ramp down to  
2. How quickly the sound ramps to the destination semitone  
3. How long it stays at that semitone  
4. How quickly it ramps back up to the original pitch.

The temporal 'Ramp' parameters are ultimately governed by the settings of the Tempo page: tempo, note type, and quantity of notes. For example, say the Tempo page is set to the following: 120 BPM and 1x Quarter note. This means that the ramp down, hold, and ramp up settings will all happen in the span of one quarter note at 120 BPM (aka 500 milliseconds). The Tempo, Note type, and Note Amount settings collectively set the effect 'Cycle.'

By adjusting the percentages of the ramp down, hold, and ramp up settings, you will be dividing the Quarter note accordingly. If each were set to 33%, they would each occur for ~166 milliseconds. If you changed the Tempo page settings to 2x Quarter notes (or 4x eighth notes, etc.), and kept the tempo at 120 BPM and kept the Ramp percentages at 33%, each of the Ramp events (down, hold, up) would last twice as long (~333 milliseconds each).

A third page, 'Visual', shows a graph of the Ramp settings.

HOW DO I USE THIS PATCH?  
A typical use case would be:   
1. Set the tempo, type and quantity of rhythmic notes.  
2. Set the Ramp semitone depth, and timing of the Ramp events.  
3. View the graph of the Ramp settings.  
4. Play sound into the patch  
4. Revisit the above steps in any order as needed.

To do steps 1-3 above you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The Aux menu's left column has four commands:

**Pattn**: On/Off - Setting this command to 'On' will start the pitch ramp down, hold, and ramp up effect. The bottom of the OLED screen shows the current semitone drop.

**Tempo** - Selecting this page will open the Tempo page. It has the following parameters set by the respective knobs:

Tempo: Sets the overall tempo of the effect. If external MIDI clock is being received, this setting is not controllable from within the patch.

Note: Selects the note type for the effect to count from: 16th note through Whole note.

Note Amount: Selects how many notes for the effect to count from: 1x through 16x.

Dry/Wet: Sets the mix of the 'dry' and 'wet' signals. 100% = entirely wet.

**Ramp** - Selecting this page will open the Ramp page. It has the following parameters set by the respective knobs:

Depth: Sets how many semitones to ramp down to. Range is 0 to -48.

Down Length: Sets percentage of the effect 'Cycle' to ramp to Depth setting.

Hold Length: Sets percentage of the effect 'Cycle' to hold at Depth setting.

Up Length: Sets percentage of the effect 'Cycle' to ramp from Depth setting to 'normal' pitch.

**Visual** - Selecting this page will open the Visual page. It shows a graph of the Ramp settings. Adjusting the knobs on this page will affect the settings of the Ramp page.

There is one command available on the Aux Menu's Left Column:

**NtsIn**: On/Off - if this is set to 'On' incoming MIDI notes will trigger a effect cycle. This is a fun way to sync the effect to a discrete MIDI event. It is super fun to send Audio and MIDI from the same instrument such as a drum machine or synth.   
This setting can be used in tandem with the 'Pattn: On' setting, but it might be overkill.

------------

Pressing the keyboard keys triggers the effect too. Holding the key will hold the effect at the semitone depth.

------------

If you like a setting, don’t forget to ‘Save’ in the Storage menu.

TECH SPECS:

Link enabled for syncing with other devices on a shared wireless network.

Foot Switch: Starts/Stops 'Pattn' command.
