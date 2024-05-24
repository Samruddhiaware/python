# Car rental System
# available = 1 , not_available = 0

class Car:
    def __init__(self, car_name, model, rent_per_hour, status = 1):
        self.car_name = car_name
        self.model = model
        self.rent_per_hour = rent_per_hour
        self.status = status
        
    def display(self):
        print(f"The details of the car are \nName: {self.car_name} Rent per hour: {self.rent_per_hour}")
        
    def cal_amount(self):
        if self.car_name == user_request:
            self.status = 0            
            return self.rent_per_hour*user_duration   
        else:
            print('rent cannot be calculated')
    
        
       
c1 = Car('Honda City', 'City_premium', 500)
c2 = Car('Maruti Suzuki Swift', 'Swift_Dsire', 400)
c3 = Car('Nexon', 'Tata_Nexon_EV', 600)
c1.display()
c2.display()
c3.display()
car_list = [c1,c2,c3]


user_request = input("Please select the car you need: ")
user_duration = float(input("Please specify the duration for use in hrs: "))

for i in car_list:
    if(i.car_name == user_request):
        print('Your total charges are: ',i.cal_amount())
    # else:
    #     print('not working')







        

    
    