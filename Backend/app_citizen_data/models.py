from django.db import models

# Create your models here.
class Citizen(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.surname

class PhoneNumber(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' ' + self.citizen.surname + ' - ' + self.number

class Citizenship(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    issue_date = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' ' + self.citizen.surname + ' - ' + self.number

class Passport(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    issue_date = models.CharField(max_length=50)
    expiry_date = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' ' + self.citizen.surname + ' - ' + self.number
    
class PAN(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' ' + self.citizen.surname + ' - ' + self.number


class DrivingLicense(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    renewal_date = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' ' + self.citizen.surname + ' - ' + self.number

class BlueBook(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    renewal_date = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' ' + self.citizen.surname + ' - ' + self.number


class BankAccount(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' ' + self.citizen.surname + ' - ' + self.bank_name
    
class Education(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50)
    board = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    from_year = models.CharField(max_length=50)
    to_year = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' ' + self.citizen.surname + ' - ' + self.board + ' - ' + self.qualification
    
class Malpot(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' ' + self.citizen.surname + ' - ' + self.number
    
class Insurance(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    issue_date = models.CharField(max_length=50)
    expiry_date = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' ' + self.citizen.surname + ' - ' + self.number
    
class VoterID(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    issue_date = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' - ' + self.number

class EmployeesProvidentFund(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.citizen.name + ' ' + self.citizen.surname + ' - ' + self.number