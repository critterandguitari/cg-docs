---
title: KS Strings
date: 2021-08-29
tags:
  - Synthesizer
---


# KS Strings


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/mWjTGLDt0iM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Synthesizer

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/08/KS_Strings.zop)**

String synthesizer built from the Karplus-Strong algorithm.

## Details

**What Is This Patch?**  
KS Strings is a plucked/hammered string simulation synthesizer. The patch has controls for note envelope (Attack, Decay, Sustain, Release) and octave transpose. It has sequencer and latch function.

KS-Strings incorporates work from Kevin Karplus and Alexander Strong, who developed this  algorithm. More here:   
<https://en.wikipedia.org/wiki/Karplus–Strong_string_synthesis>

Miguel Moreno created and generously shared his 'str~.pd' code for the synthesis aspect of the patch. Thank you Miguel! This code and more of his work can be found here:   
<https://github.com/MikeMorenoDSP/pd-mkmr>

<https://linktr.ee/MikeMorenoDSP>

**How Do I Use This Patch?**  
This patch is provided here in the '.zop' (Zipped Organelle Package) format. This ensures proper installation on your Organelle. There are differences in processing power between the original and 'M' versions of the Organelle. The .zop installation will check which version of Organelle before installing the appropriate number of synth voices. If you have an original Organelle, KS Strings will have three-voice polyphony. The Organelle M .zop installation will install KS Strings with four-voice polyphony.

To install the .zop file, simply upload the file to your SD card or copy to your USB Drive as you normally would with other patch files. After selecting 'Reload' from the Storage menu, use the Organelle's encoder to navigate to the file location and select 'Install KS_Strings.zop.' The OLED will then display some installation information and exit upon completion.

A typical use case would be:   
1. Set note envelope with knobs1-4  
2. Set octave range for keyboard  
3. Play some notes.  
4. Record/Loop sequences of notes/knob changes.   
5. Revisit the above steps in any order as needed.

To do steps 2 & 4 above you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The following commands are available on the Aux Menu's Right Column:

OctDwn - Selecting this command will drop the keyboard one octave. Lowest transposition is -4 octaves.

OctUp - Selecting this command will raise the keyboard one octave. Maximum transposition is +4 octaves.

The following commands are available on the Aux Menu's Left Column:

Seq:Play/Stop - Plays or Stops selected sequence

Rec:Off/Armd - Controls Keyboard Sequence Recording. When selected, Sequence is first Record Armed (Enabled). LED will be Pink. Sequencer is waiting for knob adjustment, key press or incoming MIDI note. When knob adjusted, key pressed or MIDI Note received, Recording starts. LED is Red. To end recording, press Aux (new seq begins looping immediately). LED will be Green and flash White on quarter note. Sequence length will be quantized to nearest quarter note.

Dub:Off/On – Overdub on top of existing sequence. Counts in 3 Sec before starting recording. To end recording, press Aux and sequence begins looping immediately.

Undo – Reverts Sequence to previous state. If this command says 'Undid' you cannot 'undo' further.

Latch: Off/On - Turn on to keep notes playing after release.

The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record sequences to. Changing sequence slot will change the number that precedes the command in the left column.

When recording a sequence, you can record adjustments to the knobs!

______

When the Aux Menu is not visible, the patch page is displayed by default. Use Knobs 1-4 to control the note envelope:

Knob1: Attack. Set a note's attack time from 0-3000ms.  
Knob2: Decay: Set a note's decay time from 0-3000ms.  
Knob3: Sustain: Set a note's sustain level from -24 to 0 dB.   
Knob4: Release: Set a note's release time from 0-3000ms.

_______

If you like a setting, don’t forget to ‘Save’ in the Storage menu.

**Tech Specs**  
Organelle M : 4-note polyphony.  
Organelle 1 (original, no speaker, etc.) : 3-note polyphony.

MIDI Start and Stop commands will start sequencer.

Foot Switch: N/A
