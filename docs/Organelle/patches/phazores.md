---
title: Phazores
date: 2021-10-15
tags:
  - Synthesizer
  - Wavetable
  - Phasor
---


# Phazores


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/IDh5chw4IaI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Synthesizer, Wavetable, Phasor

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/10/Phazores.zip)**

Frequency-synced micro-phasor wavetable synth.

## Details

**What Is This Patch?**

When you press a note on keyboard (or receive MIDI note), two things happen: 1. two synth voices are played, each with their own waveform and, 2. a phasor is applied to each voice.

The phasor rate is influenced by the note's frequency: the minimum rate is 0.001 of frequency and the maximum rate is the frequency itself (1x). For example, if you played the A4 note, your synth voices would have a frequency of 440Hz and so your phasor rate range for that key would be 0.44Hz - 440Hz. If you played A3 (220Hz), the phasor rate range for that note would be 0.22Hz - 220Hz. If you played A3 & A4 simultaneously, you might hear some interesting phasing depending on the rate settings.

There are controls for phasor depth, transpose, waveform selection, and attack time. The patch includes a sequencer and note 'latch' too.

**How Do I Use This Patch?**

A typical use case would be:   
1. Select the two waveforms to be used in synthesis.  
2. Set the keyboard octave range and attack time.   
3. Set phasor depth and rate for both oscillators.  
4. Create a sequence with the keys and/or knobs, overdub it, etc.  
5. Revisit the above steps in any order as needed.

To do step 3 above, use the Organelle knobs. Knobs 1-2 set phasor depth and rate for note voice 1. Knobs 3-4 set phasor depth and rate for note voice 2. Changes to these parameters may be recorded and looped by the patch's sequencer.

To do steps 1, 2, and 4 above you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The Right column includes the following controls:   
Wav1 - Sets waveform for note voice 1. Choose from eight options.  
Wav2 - Sets waveform for note voice 2. Choose from eight options.  
OctDn - Selecting this command will drop the keyboard one octave. Lowest transposition is -4 octaves.

OctUp - Selecting this command will raise the keyboard one octave. Maximum transposition is +4 octaves.

Att: Select note attack time in milliseconds. Cycles through 6 options.

The following commands are available on the Aux Menu's Left Column:  
Seq:Play/Stop - Plays or Stops selected sequence

Rec:Off/Armd - Controls Keyboard Sequence Recording. When selected, Sequence is first Record Armed (Enabled). LED will be Pink. Sequencer is waiting for knob adjustment, key press or incoming MIDI note. When knob adjusted, key pressed or MIDI Note received, Recording starts. LED is Red. To end recording, press Aux (new seq begins looping immediately). LED will be Green and flash White on quarter note. Sequence length will be quantized to nearest quarter note.

Dub:Off/On – Overdub on top of existing sequence. Counts in 3 Sec before starting recording. To end recording, press Aux and sequence begins looping immediately.

Undo – Reverts Sequence to previous state. If this command says 'Undid' you cannot 'undo' further.

Latch: Off/On - Turn on to keep notes playing after release.

The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record sequences to. Changing sequence slot will change the number that precedes the command in the left column.

When recording a sequence, you can record adjustments to the knobs!

If you like a recording sample and/or setting, don’t forget to ‘Save’ in the Storage menu.

TECH SPECS:  
4-Voice polyphony. If four notes are played simulanteously, a new (fifth) note will cancel oldest note.

Link enabled for syncing with other devices on a shared wireless network.

MIDI Start and Stop commands will start sequencer.

Foot Switch: N/A
