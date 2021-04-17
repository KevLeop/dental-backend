# dental-backend
## Modelos
```
class PersonalModel(AbstractBaseUser, PermissionsMixin):
  TIPO_PERSONAL=[(1,"ADMIN"),(2,"DOCTOR"),(3,'PACIENTE')]
  personalId = models.AutoField(
    primary_key=True,
    unique=True,
    db_column='personal_id'
  )
```
