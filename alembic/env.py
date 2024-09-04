from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Alembic Config obyekti
config = context.config

# Loglarni sozlash
fileConfig(config.config_file_name)

# Modelning `MetaData` obyekti (autogenerate funksiyasi uchun)
from app.config.database import Base  # Modelingizni import qiling

target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Migratsiyalarni sinxron tarzda bajarish."""
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    # Asinxron `AsyncEngine` o'rniga oddiy `Engine` ishlatamiz
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )

    # Sinxron ulanish orqali migratsiyalarni ishlatamiz
    with connectable.connect() as connection:
        do_run_migrations(connection)


# Sinxron rejimda migratsiyalarni boshqarish
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
