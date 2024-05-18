from django.contrib import admin
from .models import TableType, Table, BookTable


admin.site.register(TableType)
admin.site.register(Table)
admin.site.register(BookTable)
