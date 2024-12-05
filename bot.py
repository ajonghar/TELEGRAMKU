from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup

def check_site(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Harap masukkan URL, contoh: /check example.com")
        return

    url = context.args[0]
    try:
        response = requests.get(f"https://trustpositif.kominfo.go.id/welcome?csrf_token=2e9df415b598c7a73825149f7b7a6270&recaptcha_token=03AFcWeA4l6tW0oT6FOYyKVzzcobETrmzKKTh37n5P0Hu56pFiHNOf6IENZEsPOZPfPKHn8pcqBy0NUTZzmE7098x0heaojQx8bxV-nFCTUltFxWe-1D0lChhNw0HaKR2VbtSlSZb9b_OjnwnXpqxrtmTwvIrjVijHWM0j1eZ1r9BVNvdSenPeTeiowPf1LawJNC1_Kw2x0zqRLN1bSoQH3NdksCgFD8ZRogF6XqotpvOlGBt5WGdj0wGbuhzRKwePPM8HuPO8CKKP0LCrLBS34XxUrAvW3TDlzTH1yq3-JItbSTcX3HvHHz3c51PGgnqHikhR7KfExxGPG5gAO9ULV2YJtQSxV6J_eSK0OhClaXq4y_HaNXhYkSVuwRl6d6-AmdeAncDrFE0jMf6rTXDTWo0hqGu1zJ_mWRmjeDKqKoJiuuw4oIHYOh12pxjTLNYROz48tZl_HDkstefTUzsdv5Jg-9LKq4UqsvUhvitemYcQxaRysBcpodjia2khk8AFnSa-lBysNjpVPDURTkG8RuCenetqSRi0SoYqIGbOsLWDZkM9ypeBxUMoG-1bEH74j3ICDO0lx2ACL7_EDvoWriv6GOxcizERcWAucJVM0NPs20RpH3cnVlAKbnvRB7FlcyzwMW8P8cBi1g7KE8h8inVcFCEmt_SjRIf1nj6CTWgt3pH7PA5BNgI1iEa0eMkI4kZRfYqMpSHbxEaVwg9l56Vrh3xWV6e65UoTJay3k_dnZbBsvF81fhd1pAqgEMpvIU8zm5M_vFH5_tRv5i_CI9JZlGk62DQQzzaSIG-02QHGdLbl5M5aYPAbFQeC1GVBj3De_hPW38v3qerY7Ge3MgIFK4zbLsWgLW-mLxzrxNQNEnF1guolH3AR38X9TFVNcVsMRTPEf0C9Z5zDbcYsqqJl5TKSLC6rD9rkcELXc42tZ4t77Z2sSxwfAmk9dZFLl65a7BdNSzOq-fsj4nG0nJ-BJiehQ43WCDfFMIEhuXgW0C3Fxyewy-hQCJTqBOUK7s8LOd4beCy4YmihHoDQ-AEEmBg05xl9l0U7d80psRlI2lj7i6THJ3YodpUiL2shNyMe240gZl6rF6iG8eCyTI8zNcPTuDoXxEgRmRR7E-yTsvxyIqw2hmlgaNleJdWE2mYu8UUEnxQNUyHuTiLP31yoYs1yGdz0mN-Hsol6uT5sVc8XymbV2sxgzTpF_QMM1AOeRWoeYAytGjUC7Tldj7x48n72YhKF_EDANfLg6rrTNUIl93dr5CIMQdt60V-0L-zLL8uYeX2QkNUkD5LK_WqqC_NvFJoGkR7fvAgx847rlq0cqQqfy_C7Rs26PmV3NGzy6XTGcR1-gu_QGSMtN0qeSAIu4yNMeN5NY1wkKZtTVpvMx0hiDwkjsZOjtjcTL-BKIhNNP4oe6Vn-wYeRfDME25V4GXLsvDMVMXwzUb8CSZBoaBz6_O_72-tibOmDJv7YsxZ6VQX9172QKDjks3FkpD0UxM0DWBA5vaAqesWvLcTzIjP0COrn03vKpFF0_1FJbwGqKSfYJ5VycQ0fOCGl3weoOgjsC6xA8V0k4hhya1gUH6Hipe4yLRH24KvydL_lGf55pt5aGlI8YxNWzwCROd48Mri7J_EhwjUpRiJb1SqzC4g5f13Y2TDJa1kFjPKQG52ihvIWNMR7zJFtMGjFGNFBsvY6nNsBsHS4spPbcbbreRVnEcxPAFXnieb6vc3bkrFTcjBN8yCY97UJ38xZ2wrkt-AUGW3yPOAldBIV0_v6TTTHhK-Hw5fTvc50Z8hrRwwKnm07X9XtC_PJ2xIBgJOzXUFJDoui8PL7joP9wdvuP-FLc4Bs_Sof2nNMikEzOJKYp63h1Q2TMAZfQdIi9jJm6vBOxPV3dGLs13vXTGd2ZvEjrNMjnFAM4bg_nh5UG0r3EbNg4wqpvFeJWItyBVNQBpSb8AT4LlD3rw9EcJbRYEoCpY8H7dnJJgV4z5B3sq4GY4LfausQQOOGvaDNmO9QSs4fLM7XiWIMh5ccGY9oY2dXN4EANqJN6NPLny4s7R1gZhcuwMA57mY6FjgK-FVSQpA7cHrJnz9J0EMS0XWj2_E65_6owrl52Ko-clUxuLedn-ErG86mLPE_PmQPS2GaVKWcIlYdjcrMmhxsG9vFyBUwNJTqga4IEBjaGzxx9rKSPvkF3sviU-JWhFN2eqtERsVjkA&domains={url}")
        if "diblokir" in response.text.lower():
            update.message.reply_text(f"❌ {url} terdaftar di Trustpositif.")
        else:
            update.message.reply_text(f"✅ {url} tidak terdaftar di Trustpositif.")
    except:
        update.message.reply_text("Terjadi kesalahan, coba lagi nanti.")

def main():
    TOKEN = "7549576387:AAE52Pf1lxH6jYbPE7gmvm1FXmXWkQg_HVc"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("check", check_site))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
