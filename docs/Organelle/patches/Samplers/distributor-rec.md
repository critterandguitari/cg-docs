---
title: Distributor Rec
date: 2019-10-03
tags:
  - Sampler
  - Sample Player
  - Arpeggiator
  - Link Enabled
  - Looper
  - Sequencer
---


# Distributor Rec


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/3RPmQ2ZnA7o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Sampler, Sample Player, Arpeggiator, Link Enabled, Looper, Sequencer

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/03/Distributor-Rec.zip)**

Record samples, slice them up on the fly, and weave them across time with other sample slices all while arpeggiating and looping them!

## Details

WHAT IS THIS PATCH?  
It is an improvement of the original Distributor patch. This patch has three main functions: 1. Records an audio sample to each key; 2. Slices up those samples and arpeggiates them; 3. Interweaves slices from one sample with other sample slices as you play keyboard (or the sequencer).

HOW DO I USE THIS PATCH?  
Patch controls are available from the ‘Aux Menu.’ The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. The available Aux Menu Commands depends on which 'page' you are currently viewing.

To select a Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The main patch controls are available in the Right Column. They are PlayMode, RecMode, and Options.

**PlayMode** page has controls for:  
Ramp: Sets pitch envelope for each slice. Slice playback pitch ramps up from 0 to the current tuning over the 0-500ms.  
Arp: Selects pattern of how each sample slice is arpeggiated up or down octaves.   
Tuning: adjust global playback speed up and down two octaves.   
BPM: Default is internal. This will change if you are sending the patch external MIDI clock or have joined a Link session.

**RecMode** page has controls for:   
Monitor Vol: Sets the volume level for monitoring (audio thru) of the incoming audio.  
A visual keyboard represents the current record destination.  
With this page selected, the following additional Aux command is available: RecordArm - ’Arms’ recording of new sample (aka Record Enable). Once armed, recording starts when incoming audio level crosses amplitude threshold. Pressing Aux or Foot Switch will arm. Pressing either again after arm will cancel recording. If you like a recording, be sure to use the ‘Save’ command in system command so you can revert back to it in case of accidental record.

The **Options** page has controls for:  
Monitor Vol: Sets the volume level for monitoring (audio thru) of the incoming audio. This controls the same parameter as the instance on the RecMode page.  
Playback Mode: Selects sample start location. Reset starts playback from the beginning. Progressive starts playback from the previous endpoint. With Reset chosen, you will not hear entire sample due to sample length, Tempo, and Beat Division settings. With Progressive the entire sample will eventually be played.   
Beat Divisions: Sets slice length. Relative to Tempo.   
Max. Record Length: Sets maximum of how long you want a specific sample to be. Samples recording can always be ended earlier than maximum by pressing Aux during recording.

The following Aux commands are available on the Left Column from the PlayMode and Options pages:

Seq:Play/Stop - Plays or Stops selected sequence

Rec:Off/Armd - Controls Sequence Recording. When selected, Sequence is first Record Armed (Enabled). LED will be Pink. Sequencer is waiting for knob adjustment, key press or incoming MIDI note. When knob adjusted, key pressed or MIDI Note received, Recording starts. LED is Red. To end recording, press Aux (new seq begins looping immediately). LED will be Green and flash White on quarter note. Sequence length will be quantized to nearest quarter note.

Dub:Off/On – Overdub on top of existing sequence. Counts in 3 Sec before starting recording. To end recording, press Aux and sequence begins looping immediately.

Undo – Reverts Sequence to previous state. If this command says 'Undid' you cannot 'undo' further.

Latch: Off/On - Toggles between playing segments after releasing keys or not.

The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record to. Changing sequence slot will change the number that precedes the command in the left column.

TECH SPECS:  
Sample slice playback will always start on the next selected beat division. A general rule of thumb: You will hear a slice sooner if you have 16th notes selected than if you had 'whole' notes selected.

For those users who become comfortable with the Aux menu: If you press both Aux and Menu command/Sequence Slot key before the menu is displayed, your choice/command will be accepted.

If you want to add samples to the patch instead of recording them, they are in the 'Sounds' folder. The numbers correspond to the keys. 1.wav is assigned to the low 'C' key and move up from there.

Link enabled for syncing with other devices on a shared wireless network.

MIDI:

‘Live’ keypresses and notes from Sequence playback are sent out on the MIDI Out Channel configured in System/Settings/MIDI Setup menu.  
Sequenced knob adjustments are sent out as CC messages on the System MIDI Out Channel. Knob1 = CC21, Knob2 = CC22, Knob3 = CC23, Knob4 = CC24.  
If sending MIDI clock to Organelle or part of a Link session:  Otherwise BPM is ‘Off.’

FUN IDEA:  
Existing sequences can be applied to new recordings!
