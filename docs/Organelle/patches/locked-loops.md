---
title: Locked Loops
date: 2021-11-30
tags:
  - Looper
  - Recorder
  - Sampler
  - Link Enabled
---


# Locked Loops


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/YXzANk0Wsd0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Looper, Recorder, Sampler, Link Enabled

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/11/Locked-Loops.zop)**

Versatile 4-track looper w/ a focus on syncing loops. Controls for global/indiv. track start/stop, track volume, record modes, metronome, input monitor, stem creation, and mix down.

## Details

Locked Loops is a 4-track looper. Tracks can be different lengths. Change track speed without changing pitch. Record mix downs.

Installation on Organelle 1 (original) vs. Organelle M: This patch is released in the .zop format to account for RAM differences between the two Organelle models. The functional difference is the maximum loop record time. The Organelle 1 can record four 96-second loops (8 bars @ 20 BPM). The Organelle M can record four 240-second loops (20 bars @ 20 BPM).

HOW DO I USE THIS PATCH?  
This patch uses two patch ‘pages,’ keyboard controls, and the ‘Aux Menu’ to control recording, playback, and mix down. The keyboard controls can be used on either page.

A typical use case would be:   
1. Set loop length, record type, and tempo and then record to track 1.  
2. Set track 1 volume.   
3. Repeat steps 1-2 to fill the three other loops.   
4. Play 'on top' of your loops using the monitor function.  
5. Mix down your current loops to a single track.

To do most of the steps above you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The following commands are available on the Aux Menu's Left Column:

Tk.1 Rec: Selecting this command starts recording to Track 1 based on the knob settings from the Loop page (Rec. Bars, Record Mode, Tempo).  Pressing ‘Aux’ during recording will stop recording. Alternatively, this command can be called with a foot switch used in tandem with Knob 3 on the Loops page.

Tk.2 Rec: Same as Track 1 above, but for Track 2.

Tk.3 Rec: Same as Track 1 above, but for Track 3.

Tk.4 Rec: Same as Track 1 above, but for Track 4.

Page: Toggles between the ‘Loops’ and ‘Vol’ pages. On the ‘Loops’ page, the record settings are entered and recording is controlled. On the ‘Vol’ page, Knobs1-4 set the volume of the respective tracks. The knobs have a ‘takeover’ requirement. You have move the knob to match the value set the last time you were on that page. This prevents values from jumping to undesired settings when you choose a new page. Once you match that previous value, the knob will respond normally. Until that previous value is reached, the OLED screen will display that previous value with a ‘!’ after it.

The Loops page has the four knob parameters. Turning a knob will display the value at the bottom of the OLED. The knobs are:  
Knob1: Rec. Bars - sets length of recording. This must be set before recording starts. Please see note at top regarding maximum loop record duration.  
Knob2: Sets record type. Countdown Rec - counts four quarter notes at the current tempo before recording starts. Free Record starts immediately. Record type must be set before recording starts.   
Knob3: FS Rec - sets target record track when using a foot switch (FS). The target track gets a rectangle printed around the track number on OLED.  
Knob4: Tempo - sets BPM of record and playback. If a Link session or incoming MIDI clock is present, this knob can be overridden externally.

The following commands are available on the Aux Menu's Right Column:

Flash: Toggles the Metronome’s flash of the LED on the quarter note.

Tick: Toggles the Metronome’s audio ‘tick’ sound on the quarter note.

Montr: Toggles Audio 'thru' on/off.

Stems: Selecting this command will save the current tracks as ‘stems.’ The individual stem files will be saved within a new numbered folder within the ’stems’ folder within the main patch folder - the newest folder will have the highest number. You can access the ‘stems’ folder via WiFi and the browser-based Patch Manager. The patch does not have any sense of when it last created stems so if you are not paying attention, you could have more than one folder containing the same stems. Saving the stems may cause a buzzing sound - this is normal and will pass shortly!

MixDn: Selecting this command starts a new 'mix down' recording of all loops currently playing plus any audio coming in through the Audio In jack (or mic on Organelle M). You must select this command again to end the mix down recording. Recordings made with this command are added to the ‘mixdowns’ folder. The maximum length of a mix down is four minutes. the newest file will have the highest number. You can access the ‘mixdowns’ folder via WiFi and the browser-based Patch Manager. While mix down is in progress, you can switch between the Loops/Vol pages to control global track start/stop, individual track start/stop/mute and individual track volumes.

The Bottom Row of keys do not apply to the Aux Menu of this patch.

______

When the Aux Menu is not visible, the some of the keys act as transport controls:

Low C#: Global Start (restart) for all four tracks.  
Low D#: Global Stop for all four tracks.

Low C: Track 1 Start/Stop. If stopped, a square will show aside the track number. If playing, a triangle.  
Low D: Track 2 Start/Stop. If stopped, a square will show aside the track number. If playing, a triangle.  
Low E: Track 3 Start/Stop. If stopped, a square will show aside the track number. If playing, a triangle.  
Low F: Track 4 Start/Stop. If stopped, a square will show aside the track number. If playing, a triangle.

High C: Track 1 Mute toggle. If mute is active, ‘M’ will show aside track number on OLED.  
High D: Track 2 Mute toggle. If mute is active, ‘M’ will show aside track number on OLED.  
High E: Track 3 Mute toggle. If mute is active, ‘M’ will show aside track number on OLED.  
High F: Track 4 Mute toggle. If mute is active, ‘M’ will show aside track number on OLED.

_______

If you like a setting, don’t forget to ‘Save’ in the Storage menu. The Organelle may make a buzzing sound, but this is normal.

TECH SPECS:  
Link enabled.

Foot Switch: Starts / Stops new track recording.

Notes about recording & playback:  
1. The patch will remember where a currently recording track started in relation to track 1’s playhead position.   
2. Playback for an individual track will start on the next beat.  
3. Record length is a function of tempo (BPM). If BPM is ‘fast’ the record time in seconds will be shorter than if the tempo is ‘slow.’ The maximum length per loop also depends on the model of Organelle used - see note re: .zop format at the top.

You may want to add existing files to the loops folder at some point. This ‘can’ be done but may have unpredictable results because the patch is expecting to record files rather than ‘import’ them. After recording, the patch analyses the audio and stores some information about the file for later use - this does not happen on import and may lead to ‘funny’ playback settings.
