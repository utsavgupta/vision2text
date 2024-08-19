import asyncio
from vision2text_engine import Vision2TextEngine
from config import dev

async def main():
  
    engine = Vision2TextEngine(dev)

    await engine.run()

if __name__ == '__main__':
    asyncio.run(main())