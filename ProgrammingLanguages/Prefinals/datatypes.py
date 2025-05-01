def main():
    strings = {
        "Location": input("Enter location: "), 
        "Destination": input("Enter destination: "), 
        "Mode of Transport": input("Enter mode of transport: "),
    }
    
    travel_time = calculate_time(float(input("Enter distance (in km): ")), float(input("Enter speed (in km/h): ")))
    
    
    print() # New Line
    
    
    for key,value in strings.items():
        print(f"{key}: {value}")
    print(f"Travel Time: {travel_time} hour(s)")
    if travel_time > 5:
        print(f"Warning: {strings['Mode of Transport']} has been running for 5 hours or more. Rest time is recommended.")
    

def calculate_time(distance, speed):
    return distance/speed
    
    
    
if __name__ == "__main__":
    main()