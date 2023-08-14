from pyrogram.types import InlineKeyboardButton

class Data:
    generate_single_button = [InlineKeyboardButton("🔥 BUAT STRING 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Kembali", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("Channel", url="https://t.me/DezetStore"),
            InlineKeyboardButton("Support", url="https://t.me/DezetSupport"),
        ],
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("Gw", callback_data="about")
        ],
        [InlineKeyboardButton("FakeDev", url="https://t.me/msdqqq")],
    ]

    START = """
**Halo {}

Gw {} Gw bisa bantu lu buat string pyrogram v1, pyrogram v2 dan telethon

Jumlah pengguna bot ini adalah {}

Kalo lu ga percaya bot ini hapus & blok aja gausah ribet yee, semua diluar tanggungjawab gw jika terjadi masalah atau bahkan disalahgunakan!

Buat id 5/6 Gausah ngambil string disini ntar akun lu deact/log out koar-koar anj🗿**

Maintenance By @MSDQQQ
    """

    HELP = """
**Perintah bot ini**

/about - Tentang gw
/help - Bantuan
/start - Memulai bot
/generate - Buat String
/cancel - Cancel
/stats - Jumlah pengguna (owner)
/gcast - Broadcast ke pengguna (owner)
"""

    ABOUT = """
**Tentang gw

Lu pasti tau gw jadi gausah dibaca lagi🥴**

**Owner** : @MSDQQQ
**CH** : @DezetStore
**GC** : @DezetSupport

**Donasi atau PP endorsement langsung pc owner diatas🙏**
    """
