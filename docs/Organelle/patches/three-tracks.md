---
title: Three Tracks
date: 2019-05-17
tags:
  - Sequencer
  - Automation
  - Link Enabled
  - Synthesizer
  - Sample Player
  - LFO
  - Looper
---


# Three Tracks


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/mpx9nqJKZQc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Sequencer, Automation, Link Enabled, Synthesizer, Sample Player, LFO, Looper

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/03/Three-Tracks.zip)**

Layer three synth/sampler Tracks together. A Track is both the sound engine (eight synths/samplers) and 14 possible stored sequences. Possibilities!

## Details

*What is this patch?*

This patch has three 'Tracks.' A Track is both the sound engine (eight synths/samplers) and 14 possible stored sequences. Tracks may be played individually or all at once.

For each Track A, B, C, select a synth/sampler to play (Knob1). Dial up a track's synth/sampler settings(Knob2-4). Record to one of the Track's sequence 'slots' using the Aux Menu (more on this below). Repeat for the other two tracks. Create variation by:

- Recording new sequences for a given Track
- Selecting other sequences while the other two Tracks continue to play the same sequences.
- Changing the synth/sampler on a currently playing sequence.

Control the volume of each Track via the Mix page. There is a fun LFO mix control which automatically fades Tracks in/out at the LFO rate.

The BPM page has a tempo control and metronome control. Dial up a specific BPM so the sequencer can quantize sequence length to the nearest quarter note.  Alternatively, if you send the Organelle MIDI clock or join a Link session, sequence playback speed will be synced to that external tempo.

*How Do I Use this Patch?*

The Aux Button controls a new ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. The available Aux Menu Commands depends on which 'page' you are currently viewing (AKA 'On'). The Right Column never changes.

To select a Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

If Track A/B/C Page is 'On' the following Aux commands are available:

- Seq:Play/Stop - Plays or Stops selected sequence
- Rec:Off/Armd - Controls Sequence Recording:
- When selected, Sequence is first Record Armed (Enabled). LED will be Pink. Sequencer is waiting for knob adjustment, key press or incoming MIDI note.
- When knob adjusted, key pressed or MIDI Note received, Recording starts. LED is Red.
- To end recording, press Aux (new seq begins looping immediately). LED will be Green and flash White on quarter note.
- Dub:Off/On – Overdub on top of existing sequence. Counts in 3 Sec before starting recording. To end recording, press Aux and sequence begins looping immediately.
- Undo – Reverts Sequence to previous state. If this command says 'Undid' you cannot 'undo' further.

The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record to. Changing sequence slot will change the number that precedes the command in the left column.

If Mix/BPM Page is 'On' the following Aux commands are available:

- PlayAll - Plays all three tracks' selected sequence.
- StopAll– Stops all of the three tracks.

The PlayAll and StopAll commands are not the same as turning on/off all sequencers in Tracks A+B+C individually. The last OLED screen line may say ‘Stopped All’ even though one or more sequencers is playing.

The Bottom Row of keys will not control anything.

*Tech-y Specs*:

There is a Transpose control for each Track. It is located at the end of the list of synths/samplers (Knob1 all the way right). The keyboard is muted when this control is selected. Take care not to have ‘hung’ MIDI notes if you enter Transpose control with sequence playing, etc.

For those users who become comfortable with the Aux menu: If you press both Aux and Menu command/Sequence Slot key before the menu is displayed, your choice/command will be accepted.

Footswitch: N/A

MIDI: ‘Live’ keypresses (MIDI notes) are sent out on the MIDI Out Channel configured in System/Settings/MIDI Setup menu. Sequences send MIDI notes out on different channels. Track A sequenced notes are sent on Ch. 1. Track B sequences are sent on Ch. 2. Track C sequences are sent on Ch. 3. You can modify these channels by editing the [pd Sequencers] file in main.pd. There are comments showing which objects to modify.

*Some fun ideas*:

- The tracks can play any sequence - they don't all have to play the same sequence slot: You might find that Sequences A2, B7, C13 is the combination you are looking for. Or maybe it is Sequences A5, B1, C12!
- You can use the same synth/sampler across all three tracks.
- You can play the keyboard on the Mix page. It will play the three voices (one from each Track)! If you have sequences playing you can play on top of them. Things can get weird quick, but if you make each track a variant of the same synth/sampler, you can dial up some nice combinations. The only problem with this feature is that you will want to sequence your sounds here and there is no fourth Track to sequence this! One solution is to sequence with MIDI from an external MIDI device or DAW.
- You can record sequences with only knob adjustments (no notes) for loops of automation.
