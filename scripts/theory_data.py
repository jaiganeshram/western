# -*- coding: utf-8 -*-
"""
Western Music Theory Datasets:
- Circle of Fifths & 12 Major Keys
- 7 Church Modes (Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian)
- Pentatonic & Blues Scales
- Chord Dictionary & Inversions
- 12 Western Intervals & Song Mnemonics
- 7 Octaves System (C1 to C7)
"""

CIRCLE_OF_FIFTHS = [
    {
        "key": "C Major",
        "root": "C",
        "accidentals": "0 ♯ / 0 ♭",
        "sharps": 0,
        "flats": 0,
        "relMinor": "A Minor (Am)",
        "notes": ["C", "D", "E", "F", "G", "A", "B"],
        "desc": "All natural white keys • The foundational major key of Western music."
    },
    {
        "key": "G Major",
        "root": "G",
        "accidentals": "1 ♯ (F#)",
        "sharps": 1,
        "flats": 0,
        "relMinor": "E Minor (Em)",
        "notes": ["G", "A", "B", "C", "D", "E", "F#"],
        "desc": "1 Sharp (F#) • Serene, bright, and pastoral tone."
    },
    {
        "key": "D Major",
        "root": "D",
        "accidentals": "2 ♯ (F#, C#)",
        "sharps": 2,
        "flats": 0,
        "relMinor": "B Minor (Bm)",
        "notes": ["D", "E", "F#", "G", "A", "B", "C#"],
        "desc": "2 Sharps • Triumphant, majestic, and bright (Pachelbel Canon)."
    },
    {
        "key": "A Major",
        "root": "A",
        "accidentals": "3 ♯ (F#, C#, G#)",
        "sharps": 3,
        "flats": 0,
        "relMinor": "F# Minor (F#m)",
        "notes": ["A", "B", "C#", "D", "E", "F#", "G#"],
        "desc": "3 Sharps • Joyful, brilliant, and youthful character."
    },
    {
        "key": "E Major",
        "root": "E",
        "accidentals": "4 ♯ (F#, C#, G#, D#)",
        "sharps": 4,
        "flats": 0,
        "relMinor": "C# Minor (C#m)",
        "notes": ["E", "F#", "G#", "A", "B", "C#", "D#"],
        "desc": "4 Sharps • Powerful, resonant classical and rock key."
    },
    {
        "key": "B Major",
        "root": "B",
        "accidentals": "5 ♯ (F#, C#, G#, D#, A#)",
        "sharps": 5,
        "flats": 0,
        "relMinor": "G# Minor (G#m)",
        "notes": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
        "desc": "5 Sharps • Sparkling and brilliant; utilizes 5 black keys."
    },
    {
        "key": "F# / Gb Major",
        "root": "F#",
        "accidentals": "6 ♯ / 6 ♭",
        "sharps": 6,
        "flats": 6,
        "relMinor": "D#m / Ebm",
        "notes": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
        "desc": "The polar point of the Circle of Fifths • 6 Sharps or 6 Flats."
    },
    {
        "key": "Db Major",
        "root": "Db",
        "accidentals": "5 ♭ (Bb, Eb, Ab, Db, Gb)",
        "sharps": 0,
        "flats": 5,
        "relMinor": "Bb Minor (Bbm)",
        "notes": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
        "desc": "5 Flats • Warm, lush, romantic piano key (Debussy Clair de Lune)."
    },
    {
        "key": "Ab Major",
        "root": "Ab",
        "accidentals": "4 ♭ (Bb, Eb, Ab, Db)",
        "sharps": 0,
        "flats": 4,
        "relMinor": "F Minor (Fm)",
        "notes": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
        "desc": "4 Flats • Noble, deeply resonant, and majestic key."
    },
    {
        "key": "Eb Major",
        "root": "Eb",
        "accidentals": "3 ♭ (Bb, Eb, Ab)",
        "sharps": 0,
        "flats": 3,
        "relMinor": "C Minor (Cm)",
        "notes": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
        "desc": "3 Flats • Heroic and bold (Beethoven's Emperor Concerto & Eroica)."
    },
    {
        "key": "Bb Major",
        "root": "Bb",
        "accidentals": "2 ♭ (Bb, Eb)",
        "sharps": 0,
        "flats": 2,
        "relMinor": "G Minor (Gm)",
        "notes": ["Bb", "C", "D", "Eb", "F", "G", "A"],
        "desc": "2 Flats • Favorite key for jazz, brass, and wind instruments."
    },
    {
        "key": "F Major",
        "root": "F",
        "accidentals": "1 ♭ (Bb)",
        "sharps": 0,
        "flats": 1,
        "relMinor": "D Minor (Dm)",
        "notes": ["F", "G", "A", "Bb", "C", "D", "E"],
        "desc": "1 Flat (Bb) • Pastoral, calm, and naturally serene key."
    }
]

