---
title: Breno
date: 2021-12-12
tags:
  - Looper
  - Recorder
  - Sampler
  - Link Enabled
---


# Breno


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/8kuk62r2YPc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Looper, Recorder, Sampler, Link Enabled

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/12/Breno.zop)**

Four track looper that's almost a game and great for musical experiments. The magic happens with the serial and parallel record modes, serial and parallel playback modes, and variable track lengths!

## Details

Looper that lends itself to exploring what you can do with four tracks of sound before recording ends! A recording always consists of four tracks. These tracks can be different lengths, and can be recorded in Serial mode (one track after another) or in Parallel mode (all four at once). Upon recording completion, the tracks will play back in either Serial mode (one track after another) or in Parallel mode (all four at once), regardless of how they were recorded!

Other fun stuff about this patch: Tracks stay synced up (if you want them to). There are controls for global/individual track start/stop, individual track volume, two record modes, two playback modes, metronome, input monitor, stem creation, and mix down!

Installation on Organelle 1 (original) vs. Organelle M: This patch is released in the .zop format to account for RAM differences between the two Organelle models. The functional difference is the maximum loop record time. The Organelle 1 can record four 96-second loops (8 bars @ 20 BPM). The Organelle M can record four 192-second loops (16 bars @ 20 BPM).

HOW DO I USE THIS PATCH?  
This patch uses two patch ‘pages,’ keyboard controls, and the ‘Aux Menu’ to control recording, playback, and mix down. The keyboard controls can be used on either page.

A typical use case would be:   
1. Set track lengths (in bars), record type, playback type, and tempo.  
2. Record four tracks.  
3. Try out the other playback type.   
4. Adjust track volumes.  
5. Repeat steps 1-4 until it all sounds great.   
6. Save your current settings with the Save command in the Organelle's Storage Menu.  
7. Save your current recordings as 'stems' for use outside the Organelle.  
8. Play 'on top' of your track using the monitor function.  
9. Mix down your current track to a single track.

To do most of the steps above you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The following commands are available on the Aux Menu's Left Column:

Rec Serial: Selecting this command starts recording tracks one after another based on the track length and tempo settings from the Loop page .  Pressing ‘Aux’ during recording will stop recording. Alternatively, this command can be called with a foot switch used in tandem with Knob 3 on the Loops page. There will be a count of four quarter notes at the current tempo before recording starts

Rec Parall: Selecting this command starts recording all four tracks simultaneously. Track length and tempo are set on the Loop page.  Pressing ‘Aux’ during recording will stop recording. Alternatively, this command can be called with a foot switch used in tandem with Knob 3 on the Loops page. There will be a count of four quarter notes at the current tempo before recording starts

Page: Toggles between the ‘Loops’ and ‘Vol’ pages. On the ‘Loops’ page, the record settings are entered, recording is controlled, and playback mode is set. On the ‘Vol’ page, Knobs1-4 set the volume of the respective tracks. The knobs have a ‘takeover’ requirement. You have move the knob to match the value set the last time you were on that page. This prevents values from jumping to undesired settings when you choose a new page. Once you match that previous value, the knob will respond normally. Until that previous value is reached, the OLED screen will display that previous value with a ‘!’ after it.

The Loops page has four knob parameters. Turning a knob will display the value at the bottom of the OLED. The knobs are:  
Knob1: Rec. Bars - sets length of recording in bars. Tracks are selected by pressing one of the high C#, D#, F# and G# keys and turning Knob1. The track length will be displayed on the OLED. This must be set before recording starts. Please see note at top regarding maximum loop record duration.   
Knob2: NxtPlay - sets the playback mode for the next time the Global Start key is pressed (low C#). Serial mode plays one track after another. Parallel mode plays all four at once.    
Knob3: FS Rec - sets record mode if using a footswitch.   
Knob4: Tempo - sets BPM of record and playback. If a Link session or incoming MIDI clock is present, this knob can be overridden externally.

The following commands are available on the Aux Menu's Right Column:

Flash: Toggles the Metronome’s LED flash on the quarter note on/off.

Tick: Toggles the Metronome’s audio ‘tick’ sound on the quarter note.

Montr: Toggles Audio 'thru' on/off.

Stems: Selecting this command will save the current tracks as ‘stems.’ The individual stem files will be saved within a new numbered folder within the ’stems’ folder within the main patch folder - the newest folder will have the highest number. You can access the ‘stems’ folder via WiFi and the browser-based Patch Manager. The patch does not have any sense of when it last created stems so if you are not paying attention, you could have more than one folder containing the same stems. Saving the stems may cause a buzzing sound - this is normal and will pass shortly!

MixDn: Selecting this command starts a new 'mix down' recording of all loops currently playing plus any audio coming in through the Audio In jack (or mic on Organelle M). You must select this command again to end the mix down recording. Recordings made with this command are added to the ‘mixdowns’ folder. The maximum length of a mix down is five minutes. the newest file will have the highest number. You can access the ‘mixdowns’ folder via WiFi and the browser-based Patch Manager. While mix down is in progress, you can switch between the Loops/Vol pages to control global track start/stop, individual track start/stop/mute and individual track volumes.

The Bottom Row of keys do not apply to the Aux Menu of this patch.

______

When the Aux Menu is not visible, the some of the keys act as transport controls:

Low C#: Global Start (restart) for all four tracks. Mode is set by Loop Page Knob2.  
Low D#: Global Stop for all four tracks.

Low C: Track 1 Start/Stop. If stopped, a square will show aside the track number. If playing, a triangle.  
Low D: Track 2 Start/Stop. If stopped, a square will show aside the track number. If playing, a triangle.  
Low E: Track 3 Start/Stop. If stopped, a square will show aside the track number. If playing, a triangle.  
Low F: Track 4 Start/Stop. If stopped, a square will show aside the track number. If playing, a triangle.

High C: Track 1 Mute toggle. If mute is active, ‘M’ will show aside track number on OLED.  
High D: Track 2 Mute toggle. If mute is active, ‘M’ will show aside track number on OLED.  
High E: Track 3 Mute toggle. If mute is active, ‘M’ will show aside track number on OLED.  
High F: Track 4 Mute toggle. If mute is active, ‘M’ will show aside track number on OLED.

High C#: If pressed and Knob1 turned, next recording track length in bars will show aside track number on OLED.  
High D#: Same as High C#, but for Track 2   
High E#: Same as High C#, but for Track 3   
High F#: Same as High C#, but for Track 4   
_______

If you like a setting, don’t forget to ‘Save’ in the Storage menu. The Organelle may make a buzzing sound, but this is normal.

TECH SPECS:  
Link enabled.

Foot Switch: Starts / Stops new track recording.

Notes about recording & playback:  
1. Playback for an individual track will start on the next beat.  
2. Record length is a function of tempo (BPM). If BPM is ‘fast’ the record time in seconds will be shorter than if the tempo is ‘slow.’ The maximum length per loop also depends on the model of Organelle used - see note re: .zop format at the top.

You may want to add existing files to the loops folder at some point. This ‘can’ be done but may have unpredictable results because the patch is expecting to record files rather than ‘import’ them. After recording, the patch analyzes the audio and stores some information about the file for later use - this does not happen on import and may lead to ‘funny’ playback settings.
