# Show Last Review Time Overlay for Anki

This Anki add-on enhances your study sessions by displaying the last review time of the current card overlaid on the reviewer's window. It shows the time in a human-readable format (e.g., '4 days ago'), making it easier to keep track of your review intervals at a glance.

## Features

- **Customizable Display**: Configurable font, size, and color to match your Anki theme.
- **Flexible Positioning**: Choose to display the overlay in the corners of the reviewer window: bottom-left, bottom-right, top-left, or top-right.
- **Human-readable Time Format**: Converts the last review time into a relative format like 'minutes ago', 'days ago', etc.

## Installation

1. Download the latest release from the [Releases](https://github.com/your-github-username/anki-last-review-overlay/releases) page.
2. In Anki, go to `Tools` -> `Add-ons` -> `Install from file...` and select the downloaded file.

## Configuration

After installation, you can customize the add-on by going to `Tools` -> `Add-ons`, selecting "Show Last Review Time Overlay", and clicking on `Config`. The following options are available:

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

Both authors have collaborated to bring this Anki add-on to life, enhancing the user experience by adding a useful overlay that displays the last review time of Anki cards.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
