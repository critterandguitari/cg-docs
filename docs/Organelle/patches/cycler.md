---
title: Cycler
date: 2022-08-23
tags:
  - Segment Player
  - Sample Player
  - Sampler
  - Sequencer
  - Filter
  - Mixer
---


# Cycler


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/RTOs8Mld6rs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Segment Player, Sample Player, Sampler, Sequencer, Filter, Mixer

**[Download Patch](https://patchstorage.com/wp-content/uploads/2022/08/Cycler.zip)**

Sample-playing patch that cycles through and crossfades samples on a given key at a controllable rate. Create evolving beats and patterns using samples of your choosing.

## Details

Cycler is similar to other C&G-made patches like Sampler Style and HRando where samples are played with key presses and sequences can be recorded from those key presses. But this patch mixes/crossfades samples 'stored' on a key. Each key has a folder with a number of audio samples in it. Each time a key is hit, the patch will play one or an amplitude-based mix of two of those samples - depending on the current settings and position of the 'cycle.' So while the drum pattern or sequence remains the same, the sound changes according to the cycle settings and samples.

For example, say there are three samples in a the low C key's sample folder: 1.wav (kick drum), 2.wav (piano note), and 3.wav (laser). Because a file's name informs its place in the ordinal series of files, 1.wav will be the first sample played. Let's also say that the patch is set to use three steps (aka key presses or sequenced presses) to completely move from one sample to the next. This 'three steps' setting means that each step will be increments of 33% (100%/3 = 33%). The total amplitude mix of every step will equal 100%.

The first time the low C key is pressed, sample 1.wav will be the only sample heard (100% sample 1.wav). The second time the low C key is pressed, the patch will start to mix in sample 2.wav - so 33% of 2.wav with 67% of 1.wav. The third press will have a mix of 67% of sample 2.wav with 33% of sample 1.wav . The fourth press (or step) will result in 100% of sample 2.wav being heard. The cycle starts over, but now sample 3.wav will start to be mixed with sample 2.wav. When that cycle is complete, sample 1.wav will start to be added in with sample 3.wav. In this way, the patch automatically crossfades between samples at a stepped interval.

Different step amounts will mix at different percentages (e.g. 10 steps will mix at 10% intervals; 20 steps at 5%, etc.)

The sound files' cycle order is determined by file name.

The samples-per-folder limit is 32768. You can use longer samples. However, the Organelle's RAM is not infinite, so the RAM is a limiting factor to how many files you can have and their size.

**How Do I Use This Patch?**

This patch uses four ‘pages’ accessible via the ‘Aux Menu’ to enter settings.

A typical use case would be:

1. Load the patch with your samples (or use the default samples included in patch).  
2. Set tempo.  
3. Play keys manually or record sequence.  
4. Set sample crossfade rate.  
5. Set global sample start point, length, playback speed and direction. Set global sample monophony/polyphony mode.  
6. Set EQ parameters.  
7. Repeat steps 2-6 until it all sounds great.  
8. Save your current settings with the Save command in the Organelle's Storage Menu.

To do most of the steps above you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The Low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The following commands are available on the Aux Menu's Left Column:

Seq:Play/Off - Plays or Stops selected sequence.   
Rec:Off/On - Controls Keyboard Sequence Recording. When selected, Sequence is first Record Armed (Enabled). LED will be Pink. Sequencer is waiting for knob adjustment, key press or incoming MIDI note. When knob adjusted, key pressed or MIDI Note received, Recording starts. LED is Red. To end recording, press Aux (new seq begins looping immediately). LED will be Green and flash White on quarter note. Sequence length will be quantized to nearest quarter note.   
Dub:Off/On - Overdub on top of existing sequence. Counts in 3 Sec before starting recording. To end recording, press Aux and sequence begins looping immediately.   
Undo - Reverts Sequence to previous state. If this command says 'Undid' you cannot 'undo' further.   
QNote: Turns quantizing On/Off for sequenced notes.

The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record to. Changing sequence slot will change the number that precedes the command in the left column.

The Aux Menu's Right Column controls the pages. The following pages are available:

XFade: Sets rate of change between samples on a played key. Knob1 sets steps needed to crossfade between samples. Setting rate to '1' will change samples with each 'hit'. This is the quickest rate of change and no crossfading will be heard. Step rates '2' and above will allow for progressively slower rates of change and longer periods of crossfading. Maximum number of steps between samples is '24.' 'None' will freeze the current state. The XFade setting can be changed at any time. Knob2 changes the position of the crossfader - it is fun to change while the XFade rate is set to 'None'.

Sample: Sets the global sample playback setting. Knob1 sets sample start point as a percentage of a given samples' length. Knob2 sets length of sample to be played as percentage of a given sample's length. Knob1 and Knob2 can be configured to play samples in a 'wrapped' method. For example if Knob1 is set to 50% and Knob2 is set to 100%, the sample will start playing at the sample's midpoint, continue to the end of sample, and then play the beginning half second! Knob3 sets playback speed and direction between -200% & +200%. Knob4 sets the global number voices: with 'Mono,' only one sample will be heard at a time, regardless of number keys pressed/sequenced. 'Choke' means that each key is monophonic but more than one key can be heard simultaneously. 'Poly' means that each key is polyphonic and more than one key can be heard simultaneously.

Note for Organelle 1 users: playing more than eight (8) samples at once in 'Poly' mode will probably result in maxing out the CPU and causing unwanted clicks. To avoid this, you can try playing fewer simultaneous notes and/or setting sample mode to 'Choke' or 'Mono.'

BPM: Sets the tempo for the sequencer. Knob1 dials in tempo and Knob2 offers 'fine' tempo adjustment.

EQ: Controls 4-band filter. Knob1 controls low frequency range. Knob2 controls medium-low frequency range. Knob3 controls medium-high frequency range. Knob4 controls high frequency range. Setting all ranges to 100% will result in the samples sounding like there is no filter on.

If you like a setting, don’t forget to ‘Save’ in the Storage menu.

**Tech Specs**

.Wav and .Aiff file types can be used for samples. Sample format should be 16-bit bit depth & 44.1kHz sample rate. AIFF files must have ending with two 'f's as in: 'coolsound.aiff'

MIDI notes and Start/Stop commands are sent out with sequencer.

Sequencer will respond to incoming MIDI Start/Stop messages.

Footswitch: n/a.

This patch uses the 'dir' object from the ELSE library. See the 'main.pd' file for more information about implementation within the patch. Used with License: https://github.com/porres/pd-else/blob/master/License.txt More about ELSE: https://github.com/porres/pd-else
