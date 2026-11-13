import asyncio
import os
from telethon import TelegramClient

# 6 аккаунттың API кілттері мен сессия файлдарының жолдары
accounts = [
    {
        "name": "akk_1",
        "api_id": 38512980,
        "api_hash": "a0b857700422c50cbcb2da756711c74e",
    },
    {
        "name": "akk_2",
        "api_id": 34561990,
        "api_hash": "6072900771694c1f35deccb110762b44",
    },
    {
        "name": "akk_3",
        "api_id": 38512980,
        "api_hash": "a0b857700422c50cbcb2da756711c74e",
    },
    {
        "name": "akk_4",
        "api_id": 34561990,
        "api_hash": "6072900771694c1f35deccb110762b44",
    },
    {
        "name": "akk_5",
        "api_id": 38512980,
        "api_hash": "a0b857700422c50cbcb2da756711c74e",
    },
    {
        "name": "akk_6",
        "api_id": 34561990,
        "api_hash": "6072900771694c1f35deccb110762b44",
    },
]


async def main():
  # Sessions папкасы жоқ болса, автоматты түрде құрады
  os.makedirs("sessions", exist_ok=True)

  for acc in accounts:
    session_path = f"sessions/{acc['name']}"
    print(
        f"\n------------------------------------------------------------\n"
        f"📱 Аккаунтты қосу: {acc['name']} (API ID: {acc['api_id']})\n"
        f"------------------------------------------------------------"
    )

    client = TelegramClient(session_path, acc["api_id"], acc["api_hash"])
    try:
      await client.start()
      me = await client.get_me()
      print(
          f"✅ {acc['name']} сәтті қосылды және файлға сақталды!"
          f" Жалғанған қолданушы: {me.first_name} (+{me.phone})"
      )
      await client.disconnect()
    except Exception as e:
      print(f"❌ {acc['name']} қосу кезінде қате шықты: {e}")


if __name__ == "__main__":
  asyncio.run(main())