WESTERN_MODES = [
    {
        "name": "1. Ionian Mode (Major Scale)",
        "formula": "1 - 2 - 3 - 4 - 5 - 6 - 7",
        "intervals": "W - W - H - W - W - W - H",
        "c_notes": "C - D - E - F - G - A - B - C",
        "mood": "Joyful, bright, uplifting, and resolute",
        "carnatic_eq": "Raga Sankarabharanam (29th Melakarta)",
        "demo": ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
    },
    {
        "name": "2. Dorian Mode (Jazz Minor)",
        "formula": "1 - 2 - ♭3 - 4 - 5 - 6 - ♭7",
        "intervals": "W - H - W - W - W - H - W",
        "c_notes": "C - D - Eb - F - G - A - Bb - C",
        "mood": "Soulful jazz, medieval folk, nostalgic (Greensleeves, Miles Davis)",
        "carnatic_eq": "Raga Kharaharapriya (22nd Melakarta)",
        "demo": ["C4", "D4", "Eb4", "F4", "G4", "A4", "Bb4", "C5"]
    },
    {
        "name": "3. Phrygian Mode (Spanish / Flamenco)",
        "formula": "1 - ♭2 - ♭3 - 4 - 5 - ♭6 - ♭7",
        "intervals": "H - W - W - W - H - W - W",
        "c_notes": "C - Db - Eb - F - G - Ab - Bb - C",
        "mood": "Spanish flamenco, dark passion, exotic mystery",
        "carnatic_eq": "Raga Hanumatodi (8th Melakarta)",
        "demo": ["C4", "Db4", "Eb4", "F4", "G4", "Ab4", "Bb4", "C5"]
    },
    {
        "name": "4. Lydian Mode (Cinematic Dream)",
        "formula": "1 - 2 - 3 - ♯4 - 5 - 6 - 7",
        "intervals": "W - W - W - H - W - W - H",
        "c_notes": "C - D - E - F# - G - A - B - C",
        "mood": "Ethereal, film score wonder, floating dream (ET, Star Wars)",
        "carnatic_eq": "Raga Mechakalyani (65th Melakarta)",
        "demo": ["C4", "D4", "E4", "F#4", "G4", "A4", "B4", "C5"]
    },
    {
        "name": "5. Mixolydian Mode (Blues & Rock)",
        "formula": "1 - 2 - 3 - 4 - 5 - 6 - ♭7",
        "intervals": "W - W - H - W - W - H - W",
        "c_notes": "C - D - E - F - G - A - Bb - C",
        "mood": "Classic rock, blues groove, energetic (Sweet Home Alabama, Hey Jude)",
        "carnatic_eq": "Raga Harikambhoji (28th Melakarta)",
        "demo": ["C4", "D4", "E4", "F4", "G4", "A4", "Bb4", "C5"]
    },
    {
        "name": "6. Aeolian Mode (Natural Minor)",
        "formula": "1 - 2 - ♭3 - 4 - 5 - ♭6 - ♭7",
        "intervals": "W - H - W - W - H - W - W",
        "c_notes": "C - D - Eb - F - G - Ab - Bb - C",
        "mood": "Melancholic, reflective, deep emotion",
        "carnatic_eq": "Raga Natabhairavi (20th Melakarta)",
        "demo": ["C4", "D4", "Eb4", "F4", "G4", "Ab4", "Bb4", "C5"]
    },
    {
        "name": "7. Locrian Mode (Diminished Tension)",
        "formula": "1 - ♭2 - ♭3 - 4 - ♭5 - ♭6 - ♭7",
        "intervals": "H - W - W - H - W - W - W",
        "c_notes": "C - Db - Eb - F - Gb - Ab - Bb - C",
        "mood": "Extreme tension, unresolved, dark diminished color",
        "carnatic_eq": "Theoretical diminished structure",
        "demo": ["C4", "Db4", "Eb4", "F4", "Gb4", "Ab4", "Bb4", "C5"]
    },
    {
        "name": "8. Major Pentatonic (5 Notes)",
        "formula": "1 - 2 - 3 - 5 - 6",
        "intervals": "W - W - 1.5W - W - 1.5W",
        "c_notes": "C - D - E - G - A - C",
        "mood": "Universal folk warmth, harmonious, joyful (Amazing Grace)",
        "carnatic_eq": "Raga Mohanam",
        "demo": ["C4", "D4", "E4", "G4", "A4", "C5"]
    },
    {
        "name": "9. Minor Pentatonic (Blues Foundation)",
        "formula": "1 - ♭3 - 4 - 5 - ♭7",
        "intervals": "1.5W - W - W - 1.5W - W",
        "c_notes": "C - Eb - F - G - Bb - C",
        "mood": "The heartbeat of rock solos, blues licks, and soulful riffs",
        "carnatic_eq": "Raga Suddha Dhanyasi",
        "demo": ["C4", "Eb4", "F4", "G4", "Bb4", "C5"]
    },
    {
        "name": "10. Blues Scale (Hexatonic)",
        "formula": "1 - ♭3 - 4 - ♭5 - 5 - ♭7",
        "intervals": "1.5W - W - H - H - 1.5W - W",
        "c_notes": "C - Eb - F - F# - G - Bb - C",
        "mood": "The quintessential 'Blue Note' (♭5) tension and soulful swagger",
        "carnatic_eq": "Vakra Blues Raga Structure",
        "demo": ["C4", "Eb4", "F4", "F#4", "G4", "Bb4", "C5"]
    }
]

