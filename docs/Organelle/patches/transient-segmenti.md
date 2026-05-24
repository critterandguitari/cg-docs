---
title: Transient Segmenti
date: 2019-06-05
tags:
  - Segment Player
  - Recorder
  - Looper
  - Sequencer
  - Rhythm Maker
---


# Transient Segmenti


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/vSWsRIOy1Gc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Segment Player, Recorder, Looper, Sequencer, Rhythm Maker

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/03/Transient-Segmenti.zip)**

A recorded track is automatically sliced into up to 24 segments (one per key) depending on where transients are detected. Create up to 14 possible stored sequences from segments.

## Details

#### What is this patch?

This patch has two main functions: 1. Record audio and automatically slice it up into as many as 24 segments based on where the patch detects transient sounds in the recording, and 2. Use keyboard or the sequencer to play segments in new ways/orders.

#### How Do I Use this Patch?

Use the Encoder to navigate between the Sample View/Rec and Jam Options pages. Sample View/Rec shows a waveform and lists how many segments (sections between detected transients) there are. The Jam Options page shows speed, pitch, segment length, and input monitor controls.

Additional patch controls are available from the ‘Aux Menu.’ The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. The available Aux Menu Commands depends on which 'page' you are currently viewing. The Left Column never changes.

To select a Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The following Aux commands are available on the Left Column:

**Seq:Play/Stop** - Plays or Stops selected sequence

**Rec:Off/Armd** - Controls Sequence Recording:

- When selected, Sequence is first Record Armed (Enabled). LED will be Pink. Sequencer is waiting for knob adjustment, key press or incoming MIDI note.
- When knob adjusted, key pressed or MIDI Note received, Recording starts. LED is Red.
- To end recording, press Aux (new seq begins looping immediately). LED will be Green and flash White on quarter note.

**Dub:Off/On** – Overdub on top of existing sequence. Counts in 3 Sec before starting recording. To end recording, press Aux and sequence begins looping immediately.

**Undo** – Reverts Sequence to previous state. If this command says 'Undid' you cannot 'undo' further.

**Latch: Off/On** - Toggles between playing segments after releasing keys or not.

The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record to. Changing sequence slot will change the number that precedes the command in the left column.

If you are on the Sample View/Rec page the following additional Aux command is available:

**RcIn:Arm** - ’Arms’ recording of new sample (aka Record Enable). Once armed, recording starts when incoming audio level crosses amplitude threshold. Pressing Aux after arm will cancel recording. If you like a recording, be sure to use the ‘Save’ command in system command so you can revert back to it in case of accidental record. Recordings can be 12000 milliseconds long or a maximum 24 segments. If recording has less than 24 segments, the segments will be repeated across the keyboard.

#### Tech Specs:

For those users who become comfortable with the Aux menu: If you press both Aux and Menu command/Sequence Slot key before the menu is displayed, your choice/command will be accepted.

Footswitch: N/A

MIDI:

- ‘Live’ keypresses and notes from Sequence playback are sent out on the MIDI Out Channel configured in System/Settings/MIDI Setup menu.
- Sequenced knob adjustments are sent out as CC messages on the System MIDI Out Channel. Knob1 = CC21, Knob2 = CC22, Knob3 = CC23, Knob4 = CC24.
- If sending MIDI clock to Organelle or part of a Link session: Sequence length will be quantized to nearest quarter note. Otherwise BPM is ‘Off.’

#### Fun Idea:

- Existing sequences can be applied to new recordings!
