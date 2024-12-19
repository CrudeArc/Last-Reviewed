# -*- coding: utf-8 -*-
# Anki Add-On: Show Last Review Time Overlay

"""
Anki Add-On: Show Last Review Time Overlay

Displays the last review time of the current card overlaid on the reviewer's window
as 'LR: X', where X is a relative time (e.g., '4 days ago').

Author: PaceBar
"""

import os
import time
from aqt import mw
from aqt.qt import QLabel, QFontDatabase, QFont
from anki.hooks import addHook

# Default configuration
default_config = {
    "font_family": "Orbitron, Roboto, Futura, Helvetica Neue, Arial, sans-serif",
    "font_size": 13,
    "color": "#0ad5e4",
    "position": "bottom-left"  # Options: 'bottom-left', 'bottom-right', 'top-left', 'top-right'
}

# Load user configuration and merge with defaults
user_config = mw.addonManager.getConfig(__name__) or {}
config = {**default_config, **user_config}

def human_readable_time(delta_seconds):
    intervals = (
        ('year', 31536000),   # 60 * 60 * 24 * 365
        ('month', 2592000),   # 60 * 60 * 24 * 30
        ('week', 604800),     # 60 * 60 * 24 * 7
        ('day', 86400),       # 60 * 60 * 24
        ('hour', 3600),       # 60 * 60
        ('minute', 60),
        ('second', 1),
    )

    for name, count in intervals:
        value = delta_seconds // count
        if value >= 1:
            return f"{int(value)} {name}{'s' if value > 1 else ''} ago"
    return "just now"

def update_overlay():
    reviewer = mw.reviewer
    if not reviewer or not reviewer.card:
        return

    card = reviewer.card
    col = mw.col
    card_id = card.id

    # Get the last review timestamp excluding the current one
    last_review = col.db.scalar(
        "SELECT max(id) FROM revlog WHERE cid = ? AND id < ?", card_id, int(time.time() * 1000)
    )

    if last_review:
        last_review_time = last_review / 1000  # Convert to seconds
        current_time = time.time()
        delta_seconds = current_time - last_review_time
        relative_time = human_readable_time(delta_seconds)
        lr_text = f"LR: {relative_time}"
    else:
        lr_text = "LR: N/A"

    # Load the Orbitron font if not already loaded
    if not hasattr(reviewer, 'orbitron_font_loaded'):
        font_path = os.path.join(os.path.dirname(__file__), 'font', 'Orbitron-Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Failed to load Orbitron font.")
        else:
            reviewer.orbitron_font_loaded = True

    # Create or update the overlay label
    if not hasattr(reviewer, 'lr_label'):
        # Create the label with mw as parent
        reviewer.lr_label = QLabel(mw)
        
        # Set the style sheet with user-configurable properties
        reviewer.lr_label.setStyleSheet(f"""
           QLabel {{
                font-size: {config['font_size']}px;
                color: {config['color']};
                font-family: {config['font_family']};
                font-weight: 300;
                }}
        """)

        # Set the font
        font = QFont()
        font.setFamily(config['font_family'])
        font.setPointSize(config['font_size'])
        reviewer.lr_label.setFont(font)
    else:
        # Update the style sheet in case the config has changed
        reviewer.lr_label.setStyleSheet(f"""
           QLabel {{
                font-size: {config['font_size']}px;
                color: {config['color']};
                font-family: {config['font_family']};
                font-weight: 300;
                }}
        """)

        # Update the font
        font = QFont()
        font.setFamily(config['font_family'])
        font.setPointSize(config['font_size'])
        reviewer.lr_label.setFont(font)

    # Update the label text and position
    reviewer.lr_label.setText(lr_text)
    reviewer.lr_label.adjustSize()
    position_overlay_label()
    reviewer.lr_label.show()

def position_overlay_label():
    reviewer = mw.reviewer
    if hasattr(reviewer, 'lr_label'):
        label = reviewer.lr_label
        x_margin = 10  # Distance from the edge
        y_margin = 50  # Distance from the edge

        if config['position'] == 'bottom-left':
            x = x_margin
            y = mw.height() - label.height() - y_margin
        elif config['position'] == 'bottom-right':
            x = mw.width() - label.width() - x_margin
            y = mw.height() - label.height() - y_margin
        elif config['position'] == 'top-left':
            x = x_margin
            y = y_margin
        elif config['position'] == 'top-right':
            x = mw.width() - label.width() - x_margin
            y = y_margin
        else:
            # Default to bottom-left if invalid position
            x = x_margin
            y = mw.height() - label.height() - y_margin

        label.move(x, y)

def on_reviewer_resize():
    # Adjust the position when the main window is resized
    reviewer = mw.reviewer
    if hasattr(reviewer, 'lr_label') and reviewer.lr_label.isVisible():
        position_overlay_label()

def on_show_answer():
    update_overlay()

def on_show_question():
    reviewer = mw.reviewer
    if hasattr(reviewer, 'lr_label') and reviewer.lr_label.isVisible():
        reviewer.lr_label.hide()

def hide_overlay_label():
    reviewer = mw.reviewer
    if hasattr(reviewer, 'lr_label') and reviewer.lr_label.isVisible():
        reviewer.lr_label.hide()

def init_addon():
    # Connect hooks
    addHook('showAnswer', on_show_answer)
    addHook('showQuestion', on_show_question)
    addHook('resize', on_reviewer_resize)

    # Hide the overlay when leaving the reviewer
    addHook('deckBrowserWillShow', hide_overlay_label)
    addHook('overviewWillShow', hide_overlay_label)
    addHook('reviewCleanup', hide_overlay_label)

# Run the initialization
init_addon()
