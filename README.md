# Show Last Review Time Overlay for Anki

This Anki add-on displays the last review time of the current card overlaid on the review window. It shows the time (e.g., '4 days ago') when it was last reviewed, making it easier to keep track of your review intervals at a glance.

## Features

- **Customizable Display**: Configurable font, size, and color to match your Anki theme.
- **Flexible Positioning**: Choose to display the overlay in the corners of the reviewer window: bottom-left, bottom-right, top-left, or top-right.
- **Human-readable Time Format**: Converts the last review time into a relative format like 'minutes ago', 'days ago', etc.

## Installation

1. Download the latest release from the [Releases]([https://github.com/your-github-username/anki-last-review-overlay/releases](https://github.com/CrudeArc/Last-Reviewed)) page.
2. Extract the file
3. Paste it in the Anki2/addons21/ directory (should be something like /home/user/.local/share/Anki2/addons21/ if you're on linux) alongside the other addons
4. If it went well, in anki Tools > addons you should see the addon appear

## Configuration

After installation, you can customize the add-on by going to `Tools` -> `Add-ons`, selecting "Last Reviewed", and clicking on `Config`. The following options are available:

- `font_family`: Sets the font family. Default is `"Orbitron, Roboto, Futura, Helvetica Neue, Arial, sans-serif"`.
- `font_size`: Sets the font size. Default is `13`.
- `color`: Sets the color of the text. Default is `"#0ad5e4"`.
- `position`: Sets the position of the overlay. Options are `"bottom-left"`, `"bottom-right"`, `"top-left"`, `"top-right"`. Default is `"bottom-left"`.

## Usage

Once installed, the add-on automatically overlays the last review time on the Anki reviewer window. The overlay updates dynamically:

- It displays the last review time when answering a card.
- It hides when viewing the question to avoid distractions.
- It repositions dynamically if the Anki window is resized.

## Support

If you encounter any issues or have suggestions for improvements, please file an issue on the [GitHub issues page](https://github.com/your-github-username/anki-last-review-overlay/issues).

## Contributing

Contributions to "Show Last Review Time Overlay" are welcome! Please review the [contributing guidelines](CONTRIBUTING.md) before making a pull request.

## Authors

- **PaceBar**
- **Ouranos**