WESTERN_INTERVALS = [
    {"semi": 0, "name": "Unison (P1)", "nameTa": "Perfect Unison", "ratio": "1:1", "example": "Same Pitch", "notes": ["C4", "C4"]},
    {"semi": 1, "name": "Minor 2nd (m2)", "nameTa": "Half Step / Semitone", "ratio": "16:15", "example": "Theme from Jaws", "notes": ["C4", "Db4"]},
    {"semi": 2, "name": "Major 2nd (M2)", "nameTa": "Whole Step / Tone", "ratio": "9:8", "example": "Happy Birthday opening", "notes": ["C4", "D4"]},
    {"semi": 3, "name": "Minor 3rd (m3)", "nameTa": "Minor Third", "ratio": "6:5", "example": "Greensleeves / Lullaby", "notes": ["C4", "Eb4"]},
    {"semi": 4, "name": "Major 3rd (M3)", "nameTa": "Major Third", "ratio": "5:4", "example": "When the Saints Go Marching In", "notes": ["C4", "E4"]},
    {"semi": 5, "name": "Perfect 4th (P4)", "nameTa": "Perfect Fourth", "ratio": "4:3", "example": "Here Comes the Bride", "notes": ["C4", "F4"]},
    {"semi": 6, "name": "Tritone (TT / Dim 5th)", "nameTa": "Tritone / Devil's Interval", "ratio": "45:32", "example": "The Simpsons theme / Maria", "notes": ["C4", "F#4"]},
    {"semi": 7, "name": "Perfect 5th (P5)", "nameTa": "Perfect Fifth", "ratio": "3:2", "example": "Star Wars / Twinkle Twinkle", "notes": ["C4", "G4"]},
    {"semi": 8, "name": "Minor 6th (m6)", "nameTa": "Minor Sixth", "ratio": "8:5", "example": "The Entertainer ragtime", "notes": ["C4", "Ab4"]},
    {"semi": 9, "name": "Major 6th (M6)", "nameTa": "Major Sixth", "ratio": "5:3", "example": "NBC Chimes / My Bonnie", "notes": ["C4", "A4"]},
    {"semi": 10, "name": "Minor 7th (m7)", "nameTa": "Minor Seventh", "ratio": "16:9", "example": "Somewhere (West Side Story)", "notes": ["C4", "Bb4"]},
    {"semi": 11, "name": "Major 7th (M7)", "nameTa": "Major Seventh", "ratio": "15:8", "example": "Take On Me (A-ha chorus)", "notes": ["C4", "B4"]},
    {"semi": 12, "name": "Perfect Octave (P8)", "nameTa": "Perfect Octave", "ratio": "2:1", "example": "Somewhere Over the Rainbow", "notes": ["C4", "C5"]}
]

