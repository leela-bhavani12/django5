from django.shortcuts import render, redirect
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,"home.html")
def flights(request):
    return render(request,"Flights.html")
def BookNow(request):
    return render(request,"BookNow.html")
def Contact(request):
    return render(request,"Contact.html")
def Login(request):
    return render(request,"Login.html")
def Details(request):
    return render(request,"Details.html")
def CalFare(request):
    return render(request,"CalFare.html")
def Destinations(request):
    return render(request,"Destinations.html")
def AboutUs(request):
    return render(request,"AboutUs.html")
def Search(request):
    return render(request,"Search.html")
def Submit(request):
    return render(request,"Submit.html")
def otp(request):
    return render(request,"otp.html")
def Card(request):
    return render(request,"Card.html")

def flightrender2(request):
    if request.method == 'POST':
        first_name = request.POST.get('fn')
        last_name = request.POST.get('ln')
        mobile_number = request.POST.get('pn')
        date_of_birth = request.POST.get('dob')
        gender = request.POST.get('gn') if 'gn' in request.POST else request.POST.get('fm')
        destination = request.POST.get('destination')
        day_to_travel = request.POST.get('day')
        flight_time = request.POST.get('flight_time')

        # Save data to the database
        travel_details = TravelDetails.objects.create(
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
            date_of_birth=date_of_birth,
            gender=gender,
            destination=destination,
            day_to_travel=day_to_travel,
            flight_time=flight_time
        )
        # Redirect to a success page or perform any other action
        return redirect('home')  # Replace 'success_page' with the URL name of your success page

    return render(request, 's.html')




def view(request):
    passengers = Passenger.objects.all()
    return render(request, 'view.html', {'passengers': passengers})

def addstu(request):
         if request.method == "POST":
             name = request.POST.get('name')
             age = request.POST.get('age')
             destination = request.POST.get('destination')
             passenger = Passenger.objects.create(name=name, age=age, destination=destination)
             return redirect('passenger_list')
         else:
             return render(request, 'add.html')


def passenger_update(request, pk):
    passenger = Passenger.objects.get(pk=pk)
    if request.method == "POST":
        passenger.name = request.POST.get('name')
        passenger.age = request.POST.get('age')
        passenger.destination = request.POST.get('destination')
        passenger.save()
        return redirect('passenger_list')
        return render(request, 'passenger_update.html', {'passenger': passenger})


        def student_delete(request, pk):
            passenger = Passenger.objects.get(pk=pk)
            if request.method == "POST":
                passenger.delete()
            return redirect('passenger_list')
            return render(request, 'passenger_delete.html', {'passenger': passenger})

        print(first_name)