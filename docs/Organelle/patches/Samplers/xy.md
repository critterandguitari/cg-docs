---
title: XY
date: 2019-11-07
tags:
  - Sequencer
  - Sample Player
  - Synthesizer
---


# XY


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/ImXVJm2gdsI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Sequencer, Sample Player, Synthesizer

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/03/XY.zip)**

A grid-based sequencer with two playheads - one for each axis. Add ‘triggers’ to the grid to build patterns. Control playhead behavior to play grid pattern in different ways.

## Details

**What is This Patch?**  
XY is a sequencer. It uses a grid to play sounds in time. Add ‘triggers’ (sounds) to the grid by first navigating the grid with two knobs to a desired location. Then place a trigger on the grid by playing a keyboard key. The keyboard key plays a drum sample and a synth simultaneously. The grid is ‘read’ by two playheads. One playhead reads the grid in the X axis and the other playhead in the Y axis. The grid can be as large as 8x8 steps or as small as 1x1. The playheads can be set to read the grid from the low to high spots (1, 2, 3, 4, ..), high to low (8, 7, 6, 5 …), or back and forth.

Depending on your pattern and the direction of playheads, the X and Y playheads will read an individual grid trigger simultaneously and you will hear it once, or they will read the same trigger at different times and you will hear it twice. Interesting patterns can be made by using a grid of irregular size (e.g. 8x3), setting the playheads to different directions, designing a grid pattern such that triggers are not read simultaneously by each playhead, or combinations of all three.

**How Do I Use This Patch?**  
There are two pages for this patch. ‘Main’ shows a grid, oscilloscope of the currently playing sounds, sample decay envelope (in percentage), and current BPM. The ‘Options’ page  has controls for grid X and Y sizes (1-8 steps), and X & Y playhead direction.   
The Aux button starts and stops the sequencer playheads (X & Y). The keyboard plays a sample and a synth at the same time. The samples are stored in the patch’s ‘Sounds’ folder. (1.wav is played by the low C key. 24.wav is played by the high B key. These files are replaceable).

If you’re on the Main page, use Knob1 to drive around the grid’s X-axis. Knob2 drives in the Y-axis. When you get to a desired spot in the grid, add a trigger by playing the keyboard. Whichever key is pressed last on a given grid spot will be played by the playheads. A long-press by any key will clear that spot on the grid. A long Aux press will clear the whole grid. Once you have added events to your grid, press Aux to start playheads. A short press on Aux will stop playheads. Knob3 sets a trigger’s decay time. Knob4 sets tempo (unless your Organelle is receiving MIDI clock).

If you’re on the Options page, set the grid size with Knobs 1-2. Knobs 3-4 will set the playhead directions for X-Y axis respectfully. If you change settings on the Options page while the sequence is playing, you will hear these changes immediately. Stopping and then restarting sequence playback will reset the playheads back to 1 so your pattern may sound different!

If you like a pattern, don’t forget to ‘Save’ in the Storage menu.

**Tech Specs**  
The ‘Updown’ playhead direction setting plays the ‘ends’ of the grid once before moving on towards center of grid. For example, if you had a grid that was four spots wide in the X-axis, the playhead would play as follows (if starting from 1): 1, 2, 3, 4, 3, 2, 1, 2… rather than 1, 2, 3, 4, 4, 3, 2, 1, 1, 2…  This is noted so that you’ll know Updown setting will be out of phase with the Up or Down settings, but eventually they will end up at the 1 spot simulaneously.

If you want to add your own samples to the patch they are in the 'Sounds' folder. The numbers correspond to the keys. 1.wav is assigned to the low 'C' key and move up from there.

Link enabled for syncing with other devices on a shared wireless network.

MIDI Start and Stop commands will start sequencers. Grid notes are sent out as MIDI notes.

**Fun Idea**  
Send a MIDI sequence from an external device and then drive around the grid. The grid will fill up with the MIDI sequence in a random/fun/cool way.
