#!/usr/bin/env python3
import asyncio
import sys
import bot  # .so ဖိုင်ကို import လုပ်တာဖြစ်ပါတယ်

if __name__ == "__main__":
    try:
        # Async Context ကို အပြင်ကနေ စနစ်တကျ ထိန်းချုပ်ပြီး run ခြင်း
        if sys.platform == 'win32':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # .so ထဲက async def main() ကို လှမ်း run ခိုင်းခြင်း
        loop.run_until_complete(bot.main())
        
    except KeyboardInterrupt:
        print("\n[!] Bot Closed Safely.")
        sys.exit(0)
