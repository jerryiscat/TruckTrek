# TruckTrek
The inspiration behind our project lies in the challenging conditions faced by the 3.5 million truck drivers in the U.S. According to the Bureau of Labor (2023). These professionals play a vital role in our economy. However, the alarming statistics of more than 160,000 truck accidents annually, with approximately 32% causing injuries and 3% resulting in fatalities (TruckInfo.net), highlight the pressing need for innovative solutions. Additionally, recognizing the health risks such as obesity, hypertension, and extreme fatigue that truck drivers face due to their demanding lifestyle further motivates our commitment to developing a solution that prioritizes both safety on the roads and the well-being of these essential workers.

# Introduction
We created this app to design the route for truck drivers to promote safety and efficiency. We advocate for a recommended break every 100 mileage, incorporating designated stops along the route for this purpose. At each stop, drivers receive information about accidents for the next stop, nearby restaurants and gas station place.

## Prerequisites
- Python 3.x
- Virtualenv (optional but recommended - helps to download all the libraries required at once)

## Setup Instructions

1. **Create a Virtual Environment (Optional):**
    ```bash
    pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Install Dependencies:**
    ```bash
    pip3 install -r requirements.txt
    ```
    
3. **Start the Flask App:**
    ```bash
    python main.py 
    ```
    Make sure to be in the same directory where you have your main.py file

2. **Access the App:**
    Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

