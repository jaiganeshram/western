# -*- coding: utf-8 -*-
"""
Full generator for index.html (Western Keyboard & Piano Master Visual Tutor)
"""
import os
import json
import shutil
from lessons_data import WESTERN_LESSONS
from theory_data import (
    CIRCLE_OF_FIFTHS,
    WESTERN_MODES,
    WESTERN_INTERVALS,
    CHORD_TYPES,
    ROOT_NOTES,
    WESTERN_OCTAVES
)

def build_html():
    lessons_json = json.dumps(WESTERN_LESSONS, ensure_ascii=False)
    circle_json = json.dumps(CIRCLE_OF_FIFTHS, ensure_ascii=False)
    modes_json = json.dumps(WESTERN_MODES, ensure_ascii=False)
    intervals_json = json.dumps(WESTERN_INTERVALS, ensure_ascii=False)
    chords_json = json.dumps(CHORD_TYPES, ensure_ascii=False)
    roots_json = json.dumps(ROOT_NOTES, ensure_ascii=False)
    octaves_json = json.dumps(WESTERN_OCTAVES, ensure_ascii=False)

    html_content = f'''<!DOCTYPE html>
<html lang="ta">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎹 Western Keyboard & Piano Master Visual Tutor | மேற்கத்திய விசைப்பலகை & பியானோ ஆசான்</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Noto+Sans+Tamil:wght@400;600;700;800;900&family=Outfit:wght@400;500;600;700;800;900&display=swap"
        rel="stylesheet">
    <style>
        :root {{
            --bg-deep: #060814;
            --bg-panel: rgba(15, 21, 43, 0.85);
            --bg-panel-solid: #0d1224;
            --bg-card: rgba(22, 30, 58, 0.75);
            --border-glow: rgba(212, 175, 55, 0.35);
            --border-subtle: rgba(255, 255, 255, 0.1);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --gold-main: #d4af37;
            --gold-bright: #fbbf24;
            --gold-glow: rgba(251, 191, 36, 0.38);
            --indigo-accent: #6366f1;
            --cyan-accent: #06b6d4;
            --emerald-accent: #10b981;
            --rose-accent: #f43f5e;
            --font-main: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-ta: 'Noto Sans Tamil', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
            --key-white-w: 38px;
            --key-white-h: 185px;
            --key-black-w: 24px;
            --key-black-h: 115px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            user-select: none;
            -webkit-user-select: none;
        }}

        body {{
            background-color: var(--bg-deep);
            background-image:
                radial-gradient(ellipse at 15% 15%, rgba(99, 102, 241, 0.15) 0%, transparent 45%),
                radial-gradient(ellipse at 85% 85%, rgba(212, 175, 55, 0.13) 0%, transparent 45%),
                radial-gradient(ellipse at 50% 50%, rgba(6, 182, 212, 0.08) 0%, transparent 60%);
            color: var(--text-main);
            font-family: var(--font-main);
            min-height: 100vh;
            overflow-x: hidden;
            overflow-y: auto;
            scroll-behavior: smooth;
        }}

        /* Scrollbar Styling */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: rgba(10, 14, 28, 0.85);
        }}
        ::-webkit-scrollbar-thumb {{
            background: rgba(212, 175, 55, 0.4);
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: rgba(212, 175, 55, 0.7);
        }}

        /* App Header */
        header.app-header {{
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(9, 13, 26, 0.96);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border-glow);
            padding: 10px 22px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 14px;
            flex-wrap: wrap;
        }}

        .brand-section {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .brand-icon {{
            width: 48px;
            height: 48px;
            border-radius: 12px;
            background: linear-gradient(135deg, #fbbf24, #b45309);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            box-shadow: 0 0 22px var(--gold-glow);
            border: 1px solid rgba(255, 255, 255, 0.25);
        }}

        .brand-title-wrap h1 {{
            font-size: 1.25rem;
            font-weight: 800;
            background: linear-gradient(135deg, #fff 40%, var(--gold-bright) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: var(--font-ta);
            letter-spacing: -0.01em;
        }}

        .brand-title-wrap p {{
            font-size: 0.76rem;
            color: var(--text-muted);
            letter-spacing: 0.02em;
        }}

        /* Top Nav Tabs */
        .header-tabs {{
            display: flex;
            align-items: center;
            background: rgba(255, 255, 255, 0.05);
            padding: 4px;
            border-radius: 12px;
            border: 1px solid var(--border-subtle);
            gap: 4px;
            overflow-x: auto;
        }}

        .nav-tab-btn {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            font-family: var(--font-ta);
            cursor: pointer;
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            gap: 6px;
            white-space: nowrap;
        }}

        .nav-tab-btn:hover {{
            color: #fff;
            background: rgba(255, 255, 255, 0.08);
        }}

        .nav-tab-btn.active {{
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.25), rgba(99, 102, 241, 0.25));
            color: var(--gold-bright);
            border: 1px solid rgba(212, 175, 55, 0.45);
            box-shadow: 0 0 12px rgba(212, 175, 55, 0.25);
        }}

        /* Header Quick Actions */
        .header-actions {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .action-toggle-badge {{
            display: flex;
            align-items: center;
            gap: 7px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border-subtle);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.78rem;
            cursor: pointer;
            transition: all 0.25s;
            font-family: var(--font-ta);
            color: var(--text-muted);
        }}

        .action-toggle-badge:hover {{
            background: rgba(255, 255, 255, 0.12);
            color: #fff;
        }}

        .action-toggle-badge.active {{
            background: rgba(16, 185, 129, 0.2);
            border-color: rgba(16, 185, 129, 0.6);
            color: #34d399;
            box-shadow: 0 0 12px rgba(16, 185, 129, 0.3);
        }}

        .action-toggle-badge.active.rec {{
            background: rgba(244, 63, 94, 0.25);
            border-color: var(--rose-accent);
            color: #fca5a5;
            box-shadow: 0 0 12px rgba(244, 63, 94, 0.35);
        }}

        .status-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #94a3b8;
            transition: 0.2s;
        }}

        .action-toggle-badge.active .status-dot {{
            background: #10b981;
            box-shadow: 0 0 8px #10b981;
            animation: pulse-dot 1.5s infinite;
        }}

        .action-toggle-badge.active.rec .status-dot {{
            background: #f43f5e;
            box-shadow: 0 0 8px #f43f5e;
        }}

        @keyframes pulse-dot {{
            0%, 100% {{ transform: scale(1); opacity: 1; }}
            50% {{ transform: scale(1.4); opacity: 0.6; }}
        }}

        .vol-slider-wrap {{
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.78rem;
            color: var(--text-muted);
        }}

        .vol-slider {{
            width: 65px;
            accent-color: var(--gold-bright);
            cursor: pointer;
        }}

        .btn-quick-link {{
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border-subtle);
            color: var(--text-muted);
            padding: 6px 12px;
            border-radius: 8px;
            font-size: 0.78rem;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: 0.2s;
        }}

        .btn-quick-link:hover {{
            background: rgba(255, 255, 255, 0.12);
            color: #fff;
            border-color: rgba(255, 255, 255, 0.25);
        }}

        /* Live Mic Tuner Gauge Panel */
        .mic-tuner-panel {{
            display: none;
            background: linear-gradient(90deg, rgba(16, 185, 129, 0.16), rgba(6, 182, 212, 0.16));
            border-bottom: 1px solid rgba(16, 185, 129, 0.4);
            padding: 8px 24px;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            animation: slideDown 0.3s ease;
        }}

        @keyframes slideDown {{
            from {{ opacity: 0; transform: translateY(-8px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .tuner-metric {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: var(--font-ta);
            font-size: 0.85rem;
        }}

        .tuner-badge {{
            background: rgba(16, 185, 129, 0.25);
            border: 1px solid #10b981;
            padding: 2px 8px;
            border-radius: 6px;
            font-weight: 800;
            color: #34d399;
            font-family: var(--font-mono);
        }}

        .tuner-gauge-track {{
            flex: 1;
            max-width: 320px;
            height: 12px;
            background: rgba(0, 0, 0, 0.55);
            border-radius: 6px;
            position: relative;
            border: 1px solid rgba(255, 255, 255, 0.15);
            overflow: hidden;
        }}

        .tuner-gauge-center {{
            position: absolute;
            top: 0;
            bottom: 0;
            left: 50%;
            width: 2px;
            background: #10b981;
            transform: translateX(-50%);
            box-shadow: 0 0 6px #10b981;
        }}

        .tuner-gauge-needle {{
            position: absolute;
            top: 1px;
            bottom: 1px;
            left: 50%;
            width: 6px;
            background: #fbbf24;
            border-radius: 3px;
            transform: translateX(-50%);
            transition: left 0.1s ease;
            box-shadow: 0 0 8px #fbbf24;
        }}

        .tuner-status {{
            font-size: 0.8rem;
            font-weight: 700;
            color: #34d399;
            font-family: var(--font-ta);
        }}

        /* Audio Recording Bar */
        .recording-bar {{
            display: none;
            background: linear-gradient(90deg, rgba(244, 63, 94, 0.22), rgba(225, 29, 72, 0.22));
            border-bottom: 1px solid rgba(244, 63, 94, 0.4);
            padding: 8px 24px;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            animation: slideDown 0.3s ease;
        }}

        /* Main Viewport Container */
        main.main-viewport {{
            max-width: 1440px;
            margin: 0 auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}

        /* View Panels */
        .view-panel {{
            display: none;
            animation: fadeIn 0.3s ease;
        }}

        .view-panel.active {{
            display: block;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Glass Cards */
        .glass-card {{
            background: var(--bg-panel);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
        }}

        /* Practice Studio Deck Layout */
        .studio-top-grid {{
            display: grid;
            grid-template-columns: 2.2fr 1fr;
            gap: 16px;
            margin-bottom: 16px;
        }}

        @media (max-width: 1024px) {{
            .studio-top-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        /* Controls Deck */
        .controls-deck {{
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}

        .controls-row {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .select-group {{
            display: flex;
            flex-direction: column;
            gap: 4px;
            flex: 1;
            min-width: 170px;
        }}

        .select-label {{
            font-size: 0.74rem;
            color: var(--text-muted);
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 6px;
            font-family: var(--font-ta);
        }}

        .custom-select {{
            background: rgba(13, 18, 36, 0.95);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: var(--text-main);
            padding: 9px 12px;
            border-radius: 10px;
            font-size: 0.85rem;
            font-family: var(--font-ta);
            outline: none;
            cursor: pointer;
            transition: 0.2s;
        }}

        .custom-select:hover,
        .custom-select:focus {{
            border-color: var(--gold-bright);
            box-shadow: 0 0 10px rgba(212, 175, 55, 0.25);
        }}

        /* Playback Control Bar */
        .playback-strip {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(11, 16, 32, 0.85);
            border: 1px solid rgba(212, 175, 55, 0.25);
            padding: 10px 18px;
            border-radius: 14px;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .btn-ctrl {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border-subtle);
            color: #fff;
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 0.86rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: var(--font-ta);
        }}

        .btn-ctrl:hover {{
            background: rgba(255, 255, 255, 0.15);
            transform: translateY(-1px);
        }}

        .btn-ctrl.btn-primary {{
            background: linear-gradient(135deg, #fbbf24, #b45309);
            border-color: rgba(255, 255, 255, 0.3);
            color: #070913;
            font-weight: 800;
            box-shadow: 0 0 16px var(--gold-glow);
        }}

        .btn-ctrl.btn-primary:hover {{
            background: linear-gradient(135deg, #fde68a, #d97706);
            transform: scale(1.02);
        }}

        .btn-ctrl.active {{
            background: rgba(244, 63, 94, 0.25);
            border-color: var(--rose-accent);
            color: #fda4af;
        }}

        /* Tempo Slider */
        .tempo-box {{
            display: flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.04);
            padding: 6px 12px;
            border-radius: 8px;
            border: 1px solid var(--border-subtle);
        }}

        .tempo-val {{
            font-family: var(--font-mono);
            font-weight: 700;
            color: var(--gold-bright);
            min-width: 58px;
            font-size: 0.85rem;
        }}

        .tempo-slider {{
            width: 85px;
            accent-color: var(--gold-bright);
            cursor: pointer;
        }}

        .btn-mini {{
            background: rgba(255, 255, 255, 0.08);
            border: none;
            color: #fff;
            width: 22px;
            height: 22px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }}

        /* Western Rhythm Visualizer Box */
        .tala-box {{
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background: linear-gradient(135deg, rgba(20, 26, 52, 0.85), rgba(12, 16, 34, 0.95));
            border: 1px solid var(--border-glow);
            border-radius: 16px;
            padding: 16px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        }}

        .tala-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 8px;
        }}

        .tala-name {{
            font-size: 0.92rem;
            font-weight: 700;
            color: var(--gold-bright);
            font-family: var(--font-ta);
        }}

        .tala-anga {{
            font-size: 0.72rem;
            color: var(--text-muted);
            font-family: var(--font-mono);
        }}

        .tala-gesture-display {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
            padding: 12px 0;
        }}

        .gesture-icon {{
            font-size: 44px;
            filter: drop-shadow(0 0 12px var(--gold-glow));
            animation: bounceIn 0.3s ease;
        }}

        @keyframes bounceIn {{
            0% {{ transform: scale(0.7); opacity: 0.5; }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}

        .gesture-info h4 {{
            font-size: 1.05rem;
            font-weight: 800;
            color: #fff;
            font-family: var(--font-ta);
        }}

        .gesture-info p {{
            font-size: 0.74rem;
            color: var(--text-muted);
        }}

        /* Beat Pulse Dots */
        .tala-dots-row {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            padding-top: 8px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            flex-wrap: wrap;
        }}

        .tala-dot {{
            width: 28px;
            height: 28px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.12);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-mono);
            font-size: 0.75rem;
            color: var(--text-muted);
            transition: all 0.2s ease;
        }}

        .tala-dot.active {{
            background: linear-gradient(135deg, var(--gold-bright), #b45309);
            color: #070913;
            font-weight: 800;
            border-color: #fff;
            box-shadow: 0 0 14px var(--gold-glow);
            transform: scale(1.15);
        }}

        .tala-dot.downbeat {{
            border-color: var(--gold-bright);
        }}

        .tala-divider {{
            color: var(--gold-bright);
            font-weight: bold;
            font-size: 1.1rem;
            margin: 0 2px;
        }}

        /* Notation Ribbon Card */
        .notation-ribbon-card {{
            margin-bottom: 16px;
            background: linear-gradient(180deg, rgba(16, 22, 45, 0.95), rgba(10, 14, 30, 0.95));
            border: 1px solid rgba(212, 175, 55, 0.25);
            border-radius: 16px;
            padding: 16px 20px;
        }}

        .ribbon-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .ribbon-title {{
            font-size: 0.92rem;
            font-weight: 700;
            color: var(--gold-bright);
            font-family: var(--font-ta);
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .ribbon-badge {{
            font-size: 0.72rem;
            background: rgba(99, 102, 241, 0.15);
            border: 1px solid rgba(99, 102, 241, 0.35);
            color: #a5b4fc;
            padding: 3px 8px;
            border-radius: 6px;
            font-family: var(--font-mono);
        }}

        .swara-ribbon-scroll {{
            display: flex;
            align-items: stretch;
            gap: 8px;
            width: 100%;
            overflow-x: scroll;
            padding: 8px 4px 14px 4px;
            scrollbar-width: thin;
        }}

        .swara-line-group {{
            display: flex;
            flex-direction: column;
            gap: 6px;
            padding: 8px;
            border: 1px solid rgba(212, 175, 55, 0.25);
            border-radius: 12px;
            background: rgba(8, 13, 28, 0.6);
            margin-bottom: 10px;
        }}

        .swara-line-header {{
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--cyan-accent);
            padding: 2px 6px;
            font-family: var(--font-ta);
        }}

        .swara-line-measures {{
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }}

        .swara-measure-block {{
            display: flex;
            align-items: center;
            gap: 5px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 8px;
            padding: 4px;
        }}

        .swara-node {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-width: 44px;
            padding: 6px 4px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            cursor: pointer;
            transition: all 0.2s;
            position: relative;
        }}

        .swara-node:hover {{
            background: rgba(255, 255, 255, 0.12);
            transform: translateY(-2px);
            border-color: var(--gold-bright);
        }}

        .swara-node.active {{
            background: linear-gradient(135deg, rgba(251, 191, 36, 0.35), rgba(99, 102, 241, 0.35));
            border-color: var(--gold-bright);
            box-shadow: 0 0 14px var(--gold-glow);
            transform: scale(1.08);
        }}

        .swara-badge-ta {{
            font-size: 0.95rem;
            font-weight: 800;
            color: #fff;
            font-family: var(--font-main);
        }}

        .swara-node.active .swara-badge-ta {{
            color: var(--gold-bright);
        }}

        .swara-west-note {{
            font-size: 0.68rem;
            color: var(--text-muted);
            font-family: var(--font-mono);
        }}

        .swara-finger-num {{
            font-size: 0.65rem;
            font-weight: 700;
            color: var(--cyan-accent);
            background: rgba(6, 182, 212, 0.15);
            padding: 1px 4px;
            border-radius: 4px;
            margin-top: 2px;
        }}

        .swara-sahitya-word {{
            font-size: 0.66rem;
            color: #a5b4fc;
            margin-top: 2px;
            max-width: 52px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }}

        /* Active Note Metric Card */
        .step-info-strip {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 10px;
            margin-bottom: 14px;
        }}

        .step-metric-box {{
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 10px;
            padding: 8px 12px;
            display: flex;
            flex-direction: column;
            gap: 2px;
        }}

        .metric-label {{
            font-size: 0.7rem;
            color: var(--text-muted);
            font-family: var(--font-ta);
        }}

        .metric-val {{
            font-size: 0.95rem;
            font-weight: 800;
            color: #fff;
            font-family: var(--font-mono);
        }}

        .metric-val.highlight {{
            color: var(--gold-bright);
        }}

        /* 61-Key Interactive Virtual Piano Bed */
        .piano-wrapper {{
            background: #090c18;
            border: 2px solid rgba(212, 175, 55, 0.35);
            border-radius: 16px;
            padding: 16px 14px 22px;
            box-shadow: 0 14px 40px rgba(0, 0, 0, 0.6);
            overflow-x: auto;
            position: relative;
        }}

        .piano-bed {{
            display: flex;
            position: relative;
            height: var(--key-white-h);
            margin: 0 auto;
            width: max-content;
        }}

        .key-white {{
            width: var(--key-white-w);
            height: var(--key-white-h);
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 85%, #cbd5e1 100%);
            border: 1px solid #64748b;
            border-radius: 0 0 6px 6px;
            position: relative;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            align-items: center;
            padding-bottom: 8px;
            transition: background 0.1s, transform 0.08s;
            box-shadow: inset 0 -4px 6px rgba(0, 0, 0, 0.2);
            z-index: 1;
        }}

        .key-white:hover {{
            background: linear-gradient(180deg, #f1f5f9 0%, #e2e8f0 100%);
        }}

        .key-white.active {{
            background: linear-gradient(180deg, #fde68a 0%, #fbbf24 100%) !important;
            transform: translateY(3px);
            box-shadow: inset 0 2px 8px rgba(180, 83, 9, 0.5), 0 0 16px var(--gold-glow);
        }}

        .key-white.active .key-west-lbl {{
            color: #78350f !important;
            font-weight: 900;
        }}

        .key-black {{
            width: var(--key-black-w);
            height: var(--key-black-h);
            background: linear-gradient(180deg, #334155 0%, #1e293b 50%, #090d16 100%);
            border: 1px solid #0f172a;
            border-radius: 0 0 4px 4px;
            position: absolute;
            top: 0;
            z-index: 2;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            align-items: center;
            padding-bottom: 6px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.6);
            transition: background 0.1s, transform 0.08s;
        }}

        .key-black:hover {{
            background: linear-gradient(180deg, #475569 0%, #334155 100%);
        }}

        .key-black.active {{
            background: linear-gradient(180deg, #38bdf8 0%, #0284c7 100%) !important;
            transform: translateY(3px);
            box-shadow: 0 0 16px rgba(56, 189, 248, 0.6);
        }}

        .key-west-lbl {{
            font-size: 0.72rem;
            font-weight: 800;
            color: #0f172a;
            font-family: var(--font-mono);
        }}

        .key-black .key-west-lbl {{
            color: #38bdf8;
            font-size: 0.62rem;
        }}

        .key-hint-lbl {{
            font-size: 0.58rem;
            color: #94a3b8;
            background: rgba(0, 0, 0, 0.08);
            border-radius: 3px;
            padding: 1px 3px;
            margin-top: 2px;
            font-family: var(--font-mono);
        }}

        .key-black .key-hint-lbl {{
            color: #cbd5e1;
            background: rgba(255, 255, 255, 0.15);
        }}

        .middle-c-crown {{
            position: absolute;
            top: 6px;
            font-size: 13px;
        }}

        /* Responsive Grids for Theory & Guides */
        .theory-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 16px;
            margin-top: 16px;
        }}

        .theory-card {{
            background: rgba(18, 25, 50, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 14px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            transition: transform 0.2s, border-color 0.2s;
        }}

        .theory-card:hover {{
            transform: translateY(-2px);
            border-color: var(--gold-bright);
        }}

        .theory-card h3 {{
            color: var(--gold-bright);
            font-size: 1.05rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .theory-card p {{
            color: var(--text-muted);
            font-size: 0.85rem;
            line-height: 1.5;
        }}

        .badge-pill {{
            background: rgba(99, 102, 241, 0.2);
            border: 1px solid rgba(99, 102, 241, 0.4);
            color: #a5b4fc;
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 0.72rem;
            font-family: var(--font-mono);
            display: inline-block;
        }}

        /* Circle of Fifths Table */
        .circle-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85rem;
            margin-top: 12px;
        }}

        .circle-table th,
        .circle-table td {{
            padding: 10px 12px;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }}

        .circle-table th {{
            background: rgba(255, 255, 255, 0.04);
            color: var(--gold-bright);
            font-weight: 700;
        }}

        .circle-table tr:hover {{
            background: rgba(255, 255, 255, 0.04);
        }}

        /* Diagram Cards Grid */
        .diagrams-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 18px;
            margin-top: 16px;
        }}

        .diagram-card {{
            background: rgba(18, 25, 50, 0.85);
            border: 1px solid rgba(212, 175, 55, 0.25);
            border-radius: 14px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            cursor: pointer;
            transition: all 0.25s;
        }}

        .diagram-card:hover {{
            transform: translateY(-4px);
            border-color: var(--gold-bright);
            box-shadow: 0 10px 24px rgba(251, 191, 36, 0.25);
        }}

        .diagram-card img {{
            width: 100%;
            height: 170px;
            object-fit: cover;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }}

        .diagram-card-info {{
            padding: 14px;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .diagram-card-info h4 {{
            font-size: 0.95rem;
            color: #fff;
            font-weight: 700;
        }}

        .diagram-card-info p {{
            font-size: 0.78rem;
            color: var(--text-muted);
        }}

        /* Modal Lightbox */
        .modal-overlay {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(8px);
            z-index: 2000;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}

        .modal-overlay.active {{
            display: flex;
        }}

        .modal-box {{
            background: #0d1224;
            border: 1px solid var(--border-glow);
            border-radius: 16px;
            max-width: 900px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            padding: 24px;
            position: relative;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
        }}

        .btn-close-modal {{
            position: absolute;
            top: 16px;
            right: 16px;
            background: rgba(255, 255, 255, 0.1);
            border: none;
            color: #fff;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            font-size: 16px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .btn-close-modal:hover {{
            background: var(--rose-accent);
        }}

        /* Fullscreen Lightbox Overlays */
        .modal-overlay.fullscreen-lightbox-overlay {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(4, 7, 20, 0.95);
            backdrop-filter: blur(16px);
            z-index: 3000;
            align-items: center;
            justify-content: center;
            padding: 12px;
        }}

        .modal-overlay.fullscreen-lightbox-overlay.active {{
            display: flex;
        }}

        .modal-window.fullscreen-lightbox-window {{
            background: #090e22;
            border: 1px solid var(--border-glow);
            border-radius: 18px;
            width: 98vw;
            max-width: 1560px;
            height: 96vh;
            max-height: 96vh;
            display: flex;
            flex-direction: column;
            padding: 20px 22px;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9);
            position: relative;
            overflow-y: auto;
            gap: 14px;
        }}

        .fullscreen-lightbox-content {{
            display: flex;
            flex-direction: column;
            gap: 14px;
            flex: 1;
        }}

        /* Responsive Mobile Styles */
        @media (max-width: 768px) {{
            header.app-header {{
                padding: 8px 14px;
            }}
            .brand-title-wrap h1 {{
                font-size: 1.05rem;
            }}
            .piano-wrapper {{
                padding: 10px 8px 16px;
            }}
            :root {{
                --key-white-w: 32px;
                --key-white-h: 150px;
                --key-black-w: 20px;
                --key-black-h: 92px;
            }}
        }}
    </style>
</head>

<body>
    <!-- App Header -->
    <header class="app-header">
        <div class="brand-section">
            <div class="brand-icon">🎹</div>
            <div class="brand-title-wrap">
                <h1>மேற்கத்திய விசைப்பலகை &amp; பியானோ ஆசான்</h1>
                <p>Western Keyboard &amp; Piano Master Visual Tutor • 61-Key Interactive Virtual Synthesizer</p>
            </div>
        </div>

        <!-- Top Navigation Tabs -->
        <nav class="header-tabs" aria-label="Navigation">
            <button class="nav-tab-btn active" onclick="switchView('studio')">🎵 பாடம் &amp; பயிற்சி (Studio)</button>
            <button class="nav-tab-btn" onclick="switchView('voice_training')">🎙️ குரல் &amp; சோல்ஃபேஜ் (Solfege)</button>
            <button class="nav-tab-btn" onclick="switchView('sthayi_theory')">📖 மேற்கத்திய ஆக்டேவ்கள் (Octaves &amp; Staff)</button>
            <button class="nav-tab-btn" onclick="switchView('melakarta')">🌀 ஸ்கேல்கள் &amp; மோடுகள் (Scales &amp; Modes)</button>
            <button class="nav-tab-btn" onclick="switchView('janya')">🎼 கார்ட் அகராதி (Chords &amp; Inversions)</button>
            <button class="nav-tab-btn" onclick="switchView('ear_training')">🎮 செவிப் பயிற்சி (Ear Training)</button>
            <button class="nav-tab-btn" onclick="switchView('swaras')">🎹 12 செமிடோன்கள் &amp; இடைவெளிகள்</button>
            <button class="nav-tab-btn" onclick="switchView('psr_guide')">🎹 விசைப்பலகை வழிகாட்டி (Tech Guide)</button>
            <button class="nav-tab-btn" onclick="switchView('diagrams')">🖼️ வரைபடங்கள் (Diagrams)</button>
        </nav>

        <!-- Header Actions -->
        <div class="header-actions">
            <!-- Metronome / Drum Beat Toggle -->
            <button id="btnDrumsToggle" class="action-toggle-badge" onclick="toggleDrumsBacking()" title="மெட்ரானோம் மற்றும் டிரம்ஸ் தாள நடை">
                <span class="status-dot"></span>
                <span>🥁 மெட்ரானோம் / டிரம்ஸ்</span>
            </button>

            <!-- Chord Pad Drone Toggle -->
            <button id="btnDroneToggle" class="action-toggle-badge" onclick="togglePadDrone()" title="அடிப்படை கார்ட் பேட் ட்ரோன் ஒலி">
                <span class="status-dot"></span>
                <span>🎹 பேட் ட்ரோன் (Pad)</span>
            </button>

            <!-- Mic Tuner Toggle -->
            <button id="btnMicToggle" class="action-toggle-badge" onclick="toggleMicListening()" title="மைக் சுருதிமானி (Live Mic Tuner)">
                <span class="status-dot"></span>
                <span>🎙️ மைக் ட்யூனர்</span>
            </button>

            <!-- Audio Recorder Toggle -->
            <button id="btnRecordToggle" class="action-toggle-badge rec" onclick="toggleAudioRecorder()" title="உங்கள் வாசிப்பை ஆடியோவாகப் பதிவு செய்">
                <span class="status-dot"></span>
                <span id="recordStatusLabel">⏺️ பதிவு செய் (Record)</span>
            </button>

            <!-- Fullscreen Lightbox Triggers -->
            <button class="action-toggle-badge" onclick="openKeyboardLightbox()" title="முழுத்திரை விசைப்பலகை லைட்பாக்ஸ் (Keyboard Lightbox)">
                <span>⛶ விசைப்பலகை</span>
            </button>
            <button class="action-toggle-badge" onclick="openNotationLightbox()" title="முழுத்திரை நோட்டேஷன் லைட்பாக்ஸ் (Notation Lightbox)">
                <span>⛶ நோட்டேஷன்</span>
            </button>

            <!-- Volume Slider -->
            <div class="vol-slider-wrap">
                <span>🔊</span>
                <input type="range" class="vol-slider" min="0" max="1" step="0.05" value="0.75" oninput="setMasterVolume(this.value)" title="ஒலி அளவு">
            </div>

            <!-- Help Modal Button -->
            <button class="btn-ctrl" onclick="openHelpModal()" style="padding: 6px 10px;" title="விசைப்பலகை குறுக்குவழிகள்">⌨️ குறுக்குவழிகள்</button>
        </div>
    </header>

    <!-- Live Mic Pitch Tuner Panel -->
    <div id="micTunerPanel" class="mic-tuner-panel">
        <div class="tuner-metric">
            <span>🎙️ கண்டறியப்பட்ட நோட்:</span>
            <span id="tunerDetectedNote" class="tuner-badge">—</span>
        </div>
        <div class="tuner-metric">
            <span>அதிர்வெண்:</span>
            <span id="tunerFrequency" class="tuner-badge">0.0 Hz</span>
        </div>
        <div class="tuner-gauge-track">
            <div class="tuner-gauge-center"></div>
            <div id="tunerNeedle" class="tuner-gauge-needle" style="left: 50%;"></div>
        </div>
        <div id="tunerStatus" class="tuner-status">தயார் • மைக்கில் வாசிக்கவும் / பாடவும்</div>
    </div>

    <!-- Live Audio Recording Bar -->
    <div id="recordingBar" class="recording-bar">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span class="status-dot" style="background: #f43f5e; box-shadow: 0 0 8px #f43f5e;"></span>
            <span style="font-weight: 700; color: #fca5a5;">ஆடியோ பதிவு செய்யப்படுகிறது...</span>
            <span id="recordingTimer" style="font-family: var(--font-mono); font-weight: 800; color: #fff;">00:00</span>
        </div>
        <button class="btn-ctrl" onclick="stopAndDownloadRecording()" style="background: #f43f5e; border-color: #fff; color: #fff; padding: 4px 12px; font-size: 0.8rem;">
            ⏹️ நிறுத்தி பதிவிறக்கு (Download WAV)
        </button>
    </div>

    <!-- Main Viewport -->
    <main class="main-viewport">

        <!-- ================= VIEW 1: STUDIO & PRACTICE ================= -->
        <div id="viewStudio" class="view-panel active">
            <div id="controlsAnchor"></div>
            <!-- Studio Top Controls Deck -->
            <div class="studio-top-grid">
                <div class="glass-card controls-deck">
                    <!-- Row 1: Category & Lesson Selector -->
                    <div class="controls-row">
                        <div class="select-group">
                            <label class="select-label" for="catSelector">📚 பயிற்சி வகை (Category):</label>
                            <select id="catSelector" class="custom-select" onchange="onCategoryChange()">
                                <option value="all">முழு மேற்கத்திய பாடத் தொகுப்பு (All 82 Lessons)</option>
                                <option value="hanon" selected>1. 🖐️ ஹெனான் &amp; விரல் பயிற்சிகள் (Hanon &amp; Czerny - 12)</option>
                                <option value="major_scales">2. 🎼 மேஜர் ஸ்கேல்கள் (Major Scales &amp; Pentatonics - 16)</option>
                                <option value="minor_scales">3. 🎵 மைனர் ஸ்கேல்கள் (Minor, Pentatonic &amp; Blues - 12)</option>
                                <option value="chords">4. 🎹 கார்ட்கள் &amp; ஆர்பெஜியோ பயிற்சிகள் (Chords &amp; Arpeggios - 12)</option>
                                <option value="progressions">5. 🎶 பிரபல கார்ட் தொடர்கள் (Progressions - 12)</option>
                                <option value="melodies">6. 👑 பிரபல பாடல்கள் &amp; மெலடிகள் (Classics &amp; World Melodies - 18)</option>
                            </select>
                        </div>

                        <div class="select-group" style="flex: 1.4;">
                            <label class="select-label" for="lessonSelector">🎼 பாடம் (Lesson):</label>
                            <select id="lessonSelector" class="custom-select" onchange="onLessonChange()">
                                <!-- Populated dynamically by JS -->
                            </select>
                        </div>
                    </div>

                    <!-- Row 2: Hand Coordination, Key Transposition, Octave & Voice -->
                    <div class="controls-row">
                        <div class="select-group" style="min-width: 140px;">
                            <label class="select-label" for="handSelector">🖐️ கை தேர்வு (Hand):</label>
                            <select id="handSelector" class="custom-select" onchange="onHandChange()">
                                <option value="both" selected>👐 Both Hands (இரு கைகள்)</option>
                                <option value="rh">🖐️ Right Hand (வலது கை 𝄞)</option>
                                <option value="lh">🖐️ Left Hand (இடது கை 𝄢)</option>
                            </select>
                        </div>

                        <div class="select-group" style="min-width: 130px;">
                            <label class="select-label" for="keySelector">🔑 கீ / சுருதி (Key Transpose):</label>
                            <select id="keySelector" class="custom-select" onchange="onKeyTransposeChange()">
                                <option value="0" selected>C Major (இயல்பு • 0)</option>
                                <option value="1">C# / Db (+1)</option>
                                <option value="2">D Major (+2)</option>
                                <option value="3">Eb Major (+3)</option>
                                <option value="4">E Major (+4)</option>
                                <option value="5">F Major (+5)</option>
                                <option value="6">F# / Gb (+6)</option>
                                <option value="7">G Major (+7)</option>
                                <option value="8">Ab Major (+8)</option>
                                <option value="9">A Major (+9)</option>
                                <option value="10">Bb Major (+10)</option>
                                <option value="11">B Major (+11)</option>
                            </select>
                        </div>

                        <div class="select-group" style="min-width: 120px;">
                            <label class="select-label" for="octaveSelector">🎹 ஆக்டேவ் ஷிப்ட் (Octave):</label>
                            <select id="octaveSelector" class="custom-select" onchange="onOctaveShiftChange()">
                                <option value="-1">கீழ் ஆக்டேவ் (C3)</option>
                                <option value="0" selected>இயல்பு (Middle C4)</option>
                                <option value="1">மேல் ஆக்டேவ் (C5)</option>
                            </select>
                        </div>

                        <div class="select-group" style="min-width: 140px;">
                            <label class="select-label" for="voiceSelector">🎻 பியானோ ஒலி (Voice):</label>
                            <select id="voiceSelector" class="custom-select" onchange="onVoiceChange()">
                                <option value="grand_piano" selected>🎹 Grand Piano (ஸ்டீன்வே பியானோ)</option>
                                <option value="electric_piano">⚡ Electric Piano (Rhodes / DX7)</option>
                                <option value="pipe_organ">⛪ Pipe Organ (சர்ச் ஆர்கன்)</option>
                                <option value="synth_strings">🎻 Synth Strings (ஸ்ட்ரிங்ஸ் பேட்)</option>
                                <option value="harpsichord">🎼 Harpsichord (ஹார்ப்சிகார்ட்)</option>
                            </select>
                        </div>
                    </div>

                    <!-- Playback Controls Bar -->
                    <div class="playback-strip">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <button id="btnPlayPause" class="btn-ctrl btn-primary" onclick="togglePlayPause()">
                                <span id="playIcon">▶️</span>
                                <span id="playLabel">வாசி (Play)</span>
                            </button>
                            <button class="btn-ctrl" onclick="stopPlayback()" title="நிறுத்து &amp; தொடக்கத்திற்கு செல்">⏹️ Stop</button>
                            <button id="btnLoop" class="btn-ctrl" onclick="toggleLoop()" title="மீண்டும் மீண்டும் வாசி (Loop)">🔁 Loop</button>
                            <button class="btn-ctrl" onclick="stepBackward()" title="முந்தைய நோட்">⏮️</button>
                            <button class="btn-ctrl" onclick="stepForward()" title="அடுத்த நோட்">⏭️</button>
                        </div>

                        <!-- Subdivisions (Note Speed 1x, 2x, 4x) -->
                        <div style="display: flex; align-items: center; gap: 6px;">
                            <span style="font-size: 0.72rem; color: var(--text-muted);">நோட் வேகம்:</span>
                            <div class="header-tabs" style="padding: 2px;">
                                <button id="btnSpeed1" class="nav-tab-btn active" style="padding: 4px 8px; font-size: 0.75rem;" onclick="setNoteSubdivision(1)">♩ 1x</button>
                                <button id="btnSpeed2" class="nav-tab-btn" style="padding: 4px 8px; font-size: 0.75rem;" onclick="setNoteSubdivision(2)">♪ 2x</button>
                                <button id="btnSpeed4" class="nav-tab-btn" style="padding: 4px 8px; font-size: 0.75rem;" onclick="setNoteSubdivision(4)">♬ 4x</button>
                            </div>
                        </div>

                        <!-- Tempo Control -->
                        <div class="tempo-box">
                            <span style="font-size: 0.75rem; color: var(--text-muted);">டெம்போ:</span>
                            <button class="btn-mini" onclick="adjustTempo(-5)">-</button>
                            <input id="tempoSlider" type="range" class="tempo-slider" min="40" max="240" value="80" oninput="onTempoSliderChange(this.value)">
                            <button class="btn-mini" onclick="adjustTempo(5)">+</button>
                            <span id="tempoDisplay" class="tempo-val">80 BPM</span>
                            <span id="tempoMarking" class="badge" style="background: rgba(212, 175, 55, 0.2); color: var(--gold-bright); border: 1px solid var(--border-glow); padding: 2px 7px; border-radius: 4px; font-size: 0.72rem; font-weight: 600;">Andante</span>
                        </div>
                    </div>
                </div>

                <!-- Western Rhythm & Conductor Visualizer Box -->
                <div class="tala-box">
                    <div class="tala-header">
                        <div>
                            <div id="meterDisplay" class="tala-name">4/4 Common Time</div>
                            <div id="meterSubtitle" class="tala-anga">4 Beats per Measure • Downbeat on 1</div>
                        </div>
                        <select id="rhythmStyleSelect" class="custom-select" style="padding: 4px 8px; font-size: 0.75rem; width: auto;" onchange="onRhythmStyleChange(this.value)">
                            <option value="metronome" selected>⏱️ Metronome Click</option>
                            <option value="pop_rock">🥁 4/4 Pop-Rock Drum Beat</option>
                            <option value="waltz">🎻 3/4 Piano Waltz Groove</option>
                            <option value="ballad">🌙 6/8 Slow Rock / Ballad</option>
                            <option value="blues">🎷 12-Bar Blues Shuffle</option>
                        </select>
                    </div>

                    <!-- Conductor Gesture Display -->
                    <div class="tala-gesture-display">
                        <div id="gestureIcon" class="gesture-icon">⬇️</div>
                        <div class="gesture-info">
                            <h4 id="gestureText">பீட் 1: டவுன்பீட் (Downbeat)</h4>
                            <p id="gestureSub">அளவின் முதல் அடி • வலிமையான ஆரம்பம்</p>
                        </div>
                    </div>

                    <!-- Beat Pulse Dots -->
                    <div id="beatDotsRow" class="tala-dots-row">
                        <!-- Populated by JS: [1] [2] [3] [4] -->
                    </div>
                </div>
            </div>

            <!-- Active Step Info Strip -->
            <div class="step-info-strip">
                <div class="step-metric-box">
                    <span class="metric-label">🎹 தற்போதைய நோட்:</span>
                    <span id="curNoteDisplay" class="metric-val highlight">C4</span>
                </div>
                <div class="step-metric-box">
                    <span class="metric-label">🗣️ சோல்ஃபேஜ் (Solfege):</span>
                    <span id="curSolfegeDisplay" class="metric-val">Do</span>
                </div>
                <div class="step-metric-box">
                    <span class="metric-label">🎼 க்ளெஃப் &amp; கை (Clef):</span>
                    <span id="curClefDisplay" class="metric-val">𝄞 RH (Right Hand)</span>
                </div>
                <div class="step-metric-box">
                    <span class="metric-label">🖐️ விரல் எண் (Finger):</span>
                    <span id="curFingerDisplay" class="metric-val highlight">விரல் 1 (Thumb)</span>
                </div>
                <div class="step-metric-box">
                    <span class="metric-label">🔊 அதிர்வெண் (Frequency):</span>
                    <span id="curFrequencyDisplay" class="metric-val">261.6 Hz</span>
                </div>
                <div class="step-metric-box">
                    <span class="metric-label">🎵 கார்ட் சூழல் (Chord):</span>
                    <span id="curChordContextDisplay" class="metric-val">C Major Triad (I)</span>
                </div>
            </div>

            <div id="notationAnchor"></div>
            <!-- Notation Ribbon Card -->
            <div class="notation-ribbon-card">
                <div class="ribbon-header">
                    <div id="ribbonLessonTitle" class="ribbon-title">
                        <span>1. C மேஜர் ஸ்கேல் (C Major Scale)</span>
                        <span id="ribbonStepBadge" class="ribbon-badge">நோட் 1 / 16</span>
                    </div>
                    <div style="display: flex; gap: 8px;">
                        <button class="btn-ctrl" onclick="centerMiddleC(true)" style="padding: 4px 10px; font-size: 0.75rem;">👑 Center Middle C</button>
                        <button class="btn-ctrl" id="btnOpenNotationLightbox" onclick="openNotationLightbox()" style="padding: 4px 10px; font-size: 0.75rem;" title="நோட்டேஷனை முழுத்திரையில் திறக்க">⛶ நோட்டேஷன் லைட்பாக்ஸ்</button>
                    </div>
                </div>

                <!-- Live Interactive Grand Staff Visualizer -->
                <div id="grandStaffContainer" class="grand-staff-box" style="margin-bottom: 12px; background: rgba(10, 14, 28, 0.75); border: 1px solid var(--border-glow); border-radius: 8px; padding: 8px 14px; display: flex; align-items: center; justify-content: space-between; gap: 14px; overflow-x: auto;">
                    <div style="flex-shrink: 0; min-width: 140px;">
                        <div style="font-size: 0.8rem; font-weight: 700; color: var(--gold-bright); display: flex; align-items: center; gap: 6px;">
                            <span>🎼 நேரடி கிராண்ட் ஸ்டாஃப்</span>
                            <span style="font-size: 0.65rem; background: rgba(99, 102, 241, 0.25); color: #818cf8; padding: 1px 5px; border-radius: 3px;">Live Sheet</span>
                        </div>
                        <div id="staffPitchLabel" style="font-size: 0.72rem; color: var(--cyan-accent); font-weight: 600; margin-top: 2px;">Treble 𝄞 • C4 (Do)</div>
                        <div id="staffDetailLabel" style="font-size: 0.68rem; color: var(--text-muted);">Middle C • Ledger Line</div>
                    </div>
                    <div style="flex: 1; display: flex; justify-content: center; min-width: 320px;">
                        <svg id="liveStaffSvg" viewBox="0 0 340 120" style="width: 100%; max-width: 340px; height: 95px;"></svg>
                    </div>
                    <div style="flex-shrink: 0; text-align: right; min-width: 110px;">
                        <div id="staffHandLabel" style="font-size: 0.75rem; font-weight: 700; color: #10b981;">வலது கை (RH 𝄞)</div>
                        <div id="staffClefDetail" style="font-size: 0.68rem; color: var(--text-muted);">Treble Clef (G-Clef)</div>
                    </div>
                </div>

                <!-- Scrollable Measures Ribbon -->
                <div id="timelineRibbon" class="swara-ribbon-scroll">
                    <!-- Populated dynamically by JS -->
                </div>
            </div>

            <div id="pianoAnchor"></div>
            <!-- Piano Bed Dock Header -->
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; flex-wrap: wrap; gap: 8px;">
                <span style="font-size: 0.85rem; font-weight: 700; color: var(--gold-bright);">🎹 61-விசை பியானோ பலகை (Virtual Synthesizer)</span>
                <div style="display: flex; gap: 8px;">
                    <button class="btn-ctrl" onclick="toggleKeyboardZoom()" style="padding: 4px 10px; font-size: 0.75rem;">🔍 ஜூம் (Zoom Keys)</button>
                    <button class="btn-ctrl" id="btnOpenKeyboardLightbox" onclick="openKeyboardLightbox()" style="padding: 4px 10px; font-size: 0.75rem;" title="விசைப்பலகையை முழுத்திரையில் திறக்க">⛶ விசைப்பலகை லைட்பாக்ஸ்</button>
                </div>
            </div>

            <!-- 61-Key Virtual Piano Bed -->
            <div class="piano-wrapper">
                <div id="pianoBed" class="piano-bed">
                    <!-- 61 Keys generated dynamically by JS -->
                </div>
            </div>
        </div>

        <!-- ================= VIEW 2: VOICE CULTURE & SOLFEGE ================= -->
        <div id="viewVoiceTraining" class="view-panel">
            <div class="glass-card">
                <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 14px; margin-bottom: 16px;">
                    <h2 style="color: var(--gold-bright); font-size: 1.35rem; font-weight: 800;">🎙️ பார்வை பாடுதல் &amp; சோல்ஃபேஜ் அரங்கம் (Sight-Singing &amp; Solfege Studio)</h2>
                    <p style="color: var(--text-muted); font-size: 0.88rem; margin-top: 4px;">Do-Re-Mi-Fa-Sol-La-Ti குரல் இனிமைப் பயிற்சிகள் • மைக் சுருதிமானி வழிகாட்டுதலுடன் சுருதி தவறாமல் பாடும் எளிய முறை</p>
                </div>

                <!-- 5 Core Exercises Grid -->
                <div class="theory-grid">
                    <div class="theory-card" style="border-left: 4px solid var(--gold-bright);">
                        <h3>🍯 1. தேன் போன்ற குரலுக்கு: 5-நோட் வோக்கலைசர்</h3>
                        <p>Do - Re - Mi - Fa - Sol - Fa - Mi - Re - Do (C-D-E-F-G-F-E-D-C) வரிசையை பியானோவுடன் சேர்த்துப் பாடி குரலை சூடேற்றும் அடிப்படை பயிற்சி.</p>
                        <button class="btn-ctrl" onclick="playVoiceVocalizerScale(this)">▶️ பியானோவுடன் பாடு (Play Scale)</button>
                    </div>

                    <div class="theory-card" style="border-left: 4px solid var(--cyan-accent);">
                        <h3>🎼 2. மேஜர் ட்ரையாட் ஆர்பெஜியோ வோக்கல்</h3>
                        <p>Do - Mi - Sol - Do' - Sol - Mi - Do (C - E - G - C5 - G - E - C). குரலின் இடைவெளித் துல்லியத்தையும் (Pitch Accuracy) ஸ்தாயி மாற்றத்தையும் உயர்த்தும் பயிற்சி.</p>
                        <button class="btn-ctrl" onclick="playVoiceArpeggioScale(this)">▶️ ஆர்பெஜியோவுடன் பாடு</button>
                    </div>

                    <div class="theory-card" style="border-left: 4px solid var(--indigo-accent);">
                        <h3>🌊 3. ஆக்டேவ் சைரன் &amp; லிப் ட்ரில் (Lip Trill)</h3>
                        <p>உதடுகளை அதிர்வடையச் செய்து (Brrrr) கீழ் ஆக்டேவிலிருந்து மேல் ஆக்டேவ் வரை சைரன் போல் வளைத்துப் பாடும் தொண்டை தளர்வுப் பயிற்சி.</p>
                        <button class="btn-ctrl" onclick="playVoiceSirenGlide(this)">▶️ சைரன் வழிகாட்டி ஒலி</button>
                    </div>

                    <div class="theory-card" style="border-left: 4px solid var(--emerald-accent);">
                        <h3>🗣️ 4. மேற்கத்திய 5 உயிர் எழுத்துப் பயிற்சி (Vowels)</h3>
                        <p>ஒரே சுருதியில் Ee (ஈ) -> Ay (ஏ) -> Ah (ஆ) -> Oh (ஓ) -> Oo (ஊ) என உதட்டு வடிவங்களை மாற்றி உச்சரிக்கும் மேற்கத்திய ஓபரா குரல் நுட்பம்.</p>
                        <button class="btn-ctrl" onclick="play5VowelsExercise(this)">▶️ வோவல் ட்யூனுடன் பாடு</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= VIEW 3: OCTAVES & GRAND STAFF THEORY ================= -->
        <div id="viewSthayiTheory" class="view-panel">
            <div class="glass-card">
                <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 14px; margin-bottom: 16px;">
                    <h2 style="color: var(--gold-bright); font-size: 1.35rem; font-weight: 800;">📖 மேற்கத்திய ஆக்டேவ்கள் &amp; கிராண்ட் ஸ்டாஃப் தத்துவம் (Octaves &amp; Grand Staff)</h2>
                    <p style="color: var(--text-muted); font-size: 0.88rem; margin-top: 4px;">Treble Clef (𝄞 RH), Bass Clef (𝄢 LH), Middle C (C4) மற்றும் 7 ஆக்டேவ்களின் முழுமையான வழிகாட்டி</p>
                </div>

                <div class="theory-grid">
                    <div class="theory-card">
                        <h3>𝄞 ட்ரெபிள் க்ளெஃப் (Treble Clef / G-Clef)</h3>
                        <p>• பொதுவாக பியானோவின் வலது கை (Right Hand) வாசிக்கும் உயர் சுருதி நோட்டுகள்.<br>
                        • <strong>கோடுகள் (Lines):</strong> Every Good Boy Does Fine (E4 - G4 - B4 - D5 - F5)<br>
                        • <strong>இடைவெளிகள் (Spaces):</strong> F - A - C - E (F4 - A4 - C5 - E5)</p>
                    </div>

                    <div class="theory-card">
                        <h3>𝄢 பேஸ் க்ளெஃப் (Bass Clef / F-Clef)</h3>
                        <p>• பொதுவாக பியானோவின் இடது கை (Left Hand) வாசிக்கும் ஆழமான பாஸ் நோட்டுகள்.<br>
                        • <strong>கோடுகள் (Lines):</strong> Good Boys Do Fine Always (G2 - B2 - D3 - F3 - A3)<br>
                        • <strong>இடைவெளிகள் (Spaces):</strong> All Cows Eat Grass (A2 - C3 - E3 - G3)</p>
                    </div>

                    <div class="theory-card">
                        <h3>👑 மிடில் சி (Middle C • C4 = 261.63 Hz)</h3>
                        <p>• பியானோ விசைப்பலகையின் மிக முக்கியமான மையப்புள்ளி!<br>
                        • ட்ரெபிள் க்ளெஃப் மற்றும் பேஸ் க்ளெஃப் இரண்டிற்கும் நடுவே லெட்ஜர் லைனில் (Ledger Line) அமர்ந்து இரு உலகங்களையும் இணைக்கிறது.</p>
                    </div>
                </div>

                <!-- 7 Octaves Audio Audition Table -->
                <div style="margin-top: 24px;">
                    <h3 style="color: var(--cyan-accent); font-size: 1.1rem; margin-bottom: 12px;">🎹 மேற்கத்திய 7 ஆக்டேவ்கள் &amp; ஒலி கேட்கும் வசதி (Audition C1 to C7)</h3>
                    <div id="octavesContainer" class="theory-grid">
                        <!-- Populated dynamically by JS -->
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= VIEW 4: SCALES & CHURCH MODES ================= -->
        <div id="viewMelakarta" class="view-panel">
            <div class="glass-card">
                <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 14px; margin-bottom: 16px;">
                    <h2 style="color: var(--gold-bright); font-size: 1.35rem; font-weight: 800;">🌀 மேற்கத்திய ஸ்கேல்கள் &amp; 7 மோடுகள் (Scales &amp; Church Modes)</h2>
                    <p style="color: var(--text-muted); font-size: 0.88rem; margin-top: 4px;">சர்க்கிள் ஆஃப் பிஃப்த்ஸ் (Circle of Fifths), 7 நடுக்கால சர்ச் மோடுகள், மேஜர், மைனர், பெண்டாடோனிக் &amp; ப்ளூஸ் ஸ்கேல்கள்</p>
                </div>

                <!-- Circle of Fifths Table -->
                <div style="overflow-x: auto; margin-bottom: 24px;">
                    <h3 style="color: var(--gold-bright); margin-bottom: 10px;">⭕ சர்க்கிள் ஆஃப் பிஃப்த்ஸ் அட்டவணை (12 Major &amp; Relative Minor Keys)</h3>
                    <table class="circle-table">
                        <thead>
                            <tr>
                                <th>Major Key</th>
                                <th>Root</th>
                                <th>Sharps / Flats</th>
                                <th>Relative Minor</th>
                                <th>Scale Notes</th>
                                <th>வாசித்துக் கேட்க</th>
                            </tr>
                        </thead>
                        <tbody id="circleTableBody">
                            <!-- Populated dynamically by JS -->
                        </tbody>
                    </table>
                </div>

                <!-- 7 Church Modes Grid -->
                <h3 style="color: var(--cyan-accent); margin-bottom: 12px;">⛪ 7 மேற்கத்திய சர்ச் மோடுகள் &amp; பெண்டாடோனிக் ஸ்கேல்கள்</h3>
                <div id="modesContainer" class="theory-grid">
                    <!-- Populated dynamically by JS -->
                </div>
            </div>
        </div>

        <!-- ================= VIEW 5: CHORD DICTIONARY & INVERSIONS ================= -->
        <div id="viewJanyaRagas" class="view-panel">
            <div class="glass-card">
                <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 14px; margin-bottom: 16px;">
                    <h2 style="color: var(--gold-bright); font-size: 1.35rem; font-weight: 800;">🎼 கார்ட் அகராதி &amp; இன்வெர்ஷன்கள் (Western Chord Dictionary &amp; Builder)</h2>
                    <p style="color: var(--text-muted); font-size: 0.88rem; margin-top: 4px;">Major, Minor, Diminished, Augmented, Sus, 7th கார்டுகள் • இன்வெர்ஷன்கள் (Root, 1st, 2nd) மற்றும் நேரடி வாசிப்பு</p>
                </div>

                <!-- Interactive Chord Builder Controls -->
                <div style="background: rgba(10, 14, 28, 0.7); border: 1px solid var(--border-glow); border-radius: 14px; padding: 18px; margin-bottom: 20px;">
                    <div class="controls-row">
                        <div class="select-group">
                            <label class="select-label" for="chordRootSelect">1. ரூட் நோட் (Root Note):</label>
                            <select id="chordRootSelect" class="custom-select" onchange="updateChordBuilder()">
                                <!-- Populated dynamically by JS -->
                            </select>
                        </div>

                        <div class="select-group">
                            <label class="select-label" for="chordTypeSelect">2. கார்ட் வகை (Chord Type):</label>
                            <select id="chordTypeSelect" class="custom-select" onchange="updateChordBuilder()">
                                <!-- Populated dynamically by JS -->
                            </select>
                        </div>

                        <div class="select-group">
                            <label class="select-label" for="chordInvSelect">3. இன்வெர்ஷன் (Inversion):</label>
                            <select id="chordInvSelect" class="custom-select" onchange="updateChordBuilder()">
                                <option value="0" selected>Root Position (அடிப்படை நிலை)</option>
                                <option value="1">1st Inversion (முதல் மாற்றம்)</option>
                                <option value="2">2nd Inversion (இரண்டாம் மாற்றம்)</option>
                            </select>
                        </div>

                        <div style="display: flex; gap: 8px; align-items: flex-end;">
                            <button class="btn-ctrl btn-primary" onclick="playCurrentBuiltChord(false)">🎹 கார்ட் வாசி (Harmonic)</button>
                            <button class="btn-ctrl" onclick="playCurrentBuiltChord(true)">🎼 ஆர்பெஜியோ (Arpeggio)</button>
                        </div>
                    </div>

                    <!-- Built Chord Result Box -->
                    <div id="chordResultDisplay" style="margin-top: 14px; padding: 12px; background: rgba(255, 255, 255, 0.04); border-radius: 8px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
                        <div>
                            <span style="font-size: 1.25rem; font-weight: 800; color: var(--gold-bright);" id="chordResultName">C Major (C)</span>
                            <span style="color: var(--text-muted); font-size: 0.85rem; margin-left: 10px;" id="chordResultFormula">1 - 3 - 5</span>
                        </div>
                        <div style="font-family: var(--font-mono); font-size: 1.05rem; font-weight: 700; color: #38bdf8;" id="chordResultNotes">C4 - E4 - G4</div>
                    </div>
                </div>

                <!-- Chord Progressions Showcase -->
                <h3 style="color: var(--cyan-accent); margin-bottom: 12px;">🎶 உலகப் புகழ்பெற்ற 5 கார்ட் தொடர்கள் (Famous Chord Progressions)</h3>
                <div class="theory-grid">
                    <div class="theory-card">
                        <h3>1. கிளாசிக் I - IV - V - I (C - F - G - C)</h3>
                        <p>ராக், கிளாசிக்கல் மற்றும் நாட்டுப்புற இசையின் ஆணிவேர்.</p>
                        <button class="btn-ctrl" onclick="playProgressionDemo(['C4,E4,G4', 'F4,A4,C5', 'G4,B4,D5', 'C4,E4,G4'], this)">▶️ வாசித்துக் கேட்க</button>
                    </div>

                    <div class="theory-card">
                        <h3>2. பாப் 4-கார்ட் ஆந்தம் (C - G - Am - F)</h3>
                        <p>லட்சக்கணக்கான உலக பாப் ஹிட் பாடல்களின் மந்திரத் தொடர்.</p>
                        <button class="btn-ctrl" onclick="playProgressionDemo(['C4,E4,G4', 'G4,B4,D5', 'A4,C5,E5', 'F4,A4,C5'], this)">▶️ வாசித்துக் கேட்க</button>
                    </div>

                    <div class="theory-card">
                        <h3>3. ஜாஸ் ii - V - I (Dm7 - G7 - Cmaj7)</h3>
                        <p>ஜாஸ் மற்றும் போசா நோவா இசையின் அடிப்படை அடித்தளம்.</p>
                        <button class="btn-ctrl" onclick="playProgressionDemo(['D4,F4,A4,C5', 'G4,B4,D5,F5', 'C4,E4,G4,B4'], this)">▶️ வாசித்துக் கேட்க</button>
                    </div>

                    <div class="theory-card">
                        <h3>4. 12-பார் ப்ளூஸ் (C7 - F7 - G7)</h3>
                        <p>ப்ளூஸ் மற்றும் ராக் அண்ட் ரோலின் பிறப்பிடம்.</p>
                        <button class="btn-ctrl" onclick="playProgressionDemo(['C4,E4,G4,Bb4', 'F4,A4,C5,Eb5', 'G4,B4,D5,F5', 'C4,E4,G4,Bb4'], this)">▶️ வாசித்துக் கேட்க</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= VIEW 6: EAR TRAINING & QUIZ ================= -->
        <div id="viewEarTraining" class="view-panel">
            <div class="glass-card">
                <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 14px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                    <div>
                        <h2 style="color: var(--gold-bright); font-size: 1.35rem; font-weight: 800;">🎮 மேற்கத்திய செவிப் பயிற்சி &amp; வினாடி-வினா (Western Ear Training)</h2>
                        <p style="color: var(--text-muted); font-size: 0.88rem; margin-top: 4px;">ஒலிகளைக் கேட்டு நோட்டுகள், இடைவெளிகள், கார்டுகள் மற்றும் ஸ்கேல்களைக் கண்டறியும் பயிற்சி விளையாட்டு</p>
                    </div>
                    <div style="display: flex; gap: 12px; align-items: center;">
                        <span class="badge-pill" style="font-size: 0.9rem; padding: 6px 12px;">மதிப்பெண்: <strong id="quizScore" style="color:#fbbf24;">0</strong></span>
                        <span class="badge-pill" style="font-size: 0.9rem; padding: 6px 12px;">தொடர் வெற்றி: <strong id="quizStreak" style="color:#34d399;">0 🔥</strong></span>
                    </div>
                </div>

                <!-- Quiz Mode Selector -->
                <div class="controls-row" style="margin-bottom: 18px;">
                    <button id="btnQuizModeNote" class="btn-ctrl active" onclick="setQuizMode('note')">🎵 1. நோட் அறிதல் (Single Note)</button>
                    <button id="btnQuizModeInterval" class="btn-ctrl" onclick="setQuizMode('interval')">📏 2. இடைவெளி (Interval Training)</button>
                    <button id="btnQuizModeChord" class="btn-ctrl" onclick="setQuizMode('chord')">🎹 3. மேஜர் vs மைனர் கார்ட்</button>
                    <button id="btnQuizModeScale" class="btn-ctrl" onclick="setQuizMode('scale')">🎼 4. ஸ்கேல் அறிதல் (Scale Mode)</button>
                </div>

                <!-- Quiz Interactive Play Box -->
                <div style="background: rgba(10, 14, 28, 0.8); border: 2px dashed rgba(212, 175, 55, 0.35); border-radius: 16px; padding: 28px; text-align: center; margin-bottom: 20px;">
                    <div style="font-size: 1.1rem; color: #fff; margin-bottom: 14px;" id="quizPromptText">ரகசிய ஒலியை கவனமாகக் கேட்டு சரியான விடையைத் தேர்ந்தெடுக்கவும்:</div>
                    <button class="btn-ctrl btn-primary" style="margin: 0 auto; font-size: 1.1rem; padding: 12px 28px;" onclick="playQuizMysterySound()">🔊 ரகசிய ஒலியை மீண்டும் கேள் (Replay Sound)</button>
                    <div id="quizFeedback" style="margin-top: 16px; font-weight: 800; font-size: 1.05rem; min-height: 28px;"></div>
                </div>

                <!-- Quiz Options Grid -->
                <div id="quizOptionsGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px;">
                    <!-- Populated dynamically by JS -->
                </div>
            </div>
        </div>

        <!-- ================= VIEW 7: 12 SEMITONES & INTERVALS ================= -->
        <div id="viewSwaras" class="view-panel">
            <div class="glass-card">
                <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 14px; margin-bottom: 16px;">
                    <h2 style="color: var(--gold-bright); font-size: 1.35rem; font-weight: 800;">🎹 12 செமிடோன்கள் &amp; மேற்கத்திய இடைவெளிகள் (12 Semitones &amp; Intervals)</h2>
                    <p style="color: var(--text-muted); font-size: 0.88rem; margin-top: 4px;">12-டோன் ஈக்வல் டெம்பராமென்ட் (12-EDO / A4 = 440 Hz) • செமிடோன் கணக்கு, விகிதம் மற்றும் நினைவில் வைக்க உதவும் உலகப் பாடல்கள்</p>
                </div>

                <div style="overflow-x: auto;">
                    <table class="circle-table">
                        <thead>
                            <tr>
                                <th>செமிடோன் (Semi)</th>
                                <th>இடைவெளிப் பெயர் (Interval)</th>
                                <th>தமிழ் விளக்கம்</th>
                                <th>அதிர்வெண் விகிதம்</th>
                                <th>நினைவுப் பாடல் (Mnemonic)</th>
                                <th>ஒலி கேட்க</th>
                            </tr>
                        </thead>
                        <tbody id="intervalsTableBody">
                            <!-- Populated dynamically by JS -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- ================= VIEW 8: KEYBOARD TECH & HARDWARE GUIDE ================= -->
        <div id="viewPsrGuide" class="view-panel">
            <div class="glass-card">
                <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 14px; margin-bottom: 16px;">
                    <h2 style="color: var(--gold-bright); font-size: 1.35rem; font-weight: 800;">🎹 மேற்கத்திய விசைப்பலகை &amp; தொழில்முறை வழிகாட்டி (Keyboard &amp; Tech Guide)</h2>
                    <p style="color: var(--text-muted); font-size: 0.88rem; margin-top: 4px;">யமஹா, ரோலண்ட், கேசியோ வாங்குதல், சரியான விரல் பொசிஷன், சஸ்டைன் பெடல் நுட்பம் மற்றும் கணினி USB-MIDI இணைப்பு</p>
                </div>

                <div class="theory-grid">
                    <div class="theory-card">
                        <h3>🎹 1. 88 Keys vs 61 Keys எது சிறந்தது?</h3>
                        <p>• <strong>88 வெயிட்டட் கீகள் (Hammer Action):</strong> உண்மையான அகௌஸ்டிக் பியானோ வாசிப்பு உணர்வு தரும். கிளாசிக்கல் மற்றும் தீவிர பியானோ பயிற்சிகளுக்கு மிகச் சிறந்தது.<br>
                        • <strong>61 செமி-வெயிட்டட் கீகள் (Arranger):</strong> பாப், சின்த் மற்றும் லைவ் கச்சேரிகளுக்கு எடை குறைவான எளிதான தேர்வு.</p>
                    </div>

                    <div class="theory-card">
                        <h3>🖐️ 2. சரியான கை வடிவம் (Proper Hand Posture)</h3>
                        <p>• கையில் ஒரு கற்பனையான டென்னிஸ் பந்தை (Tennis Ball) பிடித்திருப்பது போன்ற வளைந்த விரல்கள்.<br>
                        • மணிக்கட்டை (Wrist) தட்டையாகவும், தோள்பட்டைகளைத் தளர்வாகவும் வைத்திருக்கவும்.<br>
                        • விரல் நுனிகளால் (Fingertips) மட்டுமே விசைகளைத் தொட வேண்டும், தட்டையாக அழுத்தக் கூடாது.</p>
                    </div>

                    <div class="theory-card">
                        <h3>🦶 3. சஸ்டைன் பெடல் நுட்பம் (Damper Pedal)</h3>
                        <p>• பியானோவின் வலது பெடல் ஒலியை நீட்டிக்கச் செய்யும் (Sustain).<br>
                        • புதிய கார்டு மாறும்போது உடனே பெடலை எடுத்து மீண்டும் அழுத்த வேண்டும் (Clean Pedaling), இல்லையெனில் ஒலிகள் கலங்கி இரைச்சல் உருவாகும்.</p>
                    </div>

                    <div class="theory-card">
                        <h3>🔌 4. கணினி / DAW மென்பொருளுடன் MIDI இணைப்பு</h3>
                        <p>• USB-to-Host கேபிளைக் கணினியுடன் இணைத்தால், இந்த வலைத்தளமே உங்கள் கீபோர்டை உடனடியாக அடையாளம் கண்டு கொள்ளும் (Web MIDI API).<br>
                        • FL Studio, Logic Pro, Ableton அல்லது GarageBand மூலம் ஸ்டீன்வே கிராண்ட் பியானோ VST ஒலிகளை இயக்கலாம்.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= VIEW 9: DIAGRAMS & VISUAL MAPS ================= -->
        <div id="viewDiagrams" class="view-panel">
            <div class="glass-card">
                <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 14px; margin-bottom: 16px;">
                    <h2 style="color: var(--gold-bright); font-size: 1.35rem; font-weight: 800;">🖼️ விசைப்பலகை வரைபடங்கள் &amp; வழிகாட்டிகள் (Visual Piano Maps)</h2>
                    <p style="color: var(--text-muted); font-size: 0.88rem; margin-top: 4px;">அதிக தெளிவுத்திறன் கொண்ட SVG வரைபடங்கள் • முழுத்திரையில் பார்க்க கிளிக் செய்யவும்</p>
                </div>

                <div class="diagrams-grid">
                    <!-- Diagram 1 -->
                    <div class="diagram-card" onclick="openDiagramLightbox('diagrams/keyboard/01_western_keyboard_note_map.svg', 'மேற்கத்திய விசைப்பலகை 12 ஸ்வர வரைபடம்')">
                        <img src="diagrams/keyboard/01_western_keyboard_note_map.svg" alt="Western Keyboard Note Map">
                        <div class="diagram-card-info">
                            <h4>1. 12 ஸ்வர விசைப்பலகை வரைபடம்</h4>
                            <p>Middle C (C4), 12 செமிடோன்கள், Sharps &amp; Flats மற்றும் சோல்ஃபேஜ் வழிகாட்டி.</p>
                        </div>
                    </div>

                    <!-- Diagram 2 -->
                    <div class="diagram-card" onclick="openDiagramLightbox('diagrams/keyboard/02_grand_staff_piano_map.svg', 'கிராண்ட் ஸ்டாஃப் &amp; பியானோ மேப்பிங்')">
                        <img src="diagrams/keyboard/02_grand_staff_piano_map.svg" alt="Grand Staff Piano Map">
                        <div class="diagram-card-info">
                            <h4>2. கிராண்ட் ஸ்டாஃப் &amp; பியானோ வரைபடம்</h4>
                            <p>Treble Clef (𝄞), Bass Clef (𝄢) மற்றும் Middle C லெட்ஜர் லைன் மேப்பிங்.</p>
                        </div>
                    </div>

                    <!-- Diagram 3 -->
                    <div class="diagram-card" onclick="openDiagramLightbox('diagrams/keyboard/03_circle_of_fifths_guide.svg', 'சர்க்கிள் ஆஃப் பிஃப்த்ஸ் வழிகாட்டி')">
                        <img src="diagrams/keyboard/03_circle_of_fifths_guide.svg" alt="Circle of Fifths Guide">
                        <div class="diagram-card-info">
                            <h4>3. சர்க்கிள் ஆஃப் பிஃப்த்ஸ் (Circle of Fifths)</h4>
                            <p>12 மேஜர் கீகள், ரிலேட்டிவ் மைனர் மற்றும் Sharps / Flats வரிசை முறை.</p>
                        </div>
                    </div>

                    <!-- Diagram 4 -->
                    <div class="diagram-card" onclick="openDiagramLightbox('diagrams/keyboard/04_piano_chords_chart.svg', 'அத்தியாவசிய பியானோ கார்ட் அட்டவணை')">
                        <img src="diagrams/keyboard/04_piano_chords_chart.svg" alt="Piano Chords Chart">
                        <div class="diagram-card-info">
                            <h4>4. அத்தியாவசிய பியானோ கார்ட் அட்டவணை</h4>
                            <p>பிரைமரி மேஜர், மைனர், Dominant 7th கார்டுகள் மற்றும் இன்வெர்ஷன்கள்.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </main>

    <!-- Fullscreen Keyboard Lightbox -->
    <div id="keyboardLightbox" class="modal-overlay fullscreen-lightbox-overlay" onclick="closeKeyboardLightbox(event)">
        <div class="modal-window fullscreen-lightbox-window" onclick="event.stopPropagation()">
            <button class="btn-close-modal" onclick="closeKeyboardLightbox()" aria-label="Close">✕</button>
            <h2 style="color: var(--gold-bright); font-family: var(--font-ta); font-size: 1.15rem; margin-bottom: 8px;">🎹 விசைப்பலகை — முழுத்திரை லைட்பாக்ஸ் (Fullscreen Virtual Piano)</h2>
            <div id="keyboardLightboxContent" class="fullscreen-lightbox-content"></div>
        </div>
    </div>

    <!-- Fullscreen Notation Lightbox -->
    <div id="notationLightbox" class="modal-overlay fullscreen-lightbox-overlay" onclick="closeNotationLightbox(event)">
        <div class="modal-window fullscreen-lightbox-window" onclick="event.stopPropagation()">
            <button class="btn-close-modal" onclick="closeNotationLightbox()" aria-label="Close">✕</button>
            <h2 style="color: var(--gold-bright); font-family: var(--font-ta); font-size: 1.15rem; margin-bottom: 8px;">📜 மேற்கத்திய நோட்டேஷன் — முழுத்திரை லைட்பாக்ஸ் (Fullscreen Notation Ribbon)</h2>
            <div id="notationLightboxContent" class="fullscreen-lightbox-content"></div>
        </div>
    </div>

    <!-- Modal Lightbox for Diagrams -->
    <div id="diagramLightboxModal" class="modal-overlay" onclick="closeDiagramLightbox(event)">
        <div class="modal-box" style="max-width: 1100px;">
            <button class="btn-close-modal" onclick="closeDiagramLightbox()">✕</button>
            <h3 id="lightboxTitle" style="color: var(--gold-bright); margin-bottom: 16px;">வரைபடம்</h3>
            <img id="lightboxImg" src="" alt="Diagram Large View" style="width: 100%; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
            <div style="margin-top: 14px; text-align: right;">
                <a id="lightboxDownloadBtn" href="" download class="btn-ctrl" style="display: inline-flex; text-decoration: none;">⬇️ முழு வரைபடத்தை பதிவிறக்கு (Download SVG)</a>
            </div>
        </div>
    </div>

    <!-- Quick Help & Shortcuts Modal -->
    <div id="helpModal" class="modal-overlay" onclick="closeHelpModal(event)">
        <div class="modal-box" style="max-width: 650px;">
            <button class="btn-close-modal" onclick="closeHelpModal()">✕</button>
            <h3 style="color: var(--gold-bright); margin-bottom: 14px;">⌨️ கணினி விசைப்பலகை குறுக்குவழிகள் (Keyboard Shortcuts)</h3>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.88rem; color: #cbd5e1;">
                <div><kbd style="background:#1e293b; padding:2px 7px; border-radius:4px; color:#fff; font-weight:bold;">Space</kbd> : ▶️ வாசி / ⏸️ இடைநிறுத்து (Play / Pause)</div>
                <div><kbd style="background:#1e293b; padding:2px 7px; border-radius:4px; color:#fff; font-weight:bold;">← / →</kbd> : ⏮️ முந்தைய / ⏭️ அடுத்த நோட் (Seek)</div>
                <div><kbd style="background:#1e293b; padding:2px 7px; border-radius:4px; color:#fff; font-weight:bold;">L</kbd> : 🔁 லூப் ஆன் / ஆஃப் (Toggle Loop)</div>
                <div><kbd style="background:#1e293b; padding:2px 7px; border-radius:4px; color:#fff; font-weight:bold;">A, S, D, F, G, H, J, K, L</kbd> : 🎹 வெள்ளை விசைகள் (C4, D4, E4, F4, G4, A4, B4, C5, D5)</div>
                <div><kbd style="background:#1e293b; padding:2px 7px; border-radius:4px; color:#fff; font-weight:bold;">W, E, T, Y, U, O, P</kbd> : 🎹 கருப்பு விசைகள் (C#4, D#4, F#4, G#4, A#4, C#5, D#5)</div>
                <div><kbd style="background:#1e293b; padding:2px 7px; border-radius:4px; color:#fff; font-weight:bold;">[ / ]</kbd> : 🎹 ஆக்டேவ் மாற்றம் (Octave Down / Up)</div>
                <div><kbd style="background:#1e293b; padding:2px 7px; border-radius:4px; color:#fff; font-weight:bold;">Esc</kbd> : ✕ சாளரங்களை மூடு (Close Modal)</div>
            </div>
        </div>
    </div>

    <!-- JavaScript Audio Engine & App Controller -->
    <script>
        // Injected Western Music Datasets
        const allLessons = {lessons_json};
        const circleOfFifthsData = {circle_json};
        const westernModesData = {modes_json};
        const westernIntervalsData = {intervals_json};
        const chordTypesData = {chords_json};
        const rootNotesData = {roots_json};
        const westernOctavesData = {octaves_json};

        // App State
        let currentView = 'studio';
        let currentLessonKey = 'm1';
        let currentHand = 'both';
        let currentKeyTranspose = 0; // Semitones transpose (0 = C Major)
        let currentBaseOctave = 0;   // 0 = C4 Middle C, -1 = C3, +1 = C5
        let currentVoice = 'grand_piano';
        let masterVolume = 0.75;
        let isPlaying = false;
        let playTimer = null;
        let isLooping = true;
        let currentStepIndex = 0;
        let currentBPM = 80;
        let currentNoteSubdivision = 1; // 1 = Quarter ♩, 2 = Eighth ♪, 4 = 16th ♬
        let isDrumsBackingOn = false;
        let currentRhythmStyle = 'metronome';
        let isPadDroneOn = false;
        let padDroneTimer = null;
        let isZoomMode = false;

        // Flattened Sequence of active lesson steps
        let flatSequence = [];

        // Web Audio Context & Nodes
        let audioCtx = null;
        let masterGainNode = null;
        let padDroneGainNode = null;

        // Live Mic Tuner State
        let isMicListening = false;
        let micStream = null;
        let micSourceNode = null;
        let micAnalyser = null;
        let micRafId = null;

        // Audio Recorder State
        let isRecording = false;
        let mediaRecorder = null;
        let recordedAudioChunks = [];
        let recordStartTime = null;
        let recordTimerInterval = null;

        // Ear Training Quiz State
        let quizMode = 'note';
        let quizSecret = null;
        let quizScore = 0;
        let quizStreak = 0;

        // 61-Key Keyboard Layout constants (C2 to C7: MIDI 36 to 96)
        const startMidi = 36; // C2
        const totalKeys = 61; // C2 to C7

        // Computer Keyboard Mapping to MIDI notes (Base around C4 = 60)
        const computerKeyMap = {{
            'a': 60, 'w': 61, 's': 62, 'e': 63, 'd': 64, 'f': 65, 't': 66,
            'g': 67, 'y': 68, 'h': 69, 'u': 70, 'j': 71, 'k': 72, 'o': 73,
            'l': 74, 'p': 75, ';': 76, "'": 77
        }};

        // ================= AUDIO ENGINE (Web Audio API) =================
        function initAudio() {{
            if (!audioCtx) {{
                const AudioCtxClass = window.AudioContext || window.webkitAudioContext;
                audioCtx = new AudioCtxClass();
                masterGainNode = audioCtx.createGain();
                masterGainNode.gain.setValueAtTime(masterVolume, audioCtx.currentTime);
                masterGainNode.connect(audioCtx.destination);
            }}
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
        }}

        function setMasterVolume(val) {{
            masterVolume = parseFloat(val);
            if (masterGainNode && audioCtx) {{
                masterGainNode.gain.setValueAtTime(masterVolume, audioCtx.currentTime);
            }}
        }}

        function midiToFreq(midi) {{
            return 440 * Math.pow(2, (midi - 69) / 12);
        }}

        // Synthesize Note according to selected Voice
        function playMidiNote(midi, durationSec = 0.6) {{
            if (!audioCtx) initAudio();
            const now = audioCtx.currentTime;
            const freq = midiToFreq(midi);

            switch (currentVoice) {{
                case 'electric_piano':
                    synthElectricPiano(freq, now, durationSec);
                    break;
                case 'pipe_organ':
                    synthPipeOrgan(freq, now, durationSec);
                    break;
                case 'synth_strings':
                    synthStrings(freq, now, durationSec);
                    break;
                case 'harpsichord':
                    synthHarpsichord(freq, now, durationSec);
                    break;
                case 'grand_piano':
                default:
                    synthGrandPiano(freq, now, durationSec);
                    break;
            }}
        }}

        // 1. Acoustic Grand Piano (Steinway Style multi-harmonic synthesis)
        function synthGrandPiano(freq, now, dur) {{
            // Fundamental + 2nd, 3rd, 4th harmonics + hammer strike transient
            const osc1 = audioCtx.createOscillator();
            const osc2 = audioCtx.createOscillator();
            const osc3 = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();

            osc1.type = 'triangle';
            osc1.frequency.setValueAtTime(freq, now);

            osc2.type = 'sine';
            osc2.frequency.setValueAtTime(freq * 2.002, now); // 2nd harmonic

            osc3.type = 'sine';
            osc3.frequency.setValueAtTime(freq * 3.004, now); // 3rd harmonic

            // Hammer transient noise click
            const clickOsc = audioCtx.createOscillator();
            const clickGain = audioCtx.createGain();
            clickOsc.type = 'sawtooth';
            clickOsc.frequency.setValueAtTime(freq * 5.2, now);
            clickGain.gain.setValueAtTime(0.35, now);
            clickGain.gain.exponentialRampToValueAtTime(0.0001, now + 0.03);
            clickOsc.connect(clickGain);
            clickGain.connect(masterGainNode);
            clickOsc.start(now);
            clickOsc.stop(now + 0.035);

            // Envelope: Crisp attack, natural piano acoustic decay
            gainNode.gain.setValueAtTime(0.0001, now);
            gainNode.gain.linearRampToValueAtTime(0.85, now + 0.006);
            gainNode.gain.exponentialRampToValueAtTime(0.4, now + 0.18);
            gainNode.gain.exponentialRampToValueAtTime(0.0001, now + dur + 0.12);

            osc1.connect(gainNode);
            osc2.connect(gainNode);
            osc3.connect(gainNode);
            gainNode.connect(masterGainNode);

            osc1.start(now);
            osc2.start(now);
            osc3.start(now);

            const stopTime = now + dur + 0.15;
            osc1.stop(stopTime);
            osc2.stop(stopTime);
            osc3.stop(stopTime);
        }}

        // 2. Electric Piano (Rhodes / DX7 Bell Chime)
        function synthElectricPiano(freq, now, dur) {{
            const osc = audioCtx.createOscillator();
            const tineOsc = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();

            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, now);

            tineOsc.type = 'triangle';
            tineOsc.frequency.setValueAtTime(freq * 4.0, now); // Bell chime overtone

            gainNode.gain.setValueAtTime(0.001, now);
            gainNode.gain.linearRampToValueAtTime(0.8, now + 0.008);
            gainNode.gain.exponentialRampToValueAtTime(0.0001, now + dur + 0.2);

            osc.connect(gainNode);
            tineOsc.connect(gainNode);
            gainNode.connect(masterGainNode);

            osc.start(now);
            tineOsc.start(now);
            osc.stop(now + dur + 0.22);
            tineOsc.stop(now + dur + 0.22);
        }}

        // 3. Church Pipe Organ (Additive drawbars)
        function synthPipeOrgan(freq, now, dur) {{
            const harmonics = [1, 2, 3, 4, 8];
            const weights = [0.4, 0.25, 0.15, 0.1, 0.05];
            const gainNode = audioCtx.createGain();

            gainNode.gain.setValueAtTime(0.001, now);
            gainNode.gain.linearRampToValueAtTime(0.7, now + 0.03);
            gainNode.gain.setValueAtTime(0.65, now + dur * 0.8);
            gainNode.gain.linearRampToValueAtTime(0.0001, now + dur + 0.08);
            gainNode.connect(masterGainNode);

            harmonics.forEach((h, idx) => {{
                const osc = audioCtx.createOscillator();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq * h, now);
                const hGain = audioCtx.createGain();
                hGain.gain.setValueAtTime(weights[idx], now);
                osc.connect(hGain);
                hGain.connect(gainNode);
                osc.start(now);
                osc.stop(now + dur + 0.1);
            }});
        }}

        // 4. Synth Strings / Pad
        function synthStrings(freq, now, dur) {{
            const osc1 = audioCtx.createOscillator();
            const osc2 = audioCtx.createOscillator();
            const filter = audioCtx.createBiquadFilter();
            const gainNode = audioCtx.createGain();

            osc1.type = 'sawtooth';
            osc2.type = 'sawtooth';
            osc1.frequency.setValueAtTime(freq, now);
            osc2.frequency.setValueAtTime(freq * 1.004, now); // Detune for lushness

            filter.type = 'lowpass';
            filter.frequency.setValueAtTime(1400, now);

            gainNode.gain.setValueAtTime(0.001, now);
            gainNode.gain.linearRampToValueAtTime(0.6, now + 0.08); // Slow gentle bowed attack
            gainNode.gain.exponentialRampToValueAtTime(0.0001, now + dur + 0.35);

            osc1.connect(filter);
            osc2.connect(filter);
            filter.connect(gainNode);
            gainNode.connect(masterGainNode);

            osc1.start(now);
            osc2.start(now);
            osc1.stop(now + dur + 0.4);
            osc2.stop(now + dur + 0.4);
        }}

        // 5. Baroque Harpsichord
        function synthHarpsichord(freq, now, dur) {{
            const osc = audioCtx.createOscillator();
            const filter = audioCtx.createBiquadFilter();
            const gainNode = audioCtx.createGain();

            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(freq, now);

            filter.type = 'bandpass';
            filter.frequency.setValueAtTime(2200, now);
            filter.Q.setValueAtTime(3.0, now);

            gainNode.gain.setValueAtTime(0.001, now);
            gainNode.gain.linearRampToValueAtTime(0.85, now + 0.004);
            gainNode.gain.exponentialRampToValueAtTime(0.0001, now + dur * 0.7);

            osc.connect(filter);
            filter.connect(gainNode);
            gainNode.connect(masterGainNode);

            osc.start(now);
            osc.stop(now + dur + 0.05);
        }}

        // ================= METRONOME & DRUMS SYNTHESIZER =================
        function synthMetronomeClick(isAccent, now) {{
            if (!audioCtx) return;
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(isAccent ? 1200 : 800, now);
            gain.gain.setValueAtTime(isAccent ? 0.7 : 0.45, now);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.04);
            osc.connect(gain);
            gain.connect(masterGainNode);
            osc.start(now);
            osc.stop(now + 0.045);
        }}

        function synthDrumKick(now) {{
            if (!audioCtx) return;
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(130, now);
            osc.frequency.exponentialRampToValueAtTime(45, now + 0.12);
            gain.gain.setValueAtTime(0.9, now);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.28);
            osc.connect(gain);
            gain.connect(masterGainNode);
            osc.start(now);
            osc.stop(now + 0.3);
        }}

        function synthDrumSnare(now) {{
            if (!audioCtx) return;
            // Noise burst + tone snap
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(180, now);
            gain.gain.setValueAtTime(0.65, now);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.14);
            osc.connect(gain);
            gain.connect(masterGainNode);
            osc.start(now);
            osc.stop(now + 0.15);
        }}

        function synthDrumHiHat(now) {{
            if (!audioCtx) return;
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.type = 'square';
            osc.frequency.setValueAtTime(8000, now);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.035);
            osc.connect(gain);
            gain.connect(masterGainNode);
            osc.start(now);
            osc.stop(now + 0.04);
        }}

        function playRhythmForBeat(beatIdx, totalBeats, now) {{
            if (!isDrumsBackingOn) return;
            const isDownbeat = (beatIdx % totalBeats === 0);

            switch (currentRhythmStyle) {{
                case 'pop_rock':
                    // 4/4 Pop-Rock: Kick on 1 & 3, Snare on 2 & 4, Hi-hat on all
                    if (beatIdx % 4 === 0 || beatIdx % 4 === 2) synthDrumKick(now);
                    if (beatIdx % 4 === 1 || beatIdx % 4 === 3) synthDrumSnare(now);
                    synthDrumHiHat(now);
                    break;
                case 'waltz':
                    // 3/4 Waltz: Kick on 1, Snare/Hihat on 2 & 3
                    if (beatIdx % 3 === 0) synthDrumKick(now);
                    else synthDrumSnare(now);
                    synthDrumHiHat(now);
                    break;
                case 'ballad':
                    // 6/8 Ballad
                    if (beatIdx % 6 === 0) synthDrumKick(now);
                    else if (beatIdx % 6 === 3) synthDrumSnare(now);
                    synthDrumHiHat(now);
                    break;
                case 'blues':
                    // 12-Bar Blues Shuffle
                    if (beatIdx % 4 === 0) synthDrumKick(now);
                    else synthDrumSnare(now);
                    synthDrumHiHat(now);
                    break;
                case 'metronome':
                default:
                    synthMetronomeClick(isDownbeat, now);
                    break;
            }}
        }}

        // ================= CHORD PAD DRONE GENERATOR =================
        function togglePadDrone() {{
            initAudio();
            isPadDroneOn = !isPadDroneOn;
            const btn = document.getElementById('btnDroneToggle');
            if (btn) btn.classList.toggle('active', isPadDroneOn);

            if (isPadDroneOn) {{
                startPadDrone();
            }} else {{
                stopPadDrone();
            }}
        }}

        function startPadDrone() {{
            stopPadDrone();
            if (!audioCtx) return;
            // Root pitch based on currentKeyTranspose (Base C3 = 48 + transpose)
            const rootMidi = 48 + currentKeyTranspose;
            const rootFreq = midiToFreq(rootMidi);
            const fifthFreq = midiToFreq(rootMidi + 7);
            const octFreq = midiToFreq(rootMidi + 12);

            const now = audioCtx.currentTime;
            padDroneGainNode = audioCtx.createGain();
            padDroneGainNode.gain.setValueAtTime(0.001, now);
            padDroneGainNode.gain.linearRampToValueAtTime(0.28, now + 1.2);
            padDroneGainNode.connect(masterGainNode);

            [rootFreq, fifthFreq, octFreq].forEach(f => {{
                const osc = audioCtx.createOscillator();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(f, now);
                osc.connect(padDroneGainNode);
                osc.start(now);
            }});
        }}

        function stopPadDrone() {{
            if (padDroneGainNode && audioCtx) {{
                const now = audioCtx.currentTime;
                padDroneGainNode.gain.linearRampToValueAtTime(0.0001, now + 0.5);
                setTimeout(() => {{
                    try {{ padDroneGainNode.disconnect(); }} catch(e) {{}}
                    padDroneGainNode = null;
                }}, 600);
            }}
        }}

        function toggleDrumsBacking() {{
            initAudio();
            isDrumsBackingOn = !isDrumsBackingOn;
            const btn = document.getElementById('btnDrumsToggle');
            if (btn) btn.classList.toggle('active', isDrumsBackingOn);
        }}

        // ================= 61-KEY VIRTUAL PIANO RENDERER =================
        function render61KeyPiano() {{
            const pianoBed = document.getElementById('pianoBed');
            if (!pianoBed) return;
            pianoBed.innerHTML = '';

            let whiteIndex = 0;
            const noteNames = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];

            for (let i = 0; i < totalKeys; i++) {{
                const midi = startMidi + i;
                const noteInOct = midi % 12;
                const octave = Math.floor(midi / 12) - 1;
                const isBlack = [1, 3, 6, 8, 10].includes(noteInOct);
                const westName = noteNames[noteInOct] + octave;

                if (!isBlack) {{
                    const wKey = document.createElement('div');
                    wKey.className = 'key-white';
                    wKey.id = `key_midi_${{midi}}`;
                    wKey.dataset.midi = midi;
                    wKey.dataset.west = westName;

                    if (westName === 'C4') {{
                        const crown = document.createElement('span');
                        crown.className = 'middle-c-crown';
                        crown.textContent = '👑';
                        crown.title = 'Middle C4 (மைய சி • 261.6 Hz)';
                        wKey.appendChild(crown);
                    }}

                    // Hotkey label
                    const hintKey = getComputerKeyHint(midi);
                    if (hintKey) {{
                        const hintSpan = document.createElement('span');
                        hintSpan.className = 'key-hint-lbl';
                        hintSpan.textContent = hintKey.toUpperCase();
                        wKey.appendChild(hintSpan);
                    }}

                    const westLbl = document.createElement('span');
                    westLbl.className = 'key-west-lbl';
                    westLbl.textContent = westName;
                    wKey.appendChild(westLbl);

                    wKey.onpointerdown = (e) => onKeyPointerDown(midi, e);
                    wKey.onpointerenter = (e) => {{ if (e.buttons === 1) onKeyPointerDown(midi, e); }};
                    wKey.onpointerup = () => onKeyPointerUp(midi);
                    wKey.onpointerleave = () => onKeyPointerUp(midi);

                    pianoBed.appendChild(wKey);
                    whiteIndex++;
                }} else {{
                    const bKey = document.createElement('div');
                    bKey.className = 'key-black';
                    bKey.id = `key_midi_${{midi}}`;
                    bKey.dataset.midi = midi;
                    bKey.dataset.west = westName;

                    const whiteKeyWidth = isZoomMode ? 46 : 38;
                    const blackKeyWidth = isZoomMode ? 30 : 24;
                    const leftPos = (whiteIndex * whiteKeyWidth) - (blackKeyWidth / 2);
                    bKey.style.left = `${{leftPos}}px`;

                    const hintKey = getComputerKeyHint(midi);
                    if (hintKey) {{
                        const hintSpan = document.createElement('span');
                        hintSpan.className = 'key-hint-lbl';
                        hintSpan.textContent = hintKey.toUpperCase();
                        bKey.appendChild(hintSpan);
                    }}

                    const westLbl = document.createElement('span');
                    westLbl.className = 'key-west-lbl';
                    westLbl.textContent = westName;
                    bKey.appendChild(westLbl);

                    bKey.onpointerdown = (e) => onKeyPointerDown(midi, e);
                    bKey.onpointerenter = (e) => {{ if (e.buttons === 1) onKeyPointerDown(midi, e); }};
                    bKey.onpointerup = () => onKeyPointerUp(midi);
                    bKey.onpointerleave = () => onKeyPointerUp(midi);

                    pianoBed.appendChild(bKey);
                }}
            }}
        }}

        function getComputerKeyHint(midi) {{
            for (const [key, m] of Object.entries(computerKeyMap)) {{
                if (m === midi) return key;
            }}
            return null;
        }}

        function onKeyPointerDown(midi, e) {{
            if (e) e.preventDefault();
            initAudio();
            playMidiNote(midi, 0.7);
            highlightKeyVisual(midi, true);
        }}

        function onKeyPointerUp(midi) {{
            highlightKeyVisual(midi, false);
        }}

        function highlightKeyVisual(midi, isActive) {{
            const keyEl = document.getElementById(`key_midi_${{midi}}`);
            if (keyEl) {{
                if (isActive) keyEl.classList.add('active');
                else keyEl.classList.remove('active');
            }}
        }}

        function centerMiddleC(smooth = true) {{
            const midC = document.getElementById('key_midi_60');
            const wrapper = document.querySelector('.piano-wrapper');
            if (midC && wrapper) {{
                const offset = midC.offsetLeft - (wrapper.clientWidth / 2) + 20;
                wrapper.scrollTo({{ left: offset, behavior: smooth ? 'smooth' : 'auto' }});
            }}
        }}

        // ================= LESSON PARSING & TIMELINE RIBBON =================
        function parseWesternNoteToken(token, baseOctaveShift = 0) {{
            const clean = token.trim();
            if (clean === ',' || clean === '-' || clean === 'rest') {{
                return {{ isRest: true, noteName: '—', midi: null, solfege: 'Rest', finger: '—', clef: '—' }};
            }}

            // Regex matches Note Letter [A-G] + Optional Sharp/Flat [#|b] + Optional Octave [0-8]
            const match = clean.match(/^([A-Ga-g])([#b]?)([0-8]?)$/);
            if (!match) {{
                return {{ isRest: true, noteName: '—', midi: null, solfege: '—', finger: '—', clef: '—' }};
            }}

            const letter = match[1].toUpperCase();
            const accidental = match[2];
            let oct = match[3] !== '' ? parseInt(match[3]) : 4;
            oct += baseOctaveShift;

            const letterSemis = {{ 'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11 }};
            let semi = letterSemis[letter];
            if (accidental === '#') semi += 1;
            else if (accidental === 'b') semi -= 1;

            let midi = (oct + 1) * 12 + semi + currentKeyTranspose;
            midi = Math.max(21, Math.min(108, midi));

            const solfegeMap = {{ 0: 'Do', 1: 'Di/Ra', 2: 'Re', 3: 'Ri/Me', 4: 'Mi', 5: 'Fa', 6: 'Fi/Se', 7: 'Sol', 8: 'Si/Le', 9: 'La', 10: 'Li/Te', 11: 'Ti' }};
            const solfege = solfegeMap[((midi - currentKeyTranspose) % 12 + 12) % 12] || 'Do';

            // Clef & Hand
            const isTreble = midi >= 60;
            const clef = isTreble ? '𝄞 RH' : '𝄢 LH';

            // Recommended default fingering
            const relScaleDeg = ((midi - 60 - currentKeyTranspose) % 12 + 12) % 12;
            const fingerMap = {{ 0: 1, 2: 2, 4: 3, 5: 1, 7: 2, 9: 3, 11: 4, 12: 5 }};
            const fingerNum = fingerMap[relScaleDeg] || (isTreble ? 1 : 5);

            const noteNames = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
            const actualNoteName = noteNames[midi % 12] + (Math.floor(midi / 12) - 1);

            return {{
                isRest: false,
                noteName: actualNoteName,
                rawToken: clean,
                midi: midi,
                solfege: solfege,
                clef: clef,
                finger: `F-${{fingerNum}}`
            }};
        }}

        function buildFlatSequence() {{
            flatSequence = [];
            const lesson = allLessons[currentLessonKey];
            if (!lesson) return;

            let globalIdx = 0;
            lesson.lines.forEach((line, lineIdx) => {{
                line.measures.forEach((meas, measIdx) => {{
                    meas.forEach((token, noteIdx) => {{
                        const parsed = parseWesternNoteToken(token, currentBaseOctave);
                        const sahityamWord = (line.sahityam && line.sahityam[measIdx] && line.sahityam[measIdx][noteIdx]) ? line.sahityam[measIdx][noteIdx] : '';

                        flatSequence.push({{
                            globalIdx: globalIdx,
                            lineIdx: lineIdx,
                            measIdx: measIdx,
                            lineTitle: line.title,
                            sahityam: sahityamWord,
                            ...parsed
                        }});
                        globalIdx++;
                    }});
                }});
            }});
        }}

        function renderTimelineRibbon() {{
            const ribbon = document.getElementById('timelineRibbon');
            if (!ribbon) return;
            ribbon.innerHTML = '';

            let currentLineIdx = -1;
            let currentMeasIdx = -1;
            let lineGroup = null;
            let lineMeasures = null;
            let measBlock = null;

            flatSequence.forEach((item, idx) => {{
                if (item.lineIdx !== currentLineIdx) {{
                    currentLineIdx = item.lineIdx;
                    currentMeasIdx = -1;

                    lineGroup = document.createElement('div');
                    lineGroup.className = 'swara-line-group';

                    const lineHeader = document.createElement('div');
                    lineHeader.className = 'swara-line-header';
                    lineHeader.textContent = item.lineTitle;
                    lineGroup.appendChild(lineHeader);

                    lineMeasures = document.createElement('div');
                    lineMeasures.className = 'swara-line-measures';
                    lineGroup.appendChild(lineMeasures);
                    ribbon.appendChild(lineGroup);
                }}

                if (item.measIdx !== currentMeasIdx) {{
                    if (currentMeasIdx >= 0) {{
                        const divider = document.createElement('div');
                        divider.className = 'tala-divider';
                        divider.textContent = '|';
                        lineMeasures.appendChild(divider);
                    }}
                    currentMeasIdx = item.measIdx;
                    measBlock = document.createElement('div');
                    measBlock.className = 'swara-measure-block';
                    lineMeasures.appendChild(measBlock);
                }}

                const node = document.createElement('div');
                node.className = 'swara-node';
                node.id = `ribbon_node_${{idx}}`;
                node.onclick = () => seekToStep(idx);

                const badge = document.createElement('div');
                badge.className = 'swara-badge-ta';
                badge.textContent = item.isRest ? '𝄽' : item.noteName;

                const solfegeSpan = document.createElement('div');
                solfegeSpan.className = 'swara-west-note';
                solfegeSpan.textContent = item.solfege;

                const fingerBadge = document.createElement('div');
                fingerBadge.className = 'swara-finger-num';
                fingerBadge.textContent = item.finger;

                node.append(badge, solfegeSpan, fingerBadge);

                if (item.sahityam) {{
                    const word = document.createElement('div');
                    word.className = 'swara-sahitya-word';
                    word.textContent = item.sahityam;
                    node.appendChild(word);
                }}

                measBlock.appendChild(node);
            }});
        }}

        function updateStepDisplay(playSound = true) {{
            if (flatSequence.length === 0) return;
            if (currentStepIndex >= flatSequence.length) currentStepIndex = 0;
            if (currentStepIndex < 0) currentStepIndex = flatSequence.length - 1;

            const cur = flatSequence[currentStepIndex];
            const lesson = allLessons[currentLessonKey];

            // Update Top Info Strip
            document.getElementById('curNoteDisplay').textContent = cur.noteName;
            document.getElementById('curSolfegeDisplay').textContent = cur.solfege;
            document.getElementById('curClefDisplay').textContent = cur.clef;
            document.getElementById('curFingerDisplay').textContent = cur.finger;
            document.getElementById('curFrequencyDisplay').textContent = cur.midi ? `${{midiToFreq(cur.midi).toFixed(1)}} Hz` : '—';
            document.getElementById('curChordContextDisplay').textContent = lesson.key || 'C Major';

            document.getElementById('ribbonStepBadge').textContent = `நோட் ${{currentStepIndex + 1}} / ${{flatSequence.length}}`;

            // Active Ribbon Node Highlight & Scroll
            document.querySelectorAll('.swara-node').forEach(n => n.classList.remove('active'));
            const activeNode = document.getElementById(`ribbon_node_${{currentStepIndex}}`);
            if (activeNode) {{
                activeNode.classList.add('active');
                activeNode.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
            }}

            // Update Live Grand Staff Visualization
            updateGrandStaffVisual(cur);

            // Piano Keys Highlight
            document.querySelectorAll('.key-white, .key-black').forEach(k => k.classList.remove('active'));
            if (cur.midi) {{
                highlightKeyVisual(cur.midi, true);
            }}

            // Rhythm Conductor & Beat Dots
            const beatsPerMeasure = lesson.meter === '3/4' ? 3 : (lesson.meter === '6/8' ? 6 : 4);
            const beatIndex = currentStepIndex % beatsPerMeasure;
            updateConductorBeatVisuals(beatIndex, beatsPerMeasure, lesson.meter);

            // Play Audio
            if (playSound) {{
                initAudio();
                const stepDurationSec = (60 / currentBPM) / currentNoteSubdivision;
                if (!cur.isRest && cur.midi) {{
                    playMidiNote(cur.midi, stepDurationSec * 0.95);
                }}
                if (audioCtx) {{
                    playRhythmForBeat(beatIndex, beatsPerMeasure, audioCtx.currentTime);
                }}
            }}
        }}

        function updateConductorBeatVisuals(beatIndex, totalBeats, meter) {{
            const dotsRow = document.getElementById('beatDotsRow');
            if (dotsRow && dotsRow.dataset.beats !== String(totalBeats)) {{
                dotsRow.dataset.beats = String(totalBeats);
                dotsRow.innerHTML = '';
                for (let b = 0; b < totalBeats; b++) {{
                    const dot = document.createElement('div');
                    dot.className = `tala-dot ${{b === 0 ? 'downbeat' : ''}}`;
                    dot.textContent = b + 1;
                    dotsRow.appendChild(dot);
                }}
            }}

            document.querySelectorAll('.tala-dot').forEach((d, i) => {{
                if (i === beatIndex) d.classList.add('active');
                else d.classList.remove('active');
            }});

            const gestureIcon = document.getElementById('gestureIcon');
            const gestureText = document.getElementById('gestureText');
            const gestureSub = document.getElementById('gestureSub');

            const icons4 = ['⬇️', '⬅️', '➡️', '⬆️'];
            const names4 = ['டவுன்பீட் (Downbeat 1)', 'இன்வர்ட் (Inward 2)', 'அவுட்வர்ட் (Outward 3)', 'அப்பீட் (Upbeat 4)'];

            gestureIcon.textContent = icons4[beatIndex % icons4.length];
            gestureText.textContent = `பீட் ${{beatIndex + 1}}: ${{names4[beatIndex % names4.length]}}`;
            gestureSub.textContent = `${{meter}} அளவின் ${{beatIndex + 1}}-வது அடி`;
        }}

        // ================= PLAYBACK CONTROLS =================
        function togglePlayPause() {{
            initAudio();
            if (isPlaying) {{
                pausePlayback();
            }} else {{
                startPlayback();
            }}
        }}

        function startPlayback() {{
            isPlaying = true;
            document.getElementById('playIcon').textContent = '⏸️';
            document.getElementById('playLabel').textContent = 'நிறுத்து (Pause)';

            const stepIntervalMs = ((60 / currentBPM) / currentNoteSubdivision) * 1000;
            updateStepDisplay(true);

            playTimer = setInterval(() => {{
                currentStepIndex++;
                if (currentStepIndex >= flatSequence.length) {{
                    if (isLooping) {{
                        currentStepIndex = 0;
                    }} else {{
                        pausePlayback();
                        currentStepIndex = 0;
                        updateStepDisplay(false);
                        return;
                    }}
                }}
                updateStepDisplay(true);
            }}, stepIntervalMs);
        }}

        function pausePlayback() {{
            isPlaying = false;
            if (playTimer) {{
                clearInterval(playTimer);
                playTimer = null;
            }}
            document.getElementById('playIcon').textContent = '▶️';
            document.getElementById('playLabel').textContent = 'வாசி (Play)';
        }}

        function stopPlayback() {{
            pausePlayback();
            currentStepIndex = 0;
            updateStepDisplay(false);
        }}

        function toggleLoop() {{
            isLooping = !isLooping;
            document.getElementById('btnLoop').classList.toggle('active', isLooping);
        }}

        function stepBackward() {{
            pausePlayback();
            currentStepIndex--;
            updateStepDisplay(true);
        }}

        function stepForward() {{
            pausePlayback();
            currentStepIndex++;
            updateStepDisplay(true);
        }}

        function seekToStep(idx) {{
            pausePlayback();
            currentStepIndex = idx;
            updateStepDisplay(true);
        }}

        function setNoteSubdivision(sub) {{
            currentNoteSubdivision = sub;
            ['btnSpeed1', 'btnSpeed2', 'btnSpeed4'].forEach(b => document.getElementById(b).classList.remove('active'));
            if (sub === 1) document.getElementById('btnSpeed1').classList.add('active');
            else if (sub === 2) document.getElementById('btnSpeed2').classList.add('active');
            else if (sub === 4) document.getElementById('btnSpeed4').classList.add('active');

            if (isPlaying) {{
                pausePlayback();
                startPlayback();
            }}
        }}

        function getTempoMarking(bpm) {{
            if (bpm < 45) return 'Grave (40-44)';
            if (bpm < 60) return 'Largo (45-59)';
            if (bpm < 66) return 'Larghetto (60-65)';
            if (bpm < 76) return 'Adagio (66-75)';
            if (bpm < 108) return 'Andante (76-107)';
            if (bpm < 120) return 'Moderato (108-119)';
            if (bpm < 156) return 'Allegro (120-155)';
            if (bpm < 176) return 'Vivace (156-175)';
            if (bpm < 200) return 'Presto (176-199)';
            return 'Prestissimo (200+)';
        }}

        function updateTempoDisplay() {{
            const disp = document.getElementById('tempoDisplay');
            if (disp) disp.textContent = `${{currentBPM}} BPM`;
            const mark = document.getElementById('tempoMarking');
            if (mark) mark.textContent = getTempoMarking(currentBPM);
        }}

        function onTempoSliderChange(val) {{
            currentBPM = parseInt(val);
            updateTempoDisplay();
            if (isPlaying) {{
                pausePlayback();
                startPlayback();
            }}
        }}

        function adjustTempo(delta) {{
            const slider = document.getElementById('tempoSlider');
            const newBpm = Math.max(40, Math.min(240, currentBPM + delta));
            slider.value = newBpm;
            onTempoSliderChange(newBpm);
        }}

        // ================= LESSON & CATEGORY SELECTORS =================
        function populateLessonDropdown(cat = 'all') {{
            const selector = document.getElementById('lessonSelector');
            if (!selector) return;
            selector.innerHTML = '';

            for (const [key, lesson] of Object.entries(allLessons)) {{
                if (cat === 'all' || lesson.cat === cat) {{
                    const opt = document.createElement('option');
                    opt.value = key;
                    opt.textContent = lesson.title;
                    if (key === currentLessonKey) opt.selected = true;
                    selector.appendChild(opt);
                }}
            }}

            // If currentLessonKey not in filtered list, select first available
            if (!selector.value && selector.options.length > 0) {{
                selector.selectedIndex = 0;
                currentLessonKey = selector.value;
            }}
        }}

        function onCategoryChange() {{
            const cat = document.getElementById('catSelector').value;
            populateLessonDropdown(cat);
            onLessonChange();
        }}

        function onLessonChange() {{
            pausePlayback();
            currentLessonKey = document.getElementById('lessonSelector').value;
            const lesson = allLessons[currentLessonKey];
            if (lesson) {{
                currentBPM = lesson.tempo || 80;
                document.getElementById('tempoSlider').value = currentBPM;
                updateTempoDisplay();
                document.getElementById('meterDisplay').textContent = `${{lesson.meter}} Meter`;
                document.getElementById('ribbonLessonTitle').children[0].textContent = lesson.title;
            }}
            currentStepIndex = 0;
            buildFlatSequence();
            renderTimelineRibbon();
            updateStepDisplay(false);
        }}

        function onHandChange() {{
            currentHand = document.getElementById('handSelector').value;
            buildFlatSequence();
            renderTimelineRibbon();
            updateStepDisplay(false);
        }}

        function onKeyTransposeChange() {{
            currentKeyTranspose = parseInt(document.getElementById('keySelector').value);
            buildFlatSequence();
            renderTimelineRibbon();
            updateStepDisplay(false);
            if (isPadDroneOn) startPadDrone();
        }}

        function onOctaveShiftChange() {{
            currentBaseOctave = parseInt(document.getElementById('octaveSelector').value);
            buildFlatSequence();
            renderTimelineRibbon();
            updateStepDisplay(false);
        }}

        function onVoiceChange() {{
            currentVoice = document.getElementById('voiceSelector').value;
        }}

        function onRhythmStyleChange(style) {{
            currentRhythmStyle = style;
        }}

        // ================= THEORY & VIEWS INITIALIZERS =================
        function renderCircleOfFifthsTable() {{
            const tbody = document.getElementById('circleTableBody');
            if (!tbody) return;
            tbody.innerHTML = '';

            circleOfFifthsData.forEach(item => {{
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td style="font-weight:700; color:var(--gold-bright);">${{item.key}}</td>
                    <td style="font-family:var(--font-mono);">${{item.root}}</td>
                    <td><span class="badge-pill">${{item.accidentals}}</span></td>
                    <td style="color:#a5b4fc;">${{item.relMinor}}</td>
                    <td style="font-family:var(--font-mono); font-size:0.8rem;">${{item.notes.join(' - ')}}</td>
                    <td>
                        <button class="btn-ctrl" style="padding:3px 8px; font-size:0.75rem;" onclick="playScaleNotesDemo(['${{item.notes.join("4','")}}5'], this)">▶️ வாசி</button>
                    </td>
                `;
                tbody.appendChild(tr);
            }});
        }}

        function renderWesternModes() {{
            const container = document.getElementById('modesContainer');
            if (!container) return;
            container.innerHTML = '';

            westernModesData.forEach(m => {{
                const card = document.createElement('div');
                card.className = 'theory-card';
                card.innerHTML = `
                    <h3>${{m.name}}</h3>
                    <p>• <strong>சூத்திரம் (Formula):</strong> ${{m.formula}}<br>
                    • <strong>இடைவெளி அமைப்பு:</strong> ${{m.intervals}}<br>
                    • <strong>C-யில் அமைந்த நோட்டுகள்:</strong> <span style="font-family:var(--font-mono); color:#38bdf8;">${{m.c_notes}}</span><br>
                    • <strong>மனநிலை (Mood):</strong> ${{m.mood}}</p>
                    <button class="btn-ctrl" onclick="playScaleNotesDemo(${{JSON.stringify(m.demo)}}, this)">▶️ மோடு ஸ்கேல் வாசி</button>
                `;
                container.appendChild(card);
            }});
        }}

        function renderWesternIntervals() {{
            const tbody = document.getElementById('intervalsTableBody');
            if (!tbody) return;
            tbody.innerHTML = '';

            westernIntervalsData.forEach(item => {{
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td style="font-family:var(--font-mono); font-weight:700; color:var(--gold-bright);">${{item.semi}}</td>
                    <td style="font-weight:700;">${{item.name}}</td>
                    <td style="color:#cbd5e1;">${{item.nameTa}}</td>
                    <td style="font-family:var(--font-mono); color:#38bdf8;">${{item.ratio}}</td>
                    <td style="color:#a5b4fc;">${{item.example}}</td>
                    <td style="display:flex; gap:6px;">
                        <button class="btn-ctrl" style="padding:2px 8px; font-size:0.72rem;" onclick="playIntervalSound('${{item.notes[0]}}', '${{item.notes[1]}}', false)">ஒன்றாக (Harmonic)</button>
                        <button class="btn-ctrl" style="padding:2px 8px; font-size:0.72rem;" onclick="playIntervalSound('${{item.notes[0]}}', '${{item.notes[1]}}', true)">தொடராக (Melodic)</button>
                    </td>
                `;
                tbody.appendChild(tr);
            }});
        }}

        function renderOctavesAudition() {{
            const container = document.getElementById('octavesContainer');
            if (!container) return;
            container.innerHTML = '';

            westernOctavesData.forEach(oct => {{
                const card = document.createElement('div');
                card.className = 'theory-card';
                const baseMidi = (oct.num + 1) * 12; // C1=24, C2=36, C3=48, C4=60, C5=72, C6=84, C7=96
                card.innerHTML = `
                    <h3>${{oct.name}}</h3>
                    <p>• <strong>மைய அதிர்வெண்:</strong> <span style="font-family:var(--font-mono); color:var(--gold-bright);">${{oct.freq}}</span><br>
                    • ${{oct.desc}}</p>
                    <button class="btn-ctrl" onclick="playOctaveAuditionNote(${{baseMidi}})">🔊 C${{oct.num}} ஒலி கேள்</button>
                `;
                container.appendChild(card);
            }});
        }}

        function playOctaveAuditionNote(midi) {{
            initAudio();
            playMidiNote(midi, 1.2);
            highlightKeyVisual(midi, true);
            setTimeout(() => highlightKeyVisual(midi, false), 1200);
        }}

        function playIntervalSound(note1, note2, isMelodic) {{
            initAudio();
            const p1 = parseWesternNoteToken(note1);
            const p2 = parseWesternNoteToken(note2);
            if (!p1.midi || !p2.midi) return;

            if (isMelodic) {{
                playMidiNote(p1.midi, 0.6);
                highlightKeyVisual(p1.midi, true);
                setTimeout(() => {{
                    highlightKeyVisual(p1.midi, false);
                    playMidiNote(p2.midi, 0.8);
                    highlightKeyVisual(p2.midi, true);
                    setTimeout(() => highlightKeyVisual(p2.midi, false), 800);
                }}, 600);
            }} else {{
                playMidiNote(p1.midi, 1.0);
                playMidiNote(p2.midi, 1.0);
                highlightKeyVisual(p1.midi, true);
                highlightKeyVisual(p2.midi, true);
                setTimeout(() => {{
                    highlightKeyVisual(p1.midi, false);
                    highlightKeyVisual(p2.midi, false);
                }}, 1000);
            }}
        }}

        function playScaleNotesDemo(notesArray, btnEl) {{
            initAudio();
            let idx = 0;
            const timer = setInterval(() => {{
                if (idx >= notesArray.length) {{
                    clearInterval(timer);
                    document.querySelectorAll('.key-white, .key-black').forEach(k => k.classList.remove('active'));
                    return;
                }}
                const parsed = parseWesternNoteToken(notesArray[idx]);
                if (parsed.midi) {{
                    playMidiNote(parsed.midi, 0.35);
                    highlightKeyVisual(parsed.midi, true);
                    setTimeout(() => highlightKeyVisual(parsed.midi, false), 320);
                }}
                idx++;
            }}, 320);
        }}

        // ================= CHORD BUILDER & CHORDS DICTIONARY =================
        function populateChordBuilderSelects() {{
            const rootSel = document.getElementById('chordRootSelect');
            const typeSel = document.getElementById('chordTypeSelect');
            if (!rootSel || !typeSel) return;

            rootSel.innerHTML = '';
            rootNotesData.forEach(r => {{
                const opt = document.createElement('option');
                opt.value = r.semi;
                opt.textContent = r.name;
                rootSel.appendChild(opt);
            }});

            typeSel.innerHTML = '';
            for (const [key, c] of Object.entries(chordTypesData)) {{
                const opt = document.createElement('option');
                opt.value = key;
                opt.textContent = `${{c.name}} (${{c.formula}})`;
                typeSel.appendChild(opt);
            }}

            updateChordBuilder();
        }}

        function updateChordBuilder() {{
            const rootSemi = parseInt(document.getElementById('chordRootSelect').value);
            const chordTypeKey = document.getElementById('chordTypeSelect').value;
            const inv = parseInt(document.getElementById('chordInvSelect').value);

            const cData = chordTypesData[chordTypeKey];
            const rootObj = rootNotesData.find(r => r.semi === rootSemi) || rootNotesData[0];

            let chordMidis = cData.semis.map(s => 60 + rootSemi + s);
            // Apply Inversion
            if (inv === 1 && chordMidis.length > 1) {{
                chordMidis[0] += 12; // Shift lowest note up octave
                chordMidis.sort((a, b) => a - b);
            }} else if (inv === 2 && chordMidis.length > 2) {{
                chordMidis[0] += 12;
                chordMidis[1] += 12;
                chordMidis.sort((a, b) => a - b);
            }}

            const noteNames = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
            const chordNoteNames = chordMidis.map(m => noteNames[m % 12] + (Math.floor(m / 12) - 1));

            const invNames = ['Root Position', '1st Inversion', '2nd Inversion'];
            document.getElementById('chordResultName').textContent = `${{rootObj.name}} ${{cData.name}} • ${{invNames[inv]}}`;
            document.getElementById('chordResultFormula').textContent = `சூத்திரம்: ${{cData.formula}}`;
            document.getElementById('chordResultNotes').textContent = chordNoteNames.join(' - ');
        }}

        function playCurrentBuiltChord(isArpeggio = false) {{
            initAudio();
            const rootSemi = parseInt(document.getElementById('chordRootSelect').value);
            const chordTypeKey = document.getElementById('chordTypeSelect').value;
            const inv = parseInt(document.getElementById('chordInvSelect').value);

            const cData = chordTypesData[chordTypeKey];
            let chordMidis = cData.semis.map(s => 60 + rootSemi + s);

            if (inv === 1 && chordMidis.length > 1) {{
                chordMidis[0] += 12;
                chordMidis.sort((a, b) => a - b);
            }} else if (inv === 2 && chordMidis.length > 2) {{
                chordMidis[0] += 12;
                chordMidis[1] += 12;
                chordMidis.sort((a, b) => a - b);
            }}

            if (isArpeggio) {{
                let i = 0;
                const timer = setInterval(() => {{
                    if (i >= chordMidis.length) {{
                        clearInterval(timer);
                        return;
                    }}
                    playMidiNote(chordMidis[i], 0.6);
                    highlightKeyVisual(chordMidis[i], true);
                    setTimeout(() => highlightKeyVisual(chordMidis[i], false), 500);
                    i++;
                }}, 280);
            }} else {{
                chordMidis.forEach(m => {{
                    playMidiNote(m, 1.2);
                    highlightKeyVisual(m, true);
                    setTimeout(() => highlightKeyVisual(m, false), 1100);
                }});
            }}
        }}

        function playProgressionDemo(chordsList, btnEl) {{
            initAudio();
            let step = 0;
            const timer = setInterval(() => {{
                if (step >= chordsList.length) {{
                    clearInterval(timer);
                    document.querySelectorAll('.key-white, .key-black').forEach(k => k.classList.remove('active'));
                    return;
                }}
                const chordStr = chordsList[step];
                const tokens = chordStr.split(',');
                tokens.forEach(t => {{
                    const parsed = parseWesternNoteToken(t);
                    if (parsed.midi) {{
                        playMidiNote(parsed.midi, 0.9);
                        highlightKeyVisual(parsed.midi, true);
                        setTimeout(() => highlightKeyVisual(parsed.midi, false), 800);
                    }}
                }});
                step++;
            }}, 850);
        }}

        // ================= EAR TRAINING QUIZ ENGINE =================
        function setQuizMode(mode) {{
            quizMode = mode;
            ['btnQuizModeNote', 'btnQuizModeInterval', 'btnQuizModeChord', 'btnQuizModeScale'].forEach(b => {{
                document.getElementById(b).classList.remove('active');
            }});

            if (mode === 'note') document.getElementById('btnQuizModeNote').classList.add('active');
            else if (mode === 'interval') document.getElementById('btnQuizModeInterval').classList.add('active');
            else if (mode === 'chord') document.getElementById('btnQuizModeChord').classList.add('active');
            else if (mode === 'scale') document.getElementById('btnQuizModeScale').classList.add('active');

            generateNewQuizQuestion();
        }}

        function generateNewQuizQuestion() {{
            const grid = document.getElementById('quizOptionsGrid');
            const feedback = document.getElementById('quizFeedback');
            if (!grid) return;
            grid.innerHTML = '';
            feedback.textContent = '';

            if (quizMode === 'note') {{
                document.getElementById('quizPromptText').textContent = 'ஒற்றை நோட்டை கேட்டு சரியான நோட் பெயரைத் தேர்ந்தெடுக்கவும்:';
                const notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'];
                quizSecret = notes[Math.floor(Math.random() * notes.length)];
                notes.forEach(n => {{
                    const btn = document.createElement('button');
                    btn.className = 'btn-ctrl';
                    btn.textContent = n;
                    btn.onclick = () => checkQuizAnswer(n, btn);
                    grid.appendChild(btn);
                }});
            }} else if (quizMode === 'interval') {{
                document.getElementById('quizPromptText').textContent = 'இடைவெளியை கேட்டு சரியான இடைவெளி வகையைத் தேர்ந்தெடுக்கவும்:';
                const intervals = ['Minor 2nd', 'Major 2nd', 'Minor 3rd', 'Major 3rd', 'Perfect 4th', 'Perfect 5th', 'Octave'];
                quizSecret = intervals[Math.floor(Math.random() * intervals.length)];
                intervals.forEach(inv => {{
                    const btn = document.createElement('button');
                    btn.className = 'btn-ctrl';
                    btn.textContent = inv;
                    btn.onclick = () => checkQuizAnswer(inv, btn);
                    grid.appendChild(btn);
                }});
            }} else if (quizMode === 'chord') {{
                document.getElementById('quizPromptText').textContent = 'கார்ட் ஒலியைக் கேட்டு அது Major-ஆ அல்லது Minor-ஆ அல்லது Diminished-ஆ எனக் கூறவும்:';
                const chordQualities = ['Major Triad', 'Minor Triad', 'Diminished Triad'];
                quizSecret = chordQualities[Math.floor(Math.random() * chordQualities.length)];
                chordQualities.forEach(q => {{
                    const btn = document.createElement('button');
                    btn.className = 'btn-ctrl';
                    btn.textContent = q;
                    btn.onclick = () => checkQuizAnswer(q, btn);
                    grid.appendChild(btn);
                }});
            }} else if (quizMode === 'scale') {{
                document.getElementById('quizPromptText').textContent = 'ஸ்கேல் ஒலியைக் கேட்டு அது Major-ஆ அல்லது Minor-ஆ அல்லது Blues-ஆ எனக் கூறவும்:';
                const scales = ['Major Scale', 'Natural Minor', 'Harmonic Minor', 'Blues Scale'];
                quizSecret = scales[Math.floor(Math.random() * scales.length)];
                scales.forEach(s => {{
                    const btn = document.createElement('button');
                    btn.className = 'btn-ctrl';
                    btn.textContent = s;
                    btn.onclick = () => checkQuizAnswer(s, btn);
                    grid.appendChild(btn);
                }});
            }}

            playQuizMysterySound();
        }}

        function playQuizMysterySound() {{
            initAudio();
            if (!quizSecret) return;

            if (quizMode === 'note') {{
                const p = parseWesternNoteToken(quizSecret);
                if (p.midi) playMidiNote(p.midi, 0.9);
            }} else if (quizMode === 'interval') {{
                const map = {{
                    'Minor 2nd': 1, 'Major 2nd': 2, 'Minor 3rd': 3, 'Major 3rd': 4,
                    'Perfect 4th': 5, 'Perfect 5th': 7, 'Octave': 12
                }};
                const semi = map[quizSecret] || 4;
                playMidiNote(60, 0.6);
                setTimeout(() => playMidiNote(60 + semi, 0.8), 500);
            }} else if (quizMode === 'chord') {{
                const rootMidi = 60; // C4
                let chordMidis = [rootMidi, rootMidi + 4, rootMidi + 7];
                if (quizSecret === 'Minor Triad') chordMidis = [rootMidi, rootMidi + 3, rootMidi + 7];
                else if (quizSecret === 'Diminished Triad') chordMidis = [rootMidi, rootMidi + 3, rootMidi + 6];
                chordMidis.forEach(m => playMidiNote(m, 1.2));
            }} else if (quizMode === 'scale') {{
                let semis = [0, 2, 4, 5, 7, 9, 11, 12]; // Major
                if (quizSecret === 'Natural Minor') semis = [0, 2, 3, 5, 7, 8, 10, 12];
                else if (quizSecret === 'Harmonic Minor') semis = [0, 2, 3, 5, 7, 8, 11, 12];
                else if (quizSecret === 'Blues Scale') semis = [0, 3, 5, 6, 7, 10, 12];

                semis.forEach((s, idx) => {{
                    setTimeout(() => playMidiNote(60 + s, 0.3), idx * 260);
                }});
            }}
        }}

        function checkQuizAnswer(selected, btnEl) {{
            const feedback = document.getElementById('quizFeedback');
            if (selected === quizSecret) {{
                feedback.innerHTML = `<span style="color:#10b981;">🎉 மிகச்சரி! (${{quizSecret}}) சரியான விடை!</span>`;
                quizScore += 10;
                quizStreak += 1;
                document.getElementById('quizScore').textContent = quizScore;
                document.getElementById('quizStreak').textContent = `${{quizStreak}} 🔥`;
                setTimeout(() => generateNewQuizQuestion(), 1400);
            }} else {{
                feedback.innerHTML = `<span style="color:#f43f5e;">❌ தவறு! மீண்டும் கேட்டு முயற்சிக்கவும்.</span>`;
                quizStreak = 0;
                document.getElementById('quizStreak').textContent = `0`;
            }}
        }}

        // ================= SIGHT-SINGING & VOCAL AUDIO ENGINES =================
        function playVoiceVocalizerScale(btnEl) {{
            initAudio();
            const notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4'];
            playScaleNotesDemo(notes, btnEl);
        }}

        function playVoiceArpeggioScale(btnEl) {{
            initAudio();
            const notes = ['C4', 'E4', 'G4', 'C5', 'G4', 'E4', 'C4'];
            playScaleNotesDemo(notes, btnEl);
        }}

        function playVoiceSirenGlide(btnEl) {{
            initAudio();
            if (!audioCtx) return;
            const now = audioCtx.currentTime;
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(130, now); // C3
            osc.frequency.exponentialRampToValueAtTime(523, now + 1.8); // Glides to C5
            osc.frequency.exponentialRampToValueAtTime(130, now + 3.6); // Glides back to C3
            gain.gain.setValueAtTime(0.001, now);
            gain.gain.linearRampToValueAtTime(0.4, now + 0.2);
            gain.gain.linearRampToValueAtTime(0.0001, now + 3.8);
            osc.connect(gain);
            gain.connect(masterGainNode);
            osc.start(now);
            osc.stop(now + 3.85);
        }}

        function play5VowelsExercise(btnEl) {{
            initAudio();
            const now = audioCtx.currentTime;
            playMidiNote(60, 5.0); // Sustain Middle C for 5 seconds
        }}

        // ================= LIVE MIC PITCH DETECTION =================
        function toggleMicListening() {{
            if (isMicListening) {{
                stopMicListening();
            }} else {{
                startMicListening();
            }}
        }}

        async function startMicListening() {{
            try {{
                initAudio();
                const stream = await navigator.mediaDevices.getUserMedia({{ audio: true }});
                micStream = stream;
                micSourceNode = audioCtx.createMediaStreamSource(stream);
                micAnalyser = audioCtx.createAnalyser();
                micAnalyser.fftSize = 2048;
                micSourceNode.connect(micAnalyser);

                isMicListening = true;
                document.getElementById('btnMicToggle').classList.add('active');
                document.getElementById('micTunerPanel').style.display = 'flex';
                detectMicPitch();
            }} catch (err) {{
                alert('மைக் அணுகல் மறுக்கப்பட்டது: ' + err.message);
                stopMicListening();
            }}
        }}

        function stopMicListening() {{
            isMicListening = false;
            if (micRafId) cancelAnimationFrame(micRafId);
            if (micStream) micStream.getTracks().forEach(t => t.stop());
            document.getElementById('btnMicToggle').classList.remove('active');
            document.getElementById('micTunerPanel').style.display = 'none';
        }}

        function detectMicPitch() {{
            if (!isMicListening || !micAnalyser) return;
            const buffer = new Float32Array(micAnalyser.fftSize);
            micAnalyser.getFloatTimeDomainData(buffer);

            // Autocorrelation Pitch Detection
            const pitch = autoCorrelate(buffer, audioCtx.sampleRate);
            if (pitch !== -1 && pitch >= 60 && pitch <= 1200) {{
                const midi = 69 + 12 * Math.log2(pitch / 440);
                const roundedMidi = Math.round(midi);
                const cents = Math.round((midi - roundedMidi) * 100);

                const noteNames = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
                const detectedName = noteNames[roundedMidi % 12] + (Math.floor(roundedMidi / 12) - 1);

                document.getElementById('tunerDetectedNote').textContent = detectedName;
                document.getElementById('tunerFrequency').textContent = `${{pitch.toFixed(1)}} Hz`;

                // Needle: -50 cents = 0%, 0 cents = 50%, +50 cents = 100%
                const needlePercent = Math.max(0, Math.min(100, 50 + cents));
                document.getElementById('tunerNeedle').style.left = `${{needlePercent}}%`;

                const statusEl = document.getElementById('tunerStatus');
                if (Math.abs(cents) <= 8) {{
                    statusEl.textContent = '🎯 மிகச்சரியான சுருதி! (In Tune)';
                    statusEl.style.color = '#10b981';
                }} else if (cents < -8) {{
                    statusEl.textContent = `⬇️ சற்று குறைவு (${{cents}} cents Flat)`;
                    statusEl.style.color = '#fbbf24';
                }} else {{
                    statusEl.textContent = `⬆️ சற்று அதிகம் (+${{cents}} cents Sharp)`;
                    statusEl.style.color = '#fbbf24';
                }}

                // Light up detected key on piano
                highlightKeyVisual(roundedMidi, true);
                setTimeout(() => highlightKeyVisual(roundedMidi, false), 150);
            }}

            micRafId = requestAnimationFrame(detectMicPitch);
        }}

        function autoCorrelate(buffer, sampleRate) {{
            let size = buffer.length;
            let rms = 0;
            for (let i = 0; i < size; i++) {{
                rms += buffer[i] * buffer[i];
            }}
            rms = Math.sqrt(rms / size);
            if (rms < 0.015) return -1; // Too quiet

            let r1 = 0, r2 = size - 1, thres = 0.2;
            for (let i = 0; i < size / 2; i++) {{
                if (Math.abs(buffer[i]) < thres) {{ r1 = i; break; }}
            }}
            for (let i = 1; i < size / 2; i++) {{
                if (Math.abs(buffer[size - i]) < thres) {{ r2 = size - i; break; }}
            }}
            const buf = buffer.slice(r1, r2);
            size = buf.length;

            const c = new Float32Array(size);
            for (let i = 0; i < size; i++) {{
                for (let j = 0; j < size - i; j++) {{
                    c[i] = c[i] + buf[j] * buf[j + i];
                }}
            }}

            let d = 0;
            while (c[d] > c[d + 1]) d++;
            let maxval = -1, maxpos = -1;
            for (let i = d; i < size; i++) {{
                if (c[i] > maxval) {{
                    maxval = c[i];
                    maxpos = i;
                }}
            }}
            let T0 = maxpos;
            return sampleRate / T0;
        }}

        // ================= AUDIO RECORDER =================
        async function toggleAudioRecorder() {{
            if (isRecording) {{
                stopAndDownloadRecording();
            }} else {{
                startAudioRecording();
            }}
        }}

        async function startAudioRecording() {{
            try {{
                initAudio();
                const dest = audioCtx.createMediaStreamDestination();
                masterGainNode.connect(dest);

                mediaRecorder = new MediaRecorder(dest.stream);
                recordedAudioChunks = [];

                mediaRecorder.ondataavailable = (e) => {{
                    if (e.data.size > 0) recordedAudioChunks.push(e.data);
                }};

                mediaRecorder.start();
                isRecording = true;
                recordStartTime = Date.now();
                document.getElementById('recordingBar').style.display = 'flex';
                document.getElementById('recordStatusLabel').textContent = '⏹️ பதிவை நிறுத்து';

                recordTimerInterval = setInterval(() => {{
                    const elapsedSec = Math.floor((Date.now() - recordStartTime) / 1000);
                    const mins = String(Math.floor(elapsedSec / 60)).padStart(2, '0');
                    const secs = String(elapsedSec % 60).padStart(2, '0');
                    document.getElementById('recordingTimer').textContent = `${{mins}}:${{secs}}`;
                }}, 1000);
            }} catch (err) {{
                alert('பதிவு செய்வதில் பிழை: ' + err.message);
            }}
        }}

        function stopAndDownloadRecording() {{
            if (!isRecording || !mediaRecorder) return;
            mediaRecorder.stop();
            isRecording = false;
            clearInterval(recordTimerInterval);
            document.getElementById('recordingBar').style.display = 'none';
            document.getElementById('recordStatusLabel').textContent = '⏺️ பதிவு செய் (Record)';

            mediaRecorder.onstop = () => {{
                const blob = new Blob(recordedAudioChunks, {{ type: 'audio/webm' }});
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                a.download = `Western_Piano_Practice_${{Date.now()}}.webm`;
                document.body.appendChild(a);
                a.click();
                setTimeout(() => {{
                    document.body.removeChild(a);
                    window.URL.revokeObjectURL(url);
                }}, 200);
            }};
        }}

        // ================= WEB MIDI CONTROLLER =================
        function setupWebMidi() {{
            if (navigator.requestMIDIAccess) {{
                navigator.requestMIDIAccess().then(onMidiSuccess, onMidiFailure);
            }}
        }}

        function onMidiSuccess(midiAccess) {{
            for (let input of midiAccess.inputs.values()) {{
                input.onmidimessage = handleMidiMessage;
            }}
            midiAccess.onstatechange = (e) => {{
                if (e.port.type === 'input' && e.port.state === 'connected') {{
                    e.port.onmidimessage = handleMidiMessage;
                }}
            }};
        }}

        function onMidiFailure() {{
            console.log('Web MIDI access unavailable or declined.');
        }}

        function handleMidiMessage(msg) {{
            const [status, note, velocity] = msg.data;
            const command = status >> 4;
            if (command === 9 && velocity > 0) {{
                // Note On
                onKeyPointerDown(note);
            }} else if (command === 8 || (command === 9 && velocity === 0)) {{
                // Note Off
                onKeyPointerUp(note);
            }}
        }}

        // ================= COMPUTER KEYBOARD SHORTCUTS =================
        window.addEventListener('keydown', (e) => {{
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;

            if (e.code === 'Space') {{
                e.preventDefault();
                togglePlayPause();
            }} else if (e.code === 'ArrowRight') {{
                e.preventDefault();
                stepForward();
            }} else if (e.code === 'ArrowLeft') {{
                e.preventDefault();
                stepBackward();
            }} else if (e.key === 'l' || e.key === 'L') {{
                toggleLoop();
            }} else if (e.key === '[') {{
                const octSel = document.getElementById('octaveSelector');
                if (octSel.selectedIndex > 0) {{
                    octSel.selectedIndex--;
                    onOctaveShiftChange();
                }}
            }} else if (e.key === ']') {{
                const octSel = document.getElementById('octaveSelector');
                if (octSel.selectedIndex < octSel.options.length - 1) {{
                    octSel.selectedIndex++;
                    onOctaveShiftChange();
                }}
            }} else if (e.key === '?' || e.key === '/') {{
                openHelpModal();
            }} else if (e.key === 'Escape') {{
                closeHelpModal();
                closeDiagramLightbox();
                closeKeyboardLightbox();
                closeNotationLightbox();
            }} else {{
                const char = e.key.toLowerCase();
                if (computerKeyMap[char] !== undefined) {{
                    const midi = computerKeyMap[char] + currentKeyTranspose + (currentBaseOctave * 12);
                    onKeyPointerDown(midi);
                }}
            }}
        }});

        window.addEventListener('keyup', (e) => {{
            const char = e.key.toLowerCase();
            if (computerKeyMap[char] !== undefined) {{
                const midi = computerKeyMap[char] + currentKeyTranspose + (currentBaseOctave * 12);
                onKeyPointerUp(midi);
            }}
        }});

        // ================= VIEW SWITCHER & MODALS =================
        function switchView(viewName) {{
            currentView = viewName;
            document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));
            document.querySelectorAll('.nav-tab-btn').forEach(b => b.classList.remove('active'));

            const viewMap = {{
                'studio': 'viewStudio',
                'voice_training': 'viewVoiceTraining',
                'sthayi_theory': 'viewSthayiTheory',
                'melakarta': 'viewMelakarta',
                'janya': 'viewJanyaRagas',
                'ear_training': 'viewEarTraining',
                'swaras': 'viewSwaras',
                'psr_guide': 'viewPsrGuide',
                'diagrams': 'viewDiagrams'
            }};

            const targetId = viewMap[viewName] || 'viewStudio';
            const targetEl = document.getElementById(targetId);
            if (targetEl) targetEl.classList.add('active');

            // Set tab active
            const buttons = document.querySelectorAll('.nav-tab-btn');
            buttons.forEach(b => {{
                if (b.getAttribute('onclick') && b.getAttribute('onclick').includes(viewName)) {{
                    b.classList.add('active');
                }}
            }});

            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function fixDiagramPaths() {{
            const isSubDir = window.location.pathname.includes('/html/keyboard/');
            const basePath = isSubDir ? '../../diagrams/keyboard/' : 'diagrams/keyboard/';
            document.querySelectorAll('.diagram-card img').forEach(img => {{
                const src = img.getAttribute('src');
                if (src && !src.startsWith('http') && !src.startsWith('../')) {{
                    const fileName = src.split('/').pop();
                    img.src = basePath + fileName;
                }}
            }});
        }}

        function openDiagramLightbox(svgPath, title) {{
            const isSubDir = window.location.pathname.includes('/html/keyboard/');
            const basePath = isSubDir ? '../../diagrams/keyboard/' : 'diagrams/keyboard/';
            const fileName = svgPath.split('/').pop();
            const resolvedPath = basePath + fileName;

            document.getElementById('lightboxTitle').textContent = title;
            document.getElementById('lightboxImg').src = resolvedPath;
            document.getElementById('lightboxDownloadBtn').href = resolvedPath;
            document.getElementById('diagramLightboxModal').classList.add('active');
        }}

        function closeDiagramLightbox(e) {{
            if (!e || e.target.id === 'diagramLightboxModal' || e.target.classList.contains('btn-close-modal')) {{
                document.getElementById('diagramLightboxModal').classList.remove('active');
            }}
        }}

        function openHelpModal() {{
            document.getElementById('helpModal').classList.add('active');
        }}

        function closeHelpModal(e) {{
            if (!e || e.target.id === 'helpModal' || e.target.classList.contains('btn-close-modal')) {{
                document.getElementById('helpModal').classList.remove('active');
            }}
        }}

        function toggleKeyboardZoom() {{
            isZoomMode = !isZoomMode;
            render61KeyPiano();
            setTimeout(() => centerMiddleC(true), 60);
        }}

        function openKeyboardLightbox() {{
            const dock = document.querySelector('.piano-wrapper');
            const controls = document.querySelector('.controls-deck');
            const content = document.getElementById('keyboardLightboxContent');
            const lightbox = document.getElementById('keyboardLightbox');
            if (!dock || !content || !lightbox) return;

            if (controls) content.appendChild(controls);
            content.appendChild(dock);
            lightbox.classList.add('active');
            setTimeout(() => centerMiddleC(false), 80);
        }}

        function closeKeyboardLightbox(e) {{
            const lightbox = document.getElementById('keyboardLightbox');
            if (!lightbox || !lightbox.classList.contains('active')) return;
            if (e && e.target !== lightbox && !e.target.closest('.btn-close-modal')) return;

            const dock = lightbox.querySelector('.piano-wrapper');
            const controls = lightbox.querySelector('.controls-deck');
            const pianoAnchor = document.getElementById('pianoAnchor');
            const controlsAnchor = document.getElementById('controlsAnchor');

            if (controls && controlsAnchor) controlsAnchor.after(controls);
            if (dock && pianoAnchor) pianoAnchor.after(dock);

            lightbox.classList.remove('active');
            setTimeout(() => centerMiddleC(false), 80);
        }}

        function openNotationLightbox() {{
            const ribbon = document.querySelector('.notation-ribbon-card');
            const controls = document.querySelector('.controls-deck');
            const content = document.getElementById('notationLightboxContent');
            const lightbox = document.getElementById('notationLightbox');
            if (!ribbon || !content || !lightbox) return;

            if (controls) content.appendChild(controls);
            content.appendChild(ribbon);
            lightbox.classList.add('active');
        }}

        function closeNotationLightbox(e) {{
            const lightbox = document.getElementById('notationLightbox');
            if (!lightbox || !lightbox.classList.contains('active')) return;
            if (e && e.target !== lightbox && !e.target.closest('.btn-close-modal')) return;

            const ribbon = lightbox.querySelector('.notation-ribbon-card');
            const controls = lightbox.querySelector('.controls-deck');
            const notationAnchor = document.getElementById('notationAnchor');
            const controlsAnchor = document.getElementById('controlsAnchor');

            if (controls && controlsAnchor) controlsAnchor.after(controls);
            if (ribbon && notationAnchor) notationAnchor.after(ribbon);

            lightbox.classList.remove('active');
        }}

        function updateGrandStaffVisual(cur) {{
            const svgEl = document.getElementById('liveStaffSvg');
            const pitchLabel = document.getElementById('staffPitchLabel');
            const detailLabel = document.getElementById('staffDetailLabel');
            const handLabel = document.getElementById('staffHandLabel');
            const clefDetail = document.getElementById('staffClefDetail');
            if (!svgEl) return;

            const bgAndLines = `
                <rect width="340" height="120" rx="6" fill="rgba(8, 12, 24, 0.6)"/>
                <line x1="10" y1="20" x2="10" y2="100" stroke="rgba(212, 175, 55, 0.7)" stroke-width="2"/>
                <line x1="330" y1="20" x2="330" y2="100" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
                <line x1="10" y1="20" x2="330" y2="20" stroke="rgba(255,255,255,0.22)" stroke-width="1"/>
                <line x1="10" y1="28" x2="330" y2="28" stroke="rgba(255,255,255,0.22)" stroke-width="1"/>
                <line x1="10" y1="36" x2="330" y2="36" stroke="rgba(255,255,255,0.22)" stroke-width="1"/>
                <line x1="10" y1="44" x2="330" y2="44" stroke="rgba(255,255,255,0.22)" stroke-width="1"/>
                <line x1="10" y1="52" x2="330" y2="52" stroke="rgba(255,255,255,0.22)" stroke-width="1"/>
                <line x1="10" y1="68" x2="330" y2="68" stroke="rgba(255,255,255,0.22)" stroke-width="1"/>
                <line x1="10" y1="76" x2="330" y2="76" stroke="rgba(255,255,255,0.22)" stroke-width="1"/>
                <line x1="10" y1="84" x2="330" y2="84" stroke="rgba(255,255,255,0.22)" stroke-width="1"/>
                <line x1="10" y1="92" x2="330" y2="92" stroke="rgba(255,255,255,0.22)" stroke-width="1"/>
                <line x1="10" y1="100" x2="330" y2="100" stroke="rgba(255,255,255,0.22)" stroke-width="1"/>
                <text x="14" y="47" font-size="34" fill="#fbbf24" opacity="0.9">𝄞</text>
                <text x="14" y="89" font-size="28" fill="#06b6d4" opacity="0.9">𝄢</text>
            `;

            if (!cur || cur.isRest || !cur.noteName || cur.noteName === ',' || cur.noteName === ';') {{
                if (pitchLabel) pitchLabel.textContent = 'இடைவேளை (Rest • 𝄽)';
                if (detailLabel) detailLabel.textContent = 'Silence / Rest';
                if (handLabel) handLabel.textContent = '—';
                if (clefDetail) clefDetail.textContent = '—';
                svgEl.innerHTML = bgAndLines + `
                    <text x="175" y="66" font-size="24" fill="#94a3b8" text-anchor="middle">𝄽</text>
                    <text x="175" y="86" font-size="10" fill="#64748b" text-anchor="middle">Quarter Rest</text>
                `;
                return;
            }}

            const noteName = cur.noteName;
            const letter = noteName[0].toUpperCase();
            const acc = noteName.includes('#') ? '#' : (noteName.includes('b') ? 'b' : '');
            const octave = parseInt(noteName.slice(-1)) || 4;
            const noteSteps = {{ 'C': 0, 'D': 1, 'E': 2, 'F': 3, 'G': 4, 'A': 5, 'B': 6 }};
            const step = (noteSteps[letter] !== undefined ? noteSteps[letter] : 0) + (octave - 4) * 7;
            const y = 60 - (step * 4);

            const isTreble = octave >= 4;
            if (handLabel) {{
                handLabel.textContent = isTreble ? 'வலது கை (RH 𝄞)' : 'இடது கை (LH 𝄢)';
                handLabel.style.color = isTreble ? '#10b981' : '#38bdf8';
            }}
            if (clefDetail) clefDetail.textContent = isTreble ? 'Treble Clef (G-Clef)' : 'Bass Clef (F-Clef)';
            if (pitchLabel) pitchLabel.textContent = `${{cur.clef || (isTreble ? '𝄞 Treble' : '𝄢 Bass')}} • ${{noteName}} (${{cur.solfege || ''}})`;

            let detailStr = '';
            if (noteName === 'C4') detailStr = 'Middle C (மைய C) • Ledger Line';
            else if (y <= 52 && y >= 20) detailStr = 'Treble Staff (Line/Space)';
            else if (y <= 100 && y >= 68) detailStr = 'Bass Staff (Line/Space)';
            else if (y < 20) detailStr = 'Treble Upper Ledger Line';
            else if (y > 100) detailStr = 'Bass Lower Ledger Line';
            else detailStr = 'Between Clefs';
            if (detailLabel) detailLabel.textContent = detailStr;

            let extraSvg = '';
            if (y === 60) extraSvg += '<line x1="166" y1="60" x2="194" y2="60" stroke="#fbbf24" stroke-width="1.8"/>';
            if (y <= 12) extraSvg += '<line x1="166" y1="12" x2="194" y2="12" stroke="#fbbf24" stroke-width="1.8"/>';
            if (y <= 4) extraSvg += '<line x1="166" y1="4" x2="194" y2="4" stroke="#fbbf24" stroke-width="1.8"/>';
            if (y >= 108) extraSvg += '<line x1="166" y1="108" x2="194" y2="108" stroke="#fbbf24" stroke-width="1.8"/>';
            if (y >= 116) extraSvg += '<line x1="166" y1="116" x2="194" y2="116" stroke="#fbbf24" stroke-width="1.8"/>';

            if (acc === '#') {{
                extraSvg += `<text x="162" y="${{y + 5}}" font-size="16" fill="#fbbf24" font-weight="bold" text-anchor="end">♯</text>`;
            }} else if (acc === 'b') {{
                extraSvg += `<text x="162" y="${{y + 4}}" font-size="16" fill="#fbbf24" font-weight="bold" text-anchor="end">♭</text>`;
            }}

            extraSvg += `<ellipse cx="180" cy="${{y}}" rx="6.5" ry="5" transform="rotate(-20 180 ${{y}})" fill="#fbbf24" stroke="#d4af37" stroke-width="1.5"/>`;

            if (y >= 60) {{
                extraSvg += `<line x1="185.5" y1="${{y}}" x2="185.5" y2="${{y - 24}}" stroke="#fbbf24" stroke-width="1.8"/>`;
            }} else {{
                extraSvg += `<line x1="174.5" y1="${{y}}" x2="174.5" y2="${{y + 24}}" stroke="#fbbf24" stroke-width="1.8"/>`;
            }}

            const solf = cur.solfege ? ` (${{cur.solfege}})` : '';
            extraSvg += `<text x="202" y="${{y + 4}}" font-size="12" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-weight="700">${{noteName}}${{solf}}</text>`;

            svgEl.innerHTML = bgAndLines + extraSvg;
        }}

        // ================= APP INITIALIZATION =================
        window.addEventListener('DOMContentLoaded', () => {{
            updateTempoDisplay();
            populateLessonDropdown('hanon');
            render61KeyPiano();
            buildFlatSequence();
            renderTimelineRibbon();
            updateStepDisplay(false);

            renderCircleOfFifthsTable();
            renderWesternModes();
            renderWesternIntervals();
            renderOctavesAudition();
            populateChordBuilderSelects();
            setQuizMode('note');
            setupWebMidi();
            fixDiagramPaths();

            setTimeout(() => centerMiddleC(false), 150);
        }});
    </script>
</body>

</html>
'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Successfully wrote index.html!")

    # Also update tutor.html files
    os.makedirs(os.path.join("html", "keyboard"), exist_ok=True)
    tutor_path = os.path.join("html", "keyboard", "carnatic_keyboard_master_visual_tutor.html")
    western_tutor_path = os.path.join("html", "keyboard", "western_keyboard_master_visual_tutor.html")

    shutil.copyfile("index.html", tutor_path)
    shutil.copyfile("index.html", western_tutor_path)
    print(f"Synced to {tutor_path} and {western_tutor_path}!")

if __name__ == "__main__":
    build_html()
