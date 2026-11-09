---
title: Energia
date: 2026-07-31
tags:
  - Synthesizer

---


# Energia


**Tags:** Synthesizer

**[Download Patch](https://patchstorage.com/wp-content/uploads/2026/07/Energia-6a6ce9e19f36a.zip)**

Warm, triangle-based synth with subtle detune and vibrato, an envelope-driven filter sweep, and a bright sparkle layer on attack.

## Details

Requires Organelle OS 5

| Knob | Parameter | Description | Range |
|------|-----------|-------------|-------|
| knob1	| Attack | Envelope shape: attack, decay, and release all scale together | 0.005–0.7 sec range |
| knob2 | Zenith | Filter brightness and resonance — how far the filter opens and how much it emphasizes the cutoff |
| knob3 | Roll | Vibrato depth and speed | 5.5–17.5 Hz |
| knob4 | Phase | Detune/thickness and stereo width |

**Oscillators:** Three detuned triangle waves plus a soft sine layer blend into a warm, rounded core tone, with knob4 spreading them further apart for extra thickness.

**Notable:** A quick shimmer of high-octave sparkle on top of every note's attack. The filter opens and closes with its own envelope. Knob4 widens the stereo image with subtle chorus-style delays.


#### Operation

The PLAY patches are synthesizers with some fun features accessed using the Aux button. They all operate in the same way, with the Aux button controlling a shift function. When you press Aux, the function of the 10 top keys on the Organelle are listed on the screen in two columns. The bottom 14 keys select various arpeggio patterns.

#### Shift Button Controls

Hold **Aux** button to access the operation menu. Black keys select functions:

| Key | Function |
|---|---|
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

The 14 white keys select different arpeggio patterns. This patch includes 14 patterns that are new and different from the PLAY patches released as part of OS 5. Please customize/organize your patterns as you see fit!

| Pattern Name | Description |
| ------------ | ----------- |
| A-Paradiddle | Octave shift on the classic paradiddle pattern - eighth notes |
| B-Paradiddle2 | Octave shift on the classic paradiddle pattern - eighth notes then sixteenth |
| C-Echo | Velocity decreasing eighth notes |
| D-Faxin’ | Intro fax machine baud sound |
| E-32nd Glide | Arpeggiates four 32nd notes between the last released note and newest pressed note |
| F-Probability | Octave Arpeggiator with some probabilistic note behavior |
| G-Arps&Trips | Octave Arpeggiator with some probabilistic triplet additions |
| H-WarbleSiren | ¡Alert! |
| I-ChordScrub | Elementary cellular automata rule 30 controls if repeated note sounds or not |
| J-RandLength | Elementary cellular automata rule 30 controls repeated note length & octave shift ±2octaves |
| K-HistoArp | Remembers last 16 notes played and loops through them. Can be customized to remember shorter/longer list of notes |
| L-LiveLooper | Loops notes and fades them out. Customizable record length, number of loops, number of velocity decaying loops |
| M-DRR | Dynamic Rate Repeater - repeats notes based on how fast you initially play them (max length is one beat) |
| N-DRR Thru | Dynamic Rate Repeater - repeats notes based on how fast you initially play them (max length is one beat). Also lets note ‘through’ |
| x-None | no arpeggiation. included here for quick addition to your patterns - just change name of file to 'A-None' or which ever slot you want |

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

It is also possible to sync to MIDI clock. If you send MIDI clock messages the patch will lock onto those. A MIDI start message resets to the top of the beat. If MIDI clock isn’t received for > 1 second, clock switches back to internal.