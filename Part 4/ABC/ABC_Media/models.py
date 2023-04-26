from django.db import models

class Admworkhours(models.Model):
    empid = models.OneToOneField('Administrator', models.DO_NOTHING, db_column='empId', primary_key=True, blank=True, null=False)  # Field name made lowercase. The composite primary key (empId, day) found, that is not supported. The first column is selected.
    day = models.DateField(blank=True, null=True)
    hours = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AdmWorkHours'


class Administers(models.Model):
    empid = models.OneToOneField('Administrator', models.DO_NOTHING, db_column='empId', primary_key=True, blank=True, null=False)  # Field name made lowercase. The composite primary key (empId, siteCode) found, that is not supported. The first column is selected.
    sitecode = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Administers'


class Administrator(models.Model):
    empid = models.AutoField(db_column='empId', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    name = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Administrator'


class Airtimepackage(models.Model):
    packageid = models.AutoField(db_column='packageId', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    class_field = models.CharField(max_length=16, db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    lastdate = models.DateField(db_column='lastDate', blank=True, null=True)  # Field name made lowercase.
    frequency = models.IntegerField(blank=True, null=True)
    videocode = models.IntegerField(db_column='videoCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AirtimePackage'


class Broadcasts(models.Model):
    videocode = models.OneToOneField('Video', models.DO_NOTHING, db_column='videoCode', primary_key=True, blank=True, null=False)  # Field name made lowercase. The composite primary key (videoCode, siteCode) found, that is not supported. The first column is selected.
    sitecode = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Broadcasts'

class Client(models.Model):
    clientid = models.AutoField(db_column='clientId', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    name = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Client'    

class Digitaldisplay(models.Model):
    serialno = models.CharField(max_length=10, db_column='serialNo', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    schedulersystem = models.CharField(max_length=10, db_column='schedulerSystem', blank=False, null=False)  # Field name made lowercase.
    modelno = models.ForeignKey('Model', models.DO_NOTHING, db_column='modelNo', blank=False, null=False)  # Field name made lowercase. 

    class Meta:
        managed = False
        db_table = 'DigitalDisplay'

class Locates(models.Model):
    serialno = models.OneToOneField(Digitaldisplay, models.DO_NOTHING, db_column='serialNo', primary_key=True, blank=True, null=False)  # Field name made lowercase. The composite primary key (serialNo, siteCode) found, that is not supported. The first column is selected.
    sitecode = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Locates'


class Model(models.Model):
    modelno = models.CharField(max_length=10, db_column='modelNo', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    width = models.TextField(db_column='width', blank=False, null=False)  # This field type is a guess.
    height = models.TextField(db_column='height', blank=False, null=False)  # This field type is a guess.
    weight = models.TextField(db_column='weight', blank=False, null=False)  # This field type is a guess.
    depth = models.TextField(db_column='depth', blank=False, null=False)  # This field type is a guess.
    screensize = models.TextField(db_column='screenSize', blank=False, null=False)  # Field name made lowercase. This field type is a guess.

    #When __str__ is called object attribute will be returned not the object
    def __str__(self):
        return self.modelno

    class Meta:
        managed = False
        db_table = 'Model'


class Purchases(models.Model):
    clientid = models.OneToOneField(Client, models.DO_NOTHING, db_column='clientId', primary_key=True, blank=True, null=False)  # Field name made lowercase. The composite primary key (clientId, empId, packageId) found, that is not supported. The first column is selected.
    empid = models.ForeignKey('Salesman', models.DO_NOTHING, db_column='empId', blank=True, null=True)  # Field name made lowercase.
    packageid = models.ForeignKey(Airtimepackage, models.DO_NOTHING, db_column='packageId', blank=True, null=True)  # Field name made lowercase.
    commissionrate = models.TextField(db_column='commissionRate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Purchases'

class Salesman(models.Model):
    empid = models.AutoField(db_column='empId', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    name = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Salesman'


class Site(models.Model):
    sitecode = models.AutoField(db_column='siteCode', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    type = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Site'


class Specializes(models.Model):
    empid = models.OneToOneField('Technicalsupport', models.DO_NOTHING, db_column='empId', primary_key=True, blank=True, null=False)  # Field name made lowercase. The composite primary key (empId, modelNo) found, that is not supported. The first column is selected.
    modelno = models.ForeignKey(Model, models.DO_NOTHING, db_column='modelNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Specializes'


class Technicalsupport(models.Model):
    empid = models.AutoField(db_column='empId', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    name = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TechnicalSupport'


class Video(models.Model):
    videocode = models.AutoField(db_column='videoCode', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    videolength = models.IntegerField(db_column='videoLength', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Video'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'