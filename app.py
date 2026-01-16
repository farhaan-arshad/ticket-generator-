import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# ================= CONFIG =================

TEMPLATE_PATH = "template.png"
FONT_PATH = "fonts/ARIALBD.ttf"
OUTPUT_DIR = "tickets"
CSV_FILE = "tickets_log.csv"

QR_SIZE = 200

QR_X = 1180
QR_Y = 155

ID_X = 1200
ID_Y = 510

# ==========================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Create CSV if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ticket_id", "prefix", "number", "generated_at"])

def generate_ticket(prefix, number):
    ticket_id = f"{prefix}{number}"

    # Generate QR code with transparent background
    qr_gen = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr_gen.add_data(f"https://www.google.com/search?q={ticket_id}")
    qr_gen.make(fit=True)
    
    # Create QR image with black and white
    qr = qr_gen.make_image(fill_color="black", back_color="white")
    qr = qr.convert("RGBA")
    
    # Make white pixels transparent
    qr_data = qr.getdata()
    new_data = []
    for item in qr_data:
        # If pixel is white (or close to white), make it transparent
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))  # Transparent
        else:
            new_data.append(item)  # Keep black pixels
    
    qr.putdata(new_data)
    qr = qr.resize((QR_SIZE, QR_SIZE), Image.Resampling.LANCZOS)

    img = Image.open(TEMPLATE_PATH).convert("RGBA")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(FONT_PATH, 28)
    except OSError:
        font = ImageFont.load_default()

    draw.text((ID_X, ID_Y), ticket_id, font=font, fill="white")
    img.paste(qr, (QR_X, QR_Y), qr)  # Use QR as mask for transparency

    # Convert back to RGB for saving as PNG
    img = img.convert("RGB")
    img.save(f"{OUTPUT_DIR}/ticket_{ticket_id}.png")

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            ticket_id,
            prefix,
            number,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])

def run_generation():
    try:
        prefix = prefix_entry.get().strip()
        start = int(start_entry.get())
        end = int(end_entry.get())

        if not prefix:
            messagebox.showerror("Error", "Prefix cannot be empty")
            return

        if start > end:
            messagebox.showerror("Error", "Start number must be ≤ End number")
            return

        total = end - start + 1
        progress["maximum"] = total
        progress["value"] = 0

        for i, num in enumerate(range(start, end + 1), start=1):
            generate_ticket(prefix, num)
            progress["value"] = i
            status_label.config(text=f"Generating {prefix}{num}")
            root.update_idletasks()

        status_label.config(text="✅ Done")
        messagebox.showinfo(
            "Success",
            f"Tickets generated:\n{prefix}{start} → {prefix}{end}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# ================= GUI =================

root = tk.Tk()
root.title("Ticket Generator")
root.geometry("480x380")
root.resizable(False, False)

tk.Label(
    root,
    text= "Ticket Generator",
    font=("Arial", 15, "bold")
).pack(pady=15)

frame = tk.Frame(root)
frame.pack(pady=10)

# Prefix
tk.Label(frame, text="Ticket Prefix:").grid(row=0, column=0, padx=10, pady=8, sticky="e")
prefix_entry = tk.Entry(frame, width=20)
prefix_entry.insert(0, "SOV-")
prefix_entry.grid(row=0, column=1)

# Start
tk.Label(frame, text="Start Number:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
start_entry = tk.Entry(frame, width=20)
start_entry.grid(row=1, column=1)

# End
tk.Label(frame, text="End Number:").grid(row=2, column=0, padx=10, pady=8, sticky="e")
end_entry = tk.Entry(frame, width=20)
end_entry.grid(row=2, column=1)

# Progress bar
progress = ttk.Progressbar(root, length=380, mode="determinate")
progress.pack(pady=20)

status_label = tk.Label(root, text="Waiting…", font=("Arial", 10))
status_label.pack()

tk.Button(
    root,
    text="Generate Tickets",
    font=("Arial", 12, "bold"),
    width=24,
    height=2,
    command=run_generation
).pack(pady=25)

root.mainloop()
