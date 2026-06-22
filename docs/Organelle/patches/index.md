# Organelle Patches

A library of <span id="pc-count"></span> patches for the Organelle. Browse them by category in the sidebar, or filter by tag and search by name below. Combine tags to narrow things down.

<div id="patch-explorer">
  <input id="pc-search" type="text" placeholder="Search patches by name..." autocomplete="off">
  <div id="pc-cloud" class="pc-cloud"></div>
  <div id="pc-active"></div>
  <div id="pc-results" class="pc-results"></div>
</div>

<style>
#patch-explorer { margin: 1.4rem 0 2rem; }
#pc-search {
  width: 100%; box-sizing: border-box; padding: 0.6rem 0.8rem;
  font-size: inherit; border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 0.4rem; background: var(--md-default-bg-color);
  color: var(--md-default-fg-color); margin-bottom: 1.2rem;
}
.pc-cloud {
  display: flex; flex-wrap: wrap; gap: 0.4rem 0.55rem;
  align-items: baseline; line-height: 1.4; margin-bottom: 1.2rem;
}
.pc-tag {
  cursor: pointer; border-radius: 1rem; padding: 0.15em 0.7em;
  font-size: 0.8rem;
  color: var(--md-default-fg-color); background: var(--md-default-fg-color--lightest);
  white-space: nowrap; transition: background 0.12s ease, color 0.12s ease, opacity 0.12s ease;
  user-select: none;
}
.pc-tag:hover { background: var(--md-default-fg-color--lighter); }
.pc-tag .pc-n { opacity: 0.5; font-size: 0.7em; margin-left: 0.25em; }
.pc-tag.pc-on { background: var(--md-primary-fg-color); color: var(--md-primary-bg-color); }
.pc-tag.pc-on .pc-n { opacity: 0.75; }
.pc-tag.pc-dim { opacity: 0.3; }
#pc-active { margin-bottom: 1rem; font-size: 0.8rem; min-height: 1.2em; }
#pc-active a { cursor: pointer; }
.pc-results { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 0.6rem; }
.pc-item {
  display: block; padding: 0.6rem 0.8rem; border-radius: 0.4rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  text-decoration: none !important; color: var(--md-default-fg-color) !important;
  transition: border-color 0.12s ease, transform 0.12s ease;
}
.pc-item:hover { border-color: var(--md-default-fg-color--light); transform: translateY(-2px); }
.pc-item .pc-title { font-weight: 500; }
.pc-item .pc-cat { font-size: 0.72rem; opacity: 0.55; }
.pc-empty { opacity: 0.6; font-style: italic; }
</style>

