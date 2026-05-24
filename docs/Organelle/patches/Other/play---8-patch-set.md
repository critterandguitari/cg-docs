---
title: "PLAY - 8 Patch Set"
date: 2026-04-04
tags:
  - Synthesizer
  - PLAY
---


# PLAY - 8 Patch Set


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/a5P7I7kWdOE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Synthesizer, PLAY

**[Download Patch](https://patchstorage.com/wp-content/uploads/2026/04/PLAY-69e4b9e28475a.zop)**

PLAY Patches for the Organelle. Fun Synthesizers.

There are 8 Patches in the .zop. Upload to Organelle and choose Install.

Requires Organelle OS 5 - only available for Organelle S2, S, and M models. More information in the [manual](https://critterandguitari.github.io/cg-docs/Organelle/og_sms2/#71-burning-sd-card-disk-image).

## Details

The PLAY patches are synthesizers with some fun features accessed using the Aux button. They all operate in the same way, with the Aux button controlling a shift function. When you press Aux, the function of the 10 top keys on the Organelle are listed on the screen in two columns. The bottom 14 keys select various arpeggio patterns.

#### Shift Button Controls

Hold **Aux** button to access the operation menu. Black keys select functions:

| Key | Function |  
|—–|———-|  
| C# | Play/Stop |  
| D# | Arm Recording |  
| F# | Previous Preset |  
| G# | Save Preset |  
| A# | Next Preset |  
| C#+ | Octave Down |  
| D#+ | Octave Up |  
| F#+ | Latch Toggle |  
| G#+ | Metronome |  
| A#+ | Delete Preset |

The 14 white keys select different arpeggio patterns. The first key is no pattern.

#### BPM

Hold the **Aux** button while turning the encoder to adjust BPM (20-250). If you are connected to a network and a LINK session is present the Organelle will connect automatically.

#### Recording a Sequence

1. Press Arm (shift + D#) – LED turns purple  
2. Play notes and / or turn knobs – recording starts on first note or knob movement, LED turns red  
3. Press Aux to stop recording – playback begins, LED turns green

#### MIDI

Use the system MIDI Setup menu to select MIDI channel for note and CC messages.

**MIDI CC message mapping:**

| Control | CC |  
|———|—–|  
| knob1 | 21 |  
| knob2 | 22 |  
| knob3 | 23 |  
| knob4 | 24 |

**MIDI Clock Sync**

By default an internal metronome is used for timing. If you are connected to a network with other LINK devices, timing and tempo will be synchronized to those devices.

It is also possible to sync to MIDI clock.  If you send MIDI clock messages the patch will lock onto those. A MIDI start message resets to the top of the beat. If MIDI clock isn’t received for > 1 second, clock switches back to internal.
