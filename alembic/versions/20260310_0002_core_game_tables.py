"""core game tables"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "20260310_0002"
down_revision = "20260310_0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("code", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("effect_type", sa.String(length=32), nullable=False),
        sa.Column("effect_value", sa.Integer(), nullable=False),
        sa.Column("stackable", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("code", name="uq_items_code"),
    )
    op.create_index("ix_items_code", "items", ["code"])

    op.create_table(
        "quests",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("code", sa.String(length=64), nullable=False),
        sa.Column("title", sa.String(length=128), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("quest_type", sa.String(length=32), nullable=False),
        sa.Column("target_value", sa.Integer(), nullable=False),
        sa.Column("reward_gold", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("reward_exp", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("code", name="uq_quests_code"),
    )
    op.create_index("ix_quests_code", "quests", ["code"])
    op.create_index("ix_quests_quest_type", "quests", ["quest_type"])

    op.create_table(
        "inventory_items",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.BigInteger(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("item_id", sa.Integer(), sa.ForeignKey("items.id", ondelete="CASCADE"), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("user_id", "item_id", name="uq_inventory_items_user_item"),
    )
    op.create_index("ix_inventory_items_user_id", "inventory_items", ["user_id"])
    op.create_index("ix_inventory_items_item_id", "inventory_items", ["item_id"])

    op.create_table(
        "user_quests",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.BigInteger(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("quest_id", sa.Integer(), sa.ForeignKey("quests.id", ondelete="CASCADE"), nullable=False),
        sa.Column("progress", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("status", sa.String(length=32), nullable=False, server_default="active"),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("user_id", "quest_id", name="uq_user_quests_user_quest"),
    )
    op.create_index("ix_user_quests_user_id", "user_quests", ["user_id"])
    op.create_index("ix_user_quests_quest_id", "user_quests", ["quest_id"])
    op.create_index("ix_user_quests_status", "user_quests", ["status"])

    op.create_table(
        "battle_logs",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.BigInteger(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("mob_code", sa.String(length=64), nullable=False),
        sa.Column("result", sa.String(length=16), nullable=False),
        sa.Column("turns", sa.Integer(), nullable=False),
        sa.Column("reward_gold", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("reward_exp", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("details", sa.Text(), nullable=False, server_default=""),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_battle_logs_user_id", "battle_logs", ["user_id"])
    op.create_index("ix_battle_logs_result", "battle_logs", ["result"])

    op.create_table(
        "transactions",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.BigInteger(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("transaction_type", sa.String(length=32), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("reason", sa.Text(), nullable=False, server_default=""),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_transactions_user_id", "transactions", ["user_id"])
    op.create_index("ix_transactions_transaction_type", "transactions", ["transaction_type"])

    op.create_table(
        "admin_logs",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("admin_id", sa.BigInteger(), nullable=False),
        sa.Column("target_user_id", sa.BigInteger(), nullable=True),
        sa.Column("action", sa.String(length=32), nullable=False),
        sa.Column("payload", sa.Text(), nullable=False, server_default=""),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_admin_logs_admin_id", "admin_logs", ["admin_id"])
    op.create_index("ix_admin_logs_target_user_id", "admin_logs", ["target_user_id"])
    op.create_index("ix_admin_logs_action", "admin_logs", ["action"])


def downgrade() -> None:
    op.drop_index("ix_admin_logs_action", table_name="admin_logs")
    op.drop_index("ix_admin_logs_target_user_id", table_name="admin_logs")
    op.drop_index("ix_admin_logs_admin_id", table_name="admin_logs")
    op.drop_table("admin_logs")

    op.drop_index("ix_transactions_transaction_type", table_name="transactions")
    op.drop_index("ix_transactions_user_id", table_name="transactions")
    op.drop_table("transactions")

    op.drop_index("ix_battle_logs_result", table_name="battle_logs")
    op.drop_index("ix_battle_logs_user_id", table_name="battle_logs")
    op.drop_table("battle_logs")

    op.drop_index("ix_user_quests_status", table_name="user_quests")
    op.drop_index("ix_user_quests_quest_id", table_name="user_quests")
    op.drop_index("ix_user_quests_user_id", table_name="user_quests")
    op.drop_table("user_quests")

    op.drop_index("ix_inventory_items_item_id", table_name="inventory_items")
    op.drop_index("ix_inventory_items_user_id", table_name="inventory_items")
    op.drop_table("inventory_items")

    op.drop_index("ix_quests_quest_type", table_name="quests")
    op.drop_index("ix_quests_code", table_name="quests")
    op.drop_table("quests")

    op.drop_index("ix_items_code", table_name="items")
    op.drop_table("items")
