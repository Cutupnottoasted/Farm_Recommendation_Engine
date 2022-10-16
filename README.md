# Hackathon2022JohnDeer
Recommendation engine 

## How to Run
This is a Django Project, so in order to run, download the project as a zip file and cd into the main directory. From there, you can run by going into 
your terminal and running "python manage.py runserver"

## Use and Functionality
The following web app works to help farmers find the best crops to plant given their soil conditions. What will happen is that the farmer gives their info
on their soil. Specifically, they must provide: Nitrogen ratio, Phosphorus ratio, Potassium Ratio, Temperature, Humidity, PH level, and Rainfall. From there, 
using a csv file with data samples on these 7 conditions and the best recommended crop, we take the data the user gives us and find the crop condition that 
it is most similar to. We used a least difference equation to find the crop mean that the input is most similar to 
