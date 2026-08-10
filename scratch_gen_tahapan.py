import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up figure and axis
fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
ax.set_xlim(0, 12)
ax.set_ylim(0, 7.5)
ax.axis('off')

# Style parameters
box_width = 2.4
box_height = 2.8
header_height = 0.5

# Box definitions: (x, y, title, bullets)
boxes = [
    # Top Row
    (0.3, 4.2, "Pengumpulan Data", [
        "• Data sekunder dari\n  Dinas Sosial",
        "• Data sintetis\n  karakteristik kelistrikan"
    ]),
    (3.2, 4.2, "Preprocessing Data", [
        "• Cleaning Data",
        "• Encoding Variabel",
        "• Normalisasi Data",
        "• Split Data Training/\n  Testing"
    ]),
    (6.1, 4.2, "Model LightGBM", [
        "• Pelatihan Model\n  (Training)",
        "• Tuning Parameter"
    ]),
    (9.0, 4.2, "Evaluasi Model", [
        "• Accuracy, Precision,\n  Recall, F1-Score",
        "• Confusion Matrix"
    ]),
    # Bottom Row
    (9.0, 0.5, "Pengembangan Sistem", [
        "• Perancangan Sistem\n  (UML)",
        "• Implementasi Sistem\n  (Next.js, Flask,\n   Supabase)",
        "• Integrasi Model\n  LightGBM"
    ]),
    (6.1, 0.5, "Pengujian Sistem", [
        "• Blackbox Testing"
    ])
]

# Draw Boxes
for x, y, title, bullets in boxes:
    # Outer box
    rect = patches.FancyBboxPatch(
        (x, y), box_width, box_height,
        boxstyle="square,pad=0",
        linewidth=1.5, edgecolor='black', facecolor='white'
    )
    ax.add_patch(rect)
    
    # Header separator line
    ax.plot([x, x + box_width], [y + box_height - header_height, y + box_height - header_height], color='black', lw=1.5)
    
    # Title text
    ax.text(
        x + box_width / 2, y + box_height - header_height / 2, title,
        ha='center', va='center', fontsize=11, fontweight='bold', color='black'
    )
    
    # Bullet points
    text_content = "\n\n".join(bullets)
    ax.text(
        x + 0.15, y + box_height - header_height - 0.25, text_content,
        ha='left', va='top', fontsize=9.5, color='black', linespacing=1.3
    )

# Draw Arrows
arrow_props = dict(arrowstyle="-|>", color="black", lw=1.5, mutation_scale=15)

# Top row horizontal arrows
# Box 1 to Box 2
ax.annotate("", xy=(3.2, 5.6), xytext=(2.7, 5.6), arrowprops=arrow_props)

# Box 2 to Box 3
ax.annotate("", xy=(6.1, 5.6), xytext=(5.6, 5.6), arrowprops=arrow_props)

# Box 3 to Box 4
ax.annotate("", xy=(9.0, 5.6), xytext=(8.5, 5.6), arrowprops=arrow_props)

# Downward arrow: Box 4 to Box 5
ax.annotate("", xy=(10.2, 3.3), xytext=(10.2, 4.2), arrowprops=arrow_props)

# Leftward arrow: Box 5 to Box 6
ax.annotate("", xy=(8.5, 1.9), xytext=(9.0, 1.9), arrowprops=arrow_props)

plt.tight_layout()
plt.savefig(r"d:\PROJECT\Skripsi\gambar\tahapan_penelitian.png", bbox_inches='tight', dpi=300)
print("Successfully generated tahapan_penelitian.png")
