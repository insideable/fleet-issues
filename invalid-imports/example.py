from telegram.ext import Application


def make_app(use_updater: bool = False) -> Application:
    builder = Application.builder().token("token").read_timeout(10).get_updates_read_timeout(20)

    if use_updater:
        bot_app = builder.build()
    else:
        bot_app = builder.updater(None).build()

    return bot_app


def foo(app: Application) -> Application:
    app.bot.add_sticker_to_set()
    app.bot.send_audio()
    return app


foo(make_app())
