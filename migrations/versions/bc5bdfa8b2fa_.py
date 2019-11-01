"""empty message

Revision ID: bc5bdfa8b2fa
Revises: 11446b6baf42
Create Date: 2019-11-01 12:13:59.411819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc5bdfa8b2fa'
down_revision = '11446b6baf42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('device_group_admin_id_fkey', 'device_group', type_='foreignkey')
    op.create_foreign_key(None, 'device_group', 'admin', ['admin_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('executive_device_device_group_id_fkey', 'executive_device', type_='foreignkey')
    op.drop_constraint('executive_device_user_group_id_fkey', 'executive_device', type_='foreignkey')
    op.drop_constraint('executive_device_formula_id_fkey', 'executive_device', type_='foreignkey')
    op.drop_constraint('executive_device_executive_type_id_fkey', 'executive_device', type_='foreignkey')
    op.create_foreign_key(None, 'executive_device', 'user_group', ['user_group_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'executive_device', 'device_group', ['device_group_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'executive_device', 'formula', ['formula_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'executive_device', 'executive_type', ['executive_type_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('executive_type_device_group_id_fkey', 'executive_type', type_='foreignkey')
    op.create_foreign_key(None, 'executive_type', 'device_group', ['device_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('formula_user_group_id_fkey', 'formula', type_='foreignkey')
    op.create_foreign_key(None, 'formula', 'user_group', ['user_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('log_device_group_id_fkey', 'log', type_='foreignkey')
    op.create_foreign_key(None, 'log', 'device_group', ['device_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('reading_enumerator_sensor_type_id_fkey', 'reading_enumerator', type_='foreignkey')
    op.create_foreign_key(None, 'reading_enumerator', 'sensor_type', ['sensor_type_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('sensor_user_group_id_fkey', 'sensor', type_='foreignkey')
    op.drop_constraint('sensor_device_group_id_fkey', 'sensor', type_='foreignkey')
    op.drop_constraint('sensor_sensor_type_id_fkey', 'sensor', type_='foreignkey')
    op.create_foreign_key(None, 'sensor', 'sensor_type', ['sensor_type_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'sensor', 'device_group', ['device_group_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'sensor', 'user_group', ['user_group_id'], ['id'], ondelete='SET NULL')
    op.drop_constraint('sensor_reading_sensor_id_fkey', 'sensor_reading', type_='foreignkey')
    op.create_foreign_key(None, 'sensor_reading', 'sensor', ['sensor_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('sensor_type_device_group_id_fkey', 'sensor_type', type_='foreignkey')
    op.create_foreign_key(None, 'sensor_type', 'device_group', ['device_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('state_enumerator_executive_type_id_fkey', 'state_enumerator', type_='foreignkey')
    op.create_foreign_key(None, 'state_enumerator', 'executive_type', ['executive_type_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('unconfigured_device_device_group_id_fkey', 'unconfigured_device', type_='foreignkey')
    op.create_foreign_key(None, 'unconfigured_device', 'device_group', ['device_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('user_group_device_group_id_fkey', 'user_group', type_='foreignkey')
    op.create_foreign_key(None, 'user_group', 'device_group', ['device_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('user_group_member_user_group_id_fkey', 'user_group_member', type_='foreignkey')
    op.drop_constraint('user_group_member_user_id_fkey', 'user_group_member', type_='foreignkey')
    op.create_foreign_key(None, 'user_group_member', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'user_group_member', 'user_group', ['user_group_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_group_member', type_='foreignkey')
    op.drop_constraint(None, 'user_group_member', type_='foreignkey')
    op.create_foreign_key('user_group_member_user_id_fkey', 'user_group_member', 'user', ['user_id'], ['id'])
    op.create_foreign_key('user_group_member_user_group_id_fkey', 'user_group_member', 'user_group', ['user_group_id'], ['id'])
    op.drop_constraint(None, 'user_group', type_='foreignkey')
    op.create_foreign_key('user_group_device_group_id_fkey', 'user_group', 'device_group', ['device_group_id'], ['id'])
    op.drop_constraint(None, 'unconfigured_device', type_='foreignkey')
    op.create_foreign_key('unconfigured_device_device_group_id_fkey', 'unconfigured_device', 'device_group', ['device_group_id'], ['id'])
    op.drop_constraint(None, 'state_enumerator', type_='foreignkey')
    op.create_foreign_key('state_enumerator_executive_type_id_fkey', 'state_enumerator', 'executive_type', ['executive_type_id'], ['id'])
    op.drop_constraint(None, 'sensor_type', type_='foreignkey')
    op.create_foreign_key('sensor_type_device_group_id_fkey', 'sensor_type', 'device_group', ['device_group_id'], ['id'])
    op.drop_constraint(None, 'sensor_reading', type_='foreignkey')
    op.create_foreign_key('sensor_reading_sensor_id_fkey', 'sensor_reading', 'sensor', ['sensor_id'], ['id'])
    op.drop_constraint(None, 'sensor', type_='foreignkey')
    op.drop_constraint(None, 'sensor', type_='foreignkey')
    op.drop_constraint(None, 'sensor', type_='foreignkey')
    op.create_foreign_key('sensor_sensor_type_id_fkey', 'sensor', 'sensor_type', ['sensor_type_id'], ['id'])
    op.create_foreign_key('sensor_device_group_id_fkey', 'sensor', 'device_group', ['device_group_id'], ['id'])
    op.create_foreign_key('sensor_user_group_id_fkey', 'sensor', 'user_group', ['user_group_id'], ['id'])
    op.drop_constraint(None, 'reading_enumerator', type_='foreignkey')
    op.create_foreign_key('reading_enumerator_sensor_type_id_fkey', 'reading_enumerator', 'sensor_type', ['sensor_type_id'], ['id'])
    op.drop_constraint(None, 'log', type_='foreignkey')
    op.create_foreign_key('log_device_group_id_fkey', 'log', 'device_group', ['device_group_id'], ['id'])
    op.drop_constraint(None, 'formula', type_='foreignkey')
    op.create_foreign_key('formula_user_group_id_fkey', 'formula', 'user_group', ['user_group_id'], ['id'])
    op.drop_constraint(None, 'executive_type', type_='foreignkey')
    op.create_foreign_key('executive_type_device_group_id_fkey', 'executive_type', 'device_group', ['device_group_id'], ['id'])
    op.drop_constraint(None, 'executive_device', type_='foreignkey')
    op.drop_constraint(None, 'executive_device', type_='foreignkey')
    op.drop_constraint(None, 'executive_device', type_='foreignkey')
    op.drop_constraint(None, 'executive_device', type_='foreignkey')
    op.create_foreign_key('executive_device_executive_type_id_fkey', 'executive_device', 'executive_type', ['executive_type_id'], ['id'])
    op.create_foreign_key('executive_device_formula_id_fkey', 'executive_device', 'formula', ['formula_id'], ['id'])
    op.create_foreign_key('executive_device_user_group_id_fkey', 'executive_device', 'user_group', ['user_group_id'], ['id'])
    op.create_foreign_key('executive_device_device_group_id_fkey', 'executive_device', 'device_group', ['device_group_id'], ['id'])
    op.drop_constraint(None, 'device_group', type_='foreignkey')
    op.create_foreign_key('device_group_admin_id_fkey', 'device_group', 'admin', ['admin_id'], ['id'])
    # ### end Alembic commands ###
