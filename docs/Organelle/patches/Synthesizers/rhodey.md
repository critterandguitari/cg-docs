---
title: Rhodey
date: 2016-04-20
tags:
  - Synthesizer
  - Electric Piano
  - FM
---


# Rhodey


<iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/259760347&color=%23ff5500"></iframe>

**Tags:** Synthesizer, Electric Piano, FM

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/04/Rhodey.zip)**

Electric piano emulator.

## Details

Electric piano emulation using FM synthesis.  Controls for tone, modulation, transposition and decay.  You can turn the modulation up to get tones that sound less like a Rhodes and more like a classic FM synth.  Based on the rjdj rhodey patch which itself is based on the STK rhodey code.

HOW DO I USE THIS PATCH?  
A typical use case would be:   
1. Use keys to play synth.  
2. Update synth settings.  
3. Record a sequence of knob adjustments and/or a sequence of key presses.  
4. Overdub it, etc.  
5. Revisit the above steps in any order as needed.

To do step 2, you will need to use knobs:  
Knob1: Tone  
Knob2: Modulation  
Knob3: Decay Time  
Knob4: Transposition

To do steps 3 and 4 above you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The following commands are available on the Aux Menu's Left Column:  
Seq:Play/Stop - Plays or Stops selected sequence

Rec:Off/Armd - Controls Keyboard Sequence Recording. When selected, Sequence is first Record Armed (Enabled). LED will be Pink. Sequencer is waiting for knob adjustment, key press or incoming MIDI note. When knob adjusted, key pressed or MIDI Note received, Recording starts. LED is Red. To end recording, press Aux (new seq begins looping immediately). LED will be Green and flash White on quarter note. Sequence length will be quantized to nearest quarter note.

Dub:Off/On – Overdub on top of existing sequence. Counts in 3 Sec before starting recording. To end recording, press Aux and sequence begins looping immediately.

Undo – Reverts Sequence to previous state. If this command says 'Undid' you cannot 'undo' further.

Latch: Off/On - Turn on to keep notes playing after release.

The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record sequences to. Changing sequence slot will change the number that precedes the command in the left column.

When recording a sequence, you can record adjustments to the knobs!

TECH SPECS:

Link enabled for syncing with other devices on a shared wireless network.

MIDI Start and Stop commands will start sequencer.

Foot Switch: n/a
