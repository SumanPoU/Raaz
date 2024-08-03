from django.contrib import admin
from .models import *


class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 1

class CitizenshipInline(admin.StackedInline):
    model = Citizenship
    extra = 0

class PassportInline(admin.StackedInline):
    model = Passport
    extra = 0

class PANInline(admin.StackedInline):
    model = PAN
    extra = 0

class EducationInline(admin.StackedInline):
    model = Education
    extra = 1

class DrivingLicenseInline(admin.StackedInline):
    model = DrivingLicense
    extra = 1

class BlueBookInline(admin.StackedInline):
    model = BlueBook
    extra = 1

class BankAccountInline(admin.StackedInline):
    model = BankAccount
    extra = 1

class InsuranceInline(admin.StackedInline):
    model = Insurance
    extra = 1

class VoterIDInline(admin.StackedInline):
    model = VoterID
    extra = 0

class EmployeesProvidentFundInline(admin.StackedInline):
    model = EmployeesProvidentFund
    extra = 0

class MalpotInline(admin.StackedInline):
    model = Malpot
    extra = 1

class CitizenAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberInline, CitizenshipInline, PassportInline, PANInline, EducationInline, DrivingLicenseInline, BlueBookInline, BankAccountInline, InsuranceInline, VoterIDInline, EmployeesProvidentFundInline, MalpotInline]

# Register your models here.
admin.site.register(Citizen, CitizenAdmin)
admin.site.register(PhoneNumber)
admin.site.register(Citizenship)
admin.site.register(Passport)
admin.site.register(PAN)
admin.site.register(Education)
admin.site.register(DrivingLicense)
admin.site.register(BlueBook)
admin.site.register(BankAccount)
admin.site.register(Insurance)
admin.site.register(VoterID)
admin.site.register(EmployeesProvidentFund)
admin.site.register(Malpot)