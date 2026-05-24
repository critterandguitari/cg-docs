---
title: Zample
date: 2021-02-16
tags:
  - Sampler
  - Sequencer
  - Sample Player
  - Recorder
  - Weirdmaker
  - LFO
  - Mixer
---


# Zample


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/ar9gid3tpsE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Sampler, Sequencer, Sample Player, Recorder, Weirdmaker, LFO, Mixer

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/02/Zample-1.zip)**

A keyboard sample player with four samples arranged in a 2-D grid. A playhead crossfades between them as it is controlled by separate LFOs on each axis. Record your own samples. Create sequences.

## Details

WHAT IS THIS PATCH?  
Zample is a keyboard sampler that plays and crossfades between samples in a predictable but not entirely 'regular' way.

This patch is based on a two-dimensional grid with a playhead that moves around the grid. Each grid quadrant is assigned an audio sample. The sample's waveform fills its quadrant. As the playhead moves across a quadrant it plays the sections of the waveform it encounters. The keyboard transposes the samples. LFOs control the playhead position.

The playhead's X and Y axes have independent LFOs with rate and waveform parameters. Set the playhead's size to play larger sections or small granules of a sample as the playhead moves around the grid.

Populate your grid quadrants with one of 24 samples. You can customize the order and change samples on the fly. You can also record new samples. Create sequences from key presses and/or parameter adjustments.

This patch is related to the 'Zone' patch, which is where the 'Z' comes from.

HOW DO I USE THIS PATCH?  
A typical use case would be:   
1. Select samples to crossfade between.  
2. Dial in playhead settings: X & Y LFO rates, LFO waveforms, 'Chunk' (playhead) size, etc.   
3. Record an audio sample and add it to the 2-D grid.  
4. Replace an audio sample in the 2-D grid.   
5. Create a sequence with the keys, overdub it, etc.  
6. Revisit the above steps in any order as needed.

To do any of the above steps you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The main patch controls are available in the Right Column. There are five pages for this patch. The current page will be marked 'On' and the rest marked 'Off.' The pages are:

Global - Use Knobs 1-4 to X & Y LFO rates, 'Chunk' (playhead) size, and Transposition.

View - displays waveforms of the currently selected samples and the size and position of the playhead. Knobs 1-4 control the same parameters as in the 'Global' page

Record - Set Input Record and Monitor levels. The keyboard selects 1 of 24 possible samples to record. Samples are named 1.wav, 2.wav, ... in the patch folder. Once you have selected the key/file to record to, press and hold Aux key again and select the low C# key to Record Enable. Recording will start once a noise crosses a threshold. Stop recording by pressing Aux. Max record length is 5 seconds. You can also use a foot switch to Record Enable and stop record.

Zampz - Use the knobs to select the samples to crossfade between starting at the top left and moving clockwise. You can choose the same sample more than once.

Waves - Select the LFO waveforms for each axis.

The following commands are available on the Aux Menu's Left Column:  
Seq:Play/Stop - Plays or Stops selected sequence

Rec:Off/Armd - Controls Sequence Recording. When selected, Sequence is first Record Armed (Enabled). LED will be Pink. Sequencer is waiting for knob adjustment, key press or incoming MIDI note. When knob adjusted, key pressed or MIDI Note received, Recording starts. LED is Red. To end recording, press Aux (new seq begins looping immediately). LED will be Green and flash White on quarter note. Sequence length will be quantized to nearest quarter note.

Dub:Off/On – Overdub on top of existing sequence. Counts in 3 Sec before starting recording. To end recording, press Aux and sequence begins looping immediately.

Undo – Reverts Sequence to previous state. If this command says 'Undid' you cannot 'undo' further.

Latch: Off/On - Turn on to keep notes playing after release.

The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record sequences to. Changing sequence slot will change the number that precedes the command in the left column.

If you like a setting, don’t forget to ‘Save’ in the Storage menu.

TECH SPECS:  
If you want to add your own samples to the patch they are in the 'Sounds' folder. The numbers correspond to the keys. 1.wav is assigned to the low 'C' key and move up from there.

Link enabled for syncing with other devices on a shared wireless network.

MIDI Start and Stop commands will start sequencers.

4-voice polyphony.

This patch will work on the original Organelle (no speaker or batteries) but the screen animation will slow down after third voice.

Fun Idea:  
You can create a sequence with only knob adjustments (no note presses) to automate sample selection or LFO rate changes. Next level: once you have an automation going, change the page!  
To create a 'synth & drums' voice, select one 'synth-y' sample and then three drum samples.
