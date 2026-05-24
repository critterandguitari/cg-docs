---
title: Wasis
date: 2022-09-18
tags:
  - Synthesizer
  - Wavetable
  - Evolve
---


# Wasis


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/d7Lr0MYxxEI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Synthesizer, Wavetable, Evolve

**[Download Patch](https://patchstorage.com/wp-content/uploads/2022/09/Wasis.zip)**

Synthesizer with evolving waveform. Sync the evolution to tempo, key presses / sequences, or change manually. With each evolution, the subsequent partial is added to the waveform.

## Details

How do I use this patch?

This patch uses three ‘pages,’ keyboard controls, and the ‘Aux Menu’ to control the synth.

A typical use case would be:

1. Set waveform evolution parameters.  
2. Set tempo and evolution time parameters.  
3. Set synth envelope (ADSR) parameters.   
4. Record and play sequences.  
5. Repeat steps 1-4 until it all sounds great.   
6. Save your current settings with the Save command in the Organelle's Storage Menu.

To do most of the steps above you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The Low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

Aux Menu Guide:

The following commands are available on the Aux Menu's Left Column:

Seq:Play/Off - Plays or Stops selected sequence.

Rec:Off/On - Controls Keyboard Sequence Recording. When selected, Sequence is first Record Armed (Enabled). LED will be Pink. Sequencer is waiting for knob adjustment, key press or incoming MIDI note. When knob adjusted, key pressed or MIDI Note received, Recording starts. LED is Red. To end recording, press Aux (new seq begins looping immediately). LED will be Green and flash White on quarter note. Sequence length will be quantized to nearest quarter note.

Dub:Off/On - Overdub on top of existing sequence. Counts in 3 Sec before starting recording. To end recording, press Aux and sequence begins looping immediately.

Undo - Reverts Sequence to previous state. If this command says 'Undid' you cannot 'undo' further.

Latch: Turns latched (held) notes On/Off.

The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record to. Changing sequence slot will change the number that precedes the command in the left column.

The Aux Menu's Right Column controls the pages and two commands.

The following pages are available:

Wave: This page sets the waveform evolution parameters. *Knob4* sets the 'Wave Range' or how many evolutions/partials the waveform will go through before looping back to the beginning. Knob1 sets evolution method: Manual uses the Evolve and Devolve commands in the Aux Menu. The Key Press option will evolve with each key press on the Organelle's keyboard, a sequence, and/or incoming MIDI notes. Up, Down and UpDown loop in the direction of the name - e.g. Up starts with the root partial and evolves to the highest partial (set with Knob4). Knob2 selects the algorithm type of the waveform. Knob3 sets 'Rez' (Resolution) that is applied to each evolution. If the Rez is high, the new partial will have a strong influence on the new waveform; if it is low, it will have a weaker influence.  
   
Rate: Sets the different temporal aspects of the patch. Knob1 dials in tempo for the the Up, Down and UpDown evolve patterns. This knob is disabled if incoming MIDI clock or Link is present. Knob2 sets note type for how quickly the evolution occurs. The note type is dependent on Knob1's tempo setting. This parameter is disabled if the *Evolve* setting is set to Manual or Key Press. *Knob3* sets the cross fade time between evolutions. Knob4 transposes the keyboard.

ADSR: Sets the envelope for the synthesis: classic Attack, Decay, Sustain, and Release controls.

If you like a setting, don’t forget to ‘Save’ in the Storage menu.

TECH SPECS:

Foot Switch: N/A.

Four-voice polyphony.
