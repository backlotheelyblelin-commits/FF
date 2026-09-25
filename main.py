"""
Entry point — chạy bot Dev_NQR.
"""
import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)
from config import BOT_TOKEN


# ═══════════════════════════════════════════
# LOGGING
# ═══════════════════════════════════════════
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════
# POST INIT — Set commands
# ═══════════════════════════════════════════
async def post_init(app):
    from telegram import BotCommand

    commands = [
        BotCommand("start", "🏠 Menu chính"),
        BotCommand("mn", "📖 DS lệnh"),
        BotCommand("help", "❓ Trợ giúp"),
        BotCommand("id", "🆔 Lấy ID"),
        BotCommand("ping", "🏓 Test"),
        BotCommand("lang", "🌐 Ngôn ngữ"),
        BotCommand("voice", "🎤 Text → MP3"),
        BotCommand("giong", "🔊 DS giọng"),
        BotCommand("thay", "🎚️ Đổi giọng"),
        BotCommand("tag", "🎯 Spam + tag"),
        BotCommand("tag2", "🎭 Tag ẩn"),
        BotCommand("call", "📞 Call"),
        BotCommand("treongon", "🔄 Treo ngôn"),
        BotCommand("set", "⏱️ Delay spam"),
        BotCommand("setcall", "⏱️ Delay call"),
        BotCommand("off", "🔴 Dừng"),
        BotCommand("log", "📊 Log"),
        BotCommand("status", "📈 Trạng thái"),
        BotCommand("addtk", "➕ Thêm acc"),
        BotCommand("mytk", "👤 DS acc"),
        BotCommand("checktk", "🔍 Test acc"),
        BotCommand("settk", "⭐ Default"),
        BotCommand("deltk", "🗑️ Xóa acc"),
        BotCommand("im", "🔇 Im"),
        BotCommand("noi", "🔊 Cho nói"),
        BotCommand("cam", "🔇 Cam group"),
        BotCommand("sua", "🔊 Bỏ cam"),
        BotCommand("clear", "🗑️ Xóa 200 tin"),
        BotCommand("mybot", "🤖 Bot con"),
        BotCommand("addngon", "📎 Thêm ngôn"),
    ]

    await app.bot.set_my_commands(commands)
    logger.info("✅ Đã set commands")


# ═══════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════
def main():
    logger.info("🚀 Bot Dev_NQR starting...")

    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # ═══ ĐĂNG KÝ HANDLERS ═══
    from handlers.main_menu import start_cmd, main_menu_callback
    from handlers.menu import mn_cmd, help_callback
    from handlers.help_all import help_all_callback
    from handlers.verify import verify_callback
    from handlers.lang import lang_cmd, lang_callback
    from handlers.ping import ping_cmd
    from handlers.addtk import get_addtk_handler
    from handlers.mytk import mytk_cmd, mytk_callback
    from handlers.off import off_cmd, offall_cmd
    from handlers.tag import tag_cmd
    from handlers.call import call_cmd, setcall_cmd
    from handlers.set import set_cmd
    from handlers.treongon import treongon_cmd
    from handlers.im import im_cmd
    from handlers.noi import noi_cmd
    from handlers.cam import cam_cmd
    from handlers.sua import sua_cmd
    from handlers.clear import clear_cmd
    from handlers.status import status_cmd
    from handlers.log import log_cmd
    from handlers.voice import voice_cmd
    from handlers.sc import sc_cmd
    from handlers.anti import anti_cmd
    from handlers.backup import backup_cmd, restore_cmd, dbcheck_cmd, dblist_cmd
    from handlers.admin import setadmin_cmd, deladmin_cmd, listadmin_cmd

    # Menu
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("mn", mn_cmd))
    app.add_handler(CommandHandler("help", mn_cmd))
    app.add_handler(CommandHandler("lang", lang_cmd))
    app.add_handler(CommandHandler("ping", ping_cmd))

    # Tài khoản
    app.add_handler(get_addtk_handler())
    app.add_handler(CommandHandler("mytk", mytk_cmd))

    # Spam
    app.add_handler(CommandHandler("tag", tag_cmd))
    app.add_handler(CommandHandler("call", call_cmd))
    app.add_handler(CommandHandler("set", set_cmd))
    app.add_handler(CommandHandler("setcall", setcall_cmd))
    app.add_handler(CommandHandler("treongon", treongon_cmd))
    app.add_handler(CommandHandler("off", off_cmd))
    app.add_handler(CommandHandler("offall", offall_cmd))

    # Mod
    app.add_handler(CommandHandler("im", im_cmd))
    app.add_handler(CommandHandler("noi", noi_cmd))
    app.add_handler(CommandHandler("cam", cam_cmd))
    app.add_handler(CommandHandler("sua", sua_cmd))
    app.add_handler(CommandHandler("clear", clear_cmd))
    app.add_handler(CommandHandler("sc", sc_cmd))
    app.add_handler(CommandHandler("anti", anti_cmd))

    # Thống kê
    app.add_handler(CommandHandler("status", status_cmd))
    app.add_handler(CommandHandler("log", log_cmd))

    # Voice
    app.add_handler(CommandHandler("voice", voice_cmd))

    # Owner
    app.add_handler(CommandHandler("backup", backup_cmd))
    app.add_handler(CommandHandler("restore", restore_cmd))
    app.add_handler(CommandHandler("dbcheck", dbcheck_cmd))
    app.add_handler(CommandHandler("dblist", dblist_cmd))
    app.add_handler(CommandHandler("setadmin", setadmin_cmd))
    app.add_handler(CommandHandler("deladmin", deladmin_cmd))
    app.add_handler(CommandHandler("listadmin", listadmin_cmd))

    # Callbacks
    app.add_handler(CallbackQueryHandler(main_menu_callback, pattern="^main:"))
    app.add_handler(CallbackQueryHandler(help_callback, pattern="^help:"))
    app.add_handler(CallbackQueryHandler(help_all_callback, pattern="^help:all$"))
    app.add_handler(CallbackQueryHandler(verify_callback, pattern="^verify:"))
    app.add_handler(CallbackQueryHandler(lang_callback, pattern="^lang:"))
    app.add_handler(CallbackQueryHandler(mytk_callback, pattern="^mytk:"))

    logger.info("✅ Bot ready!")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()