CHORD_TYPES = {
    "maj": {"name": "Major Triad", "nameTa": "Major Triad (Bright & Resolute)", "formula": "1 - 3 - 5", "semis": [0, 4, 7], "symbol": ""},
    "min": {"name": "Minor Triad", "nameTa": "Minor Triad (Emotional & Somber)", "formula": "1 - ♭3 - 5", "semis": [0, 3, 7], "symbol": "m"},
    "dim": {"name": "Diminished", "nameTa": "Diminished Triad (Tense & Narrow)", "formula": "1 - ♭3 - ♭5", "semis": [0, 3, 6], "symbol": "dim"},
    "aug": {"name": "Augmented", "nameTa": "Augmented Triad (Dreamy & Floating)", "formula": "1 - 3 - ♯5", "semis": [0, 4, 8], "symbol": "aug"},
    "sus2": {"name": "Suspended 2nd", "nameTa": "Suspended 2nd (Open & Ethereal)", "formula": "1 - 2 - 5", "semis": [0, 2, 7], "symbol": "sus2"},
    "sus4": {"name": "Suspended 4th", "nameTa": "Suspended 4th (Expectant & Unresolved)", "formula": "1 - 4 - 5", "semis": [0, 5, 7], "symbol": "sus4"},
    "dom7": {"name": "Dominant 7th", "nameTa": "Dominant 7th (Blues & Cadential Tension)", "formula": "1 - 3 - 5 - ♭7", "semis": [0, 4, 7, 10], "symbol": "7"},
    "maj7": {"name": "Major 7th", "nameTa": "Major 7th (Lush & Romantic Jazz)", "formula": "1 - 3 - 5 - 7", "semis": [0, 4, 7, 11], "symbol": "maj7"},
    "min7": {"name": "Minor 7th", "nameTa": "Minor 7th (Mellow & Cool Jazz)", "formula": "1 - ♭3 - 5 - ♭7", "semis": [0, 3, 7, 10], "symbol": "m7"},
    "dim7": {"name": "Diminished 7th", "nameTa": "Diminished 7th (Dramatic Suspense)", "formula": "1 - ♭3 - ♭5 - 𝄫7", "semis": [0, 3, 6, 9], "symbol": "dim7"}
}

ROOT_NOTES = [
    {"name": "C", "semi": 0},
    {"name": "C# / Db", "semi": 1},
    {"name": "D", "semi": 2},
    {"name": "D# / Eb", "semi": 3},
    {"name": "E", "semi": 4},
    {"name": "F", "semi": 5},
    {"name": "F# / Gb", "semi": 6},
    {"name": "G", "semi": 7},
    {"name": "G# / Ab", "semi": 8},
    {"name": "A", "semi": 9},
    {"name": "A# / Bb", "semi": 10},
    {"name": "B", "semi": 11}
]

WESTERN_OCTAVES = [
    {"num": 1, "name": "C1 (Sub-Contra Octave)", "freq": "32.7 Hz", "desc": "Sub-bass register • Deep rumble of 32-foot pipe organs and contrabassoon."},
    {"num": 2, "name": "C2 (Contra / Deep Bass)", "freq": "65.4 Hz", "desc": "Deep bass foundation • Lowest register of cello, bass guitar, and tuba."},
    {"num": 3, "name": "C3 (Bass / Tenor Octave)", "freq": "130.8 Hz", "desc": "Bass Clef (𝄢) register • Left hand piano chords and baritone vocal range."},
    {"num": 4, "name": "C4 (Middle C / One-Line Octave)", "freq": "261.63 Hz", "desc": "👑 The central anchor of the keyboard! Connects Treble and Bass Clefs."},
    {"num": 5, "name": "C5 (Treble / Two-Line Octave)", "freq": "523.3 Hz", "desc": "Treble Clef (𝄞) melody zone • Right hand lead melodies and soprano vocals."},
    {"num": 6, "name": "C6 (High Treble / Three-Line)", "freq": "1046.5 Hz", "desc": "High register • Flute, violin top range, and bright piano flourishes."},
    {"num": 7, "name": "C7 (Piccolo / Four-Line Octave)", "freq": "2093.0 Hz", "desc": "Crystalline bell-like sparkle • Topmost acoustic piano register."}
]
