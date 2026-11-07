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
    {"key": "C Major", "root": "C", "accidentals": "0 ♯ / 0 ♭", "sharps": 0, "flats": 0, "relMinor": "A Minor (Am)", "notes": ["C", "D", "E", "F", "G", "A", "B"], "desc": "அனைத்து வெள்ளை விசைகள் • மேற்கத்திய இசையின் அடிப்படை மேஜர் கீ."},
    {"key": "G Major", "root": "G", "accidentals": "1 ♯ (F#)", "sharps": 1, "flats": 0, "relMinor": "E Minor (Em)", "notes": ["G", "A", "B", "C", "D", "E", "F#"], "desc": "1 Sharp (F#) • அமைதியான பிரகாசமான கீ."},
    {"key": "D Major", "root": "D", "accidentals": "2 ♯ (F#, C#)", "sharps": 2, "flats": 0, "relMinor": "B Minor (Bm)", "notes": ["D", "E", "F#", "G", "A", "B", "C#"], "desc": "2 Sharps • வெற்றிக் களிப்பும் கம்பீரமும் கொண்ட கீ (பாச்சல்பெல் கேனான்)."},
    {"key": "A Major", "root": "A", "accidentals": "3 ♯ (F#, C#, G#)", "sharps": 3, "flats": 0, "relMinor": "F# Minor (F#m)", "notes": ["A", "B", "C#", "D", "E", "F#", "G#"], "desc": "3 Sharps • உற்சாகமும் இளமையும் ததும்பும் கீ."},
    {"key": "E Major", "root": "E", "accidentals": "4 ♯ (F#, C#, G#, D#)", "sharps": 4, "flats": 0, "relMinor": "C# Minor (C#m)", "notes": ["E", "F#", "G#", "A", "B", "C#", "D#"], "desc": "4 Sharps • பிரம்மாண்டமான கிளாசிக்கல் மற்றும் ராக் கீ."},
    {"key": "B Major", "root": "B", "accidentals": "5 ♯ (F#, C#, G#, D#, A#)", "sharps": 5, "flats": 0, "relMinor": "G# Minor (G#m)", "notes": ["B", "C#", "D#", "E", "F#", "G#", "A#"], "desc": "5 Sharps • 5 கருப்பு விசைகள் கொண்ட பளபளக்கும் கீ."},
    {"key": "F# / Gb Major", "root": "F#", "accidentals": "6 ♯ / 6 ♭", "sharps": 6, "flats": 6, "relMinor": "D#m / Ebm", "notes": ["F#", "G#", "A#", "B", "C#", "D#", "E#"], "desc": "Circle-ன் அடிமட்ட துருவ புள்ளி • 6 Sharps அல்லது 6 Flats."},
    {"key": "Db Major", "root": "Db", "accidentals": "5 ♭ (Bb, Eb, Ab, Db, Gb)", "sharps": 0, "flats": 5, "relMinor": "Bb Minor (Bbm)", "notes": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"], "desc": "5 Flats • மென்மையான ரொமாண்டிக் பியானோ கீ (டெபஸ்ஸி Claire de Lune)."},
    {"key": "Ab Major", "root": "Ab", "accidentals": "4 ♭ (Bb, Eb, Ab, Db)", "sharps": 0, "flats": 4, "relMinor": "F Minor (Fm)", "notes": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"], "desc": "4 Flats • கம்பீரமான அமைதி தரும் கீ."},
    {"key": "Eb Major", "root": "Eb", "accidentals": "3 ♭ (Bb, Eb, Ab)", "sharps": 0, "flats": 3, "relMinor": "C Minor (Cm)", "notes": ["Eb", "F", "G", "Ab", "Bb", "C", "D"], "desc": "3 Flats • பீத்தோவனின் எம்பரோர் கன்சர்ட்டோ அமைந்த கம்பீர கீ."},
    {"key": "Bb Major", "root": "Bb", "accidentals": "2 ♭ (Bb, Eb)", "sharps": 0, "flats": 2, "relMinor": "G Minor (Gm)", "notes": ["Bb", "C", "D", "Eb", "F", "G", "A"], "desc": "2 Flats • ஜாஸ் மற்றும் பித்தளை வாத்தியங்களின் பிரியமான கீ."},
    {"key": "F Major", "root": "F", "accidentals": "1 ♭ (Bb)", "sharps": 0, "flats": 1, "relMinor": "D Minor (Dm)", "notes": ["F", "G", "A", "Bb", "C", "D", "E"], "desc": "1 Flat (Bb) • மேய்ச்சல் நில அமைதியும் இயற்கையும் தரும் கீ."}
]

WESTERN_MODES = [
    {
        "name": "1. ஐயோனியன் மோடு (Ionian Mode • Major)",
        "formula": "1 - 2 - 3 - 4 - 5 - 6 - 7",
        "intervals": "W - W - H - W - W - W - H",
        "c_notes": "C - D - E - F - G - A - B - C",
        "mood": "மகிழ்ச்சி, பிரகாசம், உறுதி, கம்பீரம் (Joyful & Triumphant)",
        "carnatic_eq": "29. சங்கராபரணம் (Sankarabharanam)",
        "demo": ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
    },
    {
        "name": "2. டோரியன் மோடு (Dorian Mode • Jazz Minor)",
        "formula": "1 - 2 - ♭3 - 4 - 5 - 6 - ♭7",
        "intervals": "W - H - W - W - W - H - W",
        "c_notes": "C - D - Eb - F - G - A - Bb - C",
        "mood": "ஜாஸ் நயம், மெல்லிய சோகம், நடுக்கால போக் இசை (Greensleeves, Miles Davis So What)",
        "carnatic_eq": "22. கரகரப்பிரியா (Kharaharapriya)",
        "demo": ["C4", "D4", "Eb4", "F4", "G4", "A4", "Bb4", "C5"]
    },
    {
        "name": "3. ஃபிரிஜியன் மோடு (Phrygian Mode • Spanish / Flamenco)",
        "formula": "1 - ♭2 - ♭3 - 4 - 5 - ♭6 - ♭7",
        "intervals": "H - W - W - W - H - W - W",
        "c_notes": "C - Db - Eb - F - G - Ab - Bb - C",
        "mood": "ஸ்பானிஷ் ஃபிளமென்கோ, தீவிர உணர்ச்சி, மர்மம் (Flamenco & Exotic Mystery)",
        "carnatic_eq": "8. ஹனுமத்தோடி (Hanumatodi)",
        "demo": ["C4", "Db4", "Eb4", "F4", "G4", "Ab4", "Bb4", "C5"]
    },
    {
        "name": "4. லிடியன் மோடு (Lydian Mode • Cinematic Dream)",
        "formula": "1 - 2 - 3 - ♯4 - 5 - 6 - 7",
        "intervals": "W - W - W - H - W - W - H",
        "c_notes": "C - D - E - F# - G - A - B - C",
        "mood": "ஹாலிவுட் விண்வெளி சினிமா இசை, கனவு போன்ற மிதக்கும் உணர்வு (ET, The Simpsons, Star Wars)",
        "carnatic_eq": "65. மேசகல்யாணி (Kalyani)",
        "demo": ["C4", "D4", "E4", "F#4", "G4", "A4", "B4", "C5"]
    },
    {
        "name": "5. மிக்ஸோலிடியன் மோடு (Mixolydian Mode • Blues & Rock)",
        "formula": "1 - 2 - 3 - 4 - 5 - 6 - ♭7",
        "intervals": "W - W - H - W - W - H - W",
        "c_notes": "C - D - E - F - G - A - Bb - C",
        "mood": "கிளாசிக் ராக், ப்ளூஸ், உற்சாகமான நடனம் (Sweet Home Alabama, Hey Jude)",
        "carnatic_eq": "28. ஹரிகாம்போஜி (Harikambhoji)",
        "demo": ["C4", "D4", "E4", "F4", "G4", "A4", "Bb4", "C5"]
    },
    {
        "name": "6. ஏயோலியன் மோடு (Aeolian Mode • Natural Minor)",
        "formula": "1 - 2 - ♭3 - 4 - 5 - ♭6 - ♭7",
        "intervals": "W - H - W - W - H - W - W",
        "c_notes": "C - D - Eb - F - G - Ab - Bb - C",
        "mood": "சோகம், அமைதி, உணர்ச்சிப்பூர்வமான ஆழம் (Melancholy & Emotional)",
        "carnatic_eq": "20. நடபைரவி (Natabhairavi)",
        "demo": ["C4", "D4", "Eb4", "F4", "G4", "Ab4", "Bb4", "C5"]
    },
    {
        "name": "7. லோக்ரியன் மோடு (Locrian Mode • Diminished Tension)",
        "formula": "1 - ♭2 - ♭3 - 4 - ♭5 - ♭6 - ♭7",
        "intervals": "H - W - W - H - W - W - W",
        "c_notes": "C - Db - Eb - F - Gb - Ab - Bb - C",
        "mood": "அதிகபட்ச பதற்றம், இருள், தளர்வின்மை (Diminished Tritone Tension)",
        "carnatic_eq": "தீவிர விக்ருத அமைப்பு",
        "demo": ["C4", "Db4", "Eb4", "F4", "Gb4", "Ab4", "Bb4", "C5"]
    },
    {
        "name": "8. மேஜர் பெண்டாடோனிக் (Major Pentatonic • 5 Notes)",
        "formula": "1 - 2 - 3 - 5 - 6",
        "intervals": "W - W - 1.5W - W - 1.5W",
        "c_notes": "C - D - E - G - A - C",
        "mood": "மங்களகரம், உலகம் தழுவிய நாட்டுப்புற இனிமை (Amazing Grace)",
        "carnatic_eq": "மோஹனம் (Mohanam)",
        "demo": ["C4", "D4", "E4", "G4", "A4", "C5"]
    },
    {
        "name": "9. மைனர் பெண்டாடோனிக் (Minor Pentatonic • Blues Foundation)",
        "formula": "1 - ♭3 - 4 - 5 - ♭7",
        "intervals": "1.5W - W - W - 1.5W - W",
        "c_notes": "C - Eb - F - G - Bb - C",
        "mood": "ராக் சோலோ மற்றும் ப்ளூஸ் இசையின் தலையாய ஸ்கேல்",
        "carnatic_eq": "சுத்த தன்யாசி (Suddhadhanyasi)",
        "demo": ["C4", "Eb4", "F4", "G4", "Bb4", "C5"]
    },
    {
        "name": "10. ப்ளூஸ் ஸ்கேல் (The Blues Scale • with Blue Note ♭5)",
        "formula": "1 - ♭3 - 4 - ♭5 - 5 - ♭7",
        "intervals": "1.5W - W - H - H - 1.5W - W",
        "c_notes": "C - Eb - F - F# - G - Bb - C",
        "mood": "ப்ளூஸ், ஜாஸ், ராக் இசையின் தனித்துவமான ப்ளூ நோட் (Blue Note F#)",
        "carnatic_eq": "ப்ளூஸ் ஜன்ய வடிவம்",
        "demo": ["C4", "Eb4", "F4", "F#4", "G4", "Bb4", "C5"]
    }
]

WESTERN_INTERVALS = [
    {"semi": 0, "name": "Perfect Unison (P1)", "nameTa": "ஒரே ஒலி (Root)", "ratio": "1:1", "example": "அடிப்படை நோட்", "notes": ["C4", "C4"]},
    {"semi": 1, "name": "Minor 2nd (m2 / Half Step)", "nameTa": "சிறிய இரண்டாம் இடைவெளி", "ratio": "16:15", "example": "Jaws திரைப்பட தீம்", "notes": ["C4", "C#4"]},
    {"semi": 2, "name": "Major 2nd (M2 / Whole Step)", "nameTa": "பெரிய இரண்டாம் இடைவெளி", "ratio": "9:8", "example": "Happy Birthday துவக்கம்", "notes": ["C4", "D4"]},
    {"semi": 3, "name": "Minor 3rd (m3)", "nameTa": "சிறிய மூன்றாம் இடைவெளி", "ratio": "6:5", "example": "Greensleeves / Lullaby", "notes": ["C4", "Eb4"]},
    {"semi": 4, "name": "Major 3rd (M3)", "nameTa": "பெரிய மூன்றாம் இடைவெளி", "ratio": "5:4", "example": "Oh When the Saints / Kumbaya", "notes": ["C4", "E4"]},
    {"semi": 5, "name": "Perfect 4th (P4)", "nameTa": "முழுமையான நான்காம் இடைவெளி", "ratio": "4:3", "example": "Here Comes the Bride", "notes": ["C4", "F4"]},
    {"semi": 6, "name": "Tritone / Diminished 5th (TT)", "nameTa": "ட்ரைடோன் (சாத்தானின் இடைவெளி)", "ratio": "45:32", "example": "The Simpsons தொடக்க இசை", "notes": ["C4", "F#4"]},
    {"semi": 7, "name": "Perfect 5th (P5)", "nameTa": "முழுமையான ஐந்தாம் இடைவெளி", "ratio": "3:2", "example": "Star Wars / Twinkle Twinkle", "notes": ["C4", "G4"]},
    {"semi": 8, "name": "Minor 6th (m6)", "nameTa": "சிறிய ஆறாம் இடைவெளி", "ratio": "8:5", "example": "The Entertainer ராக்டைம்", "notes": ["C4", "Ab4"]},
    {"semi": 9, "name": "Major 6th (M6)", "nameTa": "பெரிய ஆறாம் இடைவெளி", "ratio": "5:3", "example": "NBC Chimes / My Bonnie", "notes": ["C4", "A4"]},
    {"semi": 10, "name": "Minor 7th (m7)", "nameTa": "சிறிய ஏழாம் இடைவெளி", "ratio": "16:9", "example": "Somewhere (West Side Story)", "notes": ["C4", "Bb4"]},
    {"semi": 11, "name": "Major 7th (M7)", "nameTa": "பெரிய ஏழாம் இடைவெளி", "ratio": "15:8", "example": "Take On Me (A-ha) கோரஸ்", "notes": ["C4", "B4"]},
    {"semi": 12, "name": "Perfect Octave (P8)", "nameTa": "முழுமையான ஆக்டேவ்", "ratio": "2:1", "example": "Somewhere Over the Rainbow", "notes": ["C4", "C5"]}
]

CHORD_TYPES = {
    "maj": {"name": "Major Triad", "nameTa": "மேஜர் ட்ரையாட்", "formula": "1 - 3 - 5", "semis": [0, 4, 7], "symbol": ""},
    "min": {"name": "Minor Triad", "nameTa": "மைனர் ட்ரையாட்", "formula": "1 - ♭3 - 5", "semis": [0, 3, 7], "symbol": "m"},
    "dim": {"name": "Diminished", "nameTa": "டிமினிஷ்ட் ட்ரையாட்", "formula": "1 - ♭3 - ♭5", "semis": [0, 3, 6], "symbol": "dim"},
    "aug": {"name": "Augmented", "nameTa": "ஆக்மென்டட்", "formula": "1 - 3 - ♯5", "semis": [0, 4, 8], "symbol": "aug"},
    "sus2": {"name": "Suspended 2nd", "nameTa": "சஸ்பென்டட் 2", "formula": "1 - 2 - 5", "semis": [0, 2, 7], "symbol": "sus2"},
    "sus4": {"name": "Suspended 4th", "nameTa": "சஸ்பென்டட் 4", "formula": "1 - 4 - 5", "semis": [0, 5, 7], "symbol": "sus4"},
    "dom7": {"name": "Dominant 7th", "nameTa": "டாமினன்ட் 7th", "formula": "1 - 3 - 5 - ♭7", "semis": [0, 4, 7, 10], "symbol": "7"},
    "maj7": {"name": "Major 7th", "nameTa": "மேஜர் 7th", "formula": "1 - 3 - 5 - 7", "semis": [0, 4, 7, 11], "symbol": "maj7"},
    "min7": {"name": "Minor 7th", "nameTa": "மைனர் 7th", "formula": "1 - ♭3 - 5 - ♭7", "semis": [0, 3, 7, 10], "symbol": "m7"},
    "dim7": {"name": "Diminished 7th", "nameTa": "டிமினிஷ்ட் 7th", "formula": "1 - ♭3 - ♭5 - 𝄫7", "semis": [0, 3, 6, 9], "symbol": "dim7"}
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
    {"num": 1, "name": "C1 (Sub-Contra Octave)", "freq": "32.7 Hz", "desc": "மிக ஆழமான பாஸ் அதிர்வுகள் • பெரிய சர்ச் ஆர்கன்களின் பெடல் விசைகள்."},
    {"num": 2, "name": "C2 (Contra / Deep Bass)", "freq": "65.4 Hz", "desc": "ஆழமான பேஸ் ரம்பில் • செல்லோ மற்றும் பாஸ் கிட்டார் கீழ் எல்லை."},
    {"num": 3, "name": "C3 (Bass / Tenor Octave)", "freq": "130.8 Hz", "desc": "பியானோவின் இடது கை பேஸ் க்ளெஃப் (𝄢) கார்டுகள் வாசிக்கும் தளம்."},
    {"num": 4, "name": "C4 (Middle C / One-Line Octave)", "freq": "261.6 Hz", "desc": "👑 பியானோவின் நடுமையம்! ட்ரெபிள் மற்றும் பேஸ் க்ளெஃப்களை இணைக்கும் புள்ளி."},
    {"num": 5, "name": "C5 (Treble / Two-Line Octave)", "freq": "523.3 Hz", "desc": "வலது கையின் பிரகாசமான மெலடி எல்லை (Treble Clef 𝄞)."},
    {"num": 6, "name": "C6 (High Treble / Three-Line)", "freq": "1046.5 Hz", "desc": "உயர் மெலடி மற்றும் ஆபரண ஓட்டங்கள் (High Flourishes)."},
    {"num": 7, "name": "C7 (Piccolo / Four-Line Octave)", "freq": "2093.0 Hz", "desc": "மணி போன்ற மினுமினுக்கும் உச்சக்கட்ட பியானோ ஒலி."}
]

