# Generated by Django 3.2.3 on 2021-06-21 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_apppermission_setup_data'),
    ]

    operations = [
        # アプリからデータアクセスを許可する 参照のみ
        migrations.RunSQL("""
            GRANT select ON myapp_apppermission TO tenantuser;
        """,
        reverse_sql="""
            REVOKE select ON myapp_apppermission FROM tenantuser;
        """),
        # RLS設定
        migrations.RunSQL("""
            ALTER TABLE myapp_apppermission ENABLE ROW LEVEL SECURITY;
            CREATE POLICY tenantuser_apppermission ON myapp_apppermission USING(tenant_id::text = current_user);
        """,
        reverse_sql='''
            ALTER TABLE myapp_apppermission DISABLE ROW LEVEL SECURITY;
            DROP POLICY tenantuser_apppermission ON myapp_apppermission;
        ''')
    ]