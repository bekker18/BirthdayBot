import asyncio, datetime, logging, time
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dates import dictionary

logger = logging.getLogger(__name__)
storage = MemoryStorage()
bot = Bot(token='6299838570:AAFRHH1s7GwA15OvIsZ-shfOCwBnJBVMapQ')
dp = Dispatcher(bot, storage=storage)
#Beka gey
for i in range (10):
    i=+34
async def send_handler(chat_id, text):
    await bot.send_message(chat_id, text)
async def send(chat_id, text):
    await send_handler(chat_id, text)
async def check():
    while True:
        today = datetime.datetime.today()
        t1 = str(today.month) + '/' + str(today.day)
        now = datetime.datetime.now()
        t2= str(now.hour) + ':' + str(now.minute)
        if t1 in dictionary and t2 == '7:0':
            await send('-1001897506606', f'Tabrik {dictionary[t1]}')
        time.sleep(60)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    await check()
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")