<script>
(function () {
  var PATCHES = [{"t":"1008","u":"Hybrids/1008/","c":"Hybrids","g":["Multi-Instrument","Sequencer","Synthesizer","Sampler","Effect"]},{"t":"4wave","u":"Synthesizers/4wave/","c":"Synthesizers","g":["Synthesizer","Link Enabled","Wavetable"]},{"t":"4waveFM","u":"Synthesizers/4wavefm/","c":"Synthesizers","g":["Synthesizer","Link Enabled","Wavetable","FM"]},{"t":"Additive Synth","u":"Synthesizers/additive-synth/","c":"Synthesizers","g":["Additive","Synthesizer","Partials","Sequencer"]},{"t":"Analog Style","u":"Synthesizers/analog-style/","c":"Synthesizers","g":["Synthesizer","Sequencer"]},{"t":"Arp-II (AARRPP)","u":"Synthesizers/arp-ii/","c":"Synthesizers","g":["Arpeggiator","Link Enabled","Synthesizer","Probability","Randomizer","Reverb"]},{"t":"Arp-III (AAARRRPPP)","u":"Synthesizers/arp-iii/","c":"Synthesizers","g":["Arpeggiator","Synthesizer","Probability","Randomizer","Link Enabled"]},{"t":"Arpeggio Sampler","u":"Samplers/arpeggio-sampler/","c":"Samplers","g":["Arpeggiator","Link Enabled","Sampler"]},{"t":"Arpeggio Synth","u":"Synthesizers/arpeggio-synth/","c":"Synthesizers","g":["Arpeggiator","Synthesizer","Link Enabled"]},{"t":"Basic Poly","u":"Synthesizers/basic-poly/","c":"Synthesizers","g":["Synthesizer","Vibrato"]},{"t":"Basic Sampler","u":"Samplers/basic-sampler/","c":"Samplers","g":["Sampler"]},{"t":"Beats and Pieces","u":"Samplers/beats-and-pieces/","c":"Samplers","g":["Sample Player","Delay"]},{"t":"Breno","u":"Samplers/breno/","c":"Samplers","g":["Looper","Recorder","Sampler","Link Enabled"]},{"t":"BS FX PB","u":"Hybrids/bs-fx-pb/","c":"Hybrids","g":["Sampler","Sequencer","Polybeats","Multi-effects","Link Enabled"]},{"t":"CA Additive","u":"Synthesizers/ca-additive/","c":"Synthesizers","g":["Cellular Automata","Additive","Synthesizer"]},{"t":"CA Filter","u":"Effects/ca-filter/","c":"Effects","g":["Cellular Automata","Filter","Effect"]},{"t":"CAmenti","u":"Samplers/camenti/","c":"Samplers","g":["Sampler","Cellular Automata","Generative"]},{"t":"Cannabits","u":"Effects/cannabits/","c":"Effects","g":["Effect","Randomizer","Automation","Link Enabled","Weirdmaker","Multi-effects"]},{"t":"CCquencer2","u":"Other/ccquencer2/","c":"Other","g":["Automation","Utility","Sequencer"]},{"t":"Children of Sample","u":"Samplers/children-of-sample/","c":"Samplers","g":["Sampler","Sequencer","Sample Player","Delay"]},{"t":"Chordi","u":"Synthesizers/chordi/","c":"Synthesizers","g":["Chords","Looper","Sampler","Sample Player"]},{"t":"Chords Roll","u":"Synthesizers/chords-roll/","c":"Synthesizers","g":["Chords","Synthesizer"]},{"t":"Constant Gardener","u":"Effects/constant-gardener/","c":"Effects","g":["Phase Vocoder","Effect","Mixer","Vocoder","Reverb"]},{"t":"Countdown Timer","u":"Utilities/countdown-timer/","c":"Utilities","g":["Timer","Alarm","Synthesizer"]},{"t":"Cycler","u":"Samplers/cycler/","c":"Samplers","g":["Segment Player","Sample Player","Sampler","Sequencer","Filter","Mixer"]},{"t":"CZZ-Multi","u":"Synthesizers/czz-multi/","c":"Synthesizers","g":["Synthesizer","Sequencer"]},{"t":"Deterior","u":"Effects/deterior/","c":"Effects","g":["Effect","Multi-effects","Looper","Sampler","Sample Player"]},{"t":"Distributor","u":"Samplers/distributor/","c":"Samplers","g":["Sample Player","Link Enabled","Arpeggiator","Looper"]},{"t":"Distributor Rec","u":"Samplers/distributor-rec/","c":"Samplers","g":["Sampler","Sample Player","Arpeggiator","Link Enabled","Looper","Sequencer"]},{"t":"DJ Patch","u":"Samplers/dj-patch/","c":"Samplers","g":["Sample Player","Looper","Weirdmaker"]},{"t":"DJ Patch Record","u":"Samplers/dj-patch-record/","c":"Samplers","g":["Sampler","Looper","Recorder","Weirdmaker","Sample Player"]},{"t":"Drone 1","u":"Synthesizers/drone-1/","c":"Synthesizers","g":["Drone","Synthesizer","Harmonic"]},{"t":"Dropper","u":"Synthesizers/dropper/","c":"Synthesizers","g":["Synthesizer"]},{"t":"Drummy","u":"Synthesizers/drummy/","c":"Synthesizers","g":["Drum Machine","Sequencer","Synthesizer"]},{"t":"EnvelopeFX","u":"Effects/envelopefx/","c":"Effects","g":["Multi-effects","Envelope","Effect","Automation"]},{"t":"Euclidean Rhythms","u":"Samplers/euclidean-rhythms/","c":"Samplers","g":["Drum Machine","Rhythm Maker","Link Enabled","Sample Player"]},{"t":"Freeze by Tempo","u":"Effects/freeze-by-tempo/","c":"Effects","g":["Effect","Looper","Link Enabled"]},{"t":"Freeze Patch","u":"Effects/freeze-patch/","c":"Effects","g":["Effect","Link Enabled","Looper"]},{"t":"FunFX","u":"Synthesizers/funfx/","c":"Synthesizers","g":["Effect","Sequencer"]},{"t":"FX-13","u":"Effects/fx-13/","c":"Effects","g":["Multi-effects","Effect","Reverb","Delay","Distortion"]},{"t":"Genny 1","u":"Synthesizers/genny-1/","c":"Synthesizers","g":["Synthesizer","Generative","Arpeggiator"]},{"t":"Genny HRando FX","u":"Hybrids/genny-hrando-fx/","c":"Hybrids","g":["Randomizer","Sample Player","Generative","Multi-effects"]},{"t":"Granular Freezer","u":"Effects/granular-freezer/","c":"Effects","g":["Granular","Sampler","Effect","Delay"]},{"t":"Guitar2ARP","u":"Effects/guitar2arp/","c":"Effects","g":["Pitch Tracker","Arpeggiator","Synthesizer","Effect","Link Enabled"]},{"t":"Guitar2Synth","u":"Effects/guitar2synth/","c":"Effects","g":["Pitch Tracker","Synthesizer"]},{"t":"h Rando","u":"Samplers/h-rando/","c":"Samplers","g":["Sample Player","Drum Machine","Randomizer","Sequencer"]},{"t":"I Take Up","u":"Samplers/i-take-up/","c":"Samplers","g":["Sampler","Weirdmaker","Recorder","Looper"]},{"t":"I Take Up - Quantize (ITUQ)","u":"Other/i-take-up-quantize/","c":"Other","g":["Looper","Weirdmaker","Sequencer","Sampler","Link Enabled","Recorder"]},{"t":"Jeraphy","u":"Samplers/jeraphy/","c":"Samplers","g":["Sample Player","Looper","Link Enabled","Rhythm Maker"]},{"t":"Jeraphy Simple","u":"Other/jeraphy-simple/","c":"Other","g":["Sample Player","Looper","Link Enabled","Rhythm Maker"]},{"t":"K-Loop","u":"Samplers/k-loop/","c":"Samplers","g":["Looper","Recorder","Sampler","Weirdmaker"]},{"t":"K-LoopOver","u":"Samplers/k-loopover/","c":"Samplers","g":["Looper","Recorder","Sampler","Weirdmaker"]},{"t":"KS Strings","u":"Synthesizers/ks-strings/","c":"Synthesizers","g":["Synthesizer"]},{"t":"Laura Derwn","u":"Other/laura-derwn/","c":"Other","g":["Pitch Shift","Effect","Vibrato"]},{"t":"LFO Delay","u":"Effects/lfo-delay/","c":"Effects","g":["Effect","LFO","Delay"]},{"t":"LFOmlog","u":"Synthesizers/lfomlog/","c":"Synthesizers","g":["LFO","Synthesizer"]},{"t":"Locked Loops","u":"Samplers/locked-loops/","c":"Samplers","g":["Looper","Recorder","Sampler","Link Enabled"]},{"t":"Loop Jam Rec","u":"Samplers/loop-jam-rec/","c":"Samplers","g":["Sampler","Looper","Recorder"]},{"t":"Metronome","u":"Utilities/metronome/","c":"Utilities","g":["Utility","Link Enabled","Synthesizer","Timer"]},{"t":"Midi File Sampler","u":"Samplers/midi-file-sampler/","c":"Samplers","g":["MIDI","Sampler","Sequencer","Link Enabled"]},{"t":"Midi File Synth","u":"Synthesizers/midi-file-synth/","c":"Synthesizers","g":["MIDI","Synthesizer","Sequencer","Link Enabled"]},{"t":"MIDI Maker","u":"Other/midi-maker/","c":"Other","g":["Pitch Tracker","MIDI","Automation","Utility"]},{"t":"MIDI Maker Tempo","u":"Other/midi-maker-tempo/","c":"Other","g":["Pitch Tracker","MIDI","Automation","Utility"]},{"t":"Mutations 23","u":"Samplers/mutations-23/","c":"Samplers","g":["Multi-effects","Delay","Effect","Filter","Sequencer","Sampler","Recorder","Looper"]},{"t":"Namesake","u":"Synthesizers/namesake/","c":"Synthesizers","g":["Synthesizer"]},{"t":"Nice Surprises","u":"Synthesizers/nice-surprises/","c":"Synthesizers","g":["Synthesizer","Sequencer"]},{"t":"Nice Surprises Poly","u":"Synthesizers/nice-surprises-poly/","c":"Synthesizers","g":["Synthesizer","Sequencer"]},{"t":"Nori Grains","u":"Samplers/nori-grains/","c":"Samplers","g":["Granular","Sampler","Randomizer","Drone"]},{"t":"Nori Sampler","u":"Samplers/nori-sampler/","c":"Samplers","g":["Sampler"]},{"t":"Nori Sampler Mono","u":"Samplers/nori-sampler-mono/","c":"Samplers","g":["Sampler"]},{"t":"Overloop","u":"Samplers/overloop/","c":"Samplers","g":["Sampler","Looper","Recorder"]},{"t":"Partial Party","u":"Synthesizers/partial-party/","c":"Synthesizers","g":["Synthesizer","Effect","Partials","Pitch Tracker"]},{"t":"PB HRando FX13","u":"Hybrids/pb-hrando-fx13/","c":"Hybrids","g":["Sampler","Randomizer","Sequencer","Link Enabled"]},{"t":"Phase Vocoder","u":"Samplers/phase-vocoder/","c":"Samplers","g":["Phase Vocoder","Sampler","Looper"]},{"t":"Phazores","u":"Synthesizers/phazores/","c":"Synthesizers","g":["Synthesizer","Wavetable","Phasor"]},{"t":"PingPongInn","u":"Other/ping-pong-inn/","c":"Other","g":["Panning","Weirdmaker","Effect"]},{"t":"Pink Mode","u":"Synthesizers/pink-mode/","c":"Synthesizers","g":["Sequencer","Synthesizer","Link Enabled"]},{"t":"PLAY - 8 Patch Set","u":"Other/play---8-patch-set/","c":"Other","g":["Synthesizer","PLAY"]},{"t":"Polybeats DRG32V","u":"Samplers/polybeats-drg32v/","c":"Samplers","g":["Drum Machine","Sequencer","Link Enabled","Polybeats"]},{"t":"Pow Pow's Polybeats","u":"Samplers/pow-pows-polybeats/","c":"Samplers","g":["Drum Machine","Link Enabled","Polybeats","Sample Player"]},{"t":"Prairie Loops","u":"Samplers/prairie-loops/","c":"Samplers","g":["Looper","Recorder","Sample Player","Sampler","Weirdmaker"]},{"t":"Punchy","u":"Synthesizers/punchy/","c":"Synthesizers","g":["Synthesizer","Sequencer","Arpeggiator","Link Enabled"]},{"t":"Punchy HRando FX","u":"Hybrids/punchy-hrando-fx/","c":"Hybrids","g":["Sequencer","Randomizer","Sampler","Link Enabled","Multi-effects"]},{"t":"Quad Delay","u":"Effects/quad-delay/","c":"Effects","g":["Delay","Effect"]},{"t":"Quad Delay Tuned","u":"Other/quad-delay-tuned/","c":"Other","g":["Effect"]},{"t":"Quilt","u":"Effects/quilt/","c":"Effects","g":["Multi-effects","Delay","Filter","Rhythm"]},{"t":"Rampi","u":"Synthesizers/rampi/","c":"Synthesizers","g":["Synthesizer"]},{"t":"Rampi Bass Synth","u":"Other/rampi-bass-synth/","c":"Other","g":["Synthesizer","Bass","Sequencer"]},{"t":"Rampi PB","u":"Hybrids/rampi-pb/","c":"Hybrids","g":["Synthesizer","Sequencer","Polybeats","Link Enabled"]},{"t":"Randomlog","u":"Synthesizers/randomlog/","c":"Synthesizers","g":["Synthesizer","Randomizer","Sequencer","Envelope","Filter"]},{"t":"Recorder","u":"Samplers/recorder/","c":"Samplers","g":["Recorder","Sampler"]},{"t":"Repeats","u":"Samplers/repeats/","c":"Samplers","g":["Rhythm","Rhythm Maker","Drum Machine","Sample Player","Link Enabled"]},{"t":"Repeats the Synth","u":"Synthesizers/repeats-the-synth/","c":"Synthesizers","g":["Sequencer","Synthesizer","Multi-Instrument"]},{"t":"Rhodey","u":"Synthesizers/rhodey/","c":"Synthesizers","g":["Synthesizer","Electric Piano","FM"]},{"t":"Rhythm Delay Distortion","u":"Effects/rhythm-delay-dist/","c":"Effects","g":["Effect","Distortion","Delay","Link Enabled","Sequencer","Polybeats"]},{"t":"Sampler Style","u":"Other/sampler-style/","c":"Other","g":["Sequencer","Sample Player"]},{"t":"Sampler Style Delay","u":"Samplers/sampler-style-delay/","c":"Samplers","g":["Sample Player","Sequencer","Delay"]},{"t":"Sampler Style REC","u":"Samplers/sampler-style-rec/","c":"Samplers","g":["Sampler","Recorder"]},{"t":"Segmenti","u":"Samplers/segmenti/","c":"Samplers","g":["Sampler","Recorder","Sequencer"]},{"t":"Segmenti Arp","u":"Samplers/segmenti-arp/","c":"Samplers","g":["Arpeggiator","Sampler","Sequencer","Recorder","Link Enabled"]},{"t":"Side-Chain","u":"Effects/side-chain/","c":"Effects","g":["Mixer","Delay","Compressor","Automation","Link Enabled","MIDI","Envelope","Effect"]},{"t":"Sine Surprises","u":"Synthesizers/sine-surprises/","c":"Synthesizers","g":["Synthesizer","Sequencer"]},{"t":"Steppy Delay","u":"Synthesizers/steppy-delay/","c":"Synthesizers","g":["Synthesizer","Sequencer","Link Enabled"]},{"t":"Stereo Rhythmicon","u":"Synthesizers/stereo-rhythmicon/","c":"Synthesizers","g":["Synthesizer","Rhythm","Generative","Link Enabled"]},{"t":"Tapey","u":"Samplers/tapey/","c":"Samplers","g":["Sampler","Link Enabled","Looper","Sample Player"]},{"t":"Thery Scary","u":"Synthesizers/thery-scary/","c":"Synthesizers","g":["Theremin","Synthesizer","Background"]},{"t":"Three Tracks","u":"Hybrids/three-tracks/","c":"Hybrids","g":["Sequencer","Automation","Link Enabled","Synthesizer","Sample Player","LFO","Looper"]},{"t":"Transient Segmenti","u":"Samplers/transient-segmenti/","c":"Samplers","g":["Segment Player","Recorder","Looper","Sequencer","Rhythm Maker"]},{"t":"Tune D PB","u":"Hybrids/tune-d-pb/","c":"Hybrids","g":["Synthesizer","Sequencer"]},{"t":"Tuned Delay","u":"Synthesizers/tuned-delay/","c":"Synthesizers","g":["Synthesizer","Delay","Sequencer"]},{"t":"Update-OS-v2.1","u":"Other/update-os-v2-1/","c":"Other","g":["OS Update","Utility"]},{"t":"UpdateOS-3.1","u":"Other/updateos-3-1/","c":"Other","g":["OS Update","Utility"]},{"t":"Vocoder RL","u":"Effects/vocoder-rl/","c":"Effects","g":["Vocoder","Synthesizer","Reverb"]},{"t":"Wasis","u":"Synthesizers/wasis/","c":"Synthesizers","g":["Synthesizer","Wavetable","Evolve"]},{"t":"Waterfall 2.0","u":"Synthesizers/waterfall-2-0/","c":"Synthesizers","g":["Synthesizer","Arpeggiator"]},{"t":"Waterfall Down","u":"Other/waterfall-down/","c":"Other","g":["Synthesizer","Chords"]},{"t":"Waterfall Up","u":"Other/waterfall-up/","c":"Other","g":["Synthesizer","Chords"]},{"t":"Wepa!","u":"Wepa%21/wepa/","c":"Wepa!","g":["Sample Player","Sampler","Delay"]},{"t":"XY","u":"Samplers/xy/","c":"Samplers","g":["Sequencer","Sample Player","Synthesizer"]},{"t":"Ypolimenti","u":"Other/ypolimenti/","c":"Other","g":["Sampler","Polybeats","Segment Player","Link Enabled"]},{"t":"Zample","u":"Samplers/zample/","c":"Samplers","g":["Sampler","Sequencer","Sample Player","Recorder","Weirdmaker","LFO","Mixer"]},{"t":"Zone","u":"Synthesizers/zone/","c":"Synthesizers","g":["Synthesizer","Wavetable","LFO"]}];
  var active = new Set();
  var search = "";

  var counts = {};
  PATCHES.forEach(function (p) { p.g.forEach(function (t) { counts[t] = (counts[t] || 0) + 1; }); });
  var tags = Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a] || a.localeCompare(b); });

  var cloud = document.getElementById("pc-cloud");
  tags.forEach(function (t) {
    var el = document.createElement("span");
    el.className = "pc-tag";
    el.dataset.tag = t;
    el.innerHTML = t.replace(/&/g, "&amp;").replace(/</g, "&lt;") + '<span class="pc-n">' + counts[t] + "</span>";
    el.addEventListener("click", function () {
      if (active.has(t)) active.delete(t); else active.add(t);
      render();
    });
    cloud.appendChild(el);
  });

  var searchBox = document.getElementById("pc-search");
  searchBox.addEventListener("input", function () { search = this.value.trim().toLowerCase(); render(); });

  function matches(p) {
    if (search && p.t.toLowerCase().indexOf(search) === -1) return false;
    for (var t of active) { if (p.g.indexOf(t) === -1) return false; }
    return true;
  }

  function render() {
    var shown = PATCHES.filter(matches);

    document.getElementById("pc-count").textContent = PATCHES.length;

    // remaining tags among the shown set, for dimming dead-ends
    var live = {};
    shown.forEach(function (p) { p.g.forEach(function (t) { live[t] = true; }); });
    Array.prototype.forEach.call(cloud.children, function (el) {
      var t = el.dataset.tag;
      el.classList.toggle("pc-on", active.has(t));
      el.classList.toggle("pc-dim", !active.has(t) && !live[t]);
    });

    var act = document.getElementById("pc-active");
    if (active.size) {
      act.innerHTML = "Filtering by <strong>" + Array.from(active).map(function (t) {
        return t.replace(/&/g, "&amp;").replace(/</g, "&lt;");
      }).join("</strong> + <strong>") + "</strong> &nbsp; <a id='pc-clear'>clear ×</a>";
      document.getElementById("pc-clear").addEventListener("click", function () { active.clear(); render(); });
    } else {
      act.innerHTML = "";
    }

    var res = document.getElementById("pc-results");
    if (!shown.length) {
      res.innerHTML = '<p class="pc-empty">No patches match that combination.</p>';
      return;
    }
    res.innerHTML = shown.map(function (p) {
      return '<a class="pc-item" href="' + p.u + '">' +
        '<span class="pc-title">' + p.t.replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</span><br>" +
        '<span class="pc-cat">' + p.c + "</span></a>";
    }).join("");
  }

  render();
})();
</script>
