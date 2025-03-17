# Converting EYESY Modes from Python 2 to Python 3

This guide will help you convert your EYESY modes from Python 2 to Python 3. The conversion process involves addressing both Python language differences and EYESY API changes.

## Quick Start Approach

1. **Try Running the Mode As-Is**: Sometimes Python 2 code might work in Python 3 without modifications, especially if it doesn't use any Python 2-specific features.

2. **Fix Python 2 to Python 3 Syntax Errors**: If the mode fails to run, you'll need to update the Python syntax.

3. **Update EYESY API References**: Update the API calls for new EYESY.

## Step 1: Python 2 to Python 3 Common Conversion Issues

Here are the most common syntax changes you'll need to make:

### Print Statements
Python 2:

```python
print "Hello World"
```

Python 3:

```python
print("Hello World")
```

### Integer Division
Python 2:

```python
result = 5 / 2  # In Python 2 this returns 2
```

Python 3:

```python
result = 5 / 2  # In Python 3 this returns 2.5
result = 5 // 2  # Use this for integer division in Python 3 (returns 2)
```

### Unicode and String Handling
Python 2 has separate `str` and `unicode` types. Python 3 unifies these with all strings being Unicode by default.

### Dictionary Methods
Several dictionary methods behave differently:

```python
# Python 2
my_dict.keys()  # Returns a list
my_dict.items()  # Returns a list of tuples

# Python 3
my_dict.keys()  # Returns a view object, not a list
my_dict.items()  # Returns a view object, not a list
```

For a more comprehensive list of changes, refer to the [Python 3 Porting Guide](https://docs.python.org/3/howto/pyporting.html).

## Step 2: EYESY API Changes

### Namespace Change

In the new OS we call the main program object `eyesy` instead of `etc`. It is a good idea to change to be consistent with new version. Also provides a way to quickly see if the mode was written for old version or new version. 

OS 2:
```python
audio_data = etc.audio_in
```

OS 3:
```python
audio_data = eyesy.audio_in
```

### Specific API Changes

| Python 2 (etc)      | Python 3 (eyesy)     | Notes                                 |
|---------------------|----------------------|---------------------------------------|
| `etc.audio_in`      | `eyesy.audio_in`     | Functionality remains the same        |
| `etc.audio_trig`    | `eyesy.trig`         | Renamed                               |
| `etc.xres`          | `eyesy.xres`         | Functionality remains the same        |
| `etc.yres`          | `eyesy.yres`         | Functionality remains the same        |
| `etc.knob1-5`       | `eyesy.knob1-5`      | Functionality remains the same        |
| `etc.lastgrab`      | N/A                  | No direct equivalent mentioned        |
| `etc.lastgrab_thumb`| N/A                  | No direct equivalent mentioned        |
| `etc.midi_notes`    | `eyesy.midi_notes`   | Functionality remains the same        |
| `etc.midi_note_new` | `eyesy.midi_note_new`| Functionality remains the same        |
| `etc.mode`          | `eyesy.mode`         | Functionality remains the same        |
| `etc.mode_root`     | `eyesy.mode_root`    | Functionality remains the same        |
| `etc.color_picker_bg()`    | `eyesy.color_picker_bg()` | Functionality remains the same   |
| `etc.color_picker()`| `eyesy.color_picker()`   | Functionality remains the same    |
| N/A                 | `eyesy.color_picker_lfo()` | New function in Python 3 version|

### New Features in Python 3 Version

The OS 3 version includes a new color picker function with LFO capabilities:

```python
# Optional second parameter controls the maximum LFO rate (default is 0.1)
color = eyesy.color_picker_lfo(eyesy.knob4, 1.1)
```

## Common Errors and Solutions

1. **NameError: name 'etc' is not defined**
   - Solution: Replace all instances of `etc` with `eyesy`

2. **AttributeError: 'eyesy' object has no attribute 'audio_trig'**
   - Solution: Replace `eyesy.audio_trig` with `eyesy.trig`

3. **SyntaxError: Missing parentheses in call to 'print'**
   - Solution: Update print statements to use parentheses

4. **TypeError: 'dict_keys' object is not subscriptable**
   - Solution: Convert dictionary views to lists where needed: `list(my_dict.keys())`

## Resources for Python 2 to 3 Conversion

- [Python 3 Porting Guide](https://docs.python.org/3/howto/pyporting.html)
- [Pygame Documentation](https://www.pygame.org/docs/) for any Pygame-specific issues

## Final Testing Tips

After converting your mode:

1. Test all knob functionalities
2. Verify audio response and triggers work correctly
3. Test MIDI functionality if your mode uses it
4. Check for any performance issues that might indicate underlying problems

The most important changes to remember are:
- Replace `etc` with `eyesy`
- Replace `audio_trig` with `trig`
- Fix any Python 2 to 3 syntax issues

With these changes, your modes should successfully run on the Python 3 version of EYESY.
