# 🎫 Ticket Generator

A Python-based desktop application that generates custom tickets with QR codes and unique IDs. Perfect for events, conferences, or any scenario requiring numbered tickets with scannable QR codes.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- **Batch Generation**: Create multiple tickets at once with sequential numbering
- **QR Code Integration**: Each ticket includes a unique QR code with transparent background
- **Custom Prefix**: Personalize tickets with your own prefix (e.g., "SOV-001", "EVENT-001")
- **Professional Templates**: Uses a template image for consistent branding
- **CSV Logging**: Automatically logs all generated tickets with timestamps
- **User-Friendly GUI**: Simple Tkinter interface for easy operation
- **Progress Tracking**: Real-time progress bar during generation

## 🚀 How It Works

### Overview

The application takes a template image and overlays two key elements:
1. **QR Code**: Generated dynamically with a transparent background, positioned at the top-right
2. **Ticket ID**: Text overlay showing the unique ticket identifier

### Process Flow

1. **User Input**: Enter a prefix (e.g., "SOV-") and number range (start to end)
2. **QR Generation**: Creates a QR code linking to a Google search of the ticket ID
3. **Image Composition**: Overlays the QR code and ticket ID onto the template
4. **Export**: Saves each ticket as a PNG file in the `tickets/` directory
5. **Logging**: Records ticket details (ID, prefix, number, timestamp) in `tickets_log.csv`

### Technical Details

- **QR Code**: Generated with high error correction, transparent white background
- **Font**: Uses Arial Bold (28pt) for ticket ID display
- **Image Processing**: PIL/Pillow library handles all image operations
- **Template**: Base design loaded from `template.png`
- **Output**: RGB PNG images saved with naming format `ticket_[ID].png`

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/farhaan-arshad/ticket-generator-.git
   cd ticket-generator-
   ```

2. **Install required packages**:
   ```bash
   pip install qrcode[pil] pillow
   ```

   Or install individually:
   ```bash
   pip install qrcode
   pip install pillow
   ```

3. **Verify file structure**:
   ```
   ticket-generator/
   ├── app.py              # Main application
   ├── template.png        # Ticket template image
   ├── fonts/
   │   └── ARIALBD.ttf    # Arial Bold font
   └── tickets/           # Output directory (auto-created)
   ```

## 🎮 Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Configure ticket generation**:
   - **Ticket Prefix**: Enter your desired prefix (default: "SOV-")
   - **Start Number**: First ticket number in the sequence
   - **End Number**: Last ticket number in the sequence

3. **Generate tickets**:
   - Click "Generate Tickets" button
   - Watch the progress bar as tickets are created
   - View generated tickets in the `tickets/` folder

### Example

To generate tickets SOV-001 through SOV-050:
- Prefix: `SOV-`
- Start Number: `1`
- End Number: `50`

Result: 50 tickets named `ticket_SOV-1.png` through `ticket_SOV-50.png`

## 📁 Output

### Generated Files

- **Tickets**: Saved in `tickets/` directory as PNG images
- **Log File**: `tickets_log.csv` contains:
  - `ticket_id`: Full ticket identifier
  - `prefix`: The prefix used
  - `number`: The sequential number
  - `generated_at`: Timestamp of generation

### Sample CSV Log
```csv
ticket_id,prefix,number,generated_at
SOV-1,SOV-,1,2026-01-16 14:30:45
SOV-2,SOV-,2,2026-01-16 14:30:46
SOV-3,SOV-,3,2026-01-16 14:30:47
```

## ⚙️ Configuration

Edit these constants in `app.py` to customize:

```python
TEMPLATE_PATH = "template.png"    # Your template image
FONT_PATH = "fonts/ARIALBD.ttf"   # Font file path
OUTPUT_DIR = "tickets"             # Output directory
CSV_FILE = "tickets_log.csv"       # Log file name

QR_SIZE = 200                      # QR code dimensions (pixels)
QR_X = 1180                        # QR code X position
QR_Y = 155                         # QR code Y position
ID_X = 1200                        # Ticket ID X position
ID_Y = 510                         # Ticket ID Y position
```

## 🎨 Customization

### Template Image

Replace `template.png` with your own design. Recommended specifications:
- Format: PNG
- Resolution: High resolution for print quality
- Layout: Reserve space for QR code (top-right) and ticket ID

### QR Code Content

Modify line 46 in `app.py` to change QR code destination:
```python
qr_gen.add_data(f"https://www.google.com/search?q={ticket_id}")
```

### Font Style

Replace `ARIALBD.ttf` in the `fonts/` directory with any TrueType font (.ttf)

## 🐛 Troubleshooting

**Font not loading**:
- Ensure `fonts/ARIALBD.ttf` exists
- Falls back to default font if custom font fails

**Template not found**:
- Verify `template.png` is in the root directory
- Check file name spelling and case sensitivity

**QR codes not transparent**:
- White background is automatically converted to transparent
- Ensure template has appropriate background for overlay

## 📦 Dependencies

- **qrcode**: QR code generation
- **Pillow (PIL)**: Image processing and manipulation
- **tkinter**: GUI framework (included with Python)
- **csv**: Logging (standard library)
- **datetime**: Timestamps (standard library)
- **os**: File operations (standard library)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Farhaan Arshad**
- GitHub: [@farhaan-arshad](https://github.com/farhaan-arshad)

## 🙏 Acknowledgments

- QR code generation powered by [qrcode](https://pypi.org/project/qrcode/)
- Image processing by [Pillow](https://python-pillow.org/)

---

Made with ❤️ for event organizers and ticket management
