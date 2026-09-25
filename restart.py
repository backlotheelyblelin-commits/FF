"""
Auto restart bot khi crash.
Chạy: python restart.py
- Tự động chạy lại main.py khi crash
- Đợi 5 giây giữa các lần restart
- Ctrl+C để dừng hoàn toàn
"""
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MAIN_FILE = BASE_DIR / "main.py"
RESTART_DELAY = 5  # giây


def run_bot():
    """Chạy main.py và trả về exit code."""
    try:
        result = subprocess.run(
            [sys.executable, str(MAIN_FILE)],
            cwd=str(BASE_DIR),
        )
        return result.returncode
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(f"❌ Lỗi chạy bot: {e}")
        return -1


def main():
    print("=" * 50)
    print("🤖 DEV_NQR AUTO RESTART")
    print("=" * 50)
    print(f"📂 Thư mục: {BASE_DIR}")
    print(f"🚀 Chạy: {MAIN_FILE}")
    print(f"⏱️ Delay restart: {RESTART_DELAY}s")
    print(f"💡 Nhấn Ctrl+C để dừng")
    print("=" * 50)
    print()

    count = 0

    while True:
        count += 1
        start = datetime.now()

        print(f"\n🟢 Lần chạy #{count} — {start.strftime('%d/%m/%Y %H:%M:%S')}")
        print("-" * 50)

        try:
            code = run_bot()
        except KeyboardInterrupt:
            print("\n\n⛔ Đã dừng bởi user (Ctrl+C).")
            print(f"📊 Tổng số lần chạy: {count}")
            break

        end = datetime.now()
        duration = (end - start).total_seconds()

        print("-" * 50)
        print(f"🔴 Bot dừng — {end.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"📊 Exit code: {code}")
        print(f"⏱️ Thời gian chạy: {duration:.1f}s ({duration/60:.1f} phút)")

        # Nếu exit code = 0 → user chủ động dừng
        if code == 0:
            print("\n✅ Bot dừng bình thường.")
            choice = input("🔄 Restart? (y/n): ").strip().lower()
            if choice not in ("y", "yes", ""):
                print("👋 Tạm biệt!")
                break

        print(f"\n⏳ Restart sau {RESTART_DELAY}s...")
        print("💡 Nhấn Ctrl+C để dừng hoàn toàn")

        try:
            time.sleep(RESTART_DELAY)
        except KeyboardInterrupt:
            print("\n\n⛔ Đã dừng bởi user.")
            break

    print("\n" + "=" * 50)
    print("🏁 KẾT THÚC")
    print("=" * 50)


if __name__ == "__main__":
    main()