# -*- coding: utf-8 -*-
"""
Western Keyboard & Piano Curriculum: 82 Comprehensive Master Practice Lessons
Categories:
1. Hanon & Finger Drills (hanon - 12 lessons)
2. Major Scales & Pentatonics (major_scales - 16 lessons)
3. Minor, Pentatonic & Blues Scales (minor_scales - 12 lessons)
4. Chords, Inversions & Arpeggios (chords - 12 lessons)
5. Famous Chord Progressions (progressions - 12 lessons)
6. Classical Masterpieces & Melodies (melodies - 18 lessons)
Total Repertoire: 82 Master Lessons
"""

WESTERN_LESSONS = {
    # ---------------- 1. HANON & CZERNY FINGER DRILLS (ஹெனான் & விரல் பயிற்சிகள் - 12 பாடங்கள்) ----------------
    "h1": {
            "id": "h1",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "C Major",
            "title": "1. ஹெனான் பயிற்சி 1 (Hanon No. 1 • விரல் இடைவெளி & சுறுசுறுப்பு)",
            "desc": "சி.எல். ஹெனான் (C.L. Hanon - The Virtuoso Pianist) பயிற்சி 1. விரல்கள் 1 மற்றும் 2-க்கு இடையே இடைவெளியை விரித்து, விரல் சுதந்திரத்தை (Finger Independence) வளர்க்கும் அத்தியாவசிய பயிற்சி.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "பாகம் 1: ஏறுவரிசை (Ascending - C4 முதல் G4 வரை)",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "F4",
                                            "G4"
                                    ],
                                    [
                                            "A4",
                                            "G4",
                                            "F4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "F4",
                                            "G4",
                                            "A4"
                                    ],
                                    [
                                            "B4",
                                            "A4",
                                            "G4",
                                            "F4"
                                    ],
                                    [
                                            "E4",
                                            "G4",
                                            "A4",
                                            "B4"
                                    ],
                                    [
                                            "C5",
                                            "B4",
                                            "A4",
                                            "G4"
                                    ],
                                    [
                                            "F4",
                                            "A4",
                                            "B4",
                                            "C5"
                                    ],
                                    [
                                            "D5",
                                            "C5",
                                            "B4",
                                            "A4"
                                    ],
                                    [
                                            "G4",
                                            "B4",
                                            "C5",
                                            "D5"
                                    ],
                                    [
                                            "E5",
                                            "D5",
                                            "C5",
                                            "B4"
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "C",
                                            "E",
                                            "F",
                                            "G"
                                    ],
                                    [
                                            "A",
                                            "G",
                                            "F",
                                            "E"
                                    ],
                                    [
                                            "D",
                                            "F",
                                            "G",
                                            "A"
                                    ],
                                    [
                                            "B",
                                            "A",
                                            "G",
                                            "F"
                                    ],
                                    [
                                            "E",
                                            "G",
                                            "A",
                                            "B"
                                    ],
                                    [
                                            "C",
                                            "B",
                                            "A",
                                            "G"
                                    ],
                                    [
                                            "F",
                                            "A",
                                            "B",
                                            "C"
                                    ],
                                    [
                                            "D",
                                            "C",
                                            "B",
                                            "A"
                                    ],
                                    [
                                            "G",
                                            "B",
                                            "C",
                                            "D"
                                    ],
                                    [
                                            "E",
                                            "D",
                                            "C",
                                            "B"
                                    ]
                            ]
                    },
                    {
                            "title": "பாகம் 2: இறங்குவரிசை (Descending - G5 முதல் C4 வரை)",
                            "measures": [
                                    [
                                            "G5",
                                            "E5",
                                            "D5",
                                            "C5"
                                    ],
                                    [
                                            "B4",
                                            "C5",
                                            "D5",
                                            "E5"
                                    ],
                                    [
                                            "F5",
                                            "D5",
                                            "C5",
                                            "B4"
                                    ],
                                    [
                                            "A4",
                                            "B4",
                                            "C5",
                                            "D5"
                                    ],
                                    [
                                            "E5",
                                            "C5",
                                            "B4",
                                            "A4"
                                    ],
                                    [
                                            "G4",
                                            "A4",
                                            "B4",
                                            "C5"
                                    ],
                                    [
                                            "D5",
                                            "B4",
                                            "A4",
                                            "G4"
                                    ],
                                    [
                                            "F4",
                                            "G4",
                                            "A4",
                                            "B4"
                                    ],
                                    [
                                            "C5",
                                            "G4",
                                            "F4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "E4",
                                            "F4",
                                            "C4"
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "G",
                                            "E",
                                            "D",
                                            "C"
                                    ],
                                    [
                                            "B",
                                            "C",
                                            "D",
                                            "E"
                                    ],
                                    [
                                            "F",
                                            "D",
                                            "C",
                                            "B"
                                    ],
                                    [
                                            "A",
                                            "B",
                                            "C",
                                            "D"
                                    ],
                                    [
                                            "E",
                                            "C",
                                            "B",
                                            "A"
                                    ],
                                    [
                                            "G",
                                            "A",
                                            "B",
                                            "C"
                                    ],
                                    [
                                            "D",
                                            "B",
                                            "A",
                                            "G"
                                    ],
                                    [
                                            "F",
                                            "G",
                                            "A",
                                            "B"
                                    ],
                                    [
                                            "C",
                                            "G",
                                            "F",
                                            "E"
                                    ],
                                    [
                                            "D",
                                            "E",
                                            "F",
                                            "C"
                                    ]
                            ]
                    }
            ]
    },
    "h2": {
            "id": "h2",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "C Major",
            "title": "2. ஹெனான் பயிற்சி 2 (Hanon No. 2 • 3-4-5 விரல் வலிமை)",
            "desc": "பியானோவில் பொதுவாக பலவீனமான 3 (நடுவிரல்), 4 (மோதிரவிரல்), மற்றும் 5 (சிறுவிரல்) ஆகிய விரல்களை பலப்படுத்தும் உன்னத பயிற்சி.",
            "tempo": 75,
            "lines": [
                    {
                            "title": "பாகம் 1: ஏறுவரிசை (Ascending)",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "A4"
                                    ],
                                    [
                                            "G4",
                                            "F4",
                                            "E4",
                                            "D4"
                                    ],
                                    [
                                            "D4",
                                            "F4",
                                            "A4",
                                            "B4"
                                    ],
                                    [
                                            "A4",
                                            "G4",
                                            "F4",
                                            "E4"
                                    ],
                                    [
                                            "E4",
                                            "G4",
                                            "B4",
                                            "C5"
                                    ],
                                    [
                                            "B4",
                                            "A4",
                                            "G4",
                                            "F4"
                                    ],
                                    [
                                            "F4",
                                            "A4",
                                            "C5",
                                            "D5"
                                    ],
                                    [
                                            "C5",
                                            "B4",
                                            "A4",
                                            "G4"
                                    ]
                            ]
                    },
                    {
                            "title": "பாகம் 2: இறங்குவரிசை (Descending)",
                            "measures": [
                                    [
                                            "G5",
                                            "E5",
                                            "C5",
                                            "B4"
                                    ],
                                    [
                                            "C5",
                                            "D5",
                                            "E5",
                                            "F5"
                                    ],
                                    [
                                            "F5",
                                            "D5",
                                            "B4",
                                            "A4"
                                    ],
                                    [
                                            "B4",
                                            "C5",
                                            "D5",
                                            "E5"
                                    ],
                                    [
                                            "E5",
                                            "C5",
                                            "A4",
                                            "G4"
                                    ],
                                    [
                                            "A4",
                                            "B4",
                                            "C5",
                                            "D5"
                                    ],
                                    [
                                            "D5",
                                            "B4",
                                            "G4",
                                            "F4"
                                    ],
                                    [
                                            "E4",
                                            "D4",
                                            "C4",
                                            "C4"
                                    ]
                            ]
                    }
            ]
    },
    "h3": {
            "id": "h3",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "C Major",
            "title": "3. வலது கை 5-விரல் பயிற்சி (RH 5-Finger Warmup • Fingers 1-2-3-4-5)",
            "desc": "C-D-E-F-G 5 வெள்ளை விசைகளில் வலது கை 1=பெருவிரல், 2=சுட்டு, 3=நடு, 4=மோதிர, 5=சிறுவிரல் வைத்து சீராக வாசிக்கும் ஆரம்பப் பயிற்சி.",
            "tempo": 90,
            "lines": [
                    {
                            "title": "வரிசை 1: ஏறுவரிசை & இறங்குவரிசை (C D E F G F E D C)",
                            "measures": [
                                    [
                                            "C4",
                                            "D4",
                                            "E4",
                                            "F4"
                                    ],
                                    [
                                            "G4",
                                            "F4",
                                            "E4",
                                            "D4"
                                    ],
                                    [
                                            "C4",
                                            "D4",
                                            "E4",
                                            "F4"
                                    ],
                                    [
                                            "G4",
                                            "G4",
                                            "G4",
                                            ","
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "1-Thumb",
                                            "2-Index",
                                            "3-Middle",
                                            "4-Ring"
                                    ],
                                    [
                                            "5-Pinky",
                                            "4-Ring",
                                            "3-Middle",
                                            "2-Index"
                                    ],
                                    [
                                            "1-Thumb",
                                            "2-Index",
                                            "3-Middle",
                                            "4-Ring"
                                    ],
                                    [
                                            "5-Pinky",
                                            "Repeat",
                                            "Hold",
                                            "Rest"
                                    ]
                            ]
                    },
                    {
                            "title": "வரிசை 2: இரட்டை அடி விரல் சுறுசுறுப்பு (Repeated Note Drill)",
                            "measures": [
                                    [
                                            "C4",
                                            "C4",
                                            "D4",
                                            "D4"
                                    ],
                                    [
                                            "E4",
                                            "E4",
                                            "F4",
                                            "F4"
                                    ],
                                    [
                                            "G4",
                                            "G4",
                                            "F4",
                                            "F4"
                                    ],
                                    [
                                            "E4",
                                            "E4",
                                            "D4",
                                            "D4"
                                    ],
                                    [
                                            "C4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "h4": {
            "id": "h4",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "C Major",
            "title": "4. இடது கை 5-விரல் பயிற்சி (LH 5-Finger Warmup • Fingers 5-4-3-2-1)",
            "desc": "இடது கை C3 பேஸ் நோட்டிலிருந்து 5=சிறுவிரல், 4=மோதிர, 3=நடு, 2=சுட்டு, 1=பெருவிரல் வைத்து பேஸ் க்ளெஃப்பில் வாசிக்கும் பயிற்சி.",
            "tempo": 85,
            "lines": [
                    {
                            "title": "வரிசை 1: இடது கை 5-விரல் அடிப்படை (C3 D3 E3 F3 G3)",
                            "measures": [
                                    [
                                            "C3",
                                            "D3",
                                            "E3",
                                            "F3"
                                    ],
                                    [
                                            "G3",
                                            "F3",
                                            "E3",
                                            "D3"
                                    ],
                                    [
                                            "C3",
                                            "E3",
                                            "G3",
                                            "E3"
                                    ],
                                    [
                                            "C3",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "5-Pinky",
                                            "4-Ring",
                                            "3-Middle",
                                            "2-Index"
                                    ],
                                    [
                                            "1-Thumb",
                                            "2-Index",
                                            "3-Middle",
                                            "4-Ring"
                                    ],
                                    [
                                            "5-Pinky",
                                            "3-Middle",
                                            "1-Thumb",
                                            "3-Middle"
                                    ],
                                    [
                                            "5-Pinky",
                                            "Hold",
                                            "Hold",
                                            "Rest"
                                    ]
                            ]
                    }
            ]
    },
    "h5": {
            "id": "h5",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "C Major",
            "title": "5. எதிர் அசைவுப் பயிற்சி (Contrary Motion • இரு கைகள் விரிதல்)",
            "desc": "இரு கைகளும் Middle C மற்றும் C3-லிருந்து எதிரெதிர் திசைகளில் விரியும் அழகான மூளை-விரல் ஒருங்கிணைப்புப் பயிற்சி (Left moves Down, Right moves Up).",
            "tempo": 80,
            "lines": [
                    {
                            "title": "பாகம் 1: வெளிநோக்கி விரிதல் (Outward)",
                            "measures": [
                                    [
                                            "C4",
                                            "D4",
                                            "E4",
                                            "F4"
                                    ],
                                    [
                                            "G4",
                                            "F4",
                                            "E4",
                                            "D4"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "G4",
                                            "E4",
                                            "C4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "h6": {
            "id": "h6",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "C Major",
            "title": "6. ட்ரையாட் ஆர்பெஜியோ விரல் பயிற்சி (C Major Triad Arpeggio Drill)",
            "desc": "C-E-G-C (1-3-5-8) நோட்டுகளை உடைத்து ஆர்பெஜியோவாக வாசிக்கும் விரல் நீட்சி பயிற்சி (Finger Stretch & Agility).",
            "tempo": 90,
            "lines": [
                    {
                            "title": "வரிசை 1: C மேஜர் ஆர்பெஜியோ ஏறு-இறங்கு",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "E5",
                                            "C5",
                                            "G4",
                                            "E4"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "C5",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "h7": {
            "id": "h7",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "Chromatic",
            "title": "7. குரோமேட்டிக் விரல் பயிற்சி (Chromatic Drill • 1-3-1-3 விரல் முறை)",
            "desc": "வெள்ளை மற்றும் கருப்பு விசைகளில் பெருவிரல் (1) மற்றும் நடுவிரல் (3) மாற்றி மாற்றி வைத்து வாசிக்கும் பியானோ குரோமேட்டிக் விரல் நுட்பம்.",
            "tempo": 75,
            "lines": [
                    {
                            "title": "பாகம் 1: C4 முதல் F4 குரோமேட்டிக் ஏறுவரிசை",
                            "measures": [
                                    [
                                            "C4",
                                            "C#4",
                                            "D4",
                                            "D#4"
                                    ],
                                    [
                                            "E4",
                                            "F4",
                                            "F#4",
                                            "G4"
                                    ],
                                    [
                                            "G#4",
                                            "A4",
                                            "A#4",
                                            "B4"
                                    ],
                                    [
                                            "C5",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    },
                    {
                            "title": "பாகம் 2: C5 முதல் C4 குரோமேட்டிக் இறங்குவரிசை",
                            "measures": [
                                    [
                                            "C5",
                                            "B4",
                                            "A#4",
                                            "A4"
                                    ],
                                    [
                                            "G#4",
                                            "G4",
                                            "F#4",
                                            "F4"
                                    ],
                                    [
                                            "E4",
                                            "D#4",
                                            "D4",
                                            "C#4"
                                    ],
                                    [
                                            "C4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "h8": {
            "id": "h8",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "C Major",
            "title": "8. ஹெனான் பயிற்சி 3 (Hanon No. 3 • 2-3-4-5 விரல் இடைவெளி)",
            "desc": "C.L. Hanon No. 3: விரல்கள் 2, 3, 4, 5-க்கு இடையே சமநிலையான பலத்தையும் வேகத்தையும் கொடுக்கும் உன்னத பயிற்சி.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "பாகம் 1: ஏறுவரிசை (Ascending)",
                            "measures": [
                                    [
                                            "C4",
                                            "F4",
                                            "E4",
                                            "D4"
                                    ],
                                    [
                                            "C4",
                                            "D4",
                                            "E4",
                                            "F4"
                                    ],
                                    [
                                            "D4",
                                            "G4",
                                            "F4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "E4",
                                            "F4",
                                            "G4"
                                    ],
                                    [
                                            "E4",
                                            "A4",
                                            "G4",
                                            "F4"
                                    ],
                                    [
                                            "E4",
                                            "F4",
                                            "G4",
                                            "A4"
                                    ],
                                    [
                                            "F4",
                                            "B4",
                                            "A4",
                                            "G4"
                                    ],
                                    [
                                            "F4",
                                            "G4",
                                            "A4",
                                            "B4"
                                    ]
                            ]
                    },
                    {
                            "title": "பாகம் 2: இறங்குவரிசை (Descending)",
                            "measures": [
                                    [
                                            "G5",
                                            "D5",
                                            "E5",
                                            "F5"
                                    ],
                                    [
                                            "G5",
                                            "F5",
                                            "E5",
                                            "D5"
                                    ],
                                    [
                                            "F5",
                                            "C5",
                                            "D5",
                                            "E5"
                                    ],
                                    [
                                            "F5",
                                            "E5",
                                            "D5",
                                            "C5"
                                    ],
                                    [
                                            "E5",
                                            "B4",
                                            "C5",
                                            "D5"
                                    ],
                                    [
                                            "E5",
                                            "D5",
                                            "C5",
                                            "B4"
                                    ],
                                    [
                                            "D5",
                                            "A4",
                                            "B4",
                                            "C5"
                                    ],
                                    [
                                            "C4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "h9": {
            "id": "h9",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "C Major",
            "title": "9. ஹெனான் பயிற்சி 5 (Hanon No. 5 • 5-வது விரல் வேகம்)",
            "desc": "பெருவிரல் மற்றும் சிறுவிரலுக்கு இடையே 5-நோட் தாவல் பயிற்சி (C-G-F-E-D-E-F-G).",
            "tempo": 85,
            "lines": [
                    {
                            "title": "பாகம் 1: 5-வது விரல் தாவல் ஏறுவரிசை",
                            "measures": [
                                    [
                                            "C4",
                                            "G4",
                                            "F4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "E4",
                                            "F4",
                                            "G4"
                                    ],
                                    [
                                            "D4",
                                            "A4",
                                            "G4",
                                            "F4"
                                    ],
                                    [
                                            "E4",
                                            "F4",
                                            "G4",
                                            "A4"
                                    ],
                                    [
                                            "E4",
                                            "B4",
                                            "A4",
                                            "G4"
                                    ],
                                    [
                                            "F4",
                                            "G4",
                                            "A4",
                                            "B4"
                                    ],
                                    [
                                            "F4",
                                            "C5",
                                            "B4",
                                            "A4"
                                    ],
                                    [
                                            "G4",
                                            "A4",
                                            "B4",
                                            "C5"
                                    ]
                            ]
                    }
            ]
    },
    "h10": {
            "id": "h10",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "C Major",
            "title": "10. செர்னி எட்யூட் 1 (Czerny Op. 599 No. 1 • முதன்மை ஆசான் பயிற்சி)",
            "desc": "கார்ல் செர்னி (Carl Czerny) இயற்றிய ஆரம்ப பியானோ கற்போரின் உலகப் புகழ்பெற்ற பயிற்சி (Op. 599). சீரான தொடுதல் மற்றும் டெம்போ கட்டுப்பாடு.",
            "tempo": 90,
            "lines": [
                    {
                            "title": "செர்னி நோட் பயிற்சி 1",
                            "measures": [
                                    [
                                            "C4",
                                            "D4",
                                            "E4",
                                            "F4"
                                    ],
                                    [
                                            "G4",
                                            "G4",
                                            "G4",
                                            ","
                                    ],
                                    [
                                            "F4",
                                            "E4",
                                            "D4",
                                            "C4"
                                    ],
                                    [
                                            "D4",
                                            "D4",
                                            "D4",
                                            ","
                                    ],
                                    [
                                            "C4",
                                            "D4",
                                            "E4",
                                            "F4"
                                    ],
                                    [
                                            "G4",
                                            "G4",
                                            "G4",
                                            ","
                                    ],
                                    [
                                            "F4",
                                            "E4",
                                            "D4",
                                            "D4"
                                    ],
                                    [
                                            "C4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "h11": {
            "id": "h11",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "C Major",
            "title": "11. செர்னி எட்யூட் 19 (Czerny Op. 599 No. 19 • இரு கை ஒருங்கிசைவு)",
            "desc": "வலது கை மற்றும் இடது கை இரண்டும் இணைந்து சம பலத்துடன் இயங்க உதவும் செர்னி எட்யூட்.",
            "tempo": 85,
            "lines": [
                    {
                            "title": "மெலடி & பேஸ் அசைவு",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "E4"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "F4",
                                            "G4",
                                            "F4"
                                    ],
                                    [
                                            "D4",
                                            "F4",
                                            "G4",
                                            "F4"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "G4",
                                            "B4",
                                            "G4"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "C4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "h12": {
            "id": "h12",
            "cat": "hanon",
            "catTamil": "1. ஹெனான் & விரல் பயிற்சிகள் (Hanon & Finger Drills)",
            "meter": "4/4",
            "key": "C Major",
            "title": "12. ஆல்பர்ட்டி பேஸ் விரல் பயிற்சி (Alberti Bass Drill • 1-5-3-5 முறை)",
            "desc": "கிளாசிக்கல் பியானோவின் மிக முக்கியமான இடது கை கார்ட் நடை (Domenico Alberti). Root -> 5th -> 3rd -> 5th (C - G - E - G) சுழற்சி.",
            "tempo": 95,
            "lines": [
                    {
                            "title": "C மேஜர் & G7 ஆல்பர்ட்டி பேஸ் நடை",
                            "measures": [
                                    [
                                            "C3",
                                            "G3",
                                            "E3",
                                            "G3"
                                    ],
                                    [
                                            "C3",
                                            "G3",
                                            "E3",
                                            "G3"
                                    ],
                                    [
                                            "B2",
                                            "G3",
                                            "D3",
                                            "G3"
                                    ],
                                    [
                                            "B2",
                                            "G3",
                                            "D3",
                                            "G3"
                                    ],
                                    [
                                            "C3",
                                            "G3",
                                            "E3",
                                            "G3"
                                    ],
                                    [
                                            "C3",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    # ---------------- 2. MAJOR SCALES & PENTATONICS (மேஜர் ஸ்கேல்கள் - 16 பாடங்கள்) ----------------
    "m1": {
            "id": "m1",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "C Major",
            "title": "1. C மேஜர் ஸ்கேல் (C Major Scale • முழுமையான 1 ஆக்டேவ்)",
            "desc": "எந்தவித Sharps அல்லது Flats இல்லாத மேற்கத்திய இசையின் ராஜா ஸ்கேல்! RH Fingering: 1-2-3 (பெருவிரல் அடியில் நுழைத்தல் Thumb Tuck) 1-2-3-4-5. இறங்கும்போது: 5-4-3-2-1 (நடுவிரல் மேலாகத் தாண்டுதல் 3rd finger cross) 3-2-1.",
            "tempo": 85,
            "lines": [
                    {
                            "title": "ஏறுவரிசை (Ascending: C4 முதல் C5 வரை)",
                            "measures": [
                                    [
                                            "C4",
                                            "D4",
                                            "E4",
                                            "F4"
                                    ],
                                    [
                                            "G4",
                                            "A4",
                                            "B4",
                                            "C5"
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "Do (1)",
                                            "Re (2)",
                                            "Mi (3)",
                                            "Fa (1)"
                                    ],
                                    [
                                            "Sol (2)",
                                            "La (3)",
                                            "Ti (4)",
                                            "Do (5)"
                                    ]
                            ]
                    },
                    {
                            "title": "இறங்குவரிசை (Descending: C5 முதல் C4 வரை)",
                            "measures": [
                                    [
                                            "C5",
                                            "B4",
                                            "A4",
                                            "G4"
                                    ],
                                    [
                                            "F4",
                                            "E4",
                                            "D4",
                                            "C4"
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "Do (5)",
                                            "Ti (4)",
                                            "La (3)",
                                            "Sol (2)"
                                    ],
                                    [
                                            "Fa (1)",
                                            "Mi (3)",
                                            "Re (2)",
                                            "Do (1)"
                                    ]
                            ]
                    }
            ]
    },
    "m2": {
            "id": "m2",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "G Major",
            "title": "2. G மேஜர் ஸ்கேல் (G Major Scale • 1 Sharp: F#)",
            "desc": "Circle of Fifths-ல் முதல் Sharp கீ! 7-வது நோட்டு F# (Black Key). G-A-B-C-D-E-F#-G. RH Fingering: 1-2-3-1-2-3-4-5.",
            "tempo": 85,
            "lines": [
                    {
                            "title": "ஏறுவரிசை & இறங்குவரிசை (G4 to G5)",
                            "measures": [
                                    [
                                            "G4",
                                            "A4",
                                            "B4",
                                            "C5"
                                    ],
                                    [
                                            "D5",
                                            "E5",
                                            "F#5",
                                            "G5"
                                    ],
                                    [
                                            "G5",
                                            "F#5",
                                            "E5",
                                            "D5"
                                    ],
                                    [
                                            "C5",
                                            "B4",
                                            "A4",
                                            "G4"
                                    ]
                            ]
                    }
            ]
    },
    "m3": {
            "id": "m3",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "D Major",
            "title": "3. D மேஜர் ஸ்கேல் (D Major Scale • 2 Sharps: F#, C#)",
            "desc": "2 Sharps கொண்ட கம்பீரமான கீ (F# மற்றும் C#). D-E-F#-G-A-B-C#-D. பிரகாசமான ஒலி தரும்.",
            "tempo": 85,
            "lines": [
                    {
                            "title": "D மேஜர் ஏறு & இறங்கு (D4 to D5)",
                            "measures": [
                                    [
                                            "D4",
                                            "E4",
                                            "F#4",
                                            "G4"
                                    ],
                                    [
                                            "A4",
                                            "B4",
                                            "C#5",
                                            "D5"
                                    ],
                                    [
                                            "D5",
                                            "C#5",
                                            "B4",
                                            "A4"
                                    ],
                                    [
                                            "G4",
                                            "F#4",
                                            "E4",
                                            "D4"
                                    ]
                            ]
                    }
            ]
    },
    "m4": {
            "id": "m4",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "A Major",
            "title": "4. A மேஜர் ஸ்கேல் (A Major Scale • 3 Sharps: F#, C#, G#)",
            "desc": "3 Sharps கொண்ட உற்சாகமான கீ. A-B-C#-D-E-F#-G#-A. பியானோவில் 3 கருப்பு விசைகள் கையாளும் பயிற்சி.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "A மேஜர் ஏறு & இறங்கு (A3 to A4)",
                            "measures": [
                                    [
                                            "A3",
                                            "B3",
                                            "C#4",
                                            "D4"
                                    ],
                                    [
                                            "E4",
                                            "F#4",
                                            "G#4",
                                            "A4"
                                    ],
                                    [
                                            "A4",
                                            "G#4",
                                            "F#4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "C#4",
                                            "B3",
                                            "A3"
                                    ]
                            ]
                    }
            ]
    },
    "m5": {
            "id": "m5",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "E Major",
            "title": "5. E மேஜர் ஸ்கேல் (E Major Scale • 4 Sharps: F#, C#, G#, D#)",
            "desc": "4 Sharps கொண்ட இனிமையான கிளாசிக்கல் கீ. E-F#-G#-A-B-C#-D#-E.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "E மேஜர் ஏறு & இறங்கு (E4 to E5)",
                            "measures": [
                                    [
                                            "E4",
                                            "F#4",
                                            "G#4",
                                            "A4"
                                    ],
                                    [
                                            "B4",
                                            "C#5",
                                            "D#5",
                                            "E5"
                                    ],
                                    [
                                            "E5",
                                            "D#5",
                                            "C#5",
                                            "B4"
                                    ],
                                    [
                                            "A4",
                                            "G#4",
                                            "F#4",
                                            "E4"
                                    ]
                            ]
                    }
            ]
    },
    "m6": {
            "id": "m6",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "F Major",
            "title": "6. F மேஜர் ஸ்கேல் (F Major Scale • 1 Flat: Bb • விசேஷ விரல் முறை)",
            "desc": "1 Flat கொண்ட முதல் Flat கீ. F-G-A-Bb-C-D-E-F. கவனம்: F மேஜருக்கு RH Fingering 1-2-3-4 (Bb-க்கு 4-ம் விரல்) பிறகு Thumb Tuck 1-2-3-4!",
            "tempo": 85,
            "lines": [
                    {
                            "title": "F மேஜர் ஏறு & இறங்கு (F4 to F5)",
                            "measures": [
                                    [
                                            "F4",
                                            "G4",
                                            "A4",
                                            "Bb4"
                                    ],
                                    [
                                            "C5",
                                            "D5",
                                            "E5",
                                            "F5"
                                    ],
                                    [
                                            "F5",
                                            "E5",
                                            "D5",
                                            "C5"
                                    ],
                                    [
                                            "Bb4",
                                            "A4",
                                            "G4",
                                            "F4"
                                    ]
                            ]
                    }
            ]
    },
    "m7": {
            "id": "m7",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "Bb Major",
            "title": "7. Bb மேஜர் ஸ்கேல் (Bb Major Scale • 2 Flats: Bb, Eb)",
            "desc": "2 Flats கொண்ட ஜாஸ் மற்றும் பிராஸ் பேண்ட் கீ. Bb-C-D-Eb-F-G-A-Bb. கருப்பு விசை Bb-ல் பெருவிரல் வைக்காமல் 2-ம் விரல் தொடங்கும் விசேஷ முறை.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "Bb மேஜர் ஏறு & இறங்கு (Bb3 to Bb4)",
                            "measures": [
                                    [
                                            "Bb3",
                                            "C4",
                                            "D4",
                                            "Eb4"
                                    ],
                                    [
                                            "F4",
                                            "G4",
                                            "A4",
                                            "Bb4"
                                    ],
                                    [
                                            "Bb4",
                                            "A4",
                                            "G4",
                                            "F4"
                                    ],
                                    [
                                            "Eb4",
                                            "D4",
                                            "C4",
                                            "Bb3"
                                    ]
                            ]
                    }
            ]
    },
    "m8": {
            "id": "m8",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "Chromatic",
            "title": "8. முழு குரோமேட்டிக் ஸ்கேல் (Full Chromatic Scale • 12 Semitones)",
            "desc": "C4 முதல் C5 வரை உள்ள அனைத்து 12 அரைக்கட்டை (Semitone) இடைவெளிகளையும் வரிசையாக வாசிக்கும் ஸ்கேல்.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "12 செமிடோன்கள் ஏறுவரிசை",
                            "measures": [
                                    [
                                            "C4",
                                            "C#4",
                                            "D4",
                                            "D#4"
                                    ],
                                    [
                                            "E4",
                                            "F4",
                                            "F#4",
                                            "G4"
                                    ],
                                    [
                                            "G#4",
                                            "A4",
                                            "A#4",
                                            "B4"
                                    ],
                                    [
                                            "C5",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "m9": {
            "id": "m9",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "B Major",
            "title": "9. B மேஜர் ஸ்கேல் (B Major Scale • 5 Sharps: F#, C#, G#, D#, A#)",
            "desc": "5 கருப்பு விசைகள் கொண்ட பளபளக்கும் கீ! B-C#-D#-E-F#-G#-A#-B. Chopin பியானோ மாணவர்களுக்கு முதலில் கற்றுக்கொடுத்த ஸ்கேல்.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "B மேஜர் ஏறு & இறங்கு (B3 to B4)",
                            "measures": [
                                    [
                                            "B3",
                                            "C#4",
                                            "D#4",
                                            "E4"
                                    ],
                                    [
                                            "F#4",
                                            "G#4",
                                            "A#4",
                                            "B4"
                                    ],
                                    [
                                            "B4",
                                            "A#4",
                                            "G#4",
                                            "F#4"
                                    ],
                                    [
                                            "E4",
                                            "D#4",
                                            "C#4",
                                            "B3"
                                    ]
                            ]
                    }
            ]
    },
    "m10": {
            "id": "m10",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "F# Major",
            "title": "10. F# மேஜர் ஸ்கேல் (F# Major Scale • 6 Sharps: F#, C#, G#, D#, A#, E#)",
            "desc": "Circle of Fifths-ன் அடிமட்ட துருவ புள்ளி. 6 Sharps கொண்ட கம்பீரமான கீ. F#-G#-A#-B-C#-D#-E#-F#.",
            "tempo": 75,
            "lines": [
                    {
                            "title": "F# மேஜர் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "F#4",
                                            "G#4",
                                            "A#4",
                                            "B4"
                                    ],
                                    [
                                            "C#5",
                                            "D#5",
                                            "F5",
                                            "F#5"
                                    ],
                                    [
                                            "F#5",
                                            "F5",
                                            "D#5",
                                            "C#5"
                                    ],
                                    [
                                            "B4",
                                            "A#4",
                                            "G#4",
                                            "F#4"
                                    ]
                            ]
                    }
            ]
    },
    "m11": {
            "id": "m11",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "Eb Major",
            "title": "11. Eb மேஜர் ஸ்கேல் (Eb Major Scale • 3 Flats: Bb, Eb, Ab)",
            "desc": "3 Flats கொண்ட பீத்தோவனின் எம்பரோர் கன்சர்ட்டோ மற்றும் பிரம்மாண்ட சிம்பொனிகளின் கீ. Eb-F-G-Ab-Bb-C-D-Eb.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "Eb மேஜர் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "Eb4",
                                            "F4",
                                            "G4",
                                            "Ab4"
                                    ],
                                    [
                                            "Bb4",
                                            "C5",
                                            "D5",
                                            "Eb5"
                                    ],
                                    [
                                            "Eb5",
                                            "D5",
                                            "C5",
                                            "Bb4"
                                    ],
                                    [
                                            "Ab4",
                                            "G4",
                                            "F4",
                                            "Eb4"
                                    ]
                            ]
                    }
            ]
    },
    "m12": {
            "id": "m12",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "Ab Major",
            "title": "12. Ab மேஜர் ஸ்கேல் (Ab Major Scale • 4 Flats: Bb, Eb, Ab, Db)",
            "desc": "4 Flats கொண்ட மென்மையான அமைதியான ரொமாண்டிக் கீ. Ab-Bb-C-Db-Eb-F-G-Ab.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "Ab மேஜர் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "Ab3",
                                            "Bb3",
                                            "C4",
                                            "Db4"
                                    ],
                                    [
                                            "Eb4",
                                            "F4",
                                            "G4",
                                            "Ab4"
                                    ],
                                    [
                                            "Ab4",
                                            "G4",
                                            "F4",
                                            "Eb4"
                                    ],
                                    [
                                            "Db4",
                                            "C4",
                                            "Bb3",
                                            "Ab3"
                                    ]
                            ]
                    }
            ]
    },
    "m13": {
            "id": "m13",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "Db Major",
            "title": "13. Db மேஜர் ஸ்கேல் (Db Major Scale • 5 Flats)",
            "desc": "டெபஸ்ஸியின் Claire de Lune அமைந்த புகழ்பெற்ற பியானோ கீ. Db-Eb-F-Gb-Ab-Bb-C-Db.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "Db மேஜர் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "Db4",
                                            "Eb4",
                                            "F4",
                                            "Gb4"
                                    ],
                                    [
                                            "Ab4",
                                            "Bb4",
                                            "C5",
                                            "Db5"
                                    ],
                                    [
                                            "Db5",
                                            "C5",
                                            "Bb4",
                                            "Ab4"
                                    ],
                                    [
                                            "Gb4",
                                            "F4",
                                            "Eb4",
                                            "Db4"
                                    ]
                            ]
                    }
            ]
    },
    "m14": {
            "id": "m14",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "C Major",
            "title": "14. C மேஜர் 2 ஆக்டேவ்கள் (C Major 2-Octaves • பெருவிரல் நுழைத்தல்)",
            "desc": "C4 முதல் C6 வரை தொடர்ச்சியாக 2 ஆக்டேவ்கள் வாசிக்கும் சர்வதேச கிரேடு தேர்வுப் பயிற்சி (1-2-3-1-2-3-4-1-2-3-1-2-3-4-5).",
            "tempo": 90,
            "lines": [
                    {
                            "title": "2 ஆக்டேவ் ஏறுவரிசை (C4 to C6)",
                            "measures": [
                                    [
                                            "C4",
                                            "D4",
                                            "E4",
                                            "F4"
                                    ],
                                    [
                                            "G4",
                                            "A4",
                                            "B4",
                                            "C5"
                                    ],
                                    [
                                            "D5",
                                            "E5",
                                            "F5",
                                            "G5"
                                    ],
                                    [
                                            "A5",
                                            "B5",
                                            "C6",
                                            ","
                                    ]
                            ]
                    },
                    {
                            "title": "2 ஆக்டேவ் இறங்குவரிசை (C6 to C4)",
                            "measures": [
                                    [
                                            "C6",
                                            "B5",
                                            "A5",
                                            "G5"
                                    ],
                                    [
                                            "F5",
                                            "E5",
                                            "D5",
                                            "C5"
                                    ],
                                    [
                                            "B4",
                                            "A4",
                                            "G4",
                                            "F4"
                                    ],
                                    [
                                            "E4",
                                            "D4",
                                            "C4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "m15": {
            "id": "m15",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "C Major",
            "title": "15. C மேஜர் பெண்டாடோனிக் ஸ்கேல் (C Major Pentatonic • 5 நோட்டுகள்)",
            "desc": "4 மற்றும் 7 நோட்டுகள் இல்லாத 5 நோட் உலக ஸ்கேல்: C - D - E - G - A - C. கர்நாடக மோகனம் ராகத்திற்கு இணையானது.",
            "tempo": 95,
            "lines": [
                    {
                            "title": "C பெண்டாடோனிக் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "C4",
                                            "D4",
                                            "E4",
                                            "G4"
                                    ],
                                    [
                                            "A4",
                                            "C5",
                                            "A4",
                                            "G4"
                                    ],
                                    [
                                            "E4",
                                            "D4",
                                            "C4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "m16": {
            "id": "m16",
            "cat": "major_scales",
            "catTamil": "2. மேஜர் ஸ்கேல்கள் (Major Scales)",
            "meter": "4/4",
            "key": "G Major",
            "title": "16. G மேஜர் பெண்டாடோனிக் ஸ்கேல் (G Major Pentatonic)",
            "desc": "நாட்டுப்புற மற்றும் ராக் மெலடிகளுக்கு உகந்த 5 நோட் ஸ்கேல்: G - A - B - D - E - G.",
            "tempo": 95,
            "lines": [
                    {
                            "title": "G பெண்டாடோனிக் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "G4",
                                            "A4",
                                            "B4",
                                            "D5"
                                    ],
                                    [
                                            "E5",
                                            "G5",
                                            "E5",
                                            "D5"
                                    ],
                                    [
                                            "B4",
                                            "A4",
                                            "G4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    # ---------------- 3. MINOR, PENTATONIC & BLUES SCALES (மைனர் & ப்ளூஸ் ஸ்கேல்கள் - 12 பாடங்கள்) ----------------
    "mn1": {
            "id": "mn1",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "A Minor",
            "title": "1. A நேச்சுரல் மைனர் ஸ்கேல் (A Natural Minor • ஏயோலியன் மோடு)",
            "desc": "C மேஜரின் ரிலேட்டிவ் மைனர்! எந்தவித Sharps/Flats இல்லாத அனைத்து வெள்ளை விசைகள்: A-B-C-D-E-F-G-A. ஆழ்ந்த சோகமும் அமைதியும் தரும் ஒலி.",
            "tempo": 85,
            "lines": [
                    {
                            "title": "A நேச்சுரல் மைனர் ஏறு & இறங்கு (A3 to A4)",
                            "measures": [
                                    [
                                            "A3",
                                            "B3",
                                            "C4",
                                            "D4"
                                    ],
                                    [
                                            "E4",
                                            "F4",
                                            "G4",
                                            "A4"
                                    ],
                                    [
                                            "A4",
                                            "G4",
                                            "F4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "C4",
                                            "B3",
                                            "A3"
                                    ]
                            ]
                    }
            ]
    },
    "mn2": {
            "id": "mn2",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "A Minor",
            "title": "2. A ஹார்மோனிக் மைனர் ஸ்கேல் (A Harmonic Minor • Raised 7th G#)",
            "desc": "கிளாசிக்கல் மற்றும் அரேபிய இசையில் மிகவும் புகழ்பெற்ற ஸ்கேல்! 7-வது நோட்டு G# ஆக உயர்த்தப்படும்: A-B-C-D-E-F-G#-A. F-க்கும் G#-க்கும் இடையே உள்ள ஒன்றரைக்கட்டை (Augmented 2nd) மர்மமான நாடகத் தன்மையை உருவாக்கும்.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "A ஹார்மோனிக் மைனர் ஏறு & இறங்கு (A3 to A4)",
                            "measures": [
                                    [
                                            "A3",
                                            "B3",
                                            "C4",
                                            "D4"
                                    ],
                                    [
                                            "E4",
                                            "F4",
                                            "G#4",
                                            "A4"
                                    ],
                                    [
                                            "A4",
                                            "G#4",
                                            "F4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "C4",
                                            "B3",
                                            "A3"
                                    ]
                            ]
                    }
            ]
    },
    "mn3": {
            "id": "mn3",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "A Minor",
            "title": "3. A மெலோடிக் மைனர் ஸ்கேல் (A Melodic Minor • ஏறு & இறங்கு மாறுபாடு)",
            "desc": "பாட இனிமையாக இருக்கும்படி ஏறும் போது 6 & 7 உயரும் (F# & G#), இறங்கும் போது நேச்சுரல் மைனராக மாறும் (G♮ & F♮). ஏறு: A-B-C-D-E-F#-G#-A | இறங்கு: A-G-F-E-D-C-B-A.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "ஏறுவரிசை (Ascending: F# & G#)",
                            "measures": [
                                    [
                                            "A3",
                                            "B3",
                                            "C4",
                                            "D4"
                                    ],
                                    [
                                            "E4",
                                            "F#4",
                                            "G#4",
                                            "A4"
                                    ]
                            ]
                    },
                    {
                            "title": "இறங்குவரிசை (Descending: G♮ & F♮)",
                            "measures": [
                                    [
                                            "A4",
                                            "G4",
                                            "F4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "C4",
                                            "B3",
                                            "A3"
                                    ]
                            ]
                    }
            ]
    },
    "mn4": {
            "id": "mn4",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "D Minor",
            "title": "4. D ஹார்மோனிக் மைனர் ஸ்கேல் (D Harmonic Minor • Bb + C#)",
            "desc": "1 Flat (Bb) மற்றும் உயர்த்தப்பட்ட 7-வது நோட்டு (C#). D-E-F-G-A-Bb-C#-D.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "D ஹார்மோனிக் மைனர் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "D4",
                                            "E4",
                                            "F4",
                                            "G4"
                                    ],
                                    [
                                            "A4",
                                            "Bb4",
                                            "C#5",
                                            "D5"
                                    ],
                                    [
                                            "D5",
                                            "C#5",
                                            "Bb4",
                                            "A4"
                                    ],
                                    [
                                            "G4",
                                            "F4",
                                            "E4",
                                            "D4"
                                    ]
                            ]
                    }
            ]
    },
    "mn5": {
            "id": "mn5",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "E Minor",
            "title": "5. E ஹார்மோனிக் மைனர் ஸ்கேல் (E Harmonic Minor • F# + D#)",
            "desc": "1 Sharp (F#) மற்றும் உயர்த்தப்பட்ட 7-வது நோட்டு (D#). E-F#-G-A-B-C-D#-E.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "E ஹார்மோனிக் மைனர் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "E4",
                                            "F#4",
                                            "G4",
                                            "A4"
                                    ],
                                    [
                                            "B4",
                                            "C5",
                                            "D#5",
                                            "E5"
                                    ],
                                    [
                                            "E5",
                                            "D#5",
                                            "C5",
                                            "B4"
                                    ],
                                    [
                                            "A4",
                                            "G4",
                                            "F#4",
                                            "E4"
                                    ]
                            ]
                    }
            ]
    },
    "mn6": {
            "id": "mn6",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "C Minor",
            "title": "6. C ஹார்மோனிக் மைனர் ஸ்கேல் (C Harmonic Minor • Eb, Ab + B♮)",
            "desc": "பீத்தோவனின் புகழ்பெற்ற சிம்பொனி 5 அமைந்த கம்பீரமான கீ. C-D-Eb-F-G-Ab-B-C.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "C ஹார்மோனிக் மைனர் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "C4",
                                            "D4",
                                            "Eb4",
                                            "F4"
                                    ],
                                    [
                                            "G4",
                                            "Ab4",
                                            "B4",
                                            "C5"
                                    ],
                                    [
                                            "C5",
                                            "B4",
                                            "Ab4",
                                            "G4"
                                    ],
                                    [
                                            "F4",
                                            "Eb4",
                                            "D4",
                                            "C4"
                                    ]
                            ]
                    }
            ]
    },
    "mn7": {
            "id": "mn7",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "G Minor",
            "title": "7. G ஹார்மோனிக் மைனர் ஸ்கேல் (G Harmonic Minor • Bb, Eb + F#)",
            "desc": "மொஸார்ட்டின் புகழ்பெற்ற சிம்பொனி 40 அமைந்த கீ. G-A-Bb-C-D-Eb-F#-G.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "G ஹார்மோனிக் மைனர் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "G4",
                                            "A4",
                                            "Bb4",
                                            "C5"
                                    ],
                                    [
                                            "D5",
                                            "Eb5",
                                            "F#5",
                                            "G5"
                                    ],
                                    [
                                            "G5",
                                            "F#5",
                                            "Eb5",
                                            "D5"
                                    ],
                                    [
                                            "C5",
                                            "Bb4",
                                            "A4",
                                            "G4"
                                    ]
                            ]
                    }
            ]
    },
    "mn8": {
            "id": "mn8",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "B Minor",
            "title": "8. B ஹார்மோனிக் மைனர் ஸ்கேல் (B Harmonic Minor • F#, C# + A#)",
            "desc": "2 Sharps மற்றும் உயர்த்தப்பட்ட 7-வது நோட்டு (A#). B-C#-D-E-F#-G-A#-B.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "B ஹார்மோனிக் மைனர் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "B3",
                                            "C#4",
                                            "D4",
                                            "E4"
                                    ],
                                    [
                                            "F#4",
                                            "G4",
                                            "A#4",
                                            "B4"
                                    ],
                                    [
                                            "B4",
                                            "A#4",
                                            "G4",
                                            "F#4"
                                    ],
                                    [
                                            "E4",
                                            "D4",
                                            "C#4",
                                            "B3"
                                    ]
                            ]
                    }
            ]
    },
    "mn9": {
            "id": "mn9",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "F Minor",
            "title": "9. F ஹார்மோனிக் மைனர் ஸ்கேல் (F Harmonic Minor • 4 Flats + E♮)",
            "desc": "பீத்தோவனின் அப்பேஷனாட்டா சோனாட்டா (Appassionata) அமைந்த தீவிர உணர்ச்சி மிக்க கீ. F-G-Ab-Bb-C-Db-E-F.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "F ஹார்மோனிக் மைனர் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "F4",
                                            "G4",
                                            "Ab4",
                                            "Bb4"
                                    ],
                                    [
                                            "C5",
                                            "Db5",
                                            "E5",
                                            "F5"
                                    ],
                                    [
                                            "F5",
                                            "E5",
                                            "Db5",
                                            "C5"
                                    ],
                                    [
                                            "Bb4",
                                            "Ab4",
                                            "G4",
                                            "F4"
                                    ]
                            ]
                    }
            ]
    },
    "mn10": {
            "id": "mn10",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "A Minor",
            "title": "10. A மைனர் பெண்டாடோனிக் ஸ்கேல் (A Minor Pentatonic • ராக் சோலோ)",
            "desc": "உலக ராக் கிட்டார் மற்றும் பியானோ சோலோக்களின் அரசன்! A - C - D - E - G - A.",
            "tempo": 95,
            "lines": [
                    {
                            "title": "A மைனர் பெண்டாடோனிக் ஏறு & இறங்கு",
                            "measures": [
                                    [
                                            "A3",
                                            "C4",
                                            "D4",
                                            "E4"
                                    ],
                                    [
                                            "G4",
                                            "A4",
                                            "G4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "C4",
                                            "A3",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "mn11": {
            "id": "mn11",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "C Minor",
            "title": "11. C ப்ளூஸ் ஸ்கேல் (The C Blues Scale • Blue Note F#)",
            "desc": "ப்ளூஸ் இசையின் தலையாய ரகசியம்: F#-ஐ (Diminished 5th Blue Note) சேர்த்து வாசிப்பது. C - Eb - F - F# - G - Bb - C.",
            "tempo": 90,
            "lines": [
                    {
                            "title": "C ப்ளூஸ் ஸ்கேல் நடை",
                            "measures": [
                                    [
                                            "C4",
                                            "Eb4",
                                            "F4",
                                            "F#4"
                                    ],
                                    [
                                            "G4",
                                            "Bb4",
                                            "C5",
                                            "Bb4"
                                    ],
                                    [
                                            "G4",
                                            "F#4",
                                            "F4",
                                            "Eb4"
                                    ],
                                    [
                                            "C4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "mn12": {
            "id": "mn12",
            "cat": "minor_scales",
            "catTamil": "3. மைனர் ஸ்கேல்கள் (Minor Scales)",
            "meter": "4/4",
            "key": "A Minor",
            "title": "12. A ப்ளூஸ் ஸ்கேல் (The A Blues Scale • Blue Note D#)",
            "desc": "A - C - D - D# - E - G - A. ஜாஸ் மற்றும் ப்ளூஸ் சோலோ வாசிக்க மிகச் சிறந்த ஸ்கேல்.",
            "tempo": 90,
            "lines": [
                    {
                            "title": "A ப்ளூஸ் ஸ்கேல் நடை",
                            "measures": [
                                    [
                                            "A3",
                                            "C4",
                                            "D4",
                                            "D#4"
                                    ],
                                    [
                                            "E4",
                                            "G4",
                                            "A4",
                                            "G4"
                                    ],
                                    [
                                            "E4",
                                            "D#4",
                                            "D4",
                                            "C4"
                                    ],
                                    [
                                            "A3",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    # ---------------- 4. CHORDS, INVERSIONS & ARPEGGIOS (கார்ட்கள் & ஆர்பெஜியோ - 12 பாடங்கள்) ----------------
    "c1": {
            "id": "c1",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "1. C மேஜர் பிரைமரி ட்ரையாட்கள் (Primary Triads • I - IV - V - I)",
            "desc": "C Major-ன் மூன்று மிக முக்கியமான தூண்கள்: C (I: C-E-G), F (IV: F-A-C), G (V: G-B-D). உலகெங்கும் லட்சக்கணக்கான பாடல்கள் இந்த 3 கார்டுகளில் அமைந்துள்ளன.",
            "tempo": 75,
            "lines": [
                    {
                            "title": "ஆர்பெஜியோ வடிவத்தில் பிரைமரி கார்ட்கள் (Broken Chords)",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "F4",
                                            "A4",
                                            "C5",
                                            "F5"
                                    ],
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "G5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "C",
                                            "E",
                                            "G",
                                            "C (I)"
                                    ],
                                    [
                                            "F",
                                            "A",
                                            "C",
                                            "F (IV)"
                                    ],
                                    [
                                            "G",
                                            "B",
                                            "D",
                                            "G (V)"
                                    ],
                                    [
                                            "C",
                                            "E",
                                            "G",
                                            "C (I)"
                                    ]
                            ]
                    }
            ]
    },
    "c2": {
            "id": "c2",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "A Minor",
            "title": "2. மைனர் ட்ரையாட்கள் (Minor Triads • Am - Dm - Em - Am)",
            "desc": "மைனர் கார்டின் சூத்திரம்: Root + Minor 3rd (3 semitones) + Perfect 5th (7 semitones). Am: A-C-E, Dm: D-F-A, Em: E-G-B.",
            "tempo": 75,
            "lines": [
                    {
                            "title": "ஆர்பெஜியோ வடிவத்தில் மைனர் கார்ட்கள்",
                            "measures": [
                                    [
                                            "A3",
                                            "C4",
                                            "E4",
                                            "A4"
                                    ],
                                    [
                                            "D4",
                                            "F4",
                                            "A4",
                                            "D5"
                                    ],
                                    [
                                            "E4",
                                            "G4",
                                            "B4",
                                            "E5"
                                    ],
                                    [
                                            "A3",
                                            "C4",
                                            "E4",
                                            "A4"
                                    ]
                            ]
                    }
            ]
    },
    "c3": {
            "id": "c3",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "3. C மேஜர் கார்ட் இன்வெர்ஷன்கள் (Chord Inversions • Root, 1st & 2nd)",
            "desc": "கார்ட் இன்வெர்ஷன் கை அசைவைக் குறைத்து மென்மையாக வாசிக்க உதவும்: Root Position (C-E-G), 1st Inversion (E-G-C), 2nd Inversion (G-C-E).",
            "tempo": 70,
            "lines": [
                    {
                            "title": "மூன்று நிலைகள் தொடர்ச்சி (Inversion Flow)",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "E4",
                                            "G4",
                                            "C5",
                                            "E5"
                                    ],
                                    [
                                            "G4",
                                            "C5",
                                            "E5",
                                            "G5"
                                    ],
                                    [
                                            "C5",
                                            "G4",
                                            "E4",
                                            "C4"
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "Root Pos (C-E-G)",
                                            "",
                                            "",
                                            ""
                                    ],
                                    [
                                            "1st Inv (E-G-C)",
                                            "",
                                            "",
                                            ""
                                    ],
                                    [
                                            "2nd Inv (G-C-E)",
                                            "",
                                            "",
                                            ""
                                    ],
                                    [
                                            "Resolution (C-E-G)",
                                            "",
                                            "",
                                            ""
                                    ]
                            ]
                    }
            ]
    },
    "c4": {
            "id": "c4",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "4. டாமினன்ட் 7th கார்ட்கள் (Dominant 7th • G7 & C7)",
            "desc": "டாமினன்ட் 7th கார்டு தீர்க்கமான பதற்றத்தை (Tension) உருவாக்கி Tonic கார்டுக்கு வழிநடத்தும். G7: G-B-D-F -> resolves to C Major.",
            "tempo": 75,
            "lines": [
                    {
                            "title": "G7 இருந்து C மேஜருக்கு தீர்வு (G7 to C Resolution)",
                            "measures": [
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "F5"
                                    ],
                                    [
                                            "E5",
                                            "C5",
                                            "G4",
                                            "E4"
                                    ],
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "F5"
                                    ],
                                    [
                                            "C5",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "c5": {
            "id": "c5",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "5. சஸ்பென்டட் கார்ட்கள் (Sus2 & Sus4 Chords • சினிமா ஒலி)",
            "desc": "3-வது நோட்டுக்கு பதிலாக 2 அல்லது 4-வது நோட்டை வைத்து உருவாக்கும் மிதக்கும் ஒலி. Csus2: C-D-G, Csus4: C-F-G -> resolves to C Major.",
            "tempo": 75,
            "lines": [
                    {
                            "title": "Csus4 -> C -> Csus2 -> C தொடர்",
                            "measures": [
                                    [
                                            "C4",
                                            "F4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "C4",
                                            "D4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "c6": {
            "id": "c6",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "6. மேஜர் & மைனர் 7th ஜாஸ் கார்ட்கள் (Jazz 7ths • Cmaj7, Dm7, Em7)",
            "desc": "ஜாஸ் மற்றும் நவீன பாப் இசையின் இனிமை நிறைந்த கார்டுகள். Cmaj7: C-E-G-B, Dm7: D-F-A-C, Em7: E-G-B-D.",
            "tempo": 75,
            "lines": [
                    {
                            "title": "ஜாஸ் 7th கார்டுகள் ஆர்பெஜியோ",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "B4"
                                    ],
                                    [
                                            "D4",
                                            "F4",
                                            "A4",
                                            "C5"
                                    ],
                                    [
                                            "E4",
                                            "G4",
                                            "B4",
                                            "D5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "B4"
                                    ]
                            ]
                    }
            ]
    },
    "c7": {
            "id": "c7",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "G Major",
            "title": "7. G மேஜர் கார்ட் இன்வெர்ஷன்கள் (G Chord Inversions)",
            "desc": "Root (G-B-D), 1st Inv (B-D-G), 2nd Inv (D-G-B).",
            "tempo": 75,
            "lines": [
                    {
                            "title": "G மேஜர் மூன்று நிலைகள்",
                            "measures": [
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "G5"
                                    ],
                                    [
                                            "B4",
                                            "D5",
                                            "G5",
                                            "B5"
                                    ],
                                    [
                                            "D5",
                                            "G5",
                                            "B5",
                                            "D6"
                                    ],
                                    [
                                            "G5",
                                            "D5",
                                            "B4",
                                            "G4"
                                    ]
                            ]
                    }
            ]
    },
    "c8": {
            "id": "c8",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "F Major",
            "title": "8. F மேஜர் கார்ட் இன்வெர்ஷன்கள் (F Chord Inversions)",
            "desc": "Root (F-A-C), 1st Inv (A-C-F), 2nd Inv (C-F-A).",
            "tempo": 75,
            "lines": [
                    {
                            "title": "F மேஜர் மூன்று நிலைகள்",
                            "measures": [
                                    [
                                            "F4",
                                            "A4",
                                            "C5",
                                            "F5"
                                    ],
                                    [
                                            "A4",
                                            "C5",
                                            "F5",
                                            "A5"
                                    ],
                                    [
                                            "C5",
                                            "F5",
                                            "A5",
                                            "C6"
                                    ],
                                    [
                                            "F5",
                                            "C5",
                                            "A4",
                                            "F4"
                                    ]
                            ]
                    }
            ]
    },
    "c9": {
            "id": "c9",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "9. டிமினிஷ்ட் 7th கார்ட்கள் (Diminished 7ths • Bdim7 & C#dim7)",
            "desc": "அனைத்தும் மைனர் 3rd இடைவெளிகளால் அமைந்த தீவிர பதற்றம் தரும் நாடக கார்டுகள். B-D-F-Ab.",
            "tempo": 70,
            "lines": [
                    {
                            "title": "Bdim7 இருந்து C மேஜருக்கு தீர்வு",
                            "measures": [
                                    [
                                            "B3",
                                            "D4",
                                            "F4",
                                            "Ab4"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "B3",
                                            "D4",
                                            "F4",
                                            "Ab4"
                                    ],
                                    [
                                            "C4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "c10": {
            "id": "c10",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "10. ஆக்மென்டட் ட்ரையாட்கள் (Augmented Triads • Caug & Gaug)",
            "desc": "1 - 3 - ♯5 சூத்திரம் கொண்ட கனவு போன்ற விண்வெளி சினிமா கார்டு. C - E - G#.",
            "tempo": 75,
            "lines": [
                    {
                            "title": "C -> Caug -> C6 -> C7 மிதக்கும் தொடர்",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G#4",
                                            "C5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "A4",
                                            "C5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "Bb4",
                                            "C5"
                                    ]
                            ]
                    }
            ]
    },
    "c11": {
            "id": "c11",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "11. C மேஜர் 2-ஆக்டேவ் ஆர்பெஜியோ (2-Octave Arpeggio Sprint)",
            "desc": "C3-E3-G3-C4-E4-G4-C5-E5-G5 முழு பியானோவில் பாயும் மேஜர் ஆர்பெஜியோ விரல் பயிற்சி.",
            "tempo": 100,
            "lines": [
                    {
                            "title": "2-ஆக்டேவ் பியானோ ஆர்பெஜியோ ஏறு-இறங்கு",
                            "measures": [
                                    [
                                            "C3",
                                            "E3",
                                            "G3",
                                            "C4"
                                    ],
                                    [
                                            "E4",
                                            "G4",
                                            "C5",
                                            "E5"
                                    ],
                                    [
                                            "G5",
                                            "E5",
                                            "C5",
                                            "G4"
                                    ],
                                    [
                                            "E4",
                                            "C4",
                                            "G3",
                                            "E3"
                                    ],
                                    [
                                            "C3",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "c12": {
            "id": "c12",
            "cat": "chords",
            "catTamil": "4. கார்ட்கள் & ஆர்பெஜியோ பயிற்சிகள் (Chords & Inversions)",
            "meter": "4/4",
            "key": "A Minor",
            "title": "12. A மைனர் 2-ஆக்டேவ் ஆர்பெஜியோ (A Minor 2-Octave Arpeggio)",
            "desc": "A2-C3-E3-A3-C4-E4-A4-C5-E5 மைனர் பியானோ ஆர்பெஜியோ ஓட்டம்.",
            "tempo": 100,
            "lines": [
                    {
                            "title": "A மைனர் ஆர்பெஜியோ ஏறு-இறங்கு",
                            "measures": [
                                    [
                                            "A2",
                                            "C3",
                                            "E3",
                                            "A3"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "A4",
                                            "C5"
                                    ],
                                    [
                                            "E5",
                                            "C5",
                                            "A4",
                                            "E4"
                                    ],
                                    [
                                            "C4",
                                            "A3",
                                            "E3",
                                            "C3"
                                    ],
                                    [
                                            "A2",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    # ---------------- 5. FAMOUS CHORD PROGRESSIONS (பிரபல கார்ட் தொடர்கள் - 12 பாடங்கள்) ----------------
    "cp1": {
            "id": "cp1",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "1. கிளாசிக் I - IV - V - I (C - F - G - C)",
            "desc": "பாப், ராக், போக் மற்றும் மேற்கத்திய கிளாசிக்கல் இசையின் மூல அடித்தளம். Tonic (C) -> Subdominant (F) -> Dominant (G) -> Home (C).",
            "tempo": 95,
            "lines": [
                    {
                            "title": "மெலடி & கார்ட் அவுட்லைன் (Melodic Outline)",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "E4"
                                    ],
                                    [
                                            "F4",
                                            "A4",
                                            "C5",
                                            "A4"
                                    ],
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "B4"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "C Chord (I)",
                                            "",
                                            "",
                                            ""
                                    ],
                                    [
                                            "F Chord (IV)",
                                            "",
                                            "",
                                            ""
                                    ],
                                    [
                                            "G Chord (V)",
                                            "",
                                            "",
                                            ""
                                    ],
                                    [
                                            "C Chord (Home)",
                                            "",
                                            "",
                                            ""
                                    ]
                            ]
                    }
            ]
    },
    "cp2": {
            "id": "cp2",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "2. பாப் 4-கார்ட்ஸ் ஆந்தம் (Pop 4-Chords: I - V - vi - IV • C - G - Am - F)",
            "desc": "இசை வரலாற்றிலேயே மிக வெற்றிகரமான கார்ட் தொடர்! Let It Be, Someone Like You, Don't Stop Believin', Despacito உட்பட நூற்றுக்கணக்கான உலகப் புகழ்பெற்ற ஹிட் பாடல்கள் இதில் அமைந்துள்ளன.",
            "tempo": 100,
            "lines": [
                    {
                            "title": "C - G - Am - F தொடர்ச்சி",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "G4"
                                    ],
                                    [
                                            "A4",
                                            "C5",
                                            "E5",
                                            "A4"
                                    ],
                                    [
                                            "F4",
                                            "A4",
                                            "C5",
                                            "F4"
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "C Major (I)",
                                            "",
                                            "",
                                            ""
                                    ],
                                    [
                                            "G Major (V)",
                                            "",
                                            "",
                                            ""
                                    ],
                                    [
                                            "A Minor (vi)",
                                            "",
                                            "",
                                            ""
                                    ],
                                    [
                                            "F Major (IV)",
                                            "",
                                            "",
                                            ""
                                    ]
                            ]
                    }
            ]
    },
    "cp3": {
            "id": "cp3",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "3. 50ஸ் டூ-வாப் தொடர் (50s Doo-Wop: I - vi - IV - V • C - Am - F - G)",
            "desc": "Stand By Me, Earth Angel போன்ற 1950-களின் பொற்கால டூ-வாப் பாடல்கள் மற்றும் ரொமாண்டிக் மெலடிகளுக்கு வித்திட்ட புகழ்பெற்ற கார்ட் தொடர்.",
            "tempo": 90,
            "lines": [
                    {
                            "title": "C - Am - F - G தொடர்ச்சி",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "E4"
                                    ],
                                    [
                                            "A3",
                                            "C4",
                                            "E4",
                                            "C4"
                                    ],
                                    [
                                            "F3",
                                            "A3",
                                            "C4",
                                            "A3"
                                    ],
                                    [
                                            "G3",
                                            "B3",
                                            "D4",
                                            "B3"
                                    ]
                            ]
                    }
            ]
    },
    "cp4": {
            "id": "cp4",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "4. ஜாஸ் ஸ்டாண்டர்ட் ii - V - I (Dm7 - G7 - Cmaj7)",
            "desc": "ஜாஸ் இசையின் இதயம் போன்ற மிக முக்கியமான கார்ட் தொடர். Autumn Leaves, Fly Me to the Moon போன்ற எண்ணற்ற ஜாஸ் பாடல்களின் அடித்தளம்.",
            "tempo": 90,
            "lines": [
                    {
                            "title": "Dm7 -> G7 -> Cmaj7 ஜாஸ் தொடர்",
                            "measures": [
                                    [
                                            "D4",
                                            "F4",
                                            "A4",
                                            "C5"
                                    ],
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "F5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "B4"
                                    ],
                                    [
                                            "C4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "cp5": {
            "id": "cp5",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "5. 12-பார் ப்ளூஸ் தொடர் (12-Bar Blues in C • C7 - F7 - G7)",
            "desc": "ராக் அண்ட் ரோல் மற்றும் ப்ளூஸ் இசையின் பிறப்பிடம். 12 அளவுகள் (12 Measures) கொண்ட உலகப் புகழ்பெற்ற ப்ளூஸ் ஷஃபிள் நடை.",
            "tempo": 105,
            "lines": [
                    {
                            "title": "அளவுகள் 1-4: C7 அடிப்படை (4 Bars C7)",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "Bb4"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "Bb4"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "Bb4"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "Bb4"
                                    ]
                            ]
                    },
                    {
                            "title": "அளவுகள் 5-8: F7 & C7 (2 Bars F7 + 2 Bars C7)",
                            "measures": [
                                    [
                                            "F4",
                                            "A4",
                                            "C5",
                                            "Eb5"
                                    ],
                                    [
                                            "F4",
                                            "A4",
                                            "C5",
                                            "Eb5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "Bb4"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "Bb4"
                                    ]
                            ]
                    },
                    {
                            "title": "அளவுகள் 9-12: G7 -> F7 -> C7 -> G7 டர்ன்அரவுண்ட்",
                            "measures": [
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "F5"
                                    ],
                                    [
                                            "F4",
                                            "A4",
                                            "C5",
                                            "Eb5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "Bb4"
                                    ],
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "F5"
                                    ]
                            ]
                    }
            ]
    },
    "cp6": {
            "id": "cp6",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "D Major",
            "title": "6. பாச்சல்பெல் கேனான் தொடர் (Pachelbel's Canon: D - A - Bm - F#m - G - D - G - A)",
            "desc": "ஜோஹான் பாச்சல்பெல்லின் புகழ்பெற்ற கேனான் இன் D கார்ட் தொடர். கிளாசிக்கல் முதல் இன்றைய நவீன பாப் வரை கோடிக்கணக்கானோரைக் கவர்ந்த மெல்லிசை.",
            "tempo": 75,
            "lines": [
                    {
                            "title": "கேனான் 8 கார்டுகள் வரிசை",
                            "measures": [
                                    [
                                            "D4",
                                            "F#4",
                                            "A4",
                                            "D5"
                                    ],
                                    [
                                            "A3",
                                            "C#4",
                                            "E4",
                                            "A4"
                                    ],
                                    [
                                            "B3",
                                            "D4",
                                            "F#4",
                                            "B4"
                                    ],
                                    [
                                            "F#3",
                                            "A3",
                                            "C#4",
                                            "F#4"
                                    ],
                                    [
                                            "G3",
                                            "B3",
                                            "D4",
                                            "G4"
                                    ],
                                    [
                                            "D3",
                                            "F#3",
                                            "A3",
                                            "D4"
                                    ],
                                    [
                                            "G3",
                                            "B3",
                                            "D4",
                                            "G4"
                                    ],
                                    [
                                            "A3",
                                            "C#4",
                                            "E4",
                                            "A4"
                                    ]
                            ]
                    }
            ]
    },
    "cp7": {
            "id": "cp7",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "G Major",
            "title": "7. 12-பார் ப்ளூஸ் இன் G (12-Bar Blues in G • G7 - C7 - D7)",
            "desc": "G கீயில் அமைந்த உலகப் புகழ்பெற்ற ப்ளூஸ் மற்றும் ராக் ஷஃபிள் தொடர்.",
            "tempo": 105,
            "lines": [
                    {
                            "title": "G7 -> C7 -> D7 ப்ளூஸ் தொடர்ச்சி",
                            "measures": [
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "F5"
                                    ],
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "F5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "Bb4"
                                    ],
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "F5"
                                    ],
                                    [
                                            "D4",
                                            "F#4",
                                            "A4",
                                            "C5"
                                    ],
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "Bb4"
                                    ],
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "F5"
                                    ],
                                    [
                                            "D4",
                                            "F#4",
                                            "A4",
                                            "C5"
                                    ]
                            ]
                    }
            ]
    },
    "cp8": {
            "id": "cp8",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "A Minor",
            "title": "8. அண்டலூசியன் தொடர் (Andalusian Cadence • Am - G - F - E)",
            "desc": "ஸ்பானிஷ் ஃபிளமென்கோ இசையின் இதயம் போன்ற இறங்குமுக தொடர்: i -> VII -> VI -> V (Am -> G -> F -> E). Hit the Road Jack போன்ற எண்ணற்ற பாடல்கள்.",
            "tempo": 110,
            "lines": [
                    {
                            "title": "ஸ்பானிஷ் ஃபிளமென்கோ கார்ட் தொடர்ச்சி",
                            "measures": [
                                    [
                                            "A3",
                                            "C4",
                                            "E4",
                                            "A4"
                                    ],
                                    [
                                            "G3",
                                            "B3",
                                            "D4",
                                            "G4"
                                    ],
                                    [
                                            "F3",
                                            "A3",
                                            "C4",
                                            "F4"
                                    ],
                                    [
                                            "E3",
                                            "G#3",
                                            "B3",
                                            "E4"
                                    ]
                            ]
                    }
            ]
    },
    "cp9": {
            "id": "cp9",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "9. ராயல் ரோடு தொடர் (Royal Road • IV - V - iii - vi: F - G - Em - Am)",
            "desc": "ஜப்பான் மற்றும் ஆசிய அனிமேஷன் பாப் இசையின் (Anime / J-Pop) தங்கச் சுரங்க கார்ட் தொடர். ஏக்கம் கலந்த இனிமை தரும்.",
            "tempo": 100,
            "lines": [
                    {
                            "title": "F -> G -> Em -> Am ராயல் ரோடு",
                            "measures": [
                                    [
                                            "F4",
                                            "A4",
                                            "C5",
                                            "F5"
                                    ],
                                    [
                                            "G4",
                                            "B4",
                                            "D5",
                                            "G5"
                                    ],
                                    [
                                            "E4",
                                            "G4",
                                            "B4",
                                            "E5"
                                    ],
                                    [
                                            "A4",
                                            "C5",
                                            "E5",
                                            "A5"
                                    ]
                            ]
                    }
            ]
    },
    "cp10": {
            "id": "cp10",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "10. மொஸார்ட் கிளாசிக்கல் ஆல்பர்ட்டி நடை (Sonata in C Accompaniment)",
            "desc": "மொஸார்ட்டின் புகழ்பெற்ற பியானோ சோனாட்டா (K. 545) இடது கை ஆல்பர்ட்டி பேஸ் கார்ட் தொடர்.",
            "tempo": 110,
            "lines": [
                    {
                            "title": "I -> IV -> I -> V7 ஆல்பர்ட்டி சுழற்சி",
                            "measures": [
                                    [
                                            "C3",
                                            "G3",
                                            "E3",
                                            "G3"
                                    ],
                                    [
                                            "F3",
                                            "C4",
                                            "A3",
                                            "C4"
                                    ],
                                    [
                                            "C3",
                                            "G3",
                                            "E3",
                                            "G3"
                                    ],
                                    [
                                            "B2",
                                            "G3",
                                            "D3",
                                            "G3"
                                    ],
                                    [
                                            "C3",
                                            "G3",
                                            "E3",
                                            "G3"
                                    ],
                                    [
                                            "C3",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "cp11": {
            "id": "cp11",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "11. பாப் பாலாட் 1-5-8-9 உடைந்த கார்ட் நடை (Pop Ballad Pattern)",
            "desc": "நவீன சினிமா மற்றும் மெலோடி பாடல்களில் பியானோ கலைஞர்கள் பயன்படுத்தும் 1-5-8-9 அழகான ஆர்பெஜியோ நடை.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "C -> G -> Am -> F பாலாட் நடை",
                            "measures": [
                                    [
                                            "C3",
                                            "G3",
                                            "C4",
                                            "D4"
                                    ],
                                    [
                                            "G2",
                                            "D3",
                                            "G3",
                                            "A3"
                                    ],
                                    [
                                            "A2",
                                            "E3",
                                            "A3",
                                            "B3"
                                    ],
                                    [
                                            "F2",
                                            "C3",
                                            "F3",
                                            "G3"
                                    ]
                            ]
                    }
            ]
    },
    "cp12": {
            "id": "cp12",
            "cat": "progressions",
            "catTamil": "5. பிரபல கார்ட் தொடர்கள் (Famous Chord Progressions)",
            "meter": "4/4",
            "key": "C Major",
            "title": "12. ஜாஸ் டர்ன்அரவுண்ட் (Jazz Turnaround: I - vi - ii - V • Cmaj7 - Am7 - Dm7 - G7)",
            "desc": "ஜாஸ் கோரஸின் முடிவில் மீண்டும் தொடக்கத்திற்கு அழைத்து வரும் 4 கார்ட் டர்ன்அரவுண்ட் சூத்திரம்.",
            "tempo": 95,
            "lines": [
                    {
                            "title": "Cmaj7 -> Am7 -> Dm7 -> G7 தொடர்ச்சி",
                            "measures": [
                                    [
                                            "C4",
                                            "E4",
                                            "G4",
                                            "B4"
                                    ],
                                    [
                                            "A3",
                                            "C4",
                                            "E4",
                                            "G4"
                                    ],
                                    [
                                            "D4",
                                            "F4",
                                            "A4",
                                            "C5"
                                    ],
                                    [
                                            "G3",
                                            "B3",
                                            "D4",
                                            "F4"
                                    ],
                                    [
                                            "C4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    # ---------------- 6. CLASSICAL PIECES & WORLD MELODIES (பிரபல பாடல்கள் & மெலடிகள் - 18 பாடங்கள்) ----------------
    "w1": {
            "id": "w1",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "4/4",
            "key": "C Major",
            "title": "1. ஓட் டு ஜாய் (Ode to Joy • பீத்தோவன் சிம்பொனி 9 தீம்)",
            "desc": "லுட்விக் வான் பீத்தோவனின் இறுதி மற்றும் மாபெரும் சிம்பொனி 9-ன் உலகப் புகழ்பெற்ற மனித நேய மெலடி. ஆரம்ப பியானோ கற்பவர்களுக்கு உகந்த பாடல்.",
            "tempo": 105,
            "lines": [
                    {
                            "title": "பல்லவி வரி 1 (Joyful, joyful, we adore thee)",
                            "measures": [
                                    [
                                            "E4",
                                            "E4",
                                            "F4",
                                            "G4"
                                    ],
                                    [
                                            "G4",
                                            "F4",
                                            "E4",
                                            "D4"
                                    ],
                                    [
                                            "C4",
                                            "C4",
                                            "D4",
                                            "E4"
                                    ],
                                    [
                                            "E4",
                                            "D4",
                                            "D4",
                                            ","
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "Joy-",
                                            "ful,",
                                            "joy-",
                                            "ful,"
                                    ],
                                    [
                                            "we",
                                            "a-",
                                            "dore",
                                            "thee,"
                                    ],
                                    [
                                            "God",
                                            "of",
                                            "glo-",
                                            "ry,"
                                    ],
                                    [
                                            "Lord",
                                            "of",
                                            "love.",
                                            ""
                                    ]
                            ]
                    },
                    {
                            "title": "பல்லவி வரி 2 (Hearts unfold like flowers before thee)",
                            "measures": [
                                    [
                                            "E4",
                                            "E4",
                                            "F4",
                                            "G4"
                                    ],
                                    [
                                            "G4",
                                            "F4",
                                            "E4",
                                            "D4"
                                    ],
                                    [
                                            "C4",
                                            "C4",
                                            "D4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "C4",
                                            "C4",
                                            ","
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "Hearts",
                                            "un-",
                                            "fold",
                                            "like"
                                    ],
                                    [
                                            "flow'rs",
                                            "be-",
                                            "fore",
                                            "Thee,"
                                    ],
                                    [
                                            "Hail-",
                                            "ing",
                                            "Thee",
                                            "as"
                                    ],
                                    [
                                            "sun",
                                            "a-",
                                            "bove.",
                                            ""
                                    ]
                            ]
                    },
                    {
                            "title": "அனுபல்லவி & உச்சகட்டம் (Bridge & Grand Resolution)",
                            "measures": [
                                    [
                                            "D4",
                                            "D4",
                                            "E4",
                                            "C4"
                                    ],
                                    [
                                            "D4",
                                            "E4",
                                            "F4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "C4",
                                            "D4",
                                            "G3"
                                    ],
                                    [
                                            "E4",
                                            "E4",
                                            "F4",
                                            "G4"
                                    ],
                                    [
                                            "G4",
                                            "F4",
                                            "E4",
                                            "D4"
                                    ],
                                    [
                                            "C4",
                                            "C4",
                                            "D4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "C4",
                                            "C4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w2": {
            "id": "w2",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "3/4",
            "key": "A Minor",
            "title": "2. ஃபர் எலிஸ் (Für Elise • பீத்தோவன் பியானோ மாஸ்டர்பீஸ்)",
            "desc": "பீத்தோவனின் மிகப்பிரபலமான பேகடெல் (Bagatelle in A minor, WoO 59). E5 மற்றும் D#5 இடையே ஊசலாடும் அதன் தனித்துவமான அறிமுக மெலடி பியானோ உலகின் அடையாளம்.",
            "tempo": 120,
            "lines": [
                    {
                            "title": "பிரபல அறிமுக தீம் (Famous Main Theme)",
                            "measures": [
                                    [
                                            "E5",
                                            "D#5",
                                            "E5"
                                    ],
                                    [
                                            "D#5",
                                            "E5",
                                            "B4"
                                    ],
                                    [
                                            "D5",
                                            "C5",
                                            "A4"
                                    ],
                                    [
                                            ",",
                                            "C4",
                                            "E4"
                                    ],
                                    [
                                            "A4",
                                            "B4",
                                            ","
                                    ],
                                    [
                                            ",",
                                            "E4",
                                            "G#4"
                                    ],
                                    [
                                            "B4",
                                            "C5",
                                            ","
                                    ],
                                    [
                                            ",",
                                            "E4",
                                            "E5"
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "E",
                                            "D#",
                                            "E"
                                    ],
                                    [
                                            "D#",
                                            "E",
                                            "B"
                                    ],
                                    [
                                            "D",
                                            "C",
                                            "A"
                                    ],
                                    [
                                            "",
                                            "C",
                                            "E"
                                    ],
                                    [
                                            "A",
                                            "B",
                                            ""
                                    ],
                                    [
                                            "",
                                            "E",
                                            "G#"
                                    ],
                                    [
                                            "B",
                                            "C",
                                            ""
                                    ],
                                    [
                                            "",
                                            "E",
                                            "E'"
                                    ]
                            ]
                    },
                    {
                            "title": "தீம் மறுதொடர்ச்சி & முடிவு (Theme Repeat & Cadence)",
                            "measures": [
                                    [
                                            "E5",
                                            "D#5",
                                            "E5"
                                    ],
                                    [
                                            "D#5",
                                            "E5",
                                            "B4"
                                    ],
                                    [
                                            "D5",
                                            "C5",
                                            "A4"
                                    ],
                                    [
                                            ",",
                                            "C4",
                                            "E4"
                                    ],
                                    [
                                            "A4",
                                            "B4",
                                            ","
                                    ],
                                    [
                                            ",",
                                            "E4",
                                            "C5"
                                    ],
                                    [
                                            "B4",
                                            "A4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w3": {
            "id": "w3",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "4/4",
            "key": "D Major",
            "title": "3. கேனான் இன் D தீம் (Canon in D • பாச்சல்பெல் மெலடி)",
            "desc": "ஜோஹான் பாச்சல்பெல்லின் புகழ்பெற்ற மெலடி. திருமண விழாக்கள் மற்றும் மங்களகரமான நிகழ்ச்சிகளில் உலகெங்கும் வாசிக்கப்படும் இனிமையான இசை.",
            "tempo": 72,
            "lines": [
                    {
                            "title": "மெலடி வரிசை 1 (Main Theme)",
                            "measures": [
                                    [
                                            "F#4",
                                            "E4",
                                            "D4",
                                            "C#4"
                                    ],
                                    [
                                            "B3",
                                            "A3",
                                            "B3",
                                            "C#4"
                                    ],
                                    [
                                            "D4",
                                            "C#4",
                                            "B3",
                                            "A3"
                                    ],
                                    [
                                            "G3",
                                            "F#3",
                                            "G3",
                                            "E3"
                                    ]
                            ]
                    },
                    {
                            "title": "மெலடி வரிசை 2 (Variation)",
                            "measures": [
                                    [
                                            "D4",
                                            "F#4",
                                            "A4",
                                            "G4"
                                    ],
                                    [
                                            "F#4",
                                            "D4",
                                            "F#4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "B3",
                                            "D4",
                                            "A3"
                                    ],
                                    [
                                            "G3",
                                            "B3",
                                            "A3",
                                            "G3"
                                    ],
                                    [
                                            "F#3",
                                            "A3",
                                            "D4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w4": {
            "id": "w4",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "4/4",
            "key": "C Major",
            "title": "4. ட்விங்கிள் ட்விங்கிள் லிட்டில் ஸ்டார் (Twinkle Twinkle Little Star)",
            "desc": "மொஸார்ட்டின் 12 மாறுபாடுகள் பாடலின் மூல மெலடி (Ah! vous dirai-je, maman). 1-வது டிகிரி (C) மற்றும் 5-வது டிகிரி (G) தாண்டலைக் கற்பிக்கும் சிறந்த பால பாடம்.",
            "tempo": 95,
            "lines": [
                    {
                            "title": "பல்லவி (Twin-kle, twin-kle, lit-tle star)",
                            "measures": [
                                    [
                                            "C4",
                                            "C4",
                                            "G4",
                                            "G4"
                                    ],
                                    [
                                            "A4",
                                            "A4",
                                            "G4",
                                            ","
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "Twin-",
                                            "kle,",
                                            "twin-",
                                            "kle,"
                                    ],
                                    [
                                            "lit-",
                                            "tle",
                                            "star,",
                                            ""
                                    ]
                            ]
                    },
                    {
                            "title": "அனுபல்லவி 1 (How I won-der what you are)",
                            "measures": [
                                    [
                                            "F4",
                                            "F4",
                                            "E4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "D4",
                                            "C4",
                                            ","
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "How",
                                            "I",
                                            "won-",
                                            "der"
                                    ],
                                    [
                                            "what",
                                            "you",
                                            "are!",
                                            ""
                                    ]
                            ]
                    },
                    {
                            "title": "சரணம் (Up a-bove the world so high)",
                            "measures": [
                                    [
                                            "G4",
                                            "G4",
                                            "F4",
                                            "F4"
                                    ],
                                    [
                                            "E4",
                                            "E4",
                                            "D4",
                                            ","
                                    ],
                                    [
                                            "G4",
                                            "G4",
                                            "F4",
                                            "F4"
                                    ],
                                    [
                                            "E4",
                                            "E4",
                                            "D4",
                                            ","
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "Up",
                                            "a-",
                                            "bove",
                                            "the"
                                    ],
                                    [
                                            "world",
                                            "so",
                                            "high,",
                                            ""
                                    ],
                                    [
                                            "Like",
                                            "a",
                                            "dia-",
                                            "mond"
                                    ],
                                    [
                                            "in",
                                            "the",
                                            "sky.",
                                            ""
                                    ]
                            ]
                    },
                    {
                            "title": "பல்லவி முடிவு (Twin-kle, twin-kle, lit-tle star)",
                            "measures": [
                                    [
                                            "C4",
                                            "C4",
                                            "G4",
                                            "G4"
                                    ],
                                    [
                                            "A4",
                                            "A4",
                                            "G4",
                                            ","
                                    ],
                                    [
                                            "F4",
                                            "F4",
                                            "E4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            "D4",
                                            "C4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w5": {
            "id": "w5",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "3/4",
            "key": "G Major",
            "title": "5. மினுவெட் இன் G (Minuet in G Major • J.S. பாக் / பெட்சோல்ட்)",
            "desc": "அன்னா மாக்தலினா பாக் நோட்டுப் புத்தகத்திலிருந்து உலகப் புகழ்பெற்ற 3/4 வால்ட்ஸ் நடன இசை (BWV Anh. 114). G மேஜர் கீயில் விரல் நுட்பத்தை வளர்க்கும் பாடல்.",
            "tempo": 115,
            "lines": [
                    {
                            "title": "பாகம் 1 (Main Minuet Theme)",
                            "measures": [
                                    [
                                            "D5",
                                            "G4",
                                            "A4"
                                    ],
                                    [
                                            "B4",
                                            "C5",
                                            "D5"
                                    ],
                                    [
                                            "G4",
                                            "G4",
                                            ","
                                    ],
                                    [
                                            "E5",
                                            "C5",
                                            "D5"
                                    ],
                                    [
                                            "E5",
                                            "F#5",
                                            "G5"
                                    ],
                                    [
                                            "G4",
                                            "G4",
                                            ","
                                    ]
                            ]
                    },
                    {
                            "title": "பாகம் 2 (Descending Cadence)",
                            "measures": [
                                    [
                                            "C5",
                                            "D5",
                                            "C5"
                                    ],
                                    [
                                            "B4",
                                            "A4",
                                            "B4"
                                    ],
                                    [
                                            "A4",
                                            "G4",
                                            "F#4"
                                    ],
                                    [
                                            "G4",
                                            "A4",
                                            "B4"
                                    ],
                                    [
                                            "G4",
                                            "F#4",
                                            "G4"
                                    ],
                                    [
                                            "A4",
                                            "D4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w6": {
            "id": "w6",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "3/4",
            "key": "A Minor",
            "title": "6. க்ரீன்ஸ்லீவ்ஸ் (Greensleeves • பாரம்பரிய ஆங்கில மெலடி)",
            "desc": "16-ஆம் நூற்றாண்டின் பாரம்பரிய ஆங்கில போக் மெலடி (டோரியன் அல்லது மைனர் மோடு). உருக்கமான சோகமும் வரலாற்று நயமும் கலந்த பாடல்.",
            "tempo": 95,
            "lines": [
                    {
                            "title": "மெலடி பாகம் 1",
                            "measures": [
                                    [
                                            "A4",
                                            "C5",
                                            "D5"
                                    ],
                                    [
                                            "E5",
                                            "F5",
                                            "E5"
                                    ],
                                    [
                                            "D5",
                                            "B4",
                                            "G4"
                                    ],
                                    [
                                            "A4",
                                            "B4",
                                            "C5"
                                    ],
                                    [
                                            "A4",
                                            "A4",
                                            "G#4"
                                    ],
                                    [
                                            "A4",
                                            "B4",
                                            "G#4"
                                    ],
                                    [
                                            "E4",
                                            ",",
                                            ","
                                    ]
                            ]
                    },
                    {
                            "title": "மெலடி பாகம் 2",
                            "measures": [
                                    [
                                            "G5",
                                            "G5",
                                            "F#5"
                                    ],
                                    [
                                            "E5",
                                            "D5",
                                            "B4"
                                    ],
                                    [
                                            "G4",
                                            "A4",
                                            "B4"
                                    ],
                                    [
                                            "C5",
                                            "A4",
                                            "A4"
                                    ],
                                    [
                                            "G#4",
                                            "A4",
                                            "B4"
                                    ],
                                    [
                                            "G#4",
                                            "E4",
                                            "A4"
                                    ],
                                    [
                                            "A4",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w7": {
            "id": "w7",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "3/4",
            "key": "C Major",
            "title": "7. அமேசிங் கிரேஸ் (Amazing Grace • உலகப் புகழ்பெற்ற ஆன்மீகப் பாடல்)",
            "desc": "ஜான் நியூட்டன் இயற்றிய அமைதி தரும் ஆன்மீகப் பாடல். 5 நோட்டுகள் கொண்ட மேஜர் பெண்டாடோனிக் ஸ்கேலில் (Major Pentatonic: C D E G A) அமைந்த பாடல்.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "A-ma-zing grace, how sweet the sound",
                            "measures": [
                                    [
                                            "G4",
                                            "C5",
                                            "E5"
                                    ],
                                    [
                                            "C5",
                                            "E5",
                                            "D5"
                                    ],
                                    [
                                            "C5",
                                            "A4",
                                            "G4"
                                    ],
                                    [
                                            "G4",
                                            "C5",
                                            "E5"
                                    ],
                                    [
                                            "C5",
                                            "E5",
                                            "D5"
                                    ],
                                    [
                                            "G5",
                                            ",",
                                            ","
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "A-",
                                            "ma-",
                                            "zing"
                                    ],
                                    [
                                            "grace,",
                                            "how",
                                            "sweet"
                                    ],
                                    [
                                            "the",
                                            "sound,",
                                            "that"
                                    ],
                                    [
                                            "saved",
                                            "a",
                                            "wretch"
                                    ],
                                    [
                                            "like",
                                            "me!",
                                            ""
                                    ],
                                    [
                                            "",
                                            "",
                                            ""
                                    ]
                            ]
                    },
                    {
                            "title": "I once was lost, but now am found",
                            "measures": [
                                    [
                                            "E5",
                                            "G5",
                                            "E5"
                                    ],
                                    [
                                            "G5",
                                            "E5",
                                            "C5"
                                    ],
                                    [
                                            "A4",
                                            "C5",
                                            "A4"
                                    ],
                                    [
                                            "G4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "E5",
                                            "D5",
                                            "C5"
                                    ],
                                    [
                                            "C5",
                                            ",",
                                            ","
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "I",
                                            "once",
                                            "was"
                                    ],
                                    [
                                            "lost,",
                                            "but",
                                            "now"
                                    ],
                                    [
                                            "am",
                                            "found,",
                                            "was"
                                    ],
                                    [
                                            "blind,",
                                            "but",
                                            "now"
                                    ],
                                    [
                                            "I",
                                            "see.",
                                            ""
                                    ],
                                    [
                                            "",
                                            "",
                                            ""
                                    ]
                            ]
                    }
            ]
    },
    "w8": {
            "id": "w8",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "4/4",
            "key": "C# Minor",
            "title": "8. மூன்லைட் சோனாட்டா (Moonlight Sonata • பீத்தோவன் Op. 27 No. 2)",
            "desc": "பீத்தோவனின் நிலவொளி சோனாட்டா அறிமுக தீம். ட்ரிப்லெட் (Triplets) ஆர்பெஜியோ அசைவில் மெதுவாக ஓடும் கனவு போன்ற கிளாசிக்கல் இசை.",
            "tempo": 55,
            "lines": [
                    {
                            "title": "ட்ரிப்லெட் ஆர்பெஜியோ தீம் (Adagio Sostenuto)",
                            "measures": [
                                    [
                                            "G#3",
                                            "C#4",
                                            "E4",
                                            "G#3"
                                    ],
                                    [
                                            "C#4",
                                            "E4",
                                            "G#3",
                                            "C#4"
                                    ],
                                    [
                                            "A3",
                                            "C#4",
                                            "E4",
                                            "A3"
                                    ],
                                    [
                                            "C#4",
                                            "E4",
                                            "A3",
                                            "C#4"
                                    ],
                                    [
                                            "F#3",
                                            "D4",
                                            "F#4",
                                            "F#3"
                                    ],
                                    [
                                            "D4",
                                            "F#4",
                                            "G#3",
                                            "C#4"
                                    ],
                                    [
                                            "E4",
                                            "G#3",
                                            "C#4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w9": {
            "id": "w9",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "4/4",
            "key": "C Major",
            "title": "9. தி என்டர்டெயினர் (The Entertainer • ஸ்காட் ஜோப்ளின் ராக்டைம்)",
            "desc": "ஸ்காட் ஜோப்ளினின் உலகப் புகழ்பெற்ற 1902 ராக்டைம் பியானோ மெலடி (The Sting திரைப்பட இசை). சிங்கோபேஷன் (Syncopation) தாள நடைக்கு மிகச் சிறந்த பயிற்சி.",
            "tempo": 90,
            "lines": [
                    {
                            "title": "ராக்டைம் அறிமுகம் (Famous Intro)",
                            "measures": [
                                    [
                                            "D4",
                                            "D#4",
                                            "E4",
                                            "C5"
                                    ],
                                    [
                                            ",",
                                            "E4",
                                            "C5",
                                            ","
                                    ],
                                    [
                                            "E4",
                                            "C5",
                                            ",",
                                            ","
                                    ],
                                    [
                                            "C5",
                                            "D5",
                                            "D#5",
                                            "E5"
                                    ],
                                    [
                                            "C5",
                                            "D5",
                                            "E5",
                                            "C5"
                                    ],
                                    [
                                            "D5",
                                            "C5",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w10": {
            "id": "w10",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "3/4",
            "key": "C Major",
            "title": "10. பிறந்தநாள் வாழ்த்துப் பாடல் (Happy Birthday to You • 3/4 தாளம்)",
            "desc": "உலகில் மிக அதிகமாகப் பாடப்படும் பாடல்! பிக்-அப் பீட் (Anacrusis / Pickup Beat 3) மற்றும் 3/4 தாளத்தில் வாசிக்கக் கற்றுக் கொடுக்கும் அத்தியாவசிய பாடல்.",
            "tempo": 100,
            "lines": [
                    {
                            "title": "ஹேப்பி பர்த்டே டு யூ (வரி 1 & 2)",
                            "measures": [
                                    [
                                            "G4",
                                            "G4",
                                            "A4"
                                    ],
                                    [
                                            "G4",
                                            "C5",
                                            "B4"
                                    ],
                                    [
                                            "G4",
                                            "G4",
                                            "A4"
                                    ],
                                    [
                                            "G4",
                                            "D5",
                                            "C5"
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "Hap-",
                                            "py",
                                            "birth-"
                                    ],
                                    [
                                            "day",
                                            "to",
                                            "you,"
                                    ],
                                    [
                                            "Hap-",
                                            "py",
                                            "birth-"
                                    ],
                                    [
                                            "day",
                                            "to",
                                            "you,"
                                    ]
                            ]
                    },
                    {
                            "title": "ஹேப்பி பர்த்டே டியர் (வரி 3 & 4)",
                            "measures": [
                                    [
                                            "G4",
                                            "G4",
                                            "G5"
                                    ],
                                    [
                                            "E5",
                                            "C5",
                                            "B4"
                                    ],
                                    [
                                            "A4",
                                            "F5",
                                            "F5"
                                    ],
                                    [
                                            "E5",
                                            "C5",
                                            "D5"
                                    ],
                                    [
                                            "C5",
                                            ",",
                                            ","
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "Hap-",
                                            "py",
                                            "birth-"
                                    ],
                                    [
                                            "day",
                                            "dear",
                                            "friend,"
                                    ],
                                    [
                                            "Hap-",
                                            "py",
                                            "birth-"
                                    ],
                                    [
                                            "day",
                                            "to",
                                            "you!"
                                    ],
                                    [
                                            "",
                                            "",
                                            ""
                                    ]
                            ]
                    }
            ]
    },
    "w11": {
            "id": "w11",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "4/4",
            "key": "A Minor",
            "title": "11. அன்னப்பறவை ஏரி தீம் (Swan Lake Theme • சைகோவ்ஸ்கி பாலே)",
            "desc": "பியோத்தர் சைகோவ்ஸ்கியின் உலகப் புகழ்பெற்ற ஸ்வான் லேக் பாலே நாடகத்தின் மர்மமும் அழகும் நிறைந்த மூல மெலடி (Op. 20).",
            "tempo": 80,
            "lines": [
                    {
                            "title": "ஸ்வான் லேக் மெலடி வரிசை 1",
                            "measures": [
                                    [
                                            "A4",
                                            "D5",
                                            "F5",
                                            "E5"
                                    ],
                                    [
                                            "D5",
                                            "B4",
                                            "C5",
                                            "D5"
                                    ],
                                    [
                                            "A4",
                                            "D5",
                                            "F5",
                                            "E5"
                                    ],
                                    [
                                            "D5",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    },
                    {
                            "title": "மெலடி வரிசை 2",
                            "measures": [
                                    [
                                            "F5",
                                            "E5",
                                            "D5",
                                            "C#5"
                                    ],
                                    [
                                            "D5",
                                            "E5",
                                            "F5",
                                            "D5"
                                    ],
                                    [
                                            "B4",
                                            "C5",
                                            "D5",
                                            "B4"
                                    ],
                                    [
                                            "A4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w12": {
            "id": "w12",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "3/4",
            "key": "C Major",
            "title": "12. பிராம்ஸ் தாலாட்டுப் பாடல் (Brahms' Lullaby • Guten Abend, gut' Nacht)",
            "desc": "ஜோஹன்னஸ் பிராம்ஸின் உலகப் புகழ்பெற்ற தாலாட்டுப் பாடல் (Op. 49 No. 4). அமைதியான 3/4 தாளத்தில் தூங்க வைக்கும் தாய்மை இசை.",
            "tempo": 80,
            "lines": [
                    {
                            "title": "தாலாட்டுப் பாடல் பல்லவி",
                            "measures": [
                                    [
                                            "E4",
                                            "E4",
                                            "G4"
                                    ],
                                    [
                                            "E4",
                                            "E4",
                                            "G4"
                                    ],
                                    [
                                            "E4",
                                            "G4",
                                            "C5"
                                    ],
                                    [
                                            "B4",
                                            "A4",
                                            "A4"
                                    ],
                                    [
                                            "G4",
                                            "D4",
                                            "E4"
                                    ],
                                    [
                                            "F4",
                                            "D4",
                                            "D4"
                                    ],
                                    [
                                            "E4",
                                            "F4",
                                            "D4"
                                    ],
                                    [
                                            "B4",
                                            "A4",
                                            "G4"
                                    ]
                            ]
                    }
            ]
    },
    "w13": {
            "id": "w13",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "4/4",
            "key": "C Major",
            "title": "13. ஜிங்கிள் பெல்ஸ் (Jingle Bells • உலகப் புகழ்பெற்ற கிறிஸ்துமஸ் பாடல்)",
            "desc": "ஜேம்ஸ் லார்ட் பியர்பான்ட் 1857-ல் இயற்றிய உலக பிரசித்தி பெற்ற மகிழ்ச்சியான குளிர்காலப் பாடல்.",
            "tempo": 120,
            "lines": [
                    {
                            "title": "கோரஸ்: Jin-gle bells, jin-gle bells",
                            "measures": [
                                    [
                                            "E4",
                                            "E4",
                                            "E4",
                                            ","
                                    ],
                                    [
                                            "E4",
                                            "E4",
                                            "E4",
                                            ","
                                    ],
                                    [
                                            "E4",
                                            "G4",
                                            "C4",
                                            "D4"
                                    ],
                                    [
                                            "E4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ],
                            "sahityam": [
                                    [
                                            "Jin-",
                                            "gle",
                                            "bells,",
                                            ""
                                    ],
                                    [
                                            "jin-",
                                            "gle",
                                            "bells,",
                                            ""
                                    ],
                                    [
                                            "jin-",
                                            "gle",
                                            "all",
                                            "the"
                                    ],
                                    [
                                            "way!",
                                            "",
                                            "",
                                            ""
                                    ]
                            ]
                    },
                    {
                            "title": "கோரஸ் வரி 2: Oh what fun it is to ride",
                            "measures": [
                                    [
                                            "F4",
                                            "F4",
                                            "F4",
                                            "F4"
                                    ],
                                    [
                                            "F4",
                                            "E4",
                                            "E4",
                                            "E4"
                                    ],
                                    [
                                            "E4",
                                            "D4",
                                            "D4",
                                            "E4"
                                    ],
                                    [
                                            "D4",
                                            ",",
                                            "G4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w14": {
            "id": "w14",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "3/4",
            "key": "D Minor",
            "title": "14. ஸ்கார்பரோ ஃபேர் (Scarborough Fair • நடுக்கால ஆங்கில நாட்டுப்புறப் பாடல்)",
            "desc": "சைமன் அண்ட் கார்பங்கலின் புகழ்பெற்ற டோரியன் நாட்டுப்புற மெலடி (Parsley, sage, rosemary and thyme).",
            "tempo": 90,
            "lines": [
                    {
                            "title": "வரிசை 1: Are you go-ing to Scar-bo-rough Fair",
                            "measures": [
                                    [
                                            "D4",
                                            "D4",
                                            "A4"
                                    ],
                                    [
                                            "A4",
                                            "A4",
                                            "E4"
                                    ],
                                    [
                                            "F4",
                                            "E4",
                                            "D4"
                                    ],
                                    [
                                            "A4",
                                            ",",
                                            ","
                                    ]
                            ]
                    },
                    {
                            "title": "வரிசை 2: Pars-ley, sage, rose-ma-ry and thyme",
                            "measures": [
                                    [
                                            "F4",
                                            "G4",
                                            "A4"
                                    ],
                                    [
                                            "C5",
                                            "A4",
                                            "G4"
                                    ],
                                    [
                                            "F4",
                                            "E4",
                                            "D4"
                                    ],
                                    [
                                            "D4",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w15": {
            "id": "w15",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "6/8",
            "key": "C Major",
            "title": "15. ஹல்லேலூயா தீம் (Hallelujah Theme • லியோனார்ட் கோஹன்)",
            "desc": "லியோனார்ட் கோஹனின் புகழ்பெற்ற 6/8 மெதுவான பாலாட் மெலடி (The secret chord that David played).",
            "tempo": 60,
            "lines": [
                    {
                            "title": "I've heard there was a secret chord",
                            "measures": [
                                    [
                                            "E4",
                                            "G4",
                                            "G4",
                                            "G4",
                                            "G4",
                                            "A4"
                                    ],
                                    [
                                            "A4",
                                            "A4",
                                            "G4",
                                            "E4",
                                            "G4",
                                            ","
                                    ]
                            ]
                    },
                    {
                            "title": "The fourth, the fifth, the minor fall, the major lift",
                            "measures": [
                                    [
                                            "G4",
                                            "A4",
                                            "A4",
                                            "A4",
                                            "B4",
                                            "B4"
                                    ],
                                    [
                                            "B4",
                                            "C5",
                                            "C5",
                                            "B4",
                                            "A4",
                                            "G4"
                                    ]
                            ]
                    }
            ]
    },
    "w16": {
            "id": "w16",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "4/4",
            "key": "G Minor",
            "title": "16. ஆட்டம் லீவ்ஸ் (Autumn Leaves • உலகப் புகழ்பெற்ற ஜாஸ் மெலடி)",
            "desc": "ஜாஸ் உலகில் மிக அதிகமாக வாசிக்கப்படும் ஜோசப் கோஸ்மாவின் மெலடி (Les Feuilles mortes). ii-V-I கார்ட் தொடரின் உச்சம்.",
            "tempo": 95,
            "lines": [
                    {
                            "title": "தி ஃபாலிங் லீவ்ஸ் (The falling leaves drift by my window)",
                            "measures": [
                                    [
                                            "C4",
                                            "D4",
                                            "Eb4",
                                            "G4"
                                    ],
                                    [
                                            "F4",
                                            ",",
                                            ",",
                                            ","
                                    ],
                                    [
                                            "Bb3",
                                            "C4",
                                            "D4",
                                            "F4"
                                    ],
                                    [
                                            "Eb4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    },
                    {
                            "title": "வரிசை 2",
                            "measures": [
                                    [
                                            "A3",
                                            "Bb3",
                                            "C4",
                                            "Eb4"
                                    ],
                                    [
                                            "D4",
                                            ",",
                                            ",",
                                            ","
                                    ],
                                    [
                                            "G3",
                                            "A3",
                                            "Bb3",
                                            "D4"
                                    ],
                                    [
                                            "C4",
                                            ",",
                                            ",",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w17": {
            "id": "w17",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "4/4",
            "key": "A Minor",
            "title": "17. பெல்லா சியாவ் (Bella Ciao • உலகப் புகழ்பெற்ற இத்தாலிய நாட்டுப்புறப் பாடல்)",
            "desc": "இத்தாலிய புரட்சி மற்றும் மணி ஹீஸ்ட் (Money Heist) தொடரில் இடம்பெற்று உலகமெங்கும் கோடிக்கணக்கானோரைக் கவர்ந்த விறுவிறுப்பான மெலடி.",
            "tempo": 125,
            "lines": [
                    {
                            "title": "பல்லவி: Una mattina mi son alzato",
                            "measures": [
                                    [
                                            "E4",
                                            "A4",
                                            "B4",
                                            "C5"
                                    ],
                                    [
                                            "A4",
                                            "E4",
                                            "A4",
                                            "B4"
                                    ],
                                    [
                                            "C5",
                                            "A4",
                                            "E4",
                                            "A4"
                                    ],
                                    [
                                            "B4",
                                            "C5",
                                            "B4",
                                            "A4"
                                    ],
                                    [
                                            "C5",
                                            "B4",
                                            "A4",
                                            "E4"
                                    ]
                            ]
                    },
                    {
                            "title": "கோரஸ்: O bella ciao, bella ciao, bella ciao ciao ciao",
                            "measures": [
                                    [
                                            "E5",
                                            "E5",
                                            "D5",
                                            "E5"
                                    ],
                                    [
                                            "F5",
                                            "F5",
                                            "F5",
                                            "E5"
                                    ],
                                    [
                                            "D5",
                                            "F5",
                                            "E5",
                                            "D5"
                                    ],
                                    [
                                            "C5",
                                            "B4",
                                            "A4",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
    "w18": {
            "id": "w18",
            "cat": "melodies",
            "catTamil": "6. பிரபல பாடல்கள் & மெலடிகள் (Classical Masterpieces & Melodies)",
            "meter": "9/8",
            "key": "Db Major",
            "title": "18. கிளேர் டி லூன் (Clair de Lune • கிளாட் டெபஸ்ஸி பியானோ கவிதை)",
            "desc": "பிரெஞ்சு இம்ப்ரெஷனிஸ்ட் இசை மேதை கிளாட் டெபஸ்ஸியின் 'நிலவொளி' (Suite bergamasque, L. 75). பியானோ வரலாற்றின் மிக அழகான தொடக்க மெலடி.",
            "tempo": 50,
            "lines": [
                    {
                            "title": "நிலவொளி அறிமுக தீம் (Famous Impressionist Opening)",
                            "measures": [
                                    [
                                            "F5",
                                            "Eb5",
                                            "Db5",
                                            "C5",
                                            "Bb4",
                                            "Ab4"
                                    ],
                                    [
                                            "F4",
                                            "Ab4",
                                            "Db5",
                                            "F5",
                                            "Eb5",
                                            ","
                                    ]
                            ]
                    }
            ]
    },
}
