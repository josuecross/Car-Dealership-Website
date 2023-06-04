from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default="Toyota")
    description = models.CharField(max_length=1000)


    def __str__(self):
        return "Name: " + self.name + "\n" + "Description: " + self.description
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


class CarModel(models.Model):
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default="2000GT")
    dealerID = models.IntegerField()
    SEDAN = 'Sedan'
    SUV ='SUV'
    WAGON = 'WAGON'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON')
    ]
    carType = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=SEDAN
    )

    date = models.DateField(null=True)

    def __str__(self):
        return  "Car Maker: " + self.carmake.name + "," + \
                "Name: " + self.name + "," + \
                "Type: " + self.carType + "," 

# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year):
        # Dealer address
        self.dealership = dealership
        # Dealer city
        self.name = name
        # Dealer Full Name
        self.purchase = purchase
        # Dealer id
        self.review = review
        # Location lat
        self.purchase_date = purchase_date
        # Location long
        self.car_make = car_make
        # Dealer short name
        self.car_model = car_model
        # Dealer state
        self.car_year = car_year

        self.sentiment = ""

    def __str__(self):
        return "Review: " + self.review