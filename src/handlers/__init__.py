def setup_handlers():
    from handlers import user_handlers, admin_handlers

    user_handlers.setup()
    admin_handlers.setup()
