---
title: Quilt
date: 2022-08-05
tags:
  - "Multi-effects"
  - Delay
  - Filter
  - Rhythm
---


# Quilt


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/dFTbvfTL3Xk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Multi-effects, Delay, Filter, Rhythm

**[Download Patch](https://patchstorage.com/wp-content/uploads/2022/08/Quilt.zip)**

Wrap your sound up in an animated filter band selector and tempo-synced delay for a cozy and rhythmic effect.

## Details

Incoming audio is filtered by a tempo-sycned animated frequency band selector and then sent to a tempo-synced delay effect.

This patch uses four ‘pages,’ keyboard controls, and the ‘Aux Menu’ to control the effects.

A typical use case would be:

1. Connect incoming audio.  
2. Set tempo.  
2. Set frequency band pattern.  
3. Set filter parameters.  
4. Set delay parameters.  
5. Repeat steps 2-5 until it all sounds great.   
6. Save your current settings with the Save command in the Organelle's Storage Menu.

To do most of the steps above you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The Low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

Aux Menu Guide:

The following commands are available on the Aux Menu's Left Column:

Playing / Stopped: Selecting this command starts/stops the effects.

Fill KB: Selecting this command turns all filter frequency bands 'on'. This fills the keys of the visual keyboard on the Pattern page.

Clear KB: Selecting this command turns all filter frequency bands 'off'. This clears the keys of the visual keyboard on the Pattern page.

The Aux Menu's Right Column controls the pages. As you navigate between pages, please be mindful that the knobs have a ‘takeover’ or 'catch' requirement. You have move the knob to match the value set the last time you were on that page. This prevents values from jumping to undesired settings when you choose a new page. Once you match that previous value, the knob will respond normally.

The following pages are available:

BPM: Sets the global tempo for the filter pattern and delay. Knob1 sets dial-in or tap tempo. If Dial tempo is selected, Knob2 dials in tempo and Knob3 offers 'fine' tempo adjustment. If Knob1 is set to 'Tap', pressing any keyboard key four (4) times in a row will set the tempo.    
   
Pattern: Sets the pattern of frequency band - cycle up, cycle down, random, etc., and how long the filter is set to a band. Knob1 dials in pattern. Knob2 sets note type for how quickly the frequency band changes. Knob3 sets number of notes. Knob2 and Knob3 are used in tandem. The Keyboard toggles 24 frequency bands on/off. Low frequencies are set by the lower keyboard keys, higher frequencies on the upper keys.

> Note about how keyboard frequency control and pattern setting work together: the keyboard settings are evaluated first, and then the pattern is applied. For example, say you only have the low C, low E, high C, and high E keys/frequencies 'on' and the 'Down 2' pattern selected: the patch will start on the high E and then move to the low E, skipping the C keys/frequencies. The '2' component of 'Down 2' means it skips every other frequency band - in this example, it skips over the high and low C keys.

Filter: Controls for how the filter sounds. Knob4 sets the duration as a percentage of the note type and amount set on the **Pattern** page. If the duration is '100%' the filter will align with the pattern. If duration is set higher than 100%, the filter bands will start to overlap (and you will see the visual keyboard on the **Pattern** page show more than one key highlighted. A duration less than 100% will result in the filter being turned 'off' for the balance (ex: if duration is set to 40%, the filter will be off for 60% of the currently selected frequency band duration.)  
    
Delay: Controls for the delay. Delay time is synced to the global tempo. Knob1 and Knob2 are used in tandem to set delay time: Knob1 sets rhythmic note type (eighth, quarter, etc.) and Knob2 sets number of these rhythmic notes.

If you like a setting, don’t forget to ‘Save’ in the Storage menu.

TECH SPECS:

Pressing a connected foot switch will Play or Stop the effects. You can use a foot switch instead of the Aux Menu command.

As the pattern moves from one frequency band/key to the next, a MIDI note is sent out.

Outgoing CC messages are suppressed.

Fun Thing:  
As mentioned in Tech Specs, a MIDI note is sent out as the pattern animates. This means that you can use that sent MIDI note to control the sound source that you are getting the audio from! So say you have a synth as audio source, set it to receive MIDI from your Organelle. As the pattern moves though the frequency bands, the synth and the filter will be perfectly in sync!
